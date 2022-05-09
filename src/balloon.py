from time import sleep
from os import system, name
from colorama import init, Fore, Back, Style
import math
from numpy import minimum

from src.enemy import Enemy
from src.globals import *

# ariel troop
# walls and buildings do not affect its movement
# certain defensive buildings can’t attack it

# attack chronology - canon, wizard tower -> townhall, hut


class Balloon(Enemy):
    def init(self, row, col):
        Enemy.__init__(self, row, col)

    def update(self):
        self.char = 'O'
        self.speed = 2  # twice barbarian
        self.damage = 12  # twice barbarians(6)
        self.health = 100  # same as barbarians

    def move(self, game):

        # Balloons can fly over walls and other buildings
        # once they select a building to attack
        # they can move to said building without caring about the presence of walls or other buildings in their path

        # find the nearest defensive building if possible

        minimum_distance = 100.0
        target_row = 13
        target_col = 26
        flag = 0

        for row in range(rows):
            for col in range(columns):
                if(game.buildings[row][col] != 0 and game.buildings[row][col] != -1 and game.buildings[row][col].type != 1 and game.buildings[row][col].destroyed == False and game.buildings[row][col].is_defensive):
                    distance = math.sqrt(
                        (self.curr_row - row)**2 + (self.curr_col - col)**2)
                    if(distance < minimum_distance):
                        flag = 1
                        minimum_distance = distance
                        target_row = row
                        target_col = col
                        target_building = game.buildings[row][col]

        if flag == 0:
            for row in range(rows):
                for col in range(columns):
                    if(game.buildings[row][col] != 0 and game.buildings[row][col] != -1 and game.buildings[row][col].type != 1 and game.buildings[row][col].destroyed == False):
                        distance = math.sqrt(
                            (self.curr_row - row)**2 + (self.curr_col - col)**2)
                        if(distance < minimum_distance):
                            flag = 1
                            minimum_distance = distance
                            target_row = row
                            target_col = col
                            target_building = game.buildings[row][col]

        if flag == 0:
            return

        # make a move towards the target
        # 5 cases: move up, move down, move left, move right, attack

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
                    elif(game.buildings[self.curr_row + 1][self.curr_col] != target_building):
                        # there is a wall or any building other than the target in the way
                        self.curr_row += 1
                        continue
                    elif(game.buildings[self.curr_row + 1][self.curr_col] == target_building):
                        # it is a building
                        # should be our target
                        game.buildings[self.curr_row +
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
                    elif(game.buildings[self.curr_row][self.curr_col + 1] != target_building):
                        # there is a wall or any building other than the target in the way
                        self.curr_col += 1
                        continue
                    elif(game.buildings[self.curr_row][self.curr_col + 1] == target_building):
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
                    elif(game.buildings[self.curr_row][self.curr_col - 1] != target_building):
                        # there is a wall or any building other than the target in the way
                        self.curr_col -= 1
                        continue
                    elif(game.buildings[self.curr_row][self.curr_col - 1] == target_building):
                        # it is a building
                        # should be our target
                        game.buildings[self.curr_row][self.curr_col -
                                                    1].destroy(self.damage)
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
                    elif(game.buildings[self.curr_row - 1][self.curr_col] != target_building):
                        # there is a wall or any building other than the target in the way
                        self.curr_row -= 1
                        continue
                    elif(game.buildings[self.curr_row - 1][self.curr_col] == target_building):
                        # it is a building
                        # should be our target
                        game.buildings[self.curr_row -
                                    1][self.curr_col].destroy(self.damage)
                        break
