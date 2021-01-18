import random
from player import Player
from minion import *

def combat(player1, player2):
    player1 = player1.board.minions
    player2 = player2.board.minions
    print()
    print(f"Combat player1: " + ", ".join([str(minion) for minion in player1]))
    print(f"Combat player2: " + ", ".join([str(minion) for minion in player2]))
