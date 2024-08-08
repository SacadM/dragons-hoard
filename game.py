from enum import Enum
from typing import List
from player import Player
from physical import Deck, Card
from ui import UserInterface
from hand import PokerHand
import random

class Action(Enum):
    DECK = 'D'
    TREASURE = 'T'
    CHALLENGE = 'C'
    STORE = 'S'

class Game:
    """
    Represents the Dragons Hoard game and manages the game state.

    Attributes:
        players (List[Player]): The list of players in the game.
        main_deck (Deck): The main deck of cards.
        treasure_deck (List[Card]): The face-up cards in the treasure deck.
        current_player_index (int): The index of the current player.
        interface (UserInterface): The user interface for the game.
    """

    def __init__(self, player_names: List[str], interface: UserInterface):
        if len(player_names) not in [2, 3]:
            raise ValueError("This implementation supports exactly 3 players.")
        
        self.players = [Player(name) for name in player_names]
        self.main_deck = Deck()
        self.treasure_deck: List[Card] = []
        self.current_player_index = 0
        self.interface = interface

    def setup(self):
        """Set up the game by dealing cards and creating the treasure deck."""
        self.main_deck.shuffle()
        
        # Deal 7 cards to each player
        for player in self.players:
            for _ in range(7):
                card = self.main_deck.draw()
                if card:
                    player.add_card(card)

        # Set up the treasure deck
        for _ in range(9):
            card = self.main_deck.draw()
            if card:
                self.treasure_deck.append(card)

    def play(self):
        """Main game loop."""
        self.setup()

        while not self.is_game_over():
            current_player = self.players[self.current_player_index]
            self.interface.display_game_state(self)
            
            action = self.interface.get_player_action(current_player)
            self.handle_action(current_player, action)

            self.current_player_index = (self.current_player_index + 1) % len(self.players)

        winner = self.determine_winner()
        self.interface.display_winner(winner)

    def handle_action(self, player: Player, action: Action) -> bool:
        """Handle the player's chosen action. Return True if action was successful, False otherwise."""
        if action == Action.DECK:
            return self.handle_deck_action(player)
        elif action == Action.TREASURE:
            return self.handle_treasure_action(player)
        elif action == Action.CHALLENGE:
            return self.handle_challenge_action(player)
        elif action == Action.STORE:
            return self.handle_store_action(player)
        return False

    def handle_deck_action(self, player: Player) -> bool:
        """Handle the deck action: draw a card from the main deck."""
        if len(player.hand) >= 13:
            self.interface.display_message("You already have 13 cards. You can't draw more.")
            return False
        
        card = self.main_deck.draw()
        if card:
            player.add_card(card)
            return True
        else:
            self.interface.display_message("The main deck is empty.")
            return False

    def handle_treasure_action(self, player: Player) -> bool:
        """Handle the treasure action: swap a card with the treasure deck."""
        if len(self.treasure_deck) == 0:
            self.interface.display_message("The treasure deck is empty.")
            return False

        player_card = self.interface.get_card_from_hand(player)
        treasure_card = self.interface.get_card_from_treasure(self.treasure_deck)

        player.remove_card(player_card)
        player.add_card(treasure_card)
        self.treasure_deck.remove(treasure_card)
        self.treasure_deck.append(player_card)

        # Replace the taken treasure card
        if self.main_deck.cards:
            new_treasure_card = self.main_deck.draw()
            self.treasure_deck.append(new_treasure_card)

        return True

    def handle_challenge_action(self, player: Player) -> bool:
        """Handle the challenge action: challenge another player to a poker hand duel."""
        opponents = [p for p in self.players if p != player and len(p.hand) >= 3]
        if not opponents:
            self.interface.display_message("No opponents have enough cards for a challenge.")
            return False

        opponent = self.interface.select_opponent(player, opponents)
        num_cards = self.interface.get_challenge_hand_size(min(len(player.hand), len(opponent.hand), 5))

        challenger_hand = PokerHand(self.interface.select_cards(player, num_cards))
        opponent_hand = PokerHand(self.interface.select_cards(opponent, num_cards))

        challenger_rank, _ = challenger_hand.evaluate()
        opponent_rank, _ = opponent_hand.evaluate()

        winner = player if challenger_rank > opponent_rank else opponent
        self.interface.display_challenge_result(player, opponent, winner)

        cards_to_draw = challenger_rank if winner == player else opponent_rank
        self.draw_cards_after_challenge(winner, cards_to_draw)

        return True
    
    def draw_cards_after_challenge(self, player: Player, num_cards: int):
        """Allow the challenge winner to draw cards."""
        for _ in range(num_cards):
            if len(player.hand) >= 13:
                self.interface.display_message(f"{player.name} can't draw more cards (hand limit reached).")
                break

            source = self.interface.choose_draw_source()
            if source == 'treasure' and self.treasure_deck:
                card = self.treasure_deck.pop(0)
                player.add_card(card)
                if self.main_deck.cards:
                    self.treasure_deck.append(self.main_deck.draw())
            elif source == 'main' and self.main_deck.cards:
                card = self.main_deck.draw()
                player.add_card(card)
            else:
                self.interface.display_message(f"No more cards available from the {source} deck.")
                break

    def handle_store_action(self, player: Player) -> bool:
        """Handle the store action: store a valid 5-card poker hand."""
        if len(player.hand) < 5:
            self.interface.display_message("You need at least 5 cards to store a hand.")
            return False

        selected_cards = self.interface.select_cards(player, 5)
        hand = PokerHand(selected_cards)
        
        if hand.evaluate()[0] > PokerHand.HIGH_CARD:
            player.store_hand(selected_cards)
            for card in selected_cards:
                player.remove_card(card)
            return True
        else:
            self.interface.display_message("The selected hand is not a valid poker hand (at least a pair is required).")
            return False

    def is_game_over(self) -> bool:
        """Check if the game is over."""
        return len(self.main_deck.cards) == 0 and len(self.treasure_deck) == 0 and all(len(player.hand) == 0 for player in self.players)

    def determine_winner(self) -> Player:
        """Determine the winner of the game based on stored hands."""
        best_scores = []
        for player in self.players:
            if not player.stored_hands:
                best_scores.append(0)
            else:
                best_hand = max(player.stored_hands, key=lambda hand: PokerHand(hand).evaluate()[0])
                best_scores.append(PokerHand(best_hand).evaluate()[0])
        
        max_score = max(best_scores)
        winners = [player for player, score in zip(self.players, best_scores) if score == max_score]
        
        if len(winners) == 1:
            return winners[0]
        else:
            # In case of a tie, randomly select a winner
            return random.choice(winners)