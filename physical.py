from enum import Enum, auto
from typing import List, Optional
import random

class Suit(Enum):
    HEARTS = auto()
    DIAMONDS = auto()
    CLUBS = auto()
    SPADES = auto()

class Rank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

class Card:
    """
    Represents a playing card with a suit and rank.

    Attributes:
        suit (Suit): The suit of the card.
        rank (Rank): The rank of the card.
    """

    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank.name} of {self.suit.name}"

class Deck:
    """
    Represents a deck of playing cards.

    Attributes:
        cards (List[Card]): The list of cards in the deck.
    """

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Suit for rank in Rank]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self) -> Optional[Card]:
        return self.cards.pop() if self.cards else None