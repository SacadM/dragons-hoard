from collections import Counter
from typing import List, Tuple
from physical import Card, Rank

class PokerHand:
    """
    Represents a poker hand and provides methods for evaluating its rank.

    Attributes:
        cards (List[Card]): The cards in the poker hand (3-5 cards).
    """

    # Hand rankings
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9
    ROYAL_FLUSH = 10

    def __init__(self, cards: List[Card]):
        if not 3 <= len(cards) <= 5:
            raise ValueError("Poker hand must contain 3-5 cards")
        self.cards = sorted(cards, key=lambda card: card.rank.value, reverse=True)

    def evaluate(self) -> Tuple[int, List[int]]:
        """
        Evaluate the poker hand and return its rank along with tie-breaking values.

        Returns:
            Tuple[int, List[int]]: A tuple containing the hand rank and a list of
            tie-breaking values (card ranks in order of importance).
        """
        if len(self.cards) == 5 and self._is_royal_flush():
            return (self.ROYAL_FLUSH, [])
        
        if self._is_straight_flush():
            return (self.STRAIGHT_FLUSH, [self.cards[0].rank.value])
        
        if self._is_four_of_a_kind():
            four_rank, kicker = self._get_four_of_a_kind_ranks()
            return (self.FOUR_OF_A_KIND, [four_rank, kicker])
        
        if self._is_full_house():
            three_rank, pair_rank = self._get_full_house_ranks()
            return (self.FULL_HOUSE, [three_rank, pair_rank])
        
        if self._is_flush():
            return (self.FLUSH, [card.rank.value for card in self.cards])
        
        if self._is_straight():
            return (self.STRAIGHT, [self.cards[0].rank.value])
        
        if self._is_three_of_a_kind():
            three_rank, kickers = self._get_three_of_a_kind_ranks()
            return (self.THREE_OF_A_KIND, [three_rank] + kickers)
        
        if self._is_two_pair():
            high_pair, low_pair, kicker = self._get_two_pair_ranks()
            return (self.TWO_PAIR, [high_pair, low_pair, kicker])
        
        if self._is_pair():
            pair_rank, kickers = self._get_pair_ranks()
            return (self.PAIR, [pair_rank] + kickers)
        
        return (self.HIGH_CARD, [card.rank.value for card in self.cards])

    def _rank_counts(self) -> Counter:
        return Counter(card.rank.value for card in self.cards)

    def _is_flush(self) -> bool:
        return len(set(card.suit for card in self.cards)) == 1

    def _is_straight(self) -> bool:
        values = sorted(set(card.rank.value for card in self.cards))
        return len(values) == len(self.cards) and values[-1] - values[0] == len(values) - 1

    def _is_royal_flush(self) -> bool:
        return self._is_flush() and set(card.rank for card in self.cards) == {Rank.TEN, Rank.JACK, Rank.QUEEN, Rank.KING, Rank.ACE}

    def _is_straight_flush(self) -> bool:
        return self._is_flush() and self._is_straight()

    def _is_four_of_a_kind(self) -> bool:
        return 4 in self._rank_counts().values()

    def _is_full_house(self) -> bool:
        return set(self._rank_counts().values()) == {2, 3}

    def _is_three_of_a_kind(self) -> bool:
        return 3 in self._rank_counts().values()

    def _is_two_pair(self) -> bool:
        return list(self._rank_counts().values()).count(2) == 2

    def _is_pair(self) -> bool:
        return 2 in self._rank_counts().values()

    def _get_four_of_a_kind_ranks(self) -> Tuple[int, int]:
        ranks = self._rank_counts()
        four_rank = next(rank for rank, count in ranks.items() if count == 4)
        kicker = next(rank for rank, count in ranks.items() if count == 1)
        return four_rank, kicker

    def _get_full_house_ranks(self) -> Tuple[int, int]:
        ranks = self._rank_counts()
        three_rank = next(rank for rank, count in ranks.items() if count == 3)
        pair_rank = next(rank for rank, count in ranks.items() if count == 2)
        return three_rank, pair_rank

    def _get_three_of_a_kind_ranks(self) -> Tuple[int, List[int]]:
        ranks = self._rank_counts()
        three_rank = next(rank for rank, count in ranks.items() if count == 3)
        kickers = sorted([rank for rank, count in ranks.items() if count == 1], reverse=True)
        return three_rank, kickers

    def _get_two_pair_ranks(self) -> Tuple[int, int, int]:
        ranks = self._rank_counts()
        pairs = sorted([rank for rank, count in ranks.items() if count == 2], reverse=True)
        kicker = next(rank for rank, count in ranks.items() if count == 1)
        return pairs[0], pairs[1], kicker

    def _get_pair_ranks(self) -> Tuple[int, List[int]]:
        ranks = self._rank_counts()
        pair_rank = next(rank for rank, count in ranks.items() if count == 2)
        kickers = sorted([rank for rank, count in ranks.items() if count == 1], reverse=True)
        return pair_rank, kickers