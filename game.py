from enum import Enum
from typing import List
from player import Player
from physical import Deck, Card
from ui import UserInterface

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
        if len(player_names) != 3:
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

    def handle_action(self, player: Player, action: Action):
        """Handle the player's chosen action."""
        if action == Action.DECK:
            self.handle_deck_action(player)
        elif action == Action.TREASURE:
            self.handle_treasure_action(player)
        elif action == Action.CHALLENGE:
            self.handle_challenge_action(player)
        elif action == Action.STORE:
            self.handle_store_action(player)

    def handle_deck_action(self, player: Player):
        """Handle the deck action: draw a card from the main deck."""
        if len(player.hand) < 13:
            card = self.main_deck.draw()
            if card:
                player.add_card(card)
        else:
            self.interface.display_message("You already have 13 cards. You can't draw more.")

    def handle_treasure_action(self, player: Player):
        """Handle the treasure action: swap a card with the treasure deck."""
        # Implementation details to be added

    def handle_challenge_action(self, player: Player):
        """Handle the challenge action: challenge another player to a poker hand duel."""
        # Implementation details to be added

    def handle_store_action(self, player: Player):
        """Handle the store action: store a valid 5-card poker hand."""
        # Implementation details to be added

    def is_game_over(self) -> bool:
        """Check if the game is over."""
        return len(self.main_deck.cards) == 0 and len(self.treasure_deck) == 0 and all(len(player.hand) == 0 for player in self.players)

    def determine_winner(self) -> Player:
        """Determine the winner of the game based on stored hands."""
        # Implementation details to be added
        pass