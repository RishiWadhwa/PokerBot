

class Player: 
	def __init__(self, player_id:int, money:int=5000, is_ai:bool=True):
		self.stack = money
		self.hole_cards = []
		self.active = True
		self.position = None
		self.name = f"P{player_id}" if (not is_ai) else f"AI{player_id}"

	def receive_card(self, card):
		if (len(self.hole_cards) < 2):
			self.hole_cards.append(card)
		else:
			raise ValueError(f"Error001:{self.name} already has 2 cards.")

	def reset_new_hand(self):
		self.hole_cards.clear()
		self.active = True

	def fold(self):
		self.active = False

	def get_hand_raw(self):
		return self.hole_cards

	def get_hand(self):
		return " ".join([str(card) for card in self.hole_cards])

	def get_chips(self):
		return self.stack

	def bet(self, amount):
		return # implement later

	def call(self, amount):
		return # implement later

	def raise_to(self, amount):
		return # implement later

	def is_ai_player(self):
		return self.name[0]!="P"

	def get_name(self):
		return self.name

	def __str__(self):
		cards = " ".join(str(card) for card in self.hole_cards)
		return f"{self.name} | Chips: {self.stack} | Cards: {cards}"

	def __repr__(self):
		return f"Player(id={self.name}, stack={self.stack}, active={self.active})"
