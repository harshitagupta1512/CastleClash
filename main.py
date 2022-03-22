from telnetlib import GA
from time import sleep
from os import system, name
import time
from colorama import init, Fore, Back, Style
import random

from input import *
# from building import Building, Townhall, Hut, Canon, Wall
# from spell import Spell, Rage, Heal
from globals import rows, columns
# from king import King
# from troop import Troop
from game import Game


def main():

    init()
    game = Game()
    timestep = 0
    file = open("replay.txt", "w")  # file object in write mode

    while(1):

        timestep = timestep + 1
        command = input_to(Get(), 1)

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
            # print("King attacks")
            game.attack_king()

        if command == 'r':
            game.spell_rage()

        if command == 'h':
            game.spell_heal()

        if command == '1':
            # print("Pressed 1")
            game.spawn_troop(1)

        if command == '2':
            # print("Pressed 2")
            game.spawn_troop(2)

        if command == '3':
            game.spawn_troop(3)

        if command == 'e':

            # replay_timestep = 0
            game_replay = Game()

            file.close()
            file = open("replay.txt", "r")

            for line in file:

                # replay_timestep = replay_timestep + 1

                if(line == " \n"):
                    command = ' '
                else:
                    command = line.strip()

                #print(command)

                if(command == 'w'):
                    game_replay.move_king(1)
                if(command == 'a'):
                    game_replay.move_king(2)
                if(command == 's'):
                    game_replay.move_king(3)
                if(command == 'd'):
                    game_replay.move_king(4)

                if(command == ' '):
                    game_replay.attack_king()
                if(command == 'r'):
                    game_replay.spell_rage()
                if(command == 'h'):
                    game_replay.spell_heal()
                if(command == '1'):
                    game_replay.spawn_troop(1)
                if(command == '2'):
                    game_replay.spawn_troop(2)
                if(command == '3'):
                    game_replay.spawn_troop(3)

                if(command == 'e'):
                    # end replay
                    break

                if(command == '0'):
                    break

                if command == 'q':
                    game_replay.range_attack_king()

                if(game_replay.check_victory()):
                    print("You have won")
                    break

                if(game_replay.check_defeat()):
                    print("You have lost")
                    break

                # if(timestep % 2 == 0):

                if(game_replay.canon1.destroyed == False):
                    game_replay.canon1.attack(game_replay)

                if(game_replay.canon2.destroyed == False):
                    game_replay.canon2.attack(game_replay)

                for troop in game_replay.troops:
                    if(troop.dead == False):
                        troop.move(game_replay)

                game_replay.update()
                
                # replay_timestep = 0

                sleep(0.5)

            # clear()
            file.close()
            # open replay.txt again in append mode
            file = open("replay.txt", "a")

        if command == 'q':
            game.range_attack_king()

        if(game.check_victory()):
            print("You have won")
            break

        if(game.check_defeat()):
            print("You have lost")
            break

        if(timestep % 2 == 0):
            if(game.canon1.destroyed == False):
                game.canon1.attack(game)

            if(game.canon2.destroyed == False):
                game.canon2.attack(game)

            for troop in game.troops:
                if(troop.dead == False):
                    troop.move(game)

            game.update()
            timestep = 0


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


if __name__ == "main":
    main()

main()

# automated troop attack
# automated troop movement
# for movement.speed > 1

# sound effect
# upgrade displays
# review replay
