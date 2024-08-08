from physical import Card, Deck
from player import Player
from abc import ABC, abstractmethod
from typing import List

class Game:
    """
    Represents the Dragons Hoard game and manages the game state.

    Attributes:
        players (List[Player]): The list of players in the game.
        main_deck (Deck): The main deck of cards.
        treasure_deck (List[Card]): The face-up cards in the treasure deck.
        current_player_index (int): The index of the current player.
    """

    def __init__(self, player_names: List[str]):
        self.players = [Player(name) for name in player_names]
        self.main_deck = Deck()
        self.treasure_deck: List[Card] = []
        self.current_player_index = 0

    def setup(self):
        # TODO: Implement game setup
        pass

    def play_turn(self):
        # TODO: Implement turn logic
        pass

    def challenge(self, challenger: Player, opponent: Player, num_cards: int):
        # TODO: Implement challenge logic
        pass

    def is_game_over(self) -> bool:
        # TODO: Implement game over condition
        pass

    def determine_winner(self) -> Player:
        # TODO: Implement winner determination
        pass