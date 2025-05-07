from main.game.dealer import Dealer
from main.game.player import Player
import random

class Table:
	def __init__(self, inverted:bool=False, starting_stack:int=5000):
		self.players = []
		self.dealer = Dealer(inverted=inverted)
		self.starting_chips = starting_stack
		self.seat_players()

	def seat_players(self, human_count:int=1, total_count:int=6):
		for human_id in range(human_count):
			self.players.append(Player(player_id=human_id, money=self.starting_chips, is_ai=False))
		for ai_id in range(total_count-human_count):
			self.players.append(Player(player_id=ai_id, money=self.starting_chips, is_ai=True))

		random.shuffle(self.players) # random turn order

	def start_hand(self):
		self.dealer.start_new_deal()
		for player in self.players:
			player.reset_new_hand()

		self.dealer.deal_hole_cards(self.players)

	def show_table(self):
		for i in range(len(self.players)):
			print(f"Seat {i+1}: {self.players[i]}")
		print (self.dealer)

	def get_players(self):
		return self.players

	def get_dealer(self):
		return self.dealer