from main.game.deck.deck import Deck
from main.game.deck.card import Card
from main.game.player import Player
from enum import Enum

class Dealer:
	def __init__(self, inverted:bool=False, players:int=6):
		self.deck = Deck(inverted=inverted)
		self.player_count = players
		self.board = []
		self.DealerState = DealerStates.pre_flop

	def start_new_deal(self):
		self.deck.reset()
		self.deck.shuffle()
		self.board.clear()

	def deal_hole_cards(self, players:list):
		self.deck.burn_card()
		for _  in range(2):
			for i in range(self.player_count):
				player = players[i]
				card = self.deck.draw_card()
				player.receive_card(card)

	def deal_flop(self):		
		self.deck.burn_card()
		self.board.extend(self.deck.draw_card(count=3))
		self.DealerState = DealerStates.flop

	def deal_turn(self):
		self.board.append(self.deck.draw_with_burn())
		self.DealerState = DealerStates.turn

	def deal_river(self):
		self.board.append(self.deck.draw_with_burn())
		self.DealerState = DealerStates.river

	def get_board(self):
		return self.board

	def get_illustrated_board(self):
		return " ".join(str(card) for card in self.board)

	def get_dealer_state(self):
		return self.DealerState

	def get_next_state(self):
		next_state = self.DealerState.value+1
		return DealerStates(next_state)

	def __str__(self):
		return f"Board: {self.get_illustrated_board()}"

	def __repr__(self):
		return f"Board(state={self.DealerState}, player_count={self.player_count})"

class DealerStates(Enum):
	pre_flop = 0
	flop = 1
	turn = 2
	river = 3
	reveal = 4