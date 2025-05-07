from itertools import combinations
from main.game.deck.deck_constants import NUMERICAL_RANKS_LOW_ACE, STRING_SUITS
from main.game.deck.card import Card
from collections import Counter
from enum import Enum

class HandEvaluator:
	@staticmethod
	def evaluate_hand(cards:list):
		"""
		- 7 Cards: 5 board + 2 hole
		- Returns tuple: (hand_rank, list of high/kickers for tie-breaking)
		"""
		best_hand = (HandRankings.NOTHING, [])
		for combo in combinations(cards, 5):
			hand_rank, tie_break = HandEvaluator._rank_five_card_hand(combo)
			if (HandEvaluator._compare((hand_rank, tie_break), best_hand) > 0):
				best_hand = (hand_rank, tie_break)
		return best_hand

	@staticmethod
	def _rank_five_card_hand(cards:list):
		values= sorted([card.get_high_val() for card in cards], reverse=True)
		suits = [card.suit for card in cards]

		rank_counts = Counter(values)
		suit_counts = Counter(suits)

		# Flush Checker
		flush_suit = None
		for suit, count in suit_counts.items():
			if count >= 5:
				flush_suit = suit
				break

		# Straight Checker
		unique_values = sorted(set(values), reverse=True)
		if 14 in unique_values:
			unique_values.append(1) # In case of ace check for ace-low too

		straight_high = None
		for i in range(len(unique_values) - 4):
			window = unique_values[i:i+5]
			if (window[0] - window[4] == 4):
				straight_high = window[0]
				return

		# Straight Flush Checker
		if flush_suit is not None:
			flush_cards = [c for c in cards if c.suit == flush_suit]
			flush_values = sorted(set([c.get_high_val() for c in flush_cards]), reverse=True)
			
			if 14 in flush_values:
				flush_values.append(1)

			for i in range(len(unique_values)-4):
				window = unique_values[i:i+5]
				if (window[0] - window[4] == 4):
					if (window[0] == 14):
						return (HandRankings.ROYAL_FLUSH, [14])
					return (HandRankings.STRAIGHT_FLUSH, [window[0]])

		# Four of a Kind Checker
		if 4 in rank_counts.values():
			four = [rank for rank, count in rank_counts.items() if count == 4][0]
			kicker = max([v for v in values if v != four])
			return (HandRankings.FOUR_OF_A_KIND, [four, kicker])

		# Full House Checker
		three = [rank for rank, count in rank_counts.items() if count == 3]
		pairs = [rank for rank, count in rank_counts.items() if count == 2]
		if three:
			if (len(three) >= 2):
				return (HandRankings.FULL_HOUSE, [three[0], three[1]])
			elif pairs:
				return (HandRankings.FULL_HOUSE, [three[0], pairs[0]])

		# Flush Checker
		if flush_suit:
			return (HandRankings.FLUSH, flush_cards[:5])

		# Straight Checker
		if straight_high is not None:
			return (HandRankings.STRAIGHT, [straight_high])

		# Three of a Kind Checker
		if three:
			kickers = [v for v in values if v != three[0]]
			return (HandRankings.THREE_OF_A_KIND, kickers)

		# Two Pair Checker
		if pairs and len(pairs) >= 2:
			top_two = sorted(pairs, reverse=True)[:2]
			kicker = max([v for v in values if v not in top_two])
			return (HandRankings.TWO_PAIR, top_two + [kicker])

		# Pair Checker
		if pairs and len(pairs) == 1:
			kickers = [v for v in values if v != pairs[0]]
			return (HandRankings.PAIR, [pairs[0]] + kickers)

		# High Card Checker
		return (HandRankings.HIGH_CARD, values[:5])

	@staticmethod
	def _compare(hand1, hand2) -> int: # 1 for hand1, -1 for hand2
		rank1, tiebreaker1 = hand1
		rank2, tiebreaker2 = hand2

		if (rank1.value != rank2.value):
			return 1 if rank1.value > rank2.value else -1

		for val1, val2 in zip(tiebreaker1, tiebreaker2):
			if isinstance(val1, Card):
				val1 = val1.rank
			if isinstance(val2, Card):
				val2 = val2.rank
			if val1 > val2:
				return 1
			elif val1 < val2:
				return -1

		# In default/fully tie case return hand1
		return 0


class HandRankings(Enum):
	NOTHING = 0
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