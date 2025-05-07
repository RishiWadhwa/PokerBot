import random
from main.game.deck.card import Card
from main.game.deck.deck_constants import STRING_SUITS, STRING_RANKS

class Deck:
	def __init__(self, inverted:bool=False):
		self.inverted = inverted
		self.deck = [
			Card(rank, suit, inverted) for suit in STRING_SUITS for rank in STRING_RANKS
		]

	def shuffle(self):
		random.shuffle(self.deck)

	def draw(self):
		return self.deck.pop()

	def draw_card(self, count=1):
		return self.deck.pop() if (count == 1) else [self.draw() for _ in range(count)]

	def burn_card(self):
		self.deck.pop()

	def draw_with_burn(self):
		self.deck.pop() # burn card [DO NOT REVEAL]
		return self.deck.pop()

	def reset(self):
		self.__init__(inverted=self.inverted)

	def size(self):
		return len(self.deck)

	def is_empty(self):
		return (len(self.deck) == 0)

	def __str__(self):
		return f"{self.size()} cards remaining"

	def __repr__(self):
		return f"Deck(size={self.size()}, inverted={self.inverted})"
