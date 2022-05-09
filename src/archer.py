from time import sleep
from os import system, name
from colorama import init, Fore, Back, Style
# import random
import math
from numpy import minimum

from src.enemy import Enemy
from src.globals import *

class Archer(Enemy):
    def init(self, row, col):
        Enemy.__init__(self, row, col)

    # def move(self):
        # similar to that of barbarians

    # def range_attack(self, game):
        # same as king's range attack

    def update(self):
        self.char = 'A'
        self.speed = 2  # archer has twice the movement speed of a barbarian(1)
        # damage dealt by an archer is half the damage dealt by a barbarian(6)
        self.damage = 3
        # health of an archer is half the health of a barbarian(100)
        self.health = 50
        self.range = 6  # archer attacks similar to a canon(range = 5)

    def decide_target(self, game):
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
                        self.target_row = row
                        self.target_col = col
                        self.target_building = game.buildings[row][col]

    def move(self, game):

        self.decide_target(game)
        
        # make a move towards the target
        # 5 cases: move up, move down, move left, move right, attack(top/down/right/left)
        # troop cannot move if the building in range is not destroyed completely

        for i in range(self.speed):
            # check if target is in range
            distance = math.sqrt((self.curr_row - self.target_row)**2 + (self.curr_col - self.target_col)**2)
            
            if(distance <= self.range):
                self.target_building.destroy(self.damage)

            # else make a move towards the target

            elif(self.curr_row < self.target_row):

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


            elif(self.curr_row > self.target_row):
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
               

            elif(self.curr_col < self.target_col):
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

            elif(self.curr_col > self.target_col):
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
                pass
            return
