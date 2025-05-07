from main.game.table import Table
from main.game.dealer import Dealer
from main.game.player import Player
from main.game.hand_evaluation import HandEvaluator
from main.strategy.poker_strategy import PokerStrategy
import time

def wait_for_enter(phase:str):
	input("\nPress [Enter] to proceed to '{}'".format(phase))

table = Table()

aggression = 0.0

# Pre Flop
table.start_hand()
table.show_table()

for player in table.get_players():
	if player.is_ai_player():
		hand_score = PokerStrategy.get_hand_score(table.get_dealer().get_board()+player.get_hand_raw(), table.get_dealer().get_dealer_state().value)
		print(f"{player.get_name()} | {(hand_score, PokerStrategy.chip_allocation(hand_score, player.get_chips(), aggression))}")

wait_for_enter(str(table.get_dealer().get_next_state())[13:])

# Flop
table.get_dealer().deal_flop()
table.show_table()

for player in table.get_players():
	if player.is_ai_player():
		hand_score = PokerStrategy.get_hand_score(table.get_dealer().get_board()+player.get_hand_raw(), table.get_dealer().get_dealer_state().value)
		print(f"{player.get_name()} | {(hand_score, PokerStrategy.chip_allocation(hand_score, player.get_chips(), aggression))}")

wait_for_enter(str(table.get_dealer().get_next_state())[13:])

# Turn
table.get_dealer().deal_turn()
table.show_table()

for player in table.get_players():
	if player.is_ai_player():
		hand_score = PokerStrategy.get_hand_score(table.get_dealer().get_board()+player.get_hand_raw(), table.get_dealer().get_dealer_state().value)
		print(f"{player.get_name()} | {(hand_score, PokerStrategy.chip_allocation(hand_score, player.get_chips(), aggression))}")

wait_for_enter(str(table.get_dealer().get_next_state())[13:])

# River
table.get_dealer().deal_river()
table.show_table()

for player in table.get_players():
	if player.is_ai_player():
		hand_score = PokerStrategy.get_hand_score(table.get_dealer().get_board()+player.get_hand_raw(), table.get_dealer().get_dealer_state().value)
		print(f"{player.get_name()} | {(hand_score, PokerStrategy.chip_allocation(hand_score, player.get_chips()))}")

wait_for_enter(str(table.get_dealer().get_next_state())[13:])

# Reveal
players = table.get_players()
hand_evals = []
board = table.get_dealer().get_board()
for player in players:
	hand_evals.append(HandEvaluator.evaluate_hand(board+player.get_hand_raw()))

winner = 0
for i in range(len(hand_evals)-1):
	if winner != i:
		if (HandEvaluator._compare(hand_evals[i], hand_evals[winner]) > 0):
			winner = i

print(f"The winner is Seat {winner+1}")
	