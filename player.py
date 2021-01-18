from tavern import Tavern
from board import Board
from hand import Hand

class Player:
    def __init__(self, game, name):
        self.game = game
        self.name = name
        self.tavern = Tavern(self)
        self.board = Board(self)
        self.hand = Hand(self)
        self.turn = 1
        self.max_gold = 3
        self.gold = self.max_gold
        self.health = 40

        self.free_refreshs = 0

    def print_summary(self):
        print(f"{self.name}: Turn {self.turn}; {self.gold}/{self.max_gold} gold; Tavern {self.tavern.tier}" + (f" {len(self.tavern.frozen_minions)}/{len(self.tavern.minions)} frozen" if len(self.tavern.frozen_minions) > 0 else "") + (f", {self.tavern.upgrade_cost} gold upgrade" if self.tavern.tier < 6 else ""))
        print("Tavern: " + ", ".join([str(minion) for minion in self.tavern.minions]))
        print("Board: " + ", ".join([str(minion) for minion in self.board.minions]))
        print("Hand: " + ", ".join([str(minion) for minion in self.hand.minions]))

    def end_turn(self):
        self.board.trigger_end_turn()
        self.game.player_end_turn(self)

    def start_turn(self):
        self.turn += 1
        self.max_gold += 1
        if self.max_gold > 10:
            self.max_gold = 10
        self.gold = self.max_gold
        self.tavern.next_turn()
        self.board.trigger_start_turn()

    def buy_minion(self, tavern_index):
        if self.gold < 3 or tavern_index >= len(self.tavern.minions) or len(self.hand.minions) >= 10:
            return False
        minion = self.tavern.remove_minion(tavern_index)
        self.gold -= 3
        self.hand.add_minion(minion)
        self.game.remove_minion_from_pool(minion)

    def play_minion(self, hand_index):
        if hand_index >= len(self.hand.minions) or len(self.board.minions) >= 7:
            return False
        minion = self.hand.remove_minion(hand_index)
        self.board.add_minion(minion, True)
        minion.battlecry()
        self.board.trigger_play_other_minion(minion)

    def sell_minion(self, board_index):
        if board_index >= len(self.board.minions):
            return False
        minion = self.board.remove_minion(board_index)
        self.gold += 1
        if self.gold > 10:
            self.gold = 10
        minion.sell()
        self.game.add_minion_to_pool(minion)

    def reorder_minion(self, board_index, new_board_index):
        if board_index >= len(self.board.minions) or new_board_index >= len(self.board.minions):
            return False
        self.board.reorder_minion(board_index, new_board_index)

    def refresh(self):
        if self.free_refreshs > 0:
            self.free_refreshs -= 1
        elif self.gold < 1:
            return False
        else:
            self.gold -= 1
        self.tavern.refresh()

    def toggle_freeze(self):
        self.tavern.toggle_freeze()

    def upgrade_tavern(self):
        if self.gold < self.tavern.upgrade_cost or self.tavern.tier >= 6:
            return False
        self.gold -= self.tavern.upgrade_cost
        self.tavern.upgrade()

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("Dead")
