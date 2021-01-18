from game import Game

game = Game()
player1 = game.add_player("player1")
player2 = game.add_player("player2")

player = player1
while True:
    print()
    player.print_summary()
    action = input("Action: ")
    split = action.split(" ")

    if split[0] == "quit" or split[0] == "q":
        break
    elif split[0] == "switch" or split[0] == "sp":
        if player == player1:
            player = player2
            print("Switched to player2")
        else:
            player = player1
            print("Switched to player1")

    elif split[0] == "refresh" or split[0] == "r":
        player.refresh()
    elif split[0] == "freeze" or split[0] == "f":
        player.toggle_freeze()
    elif split[0] == "upgrade" or split[0] == "u":
        player.upgrade_tavern()
    elif split[0] == "end" or split[0] == "e":
        player.end_turn()

    else:
        if len(split) < 2 or not split[1].isdigit():
            print("Failed")
            continue

        if split[0] == "buy" or split[0] == "b":
            player.buy_minion(int(split[1]))
        elif split[0] == "play" or split[0] == "p":
            player.play_minion(int(split[1]))
        elif split[0] == "sell" or split[0] == "s":
            player.sell_minion(int(split[1]))

        else:
            if len(split) < 3 or not split[2].isdigit():
                print("Failed")
                continue

            elif split[0] == "reorder" or split[0] == "drag" or split[0] == "d":
                player.reorder_minion(int(split[1]), int(split[2]))
