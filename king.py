from time import sleep
from os import system, name
from colorama import init, Fore, Back, Style
import random
import math

from enemy import Enemy
from globals import *

class King(Enemy):
    # user-controlled character capable of attacking and destroying buildings
    def __init__(self, curr_row, curr_col):
        Enemy.__init__(self, curr_row, curr_col)
        self.damage = 10  # the damage each attack of the king deals to a building
        # self.health = 100
        # self.dead = False
        # self.speed = 1  # the distance that the king moves in each time step
        self.char = 'K'
        # self.curr_row = curr_row
        # self.curr_col = curr_col
        self.last_move = ''
        self.range = 5

    # def get_health(self):
    #     return self.health

    # def render(self, game):
    #     if(self.dead == False):
    #         game.update_king_tile(self.curr_row, self.curr_col, self.char)

    # def double_speed(self):
    #     self.speed = self.speed * 2

    # def double_damage(self):
    #     self.damage = self.damage * 2

    # def heal_health(self):
    #     updated_health = 1.5*self.health
    #     if(updated_health >= 100):
    #         self.health = 100
    #         return
    #     self.health = updated_health

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

        if(self.last_move == 'w'):
            if(game.buildings[self.curr_row - 1][self.curr_col] != -1 and game.buildings[self.curr_row - 1][self.curr_col] != 0):
                #print(game.buildings[self.curr_row - 1][self.curr_col])
                game.buildings[self.curr_row -
                               1][self.curr_col].destroy(self.damage)

        if(self.last_move == 'a'):
            if(game.buildings[self.curr_row][self.curr_col - 1] != -1 and game.buildings[self.curr_row][self.curr_col - 1] != 0):
                #print(game.buildings[self.curr_row][self.curr_col - 1])
                game.buildings[self.curr_row][self.curr_col -
                                              1].destroy(self.damage)

        if(self.last_move == 's'):
            if(game.buildings[self.curr_row + 1][self.curr_col] != -1 and game.buildings[self.curr_row + 1][self.curr_col] != 0):
                #print(game.buildings[self.curr_row + 1][self.curr_col])
                game.buildings[self.curr_row +
                               1][self.curr_col].destroy(self.damage)

        if(self.last_move == 'd'):
            if(game.buildings[self.curr_row][self.curr_col + 1] != -1 and game.buildings[self.curr_row][self.curr_col + 1] != 0):
                #print(game.buildings[self.curr_row][self.curr_col + 1])
                game.buildings[self.curr_row][self.curr_col +
                                              1].destroy(self.damage)

    def range_attack(self, game):
        # area of effect attack
        # attack all buildings in a specific vicinity (radius = self.range = 5)
        
        attacked = []

        for r in range(rows):
            for c in range(columns):
                if(game.buildings[r][c] != -1 and game.buildings[r][c] != 0):
                    delta_x = (r - self.curr_row)**2
                    delta_y = (c - self.curr_col)**2
                    distance = math.sqrt(delta_x + delta_y)

                    if(distance <= self.range):
                        if(game.buildings[r][c] not in attacked):
                            game.buildings[r][c].destroy(self.damage)
                            attacked.append(game.buildings[r][c])