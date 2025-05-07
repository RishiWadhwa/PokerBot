from main.game.hand_evaluation import HandEvaluator
import random

class PokerStrategy:
	@staticmethod
	def get_hand_score(cards:list, phase:str) -> float:
		"""
		- Hand Score 0.0 - 1.0 indicating strength/confidence in hand
		"""
		rank, tiebreakers = HandEvaluator.evaluate_hand(cards)

		base_score = rank.value / 10.0

		phase_bonus = {
			"pre_flop": 0.0,
			"flop": 0.05,
			"turn": 0.1,
			"river": 0.15
		}.get(phase, 0)

		high_card_bonus = tiebreakers[0] / 100.0 if tiebreakers else 0

		return min(base_score + phase_bonus + high_card_bonus, 1.0)

	@staticmethod
	def chip_allocation(score:float, chips:int, aggression:float) -> float:
		aggression = max(min(aggression, 1.0), 0.0)
		base_bet = 0
		if score<0.2:
			base_bet = 0
		elif score<0.4:
			base_bet = chips*0.1
		elif score<0.6:
			base_bet = chips*0.25
		elif score<0.8:
			base_bet = chips*0.5
		else:
			base_bet = chips*0.75

		aggression_multiplier = 1 + (aggression*0.5)
		final_bet = base_bet * aggression_multiplier
		return int(base_bet)