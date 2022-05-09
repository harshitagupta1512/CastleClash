from telnetlib import GA
from time import sleep
from os import system, name
import os
import time
from colorama import init, Fore, Back, Style
import random
from src.input import *
from src.globals import rows, columns
from src.game import Game

def main():

    player = 1
    level = 1

    # timeout = 0.10
    # frames = 0
    # rageMultiplier = 1

    init()
    print("Choose your character:")
    print("1. King")
    print("2. Queen")

    c = input()
    if c == '1':
        player = 1
    elif c == '2':
        player = 2
    else:
        print("Invalid Choice")
        exit

    file = open("replays/replay.txt", "w")  # file object in write mode
    game = Game(player, 1)

    file.write(str(player))
    file.write("\n")

    # timestep = 0
    # os.system("stty -echo")

    while(1):

        # frames += 1
        # input_time = time.time()
        # if timeout - (time.time() - input_time) >= 0:
        #     time.sleep(timeout - (time.time() - input_time))

        # timestep = timestep + 1
        command = input_to(Get())

        if(command != None):
            file.write(command)
            file.write("\n")

        if command == '0':
            print("You have exited")
            break

        if command == 'w':
            # print("You pressed w")

            game.move_king(1)

        if command == 'a':
            # print("You pressed a")

            game.move_king(2)

        if command == 's':
            # print("You pressed s")

            game.move_king(3)

        if command == 'd':
            # print("You pressed d")

            game.move_king(4)

        if command == ' ':
            # print("king attacks")
            game.attack_king()

        if command == 'r':
            game.spell_rage()
            # timeout /= 2
            # rageMultiplier *= 2

        if command == 'h':
            game.spell_heal()

        if command == '1':
            # print("Pressed 1")
            if game.total_barbarians>0:
                game.total_barbarians-=1
                game.spawn_troop(1)
            # spawn barbarian at spawining point 1

        if command == '2':
            # print("Pressed 2")
            if game.total_barbarians>0:
                game.total_barbarians-=1
                game.spawn_troop(2)
            # spawn barabrian at spawining point 2

        if command == '3':
            if game.total_barbarians>0:
                game.total_barbarians-=1
                game.spawn_troop(3)
            # spawn barbarian at spawining point 3

        if command == '4':
            if game.total_archers>0:
                game.total_archers-=1
                game.spawn_troop(4)
            # spawn archer at spawning point 1

        if command == '5':
            if game.total_archers>0:
                game.total_archers-=1
                game.spawn_troop(5)
            # spawn archer at spawning point 2

        if command == '6':
            if game.total_archers>0:
                game.total_archers-=1
                game.spawn_troop(6)
            # spawn archer at spawning point 3

        if command == '7':
            if game.total_balloons>0:
                game.total_balloons-=1
                game.spawn_troop(7)
            # spawn balloon at spawning point 1

        if command == '8':
            if game.total_balloons>0:
                game.total_balloons-=1
                game.spawn_troop(8)
            # spawn balloon at spawning point 2

        if command == '9':
            if game.total_balloons>0:
                game.total_balloons-=1
                game.spawn_troop(9)
            # spawn balloon at spawning point 3

        if command == 'q':
            game.range_attack_king()

        if command == 'g':
            # queen's eagle attack
            game.eagle_attack_queen()

        if(game.check_victory()):
            clear()
            if(game.level == 1):
                print("Level 2")
                sleep(2)
                # level = 2
                game = Game(player, 2)
            elif(game.level == 2):
                print("Level 3")
                sleep(2)
                # level = 3
                game = Game(player, 3)
            else:
                print("You have won")
                print("""\
       _      _                   
      (_)    | |                  
__   ___  ___| |_ ___  _ __ _   _ 
\ \ / / |/ __| __/ _ \| '__| | | |
 \   /| | (__| || (_) | |  | |_| |
  \_/ |_|\___|\__\___/|_|   \__, |
                             __/ |
                            |___/ 
""")
                break

        if(game.check_defeat()):
            clear()
            print("You have lost")
            print("""\
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
""")
            break

        # if(timestep % 2 == 0):
        # if frames % rageMultiplier == 0:

        for canon in game.canons:
            if(canon.destroyed == False):
                canon.attack(game)

        for tower in game.towers:
            if(tower.destroyed == False):
                tower.attack(game)

        for barbarian in game.barbarians:
            if(barbarian.dead == False):
                barbarian.move(game)

        for archer in game.archers:
            if(archer.dead == False):
                archer.move(game)

        for balloon in game.balloons:
            if(balloon.dead == False):
                balloon.move(game)

        game.update()


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


if __name__ == "main":
    main()

main()

#review everything
# timelag
# sound effect
# upgrade displays

# review replay
# replay.py and replays
# bonus (2) - BFS
