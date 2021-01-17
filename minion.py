class Minion:
    in_tavern = True

    def __init__(self, player):
        self.player = player
        self.attack = self.base_attack
        self.health = self.base_health

    def __str__(self):
        return f"{self.attack}/{self.health} {self.name}"

    def battlecry(self):
        return

    def play_other_minion(self, minion):
        self.summon_other_minion(minion)
        return

    def summon_other_minion(self, minion):
        return

    def sell(self):
        return

    def start_turn(self):
        return

    def end_turn(self):
        return

class Alleycat(Minion):
    name = "Alleycat"
    tavern_tier = 1
    type = "Beast"
    base_attack = 1
    base_health = 1

    def __init__(self, player):
        super().__init__(player)

    def battlecry(self):
        super().battlecry()
        self.player.board.add_minion(Tabbycat(self.player), False)

class Tabbycat(Minion):
    name = "Tabbycat"
    tavern_tier = 1
    type = "Beast"
    base_attack = 1
    base_health = 1

    in_tavern = False

    def __init__(self, player):
        super().__init__(player)
        self.in_tavern = False

class Scavenging_Hyena(Minion):
    name = "Scavenging Hyena"
    tavern_tier = 1
    type = "Beast"
    base_attack = 2
    base_health = 2

    def __init__(self, player):
        super().__init__(player)

class Fiendish_Servant(Minion):
    name = "Fiendish Servant"
    tavern_tier = 1
    type = "Demon"
    base_attack = 2
    base_health = 1

    def __init__(self, player):
        super().__init__(player)

class Vulgar_Homunculus(Minion):
    name = "Vulgar Homunculus"
    tavern_tier = 1
    type = "Demon"
    base_attack = 2
    base_health = 4

    def __init__(self, player):
        super().__init__(player)

    def battlecry(self):
        super().battlecry()
        self.player.take_damage(2)

class Wrath_Weaver(Minion):
    name = "Wrath Weaver"
    tavern_tier = 1
    type = "None"
    base_attack = 1
    base_health = 3

    def __init__(self, player):
        super().__init__(player)

    def play_other_minion(self, minion):
        super().play_other_minion(minion)
        if minion.type == "Demon":
            self.player.take_damage(1)
            self.attack += 2
            self.health += 2

class Dragonspawn_Lieutenant(Minion):
    name = "Dragonspawn Lieutenant"
    tavern_tier = 1
    type = "Dragon"
    base_attack = 2
    base_health = 3

    def __init__(self, player):
        super().__init__(player)

class Red_Whelp(Minion):
    name = "Red Whelp"
    tavern_tier = 1
    type = "Dragon"
    base_attack = 1
    base_health = 2

    def __init__(self, player):
        super().__init__(player)

class Refreshing_Anomaly(Minion):
    name = "Refreshing Anomaly"
    tavern_tier = 1
    type = "Elemental"
    base_attack = 1
    base_health = 3

    def __init__(self, player):
        super().__init__(player)

    def battlecry(self):
        super().battlecry()
        if self.player.free_refreshs == 0:
            self.player.free_refreshs = 1

class Sellemental(Minion):
    name = "Sellemental"
    tavern_tier = 1
    type = "Elemental"
    base_attack = 2
    base_health = 2

    def __init__(self, player):
        super().__init__(player)

    def sell(self):
        super().sell()
        self.hand.add_minion(Water_Droplet(player))

class Water_Droplet(Minion):
    name = "Water Droplet"
    tavern_tier = 1
    type = "Elemental"
    base_attack = 2
    base_health = 2

    in_tavern = False

    def __init__(self, player):
        super().__init__(player)

class Micro_Machine(Minion):
    name = "Micro Machine"
    tavern_tier = 1
    type = "Mech"
    base_attack = 1
    base_health = 2

    def __init__(self, player):
        super().__init__(player)

    def start_turn(self):
        super().start_turn()
        self.attack += 1

class Micro_Mummy(Minion):
    name = "Micro Mummy"
    tavern_tier = 1
    type = "Mech"
    base_attack = 1
    base_health = 2

    def __init__(self, player):
        super().__init__(player)

class Murloc_Tidecaller(Minion):
    name = "Murloc Tidecaller"
    tavern_tier = 1
    type = "Murloc"
    base_attack = 1
    base_health = 2

    def __init__(self, player):
        super().__init__(player)

    def summon_other_minion(self, minion):
        super().summon_other_minion(minion)
        if minion.type == "Murloc":
            self.attack += 1

class Murloc_Tidehunter(Minion):
    name = "Murloc Tidehunter"
    tavern_tier = 1
    type = "Murloc"
    base_attack = 2
    base_health = 1

    def __init__(self, player):
        super().__init__(player)

    def battlecry(self):
        super().battlecry()
        self.player.board.add_minion(Murloc_Scout(self.player), False)

class Murloc_Scout(Minion):
    name = "Murloc Scout"
    tavern_tier = 1
    type = "Murloc"
    base_attack = 1
    base_health = 1

    in_tavern = False

    def __init__(self, player):
        super().__init__(player)

class Rockpool_Hunter(Minion):
    name = "Rockpool Hunter"
    tavern_tier = 1
    type = "Murloc"
    base_attack = 2
    base_health = 3

    def __init__(self, player):
        super().__init__(player)

class Deck_Swabbie(Minion):
    name = "Deck Swabbie"
    tavern_tier = 1
    type = "Pirate"
    base_attack = 2
    base_health = 2

    def __init__(self, player):
        super().__init__(player)

class Scallywag(Minion):
    name = "Scallywag"
    tavern_tier = 1
    type = "Pirate"
    base_attack = 2
    base_health = 1

    def __init__(self, player):
        super().__init__(player)