from minion import *

class Board:
    def __init__(self, player):
        self.player = player
        self.minions = []

    def add_minion(self, minion, is_played): # Is played or summoned
        self.minions.append(minion)
        if not is_played: # Is summoned
            self.trigger_summon_other_minion(minion)

    def remove_minion(self, board_index):
        minion = self.minions.pop(board_index)
        return minion

    def reorder_minion(self, board_index, new_board_index):
        minion = self.minions.pop(board_index)
        self.minions.insert(new_board_index, minion)

    def trigger_play_other_minion(self, new_minion):
        for minion in self.minions:
            if minion != new_minion:
                minion.play_other_minion(new_minion)

    def trigger_summon_other_minion(self, new_minion):
        for minion in self.minions:
            if minion != new_minion:
                minion.summon_other_minion(new_minion)

    def trigger_start_turn(self):
        for minion in self.minions:
            minion.start_turn()

    def trigger_end_turn(self):
        for minion in self.minions:
            minion.end_turn()
