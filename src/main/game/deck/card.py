from main.game.deck.deck_constants import (STRING_SUITS, ASCII_ALTERNATE_SUITS, ASCII_SUITS, NUMERICAL_RANKS_HIGH_ACE, NUMERICAL_RANKS_LOW_ACE)

class Card:
	def __init__(self, rank:str, suit:str, inverted:bool):
		self.rank = rank
		self.suit = suit
		self.value_high = NUMERICAL_RANKS_HIGH_ACE[rank]
		self.value_low = NUMERICAL_RANKS_LOW_ACE[rank]
		self.inverted = inverted
		self.suit_image = ASCII_ALTERNATE_SUITS[STRING_SUITS.index(suit)] if (inverted) else ASCII_SUITS[STRING_SUITS.index(suit)]

	def __str__(self):
		return f"{self.suit_image} {self.rank}"

	def __repr__(self):
		return f"Card(rank='{self.rank}', suit='{self.suit}')"

	def get_low_val(self):
		return self.value_low

	def get_high_val(self):
		return self.value_high