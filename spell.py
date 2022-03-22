from time import sleep
from os import system, name
from colorama import init, Fore, Back, Style
import random

# from input import *
# from building import Building, Townhall, Hut, Canon, Wall
from globals import *
# from king import King
# from troop import Troop
# from game import Game

class Spell:
    def __init__(self, game):
        self.troops = game.get_troops()
        self.king = game.get_king()


class Rage(Spell):
    # doubles the movement speed and damage of the king and every troop alive in the game
    def __init__(self, game):
        Spell.__init__(self, game)

    def cast(self):
        for t in self.troops:
            if(t.dead == False):
                t.double_speed()
                t.double_damage()

        if(self.king.dead == False):
            self.king.double_speed()
            self.king.double_damage()


class Heal(Spell):
    def __init__(self, game):  # increases the health of every alive troop and the king to 150% of the current health (capped at 100.0)
        Spell.__init__(self, game)

    def cast(self):
        for t in self.troops:
            if(t.dead == False):
                t.heal_health()

        if(self.king.dead == False):
            self.king.heal_health()