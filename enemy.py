from time import sleep
from os import system, name
from colorama import init, Fore, Back, Style
import random
import math

from globals import *

class Enemy:
    def __init__(self, curr_row, curr_col):
        self.damage = 0
        self.health = 100
        self.dead = False
        self.speed = 1
        self.char = ' '
        self.curr_row = curr_row
        self.curr_col = curr_col
        # king
        # self.last_move = '' # w, a, s, d
        # self.range = 5

    def get_health(self):
        return self.health

    # def render(self, game):
    #     if(self.dead == False):
    #         game.update_king_tile(self.curr_row, self.curr_col, self.char)
    
    def render(self, game):
        if(self.dead == False):
            game.update_troop_tile(
                self.curr_row, self.curr_col, self.char, self.health, self)

    def double_speed(self):
        if(self.speed < 4):
            self.speed = self.speed * 2

    def double_damage(self):
        if(self.damage < 32):
            self.damage = self.damage * 2

    def heal_health(self):
        updated_health = 1.5*self.health
        if(updated_health >= 100):
            self.health = 100
            return
        self.health = updated_health