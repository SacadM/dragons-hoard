from game import Game
from player import Player

class CLIInterface():
    """
    Command-line interface implementation for the Dragons Hoard game.
    """

    def display_game_state(self, game: Game):
        # TODO: Implement CLI game state display
        pass

    def get_player_action(self, player: Player) -> str:
        # TODO: Implement CLI player action input
        pass

    def display_challenge_result(self, challenger: Player, opponent: Player, winner: Player):
        # TODO: Implement CLI challenge result display
        pass

    def display_winner(self, winner: Player):
        # TODO: Implement CLI winner display
        pass