

STRING_SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
ASCII_SUITS = ["♡", "♢", "♣", "♠"]
ASCII_ALTERNATE_SUITS = ["♥", "◆", "♧", "♤"]

STRING_RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
NUMERICAL_RANKS_HIGH_ACE = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
NUMERICAL_RANKS_LOW_ACE = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}

VAL_TO_RANK_ACE_HIGH = {v: k for k, v in NUMERICAL_RANKS_HIGH_ACE.items()}
VAL_TO_RANK_ACE_LOW = {v: k for k, v in NUMERICAL_RANKS_LOW_ACE.items()}

STD_DECK_SIZE = 52