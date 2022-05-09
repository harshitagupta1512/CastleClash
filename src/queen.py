from errno import EEXIST
from time import sleep
from os import system, name
from xml.dom.pulldom import END_ELEMENT
from colorama import init, Fore, Back, Style
# import random
import math
from numpy import minimum

from src.globals import *
from src.enemy import Enemy

class Queen(Enemy):
    def __init__(self, row, col):
        Enemy.__init__(self, row, col)
        # health, dead, curr_row, curr_col

        self.char = 'Q'
        self.speed = 1  # same as king(1)

        self.last_move = 'w'
        self.range = 5
        self.damage = 30  # less than king(10)
        # health is same as king's(100)
        self.radius = 8

    def move(self, game, c):

        updated_row = self.curr_row
        updated_col = self.curr_col

        # w
        if(c == 1):
            updated_row = self.curr_row - self.speed
            self.last_move = 'w'
            for row in range(self.curr_row - self.speed, self.curr_row):
                if(row >= 0 and row <= rows - 1):
                    if(game.grid[row][self.curr_col] != Back.CYAN + "." + Style.RESET_ALL):
                        return

        # a
        if(c == 2):
            updated_col = self.curr_col - self.speed
            self.last_move = 'a'
            for col in range(self.curr_col - self.speed, self.curr_col):
                if(col >= 0 and col <= columns - 1):
                    if(game.grid[self.curr_row][col] != Back.CYAN + "." + Style.RESET_ALL):
                        return

        # s
        if(c == 3):
            updated_row = self.curr_row + self.speed
            self.last_move = 's'
            for row in range(self.curr_row + 1, self.curr_row + self.speed + 1):
                if(row >= 0 and row <= rows - 1):
                    if(game.grid[row][self.curr_col] != Back.CYAN + "." + Style.RESET_ALL):
                        return

        # d
        if(c == 4):
            updated_col = self.curr_col + self.speed
            self.last_move = 'd'
            for col in range(self.curr_col + 1, self.curr_col + self.speed + 1):
                if(col >= 0 and col <= columns - 1):
                    if(game.grid[self.curr_row][col] != Back.CYAN + "." + Style.RESET_ALL):
                        return

        if(updated_row >= rows - 1 or updated_col <= 0):
            return

        if(updated_col >= columns - 1 or updated_col <= 0):
            return

        game.update_king_tile(updated_row, updated_col, self.char)
        self.curr_row = updated_row
        self.curr_col = updated_col

    def attack(self, game):
        self.range = 5
        self.radius = 8
        
        if(self.last_move == 'w'):
            attack_centre_x = self.curr_row - self.radius
            attack_centre_y = self.curr_col
        elif(self.last_move == 'a'):
            attack_centre_x = self.curr_row
            attack_centre_y = self.curr_col - self.radius
        elif(self.last_move == 's'):
            attack_centre_x = self.curr_row + self.radius
            attack_centre_y = self.curr_col
        elif(self.last_move == 'd'):
            attack_centre_x = self.curr_row
            attack_centre_y = self.curr_col + self.radius

        # similar to king's range attack

        attacked = []
        for r in range(rows):
            for c in range(columns):
                if(game.buildings[r][c] != -1 and game.buildings[r][c] != 0):
                    delta_x = (r - attack_centre_x)**2
                    delta_y = (c - attack_centre_y)**2
                    distance = math.sqrt(delta_x + delta_y)

                    if(distance <= self.range):
                        if(game.buildings[r][c] not in attacked):
                            game.buildings[r][c].destroy(self.damage)
                            attacked.append(game.buildings[r][c])

    def eagle_attack(self, game):
        self.range = 9
        self.radius = 16
        sleep(1)
        if(self.last_move == 'w'):
            attack_centre_x = self.curr_row - self.radius
            attack_centre_y = self.curr_col
        elif(self.last_move == 'a'):
            attack_centre_x = self.curr_row
            attack_centre_y = self.curr_col - self.radius
        elif(self.last_move == 's'):
            attack_centre_x = self.curr_row + self.radius
            attack_centre_y = self.curr_col
        elif(self.last_move == 'd'):
            attack_centre_x = self.curr_row
            attack_centre_y = self.curr_col + self.radius

        # similar to king's range attack

        attacked = []
        for r in range(rows):
            for c in range(columns):
                if(game.buildings[r][c] != -1 and game.buildings[r][c] != 0):
                    delta_x = (r - attack_centre_x)**2
                    delta_y = (c - attack_centre_y)**2
                    distance = math.sqrt(delta_x + delta_y)

                    if(distance <= self.range):
                        if(game.buildings[r][c] not in attacked):
                            game.buildings[r][c].destroy(self.damage)
                            attacked.append(game.buildings[r][c])

