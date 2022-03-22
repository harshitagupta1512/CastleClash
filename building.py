from time import sleep
from os import system, name
from tracemalloc import start
from colorama import init, Fore, Back, Style
import random
import math

from numpy import true_divide 

# from input import *
# from game import Game
# from spell import Spell, Rage, Heal
from globals import *
# from king import King
#from troop import Troop

# Inheritance and Polymorphism
class Building:
    def __init__(self):
        # default
        self.destroyed = False
        self.health = 100
        self.width = 0
        self.height = 0
        self.char = ''
        self.start_row = 0 # default
        self.start_col = 0 # default
        self.type = 0 # 1 for wall

    def destroy(self, damage):
        self.health = self.health - damage
        if(self.health <= 0):
            self.destroyed = True

    def render(self, game, start_row, start_column):
        self.start_row = start_row
        self.start_col = start_column

        if (self.destroyed == False):
            for row in range(start_row, start_row + self.height):
                for column in range(start_column, start_column + self.width):
                    game.update_tile(row, column, self.char, self.health, self)

# defensive building
class Canon(Building):
    def __init__(self):
        Building.__init__(self)
        self.height = 1
        self.width = 1
        self.range = 10  # the area till which it can attack
        self.damage = 5  # amount of damage it yields to a single troop in a second
        self.char = 'C'

    def attack(self, game):
        self.king = game.get_king()
        self.troops = game.get_troops()
        
        if(self.check_range(self.king.curr_row, self.king.curr_col)):
            if(self.king.dead == False):
                self.king.health = self.king.health - self.damage
                if(self.king.health <= 0):
                    self.king.dead = True
                return

        for troop in self.troops:
            if(self.check_range(troop.curr_row, troop.curr_col)):
                if(troop.dead == False):
                    troop.health = troop.health - self.damage
                    if(troop.health <= 0):
                        troop.dead = True
                    return

    def check_range(self, enemy_row, enemy_col):
        delta_x = (enemy_row - self.start_row)**2
        delta_y = (enemy_col - self.start_col)**2
        distance = math.sqrt(delta_x + delta_y)
        if(distance < self.range):
            return True
        
        return False

class Townhall(Building):
    def __init__(self):
        Building.__init__(self)
        self.width = 3
        self.height = 4
        self.char = 'T'

class Hut(Building):
    def __init__(self):
        Building.__init__(self)
        self.width = 2
        self.height = 2
        self.char = 'H'

class Wall(Building):
    def __init__(self, row, col):
        Building.__init__(self)
        self.height = 1
        self.width = 1
        self.row = row
        self.col = col
        self.char = 'W'
        self.health = 10
        self.type = 1

    def render(self, game):
        if (self.destroyed == False):
            game.update_wall_tile(self.row, self.col, self.char, self)