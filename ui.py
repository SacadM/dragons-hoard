from abc import ABC, abstractmethod
from player import Player

class UserInterface(ABC):
    """
    Abstract base class for user interfaces.
    """

    @abstractmethod
    def display_game_state(self, game):
        pass

    @abstractmethod
    def get_player_action(self, player: Player) -> str:
        pass

    @abstractmethod
    def display_challenge_result(self, challenger: Player, opponent: Player, winner: Player):
        pass

    @abstractmethod
    def display_winner(self, winner: Player):
        pass