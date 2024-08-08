from physical import Card
from typing import List

class PokerHand:
    """
    Represents a poker hand and provides methods for evaluating its rank.

    Attributes:
        cards (List[Card]): The cards in the poker hand.
    """

    def __init__(self, cards: List[Card]):
        self.cards = cards

    def evaluate(self) -> int:
        # TODO: Implement poker hand evaluation
        pass