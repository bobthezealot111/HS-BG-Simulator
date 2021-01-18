from minion import *

class Tavern:
    # Index is tier, index 0 is undefined
    tavern_sizes = [None, 3, 4, 5, 6, 7, 8]
    upgrade_base_costs = [None, 5, 7, 8, 9, 10, None]

    def __init__(self, player):
        self.player = player
        self.minions = []
        self.tier = 1
        self.upgrade_cost = self.upgrade_base_costs[self.tier]
        self.frozen_minions = []
        self.refresh()

    def refresh(self):
        self.minions = []
        self.frozen_minions = []
        for _ in range(self.tavern_sizes[self.tier]):
            self.minions.append(self.random_minion())

    def refresh_after_frozen(self):
        self.minions = self.frozen_minions
        self.frozen_minions = []
        for _ in range(self.tavern_sizes[self.tier] - len(self.minions)):
            self.minions.append(self.random_minion())

    def random_minion(self):
        return self.player.game.random_minion_from_pool(self.player.game.get_minion_pool(1, self.tier))(self.player)

    def next_turn(self):
        if self.tier < 6:
            self.upgrade_cost -= 1
            if self.upgrade_cost < 0:
                self.upgrade_cost = 0
        if len(self.frozen_minions) == 0:
            self.refresh()
        else:
            self.refresh_after_frozen()

    def remove_minion(self, tavern_index):
        minion = self.minions.pop(tavern_index)
        return minion

    def toggle_freeze(self):
        if len(self.frozen_minions) == 0:
            self.frozen_minions = self.minions
        else:
            self.frozen_minions = []

    def upgrade(self):
        self.tier += 1
        self.upgrade_cost = self.upgrade_base_costs[self.tier]
