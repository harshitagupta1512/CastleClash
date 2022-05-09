from socket import timeout
from src.game import Game
from src.globals import *
import time
from os import system, name
from time import sleep


timeout = 0.9


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def replay():

    # file.close()
    file = open("replays/replay.txt", "r")
    player = int(file.readline()[0])

    game = Game(player, 1)

    for line in file:

        # frames += 1
        # time.sleep(timeout)

        if(line == " \n"):
            command = ' '
        else:
            command = line.strip()

        if(command == 'w'):
            game.move_king(1)
        if(command == 'a'):
            game.move_king(2)
        if(command == 's'):
            game.move_king(3)
        if(command == 'd'):
            game.move_king(4)
        if(command == ' '):
            game.attack_king()
        if command == 'r':
            game.spell_rage()
            # timeout /= 2
            # rageMultiplier *= 2
        if(command == 'h'):
            game.spell_heal()

        if command == '1':
            game.spawn_troop(1)
        if command == '2':
            game.spawn_troop(2)

        if command == '3':
            game.spawn_troop(3)

        if command == '4':
            game.spawn_troop(4)

        if command == '5':
            game.spawn_troop(5)

        if command == '6':
            game.spawn_troop(6)

        if command == '7':
            game.spawn_troop(7)

        if command == '8':
            game.spawn_troop(8)

        if command == '9':
            game.spawn_troop(9)

        if(command == 'e'):
            break

        if(command == '0'):
            break

        if command == 'q':
            game.range_attack_king()

        if command == 'g':
            # queen's eagle attack
            game.king.eagle_attack()

        if(game.check_victory()):
            clear()
            if(game.level == 1):
                print("Level 2")
                sleep(2)
                # level = 2
                game = Game(game.player, 2)
            elif(game.level == 2):
                print("Level 3")
                sleep(2)
                # level = 3
                game = Game(game.player, 3)
            else:
                print("You have won")
            break

        if(game.check_defeat()):
            print("You have lost")
            break

        # if frames % rageMultiplier == 0:
        for canon in game.canons:
            if(canon.destroyed == False):
                canon.attack(game)

        # if frames % rageMultiplier == 0:
        for tower in game.towers:
            if(tower.destroyed == False):
                tower.attack(game)

        for troop in game.troops:
            if(troop.dead == False):
                troop.move(game)

        for archer in game.archers:
            if(archer.dead == False):
                archer.move(game)

        for balloon in game.balloons:
            if(balloon.dead == False):
                balloon.move(game)

        sleep(timeout)

        game.update()

    file.close()


replay()
