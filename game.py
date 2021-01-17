import random
from player import Player
from minion import *

class Game:
    # Index is tier, index 0 is undefined
    minion_pool_size = [None, 16, 15, 13, 11, 9, 7]

    def __init__(self):
        self.players = []

        self.minion_pool = {}
        for cls in Minion.__subclasses__():
            self.minion_pool[cls.name] = self.minion_pool_size[cls.tavern_tier]
            # print(f"{cls.name} {self.minion_pool[cls.name]}")

    def add_player(self):
        player = Player(self)
        self.players.append(player)
        return player

    def get_minion_class(self, name):
        for cls in Minion.__subclasses__():
            if cls.name == name:
                return cls
        return False

    def get_minion_pool(self, min_tavern_tier, max_tavern_tier):
        minion_pool = {}
        for key, value in self.minion_pool.items():
            cls = self.get_minion_class(key)
            if not cls.in_tavern:
                continue
            if cls.tavern_tier >= min_tavern_tier and cls.tavern_tier <= max_tavern_tier:
                minion_pool[cls.name] = self.minion_pool[cls.name]
        return minion_pool

    def random_minion_from_pool(self, minion_pool):
        sum = 0
        for key, value in minion_pool.items():
            sum += value
        chosen = random.randrange(1, sum)
        sum = 0
        for key, value in minion_pool.items():
            sum += value
            if chosen <= sum:
                return self.get_minion_class(key)
        return False
