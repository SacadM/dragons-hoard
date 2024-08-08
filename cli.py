from game import Game, Action
from player import Player
from ui import UserInterface
from physical import Card
from typing import List

class CLIInterface(UserInterface):
    """
    Command-line interface implementation for the Dragons Hoard game.
    """

    def display_game_state(self, game: Game):
        """Display the current game state."""
        print("\n" + "=" * 40)
        print("Treasure Deck:")
        for card in game.treasure_deck:
            print(f"  {card}")
        
        current_player = game.players[game.current_player_index]
        print(f"\n{current_player.name}'s Hand:")
        for card in current_player.hand:
            print(f"  {card}")
        print("=" * 40)

    def get_player_action(self, player: Player) -> Action:
        """Get the player's action choice."""
        while True:
            choice = input(f"{player.name}, choose an action (D)eck, (T)reasure, (C)hallenge, (S)tore: ").upper()
            try:
                return Action(choice)
            except ValueError:
                print("Invalid choice. Please try again.")

    def display_challenge_result(self, challenger: Player, opponent: Player, winner: Player):
        """Display the result of a challenge."""
        print(f"\n{challenger.name} challenged {opponent.name}!")
        print(f"The winner is: {winner.name}")

    def display_winner(self, winner: Player):
        """Display the winner of the game."""
        print(f"\nCongratulations! The winner is {winner.name}!")

    def display_message(self, message: str):
        """Display a message to the user."""
        print(message)

    def get_card_from_hand(self, player: Player) -> Card:
        """Prompt the player to select a card from their hand."""
        while True:
            print(f"{player.name}'s hand:")
            for i, card in enumerate(player.hand):
                print(f"{i + 1}: {card}")
            try:
                choice = int(input("Select a card number to swap: ")) - 1
                if 0 <= choice < len(player.hand):
                    return player.hand[choice]
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")

    def get_card_from_treasure(self, treasure_deck: List[Card]) -> Card:
        """Prompt the player to select a card from the treasure deck."""
        while True:
            print("Treasure deck:")
            for i, card in enumerate(treasure_deck):
                print(f"{i + 1}: {card}")
            try:
                choice = int(input("Select a card number to take: ")) - 1
                if 0 <= choice < len(treasure_deck):
                    return treasure_deck[choice]
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")

    def select_opponent(self, player: Player, opponents: List[Player]) -> Player:
        """Prompt the player to select an opponent for a challenge."""
        print(f"{player.name}, select an opponent to challenge:")
        for i, opponent in enumerate(opponents):
            print(f"{i + 1}: {opponent.name} ({len(opponent.hand)} cards)")
        while True:
            try:
                choice = int(input("Enter the number of the opponent: ")) - 1
                if 0 <= choice < len(opponents):
                    return opponents[choice]
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")

    def get_challenge_hand_size(self, max_size: int) -> int:
        """Prompt the player to select the number of cards for a challenge."""
        while True:
            try:
                size = int(input(f"Enter the number of cards for the challenge (3-{max_size}): "))
                if 3 <= size <= max_size:
                    return size
                else:
                    print(f"Invalid choice. Please enter a number between 3 and {max_size}.")
            except ValueError:
                print("Please enter a number.")

    def select_cards(self, player: Player, num_cards: int) -> List[Card]:
        """Prompt the player to select a specific number of cards from their hand."""
        selected_cards = []
        print(f"{player.name}, select {num_cards} cards:")
        while len(selected_cards) < num_cards:
            for i, card in enumerate(player.hand):
                if card not in selected_cards:
                    print(f"{i + 1}: {card}")
            try:
                choice = int(input(f"Select card {len(selected_cards) + 1}: ")) - 1
                if 0 <= choice < len(player.hand) and player.hand[choice] not in selected_cards:
                    selected_cards.append(player.hand[choice])
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")
        return selected_cards

    def choose_draw_source(self) -> str:
        """Prompt the player to choose the source for drawing cards after a challenge."""
        while True:
            choice = input("Draw from (T)reasure deck or (M)ain deck? ").upper()
            if choice == 'T':
                return 'treasure'
            elif choice == 'M':
                return 'main'
            else:
                print("Invalid choice. Please enter 'T' or 'M'.")

    def display_message(self, message: str):
        """Display a message to the user."""
        print(message)