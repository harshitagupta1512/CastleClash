from time import sleep
from os import system, name
from colorama import init, Fore, Back, Style
import random
import math

from numpy import minimum

from globals import *
from enemy import Enemy


class Troop(Enemy):

    def __init__(self, row, col):
        Enemy.__init__(self, row, col)
        self.damage = 5  # the amount of damage it will yield per attack
        # Every troop attacks once per time step
        # self.health = 100
        # health - color [100 -> 0][dark -> light]
        # self.dead = False
        # self.speed = 1
        self.char = 'B'
        # self.curr_row = row
        # self.curr_col = col

    # def render(self, game):
    #     if(self.dead == False):
    #         game.update_troop_tile(
    #             self.curr_row, self.curr_col, self.char, self.health, self)

        # def move(self):

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

        if(game.buildings[self.curr_row + 1][self.curr_col] == target_building):
            target_building.destroy(self.damage)
            # self.curr_row += 1
        elif(game.buildings[self.curr_row - 1][self.curr_col] == target_building):
            target_building.destroy(self.damage)
            # self.curr_row -= 1
        elif(game.buildings[self.curr_row][self.curr_col + 1] == target_building):
            target_building.destroy(self.damage)
            # self.curr_col += 1
        elif(game.buildings[self.curr_row][self.curr_col - 1] == target_building):
            target_building.destroy(self.damage)
            # self.curr_col -= 1
        else:
            # move towards the target and destroy any wall in the way
            if(self.curr_row < target_row):
                if(game.buildings[self.curr_row + 1][self.curr_col] != -1 and game.buildings[self.curr_row + 1][self.curr_col] != 0):
                    if(game.buildings[self.curr_row + 1][self.curr_col].type == 1):
                        game.buildings[self.curr_row +
                                       1][self.curr_col].destroy(self.damage+5)
                self.curr_row += 1

            elif(self.curr_row > target_row):
                if(game.buildings[self.curr_row - 1][self.curr_col] != -1 and game.buildings[self.curr_row - 1][self.curr_col] != 0):
                    if(game.buildings[self.curr_row - 1][self.curr_col].type == 1):
                        game.buildings[self.curr_row -
                                       1][self.curr_col].destroy(self.damage+5)
                self.curr_row -= 1

            elif(self.curr_col < target_col):
                if(game.buildings[self.curr_row][self.curr_col + 1] != -1 and game.buildings[self.curr_row][self.curr_col + 1] != 0):
                    if(game.buildings[self.curr_row][self.curr_col + 1].type == 1):
                        game.buildings[self.curr_row][self.curr_col +
                                                      1].destroy(self.damage + 5)
                self.curr_col += 1

            elif(self.curr_col > target_col):
                if(game.buildings[self.curr_row][self.curr_col - 1] != -1 and game.buildings[self.curr_row][self.curr_col - 1] != 0):
                    if(game.buildings[self.curr_row][self.curr_col - 1].type == 1):
                        game.buildings[self.curr_row][self.curr_col -
                                                      1].destroy(self.damage + 5)
                self.curr_col -= 1

            else:
                pass

        return
