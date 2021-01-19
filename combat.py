import random
import copy
from player import Player
from minion import *

def combat(player1, player2):
    print()
    print(f"Combat player1: " + ", ".join([str(minion) for minion in player1.board.minions]))
    print(f"Combat player2: " + ", ".join([str(minion) for minion in player2.board.minions]))

    # id 0 is player1, id 1 is player2
    num_combats = 1000
    display_first_fight = True
    wins = [[], []]
    ties = 0
    for game in range(num_combats):
        which_players_turn = random.randint(0, 1)
        enemy_player = 1 if which_players_turn == 0 else 0
        player1_minions = copy.deepcopy(player1.board.minions)
        player2_minions = copy.deepcopy(player2.board.minions)
        minions_alive = [player1_minions, player2_minions]

        for player in [0, 1]:
            for minion in minions_alive[player]:
                minion.start_combat()

        while True:
            if len(minions_alive[which_players_turn]) == 0 or len(minions_alive[enemy_player]) == 0:
                break

            minion_thats_attacking = None
            for minion in minions_alive[which_players_turn]:
                if not minion.attacked_this_round:
                    minion_thats_attacking = minion
                    break

            enemies_with_taunt = []
            for enemy_minion in minions_alive[enemy_player]:
                if enemy_minion.taunt:
                    enemies_with_taunt.append(enemy_minion)
            enemy_target = None
            if len(enemies_with_taunt) > 0:
                enemy_target = random.choice(enemies_with_taunt)
            else:
                enemy_target = random.choice(minions_alive[enemy_player])

            summary = f"{str(minion_thats_attacking)} attacked {str(enemy_target)}"

            minions_died = []
            for take_damage_minion in [[minion_thats_attacking, enemy_target, which_players_turn], [enemy_target, minion_thats_attacking, enemy_player]]:
                if take_damage_minion[0].divine_shield and take_damage_minion[1].attack > 0:
                    take_damage_minion[0].divine_shield = False
                    summary += f", {str(take_damage_minion[0])} lost divine shield"
                else:
                    take_damage_minion[0].health -= take_damage_minion[1].attack
                    if take_damage_minion[0].health <= 0:
                        minions_alive[take_damage_minion[2]].remove(take_damage_minion[0])
                        minions_died.append(take_damage_minion)
                        summary += f", {str(take_damage_minion[0])} died"

            summary += f", now {str(minion_thats_attacking)} and {str(enemy_target)}"

            for take_damage_minion in minions_died:
                for minion in minions_alive[take_damage_minion[2]]:
                    minion.other_minion_die(take_damage_minion[0])

            if display_first_fight:
                print(summary)

            minion_thats_attacking.attacked_this_round = True

            which_players_turn = 1 if which_players_turn == 0 else 0
            enemy_player = 1 if which_players_turn == 0 else 0

        if len(minions_alive[0]) == 0 and len(minions_alive[1]) == 0:
            ties += 1
            if display_first_fight:
                print("Tie")
        elif len(minions_alive[0]) == 0:
            damage = 0
            for minion in minions_alive[1]:
                damage += minion.tavern_tier
            damage += player2.tavern.tier
            wins[1].append(damage)
            if display_first_fight:
                print(f"player1 takes {damage} damage")
        else:
            damage = 0
            for minion in minions_alive[0]:
                damage += minion.tavern_tier
            damage += player1.tavern.tier
            wins[0].append(damage)
            if display_first_fight:
                print(f"player2 takes {damage} damage")

        if display_first_fight:
            display_first_fight = False

    player1_win_perc = len(wins[0]) / num_combats
    player2_win_perc = len(wins[1]) / num_combats
    player1_average_take_damage = int(round(sum(wins[1]) / num_combats))
    player2_average_take_damage = int(round(sum(wins[0]) / num_combats))
    player1.take_damage(player1_average_take_damage)
    player2.take_damage(player2_average_take_damage)
    print(f"{player1_win_perc} player1 win, take {player1_average_take_damage} dmg to {player1.health}; {player2_win_perc} player2 win, take {player2_average_take_damage} dmg to {player2.health}; {ties / num_combats} tie")
