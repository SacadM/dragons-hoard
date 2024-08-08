from game import Game, Action
from player import Player
from ui import UserInterface

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