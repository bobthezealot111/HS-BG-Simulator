from minion import *

class Hand:
    def __init__(self, player):
        self.player = player
        self.minions = []

    def add_minion(self, minion):
        self.minions.append(minion)

    def remove_minion(self, hand_index):
        minion = self.minions.pop(hand_index)
        return minion
