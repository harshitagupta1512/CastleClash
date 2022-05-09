from time import sleep
from os import system, name
from colorama import init, Fore, Back, Style
# import random
import math
from numpy import minimum

from src.enemy import Enemy
from src.globals import *

class Barbarian(Enemy):
    def init(self, row, col):
        super().__init__(self, row, col)
        # self.limit = 6

    def update(self):
        self.char = 'B'
        self.speed = 1
        self.damage = 6
        self.health = 100

    def get_char(self):
        return self.char

    def move(self, game):
        # find the nearest building, decide target

        minimum_distance = 100.0
        target_row = 13
        target_col = 26

        for row in range(rows):
            for col in range(columns):
                # if building exists and is not a wall
                if(game.buildings[row][col] != 0 and game.buildings[row][col] != -1 and game.buildings[row][col].type != 1):
                    distance = math.sqrt(
                        (self.curr_row - row)**2 + (self.curr_col - col)**2)
                    if(distance < minimum_distance):
                        minimum_distance = distance
                        target_row = row
                        target_col = col
                        target_building = game.buildings[row][col]

        # make a move towards the target
        # 5 cases: move up, move down, move left, move right, attack(top/down/right/left)
        # troop cannot move if the building in range is not destroyed completely

        for i in range(self.speed):
            if(self.curr_row < target_row):
                
                    if(game.buildings[self.curr_row + 1][self.curr_col] == 0):
                        # reached the boundary
                        # impossible case
                        break
                    elif(game.buildings[self.curr_row + 1][self.curr_col] == -1):
                        # clear path
                        self.curr_row += 1
                        continue
                    elif(game.buildings[self.curr_row + 1][self.curr_col].type == 1):
                        # there is a wall in the way
                        game.buildings[self.curr_row +
                                    1][self.curr_col].destroy(self.damage)
                        self.curr_row += 1
                        break
                    else:
                        # it is a building
                        # should be our target
                        game.buildings[self.curr_row +
                                    1][self.curr_col].destroy(self.damage)
                        break
            elif(self.curr_row > target_row):
                # for i in range(self.speed):
                    if(game.buildings[self.curr_row - 1][self.curr_col] == 0):
                        # reached the boundary
                        # impossible case
                        break
                    elif(game.buildings[self.curr_row - 1][self.curr_col] == -1):
                        # clear path
                        self.curr_row -= 1
                        continue
                    elif(game.buildings[self.curr_row - 1][self.curr_col].type == 1):
                        # there is a wall in the way
                        game.buildings[self.curr_row -
                                    1][self.curr_col].destroy(self.damage)
                        self.curr_row -= 1
                        break
                    else:
                        # it is a building
                        # should be our target
                        game.buildings[self.curr_row -
                                    1][self.curr_col].destroy(self.damage)
                        break
            elif(self.curr_col < target_col):
                # for i in range(self.speed):
                    if(game.buildings[self.curr_row][self.curr_col + 1] == 0):
                        # reached the boundary
                        # impossible case
                        break
                    elif(game.buildings[self.curr_row][self.curr_col + 1] == -1):
                        # clear path
                        self.curr_col += 1
                        continue
                    elif(game.buildings[self.curr_row][self.curr_col + 1].type == 1):
                        # there is a wall in the way
                        game.buildings[self.curr_row][self.curr_col +
                                                    1].destroy(self.damage)
                        self.curr_col += 1
                        break
                    else:
                        # it is a building
                        # should be our target
                        game.buildings[self.curr_row][self.curr_col +
                                                    1].destroy(self.damage)
                        break
            elif(self.curr_col > target_col):
                # for i in range(self.speed):
                    if(game.buildings[self.curr_row][self.curr_col - 1] == 0):
                        # reached the boundary
                        # impossible case
                        break
                    elif(game.buildings[self.curr_row][self.curr_col - 1] == -1):
                        # clear path
                        self.curr_col -= 1
                        continue
                    elif(game.buildings[self.curr_row][self.curr_col - 1].type == 1):
                        # there is a wall in the way
                        game.buildings[self.curr_row][self.curr_col -
                                                    1].destroy(self.damage)
                        self.curr_col -= 1
                        break
                    else:
                        # it is a building
                        # should be our target
                        game.buildings[self.curr_row][self.curr_col -
                                                    1].destroy(self.damage)
                        break
            else:
                pass
            return
