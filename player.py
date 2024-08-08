from physical import Card
from typing import List

class Player:
    """
    Represents a player in the Dragons Hoard game.

    Attributes:
        name (str): The name of the player.
        hand (List[Card]): The cards in the player's hand.
        stored_hands (List[List[Card]]): The poker hands stored by the player.
    """

    def __init__(self, name: str):
        self.name = name
        self.hand: List[Card] = []
        self.stored_hands: List[List[Card]] = []

    def add_card(self, card: Card):
        if len(self.hand) < 13:
            self.hand.append(card)
        else:
            raise ValueError("Cannot exceed 13 cards in hand")

    def remove_card(self, card: Card):
        self.hand.remove(card)

    def store_hand(self, hand: List[Card]):
        # TODO: Implement poker hand validation
        self.stored_hands.append(hand)
        for card in hand:
            self.remove_card(card)