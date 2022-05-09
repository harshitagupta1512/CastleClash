from time import sleep
from os import system, name
from tracemalloc import start
from colorama import init, Fore, Back, Style
import random
import math

from numpy import true_divide
from src.globals import *

class Building:
    def __init__(self):
        # default
        self.destroyed = False
        self.health = 100
        self.width = 0
        self.height = 0
        self.char = ''
        self.start_row = 0  # default
        self.start_col = 0  # default
        self.type = 0  # 1 for wall
        self.is_defensive = False

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
        self.range = 5  # the area till which it can attack
        self.damage = 10  # amount of damage it yields to a single troop in a second
        self.char = 'C'
        self.is_defensive = True

    def attack(self, game):

        self.king = game.get_king()

        if(self.king.dead == False):
            if(self.check_range(self.king.curr_row, self.king.curr_col)):
                self.king.health = self.king.health - self.damage
                if(self.king.health <= 0):
                    self.king.dead = True
                return

        for barbarian in game.barbarians:
            if(barbarian.dead == False):
                if(self.check_range(barbarian.curr_row, barbarian.curr_col)):
                    barbarian.health = barbarian.health - self.damage
                    if(barbarian.health <= 0):
                        barbarian.dead = True
                    return

        for archer in game.archers:
            if(archer.dead == False):
                if(self.check_range(archer.curr_row, archer.curr_col)):
                    archer.health = archer.health - self.damage
                    if(archer.health <= 0):
                        archer.dead = True
                    return

        # the cannon cannot attack aerial troops (balloon)

    def check_range(self, enemy_row, enemy_col):
        delta_x = (enemy_row - self.start_row)**2
        delta_y = (enemy_col - self.start_col)**2
        distance = math.sqrt(delta_x + delta_y)
        if(distance < self.range):
            return True

        return False

# defensive building


class Tower(Building):
    def __init__(self):
        Building.__init__(self)
        self.height = 1
        self.width = 1
        self.range = 5  # same as cannon
        self.damage = 10  # same as cannon
        self.char = 'T'
        self.is_defensive = True

    def check_range(self,centre_x, centre_y, enemy_x, enemy_y, range):
        delta_x = (enemy_x - centre_x)**2
        delta_y = (enemy_y - centre_y)**2
        distance = math.sqrt(delta_x + delta_y)
        if(distance < range):
            return True
        return False

    def range_attack(self, centre_x, centre_y, game):
        for barbarian in game.barbarians:
            if(barbarian.dead == False):
                if(self.check_range(centre_x, centre_y, barbarian.curr_row, barbarian.curr_col, 3)):
                    barbarian.health = barbarian.health - self.damage
                    if(barbarian.health <= 0):
                        barbarian.dead = True

        for archer in game.archers:
            if(archer.dead == False):
                if(self.check_range(centre_x, centre_y, archer.curr_row, archer.curr_col, 3)):
                    archer.health = archer.health - self.damage
                    if(archer.health <= 0):
                        archer.dead = True

        for balloon in game.balloons:
            if(balloon.dead == False):
                if(self.check_range(centre_x, centre_y, balloon.curr_row, balloon.curr_col, 3)):
                    balloon.health = balloon.health - self.damage
                    if(balloon.health <= 0):
                        balloon.dead = True

        if(self.king.dead == False):
            if(self.check_range(centre_x, centre_y, self.king.curr_row, self.king.curr_col, 3)):
                self.king.health = self.king.health - self.damage
                if(self.king.health <= 0):
                    self.king.dead = True

    def attack(self, game):

        self.king = game.get_king()

        if(self.king.dead == False):
            if(self.check_range(self.start_row, self.start_col, self.king.curr_row, self.king.curr_col, self.range)):
                self.king.health = self.king.health - self.damage
                if(self.king.health <= 0):
                    self.king.dead = True

                self.range_attack(self.king.curr_row, self.king.curr_col, game)

                return

        for barbarian in game.barbarians:
            if(barbarian.dead == False):
                if(self.check_range(self.start_row, self.start_col, barbarian.curr_row, barbarian.curr_col, self.range)):
                    barbarian.health = barbarian.health - self.damage
                    if(barbarian.health <= 0):
                        barbarian.dead = True

                    self.range_attack(barbarian.curr_row,
                                      barbarian.curr_col, game)
                    return

        for archer in game.archers:
            if(archer.dead == False):
                if(self.check_range(self.start_row, self.start_col, archer.curr_row, archer.curr_col, self.range)):
                    archer.health = archer.health - self.damage
                    if(archer.health <= 0):
                        archer.dead = True
                    self.range_attack(archer.curr_row, archer.curr_col, game)
                    return

        for balloon in game.balloons:
            if(balloon.dead == False):
                if(self.check_range(self.start_row, self.start_col, balloon.curr_row, balloon.curr_col, self.range)):
                    balloon.health = balloon.health - self.damage
                    if(balloon.health <= 0):
                        balloon.dead = True
                    self.range_attack(balloon.curr_row, balloon.curr_col, game)
                    return


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
        self.health = 3
        self.type = 1

    def render(self, game):
        if (self.destroyed == False):
            game.update_wall_tile(self.row, self.col, self.char, self)
