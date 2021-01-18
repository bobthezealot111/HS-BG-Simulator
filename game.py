import random
from player import Player
from minion import *
from combat import combat

class Game:
    # Index is tier, index 0 is undefined
    minion_pool_size = [None, 16, 15, 13, 11, 9, 7]
    minion_types = ["Beast", "Demon", "Dragon", "Elemental", "Mech", "Murloc", "Pirate"]

    def __init__(self):
        self.players = []
        self.players_ended_turn = []

        self.banned_minion_types = random.sample(set(self.minion_types), 2)
        print(f"Banned minion types: {self.banned_minion_types}")

        self.minion_pool = {}
        for cls in Minion.__subclasses__():
            if cls.name == "Wrath Weaver" and "Demon" in self.banned_minion_types:
                continue
            if cls.type not in self.banned_minion_types:
                self.minion_pool[cls.name] = self.minion_pool_size[cls.tavern_tier]
                # print(f"{cls.name} {self.minion_pool[cls.name]}")

    def add_player(self, name):
        player = Player(self, name)
        self.players.append(player)
        return player

    def player_end_turn(self, player):
        self.players_ended_turn.append(player)
        if len(self.players_ended_turn) == len(self.players):
            combat(self.players[0], self.players[1])

            for player in self.players:
                player.start_turn()
            self.players_ended_turn = []

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

    def remove_minion_from_pool(self, minion):
        self.minion_pool[minion.name] -= 1
        if self.minion_pool[minion.name] < 0:
            self.minion_pool[minion.name] = 0

    def add_minion_to_pool(self, minion):
        if minion.name in self.minion_pool:
            self.minion_pool[minion.name] += 1
