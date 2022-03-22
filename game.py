from time import sleep
from os import system, name
from colorama import init, Fore, Back, Style
import random

# from input import *
from building import Building, Townhall, Hut, Canon, Wall
from spell import Spell, Rage, Heal
from globals import *
from king import King
from troop import Troop

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
        

class Game:

    def __init__(self):
        # self.players = players
        self.grid = []
        self.king = King(26, 23)
        self.troops = []
        self.num_troops = 0
        self.buildings = []
        self.townhall = Townhall()
        self.hut1 = Hut()
        self.hut2 = Hut()
        self.hut3 = Hut()
        self.hut4 = Hut()
        self.hut5 = Hut()
        self.hut6 = Hut()
        self.canon1 = Canon()
        self.canon2 = Canon()
        self.walls = []
        self.create_walls()
        # 2D array of instances of class building

        for row in range(rows):
            str = []
            for col in range(columns):
                str.append(-1)
            self.buildings.append(str)

        self.update()

    def create_walls(self):
        for row in range(rows):
            for col in range(columns):
                if(row == 2 and col >= 5 and col <= 38):
                    w = Wall(row, col)
                    self.walls.append(w)
                    # w.render(self, row, col)

                if(row == 24 and col >= 5 and col <= 38):
                    w = Wall(row, col)
                    self.walls.append(w)
                    # w.render(self, row, col)

                if(col == 5 and row >= 2 and row <= 24):
                    w = Wall(row, col)
                    self.walls.append(w)
                    # w.render(self, row, col)

                if(col == 38 and row >= 2 and row <= 24):
                    w = Wall(row, col)
                    self.walls.append(w)
                    # w.render(self, row, col)

                if(row == 10 and col >= 20 and col <= 24):
                    w = Wall(row, col)
                    self.walls.append(w)
                    # w.render(self, row, col)

                if(row == 15 and col >= 20 and col <= 24):
                    w = Wall(row, col)
                    self.walls.append(w)
                    # w.render(self, row, col)

                if(col == 20 and row >= 10 and row <= 15):
                    w = Wall(row, col)
                    self.walls.append(w)
                    # w.render(self, row, col)

                if(col == 24 and row >= 10 and row <= 15):
                    w = Wall(row, col)
                    self.walls.append(w)
                    # w.render(self, row, col)

    def get_king_health(self):
        return(self.king.get_health())

    def get_troops(self):
        return(self.troops)

    def get_king(self):
        return(self.king)

    def display_king_health(self):
        health = self.get_king_health()
        if(self.king.dead == True):
            health = 0
        maxHealth = 100
        healthDashes = 20
        dashConvert = int(maxHealth/healthDashes)
        currentDashes = int(health/dashConvert)
        remainingHealth = healthDashes - currentDashes
        healthDisplay = '-' * currentDashes
        remainingDisplay = ' ' * remainingHealth
        percent = str(int((health/maxHealth)*100)) + "%"
        print("     King's Health")
        print("|" + healthDisplay + remainingDisplay + "|")
        print("         " + percent)

    # def update_canon_tile(self, row, column, char, building):
    #     self.grid[row][column] = Fore.BLUE + char + Style.RESET_ALL
    #     self.buildings[row][column] = building
    #     return

    def update_wall_tile(self, row, column, char, building):
        self.grid[row][column] = Back.WHITE + \
            Fore.BLACK + char + Style.RESET_ALL
        self.buildings[row][column] = building
        return

    def update_troop_tile(self, row, column, char, health, this_troop):

        if(health >= 50 and health <= 100):
            self.grid[row][column] = Back.WHITE + \
                Fore.RED + Style.BRIGHT + char + Style.RESET_ALL
            # self.buildings[row][column] = this_troop
            return

        if(health >= 20 and health <= 50):
            self.grid[row][column] = Back.CYAN + \
                Fore.RED + Style.NORMAL + char + Style.RESET_ALL
            # self.buildings[row][column] = this_troop
            return

        # health < 20
        self.grid[row][column] = Back.BLACK + \
            Fore.RED + Style.DIM + char + Style.RESET_ALL
        #self.buildings[row][column] = this_troop
        return

    def update_king_tile(self, row, column, char):
        self.grid[row][column] = Back.RED + char + Style.RESET_ALL
        # self.buildings[row][column] = self.king
        return

    def update_tile(self, row, column, char, health, building):

        if(health >= 50 and health <= 100):
            self.grid[row][column] = Fore.GREEN + char + Style.RESET_ALL
            self.buildings[row][column] = building
            return

        if(health >= 20 and health <= 50):
            self.grid[row][column] = Fore.YELLOW + char + Style.RESET_ALL
            self.buildings[row][column] = building
            return

        self.grid[row][column] = Fore.RED + char + Style.RESET_ALL
        self.buildings[row][column] = building
        return

    def move_king(self, c):
        self.king.move(self, c)
        self.update()

    def attack_king(self):
        self.king.attack(self)
        self.update()
    
    def range_attack_king(self):
        self.king.range_attack(self)
        self.update()

    def spell_rage(self):
        r = Rage(self)
        r.cast()
        self.update()

    def spell_heal(self):
        h = Heal(self)
        h.cast()
        self.update()

    def spawn_troop(self, c):

        self.num_troops = self.num_troops + 1

        if(c == 1):
            t = Troop(13, 2)
            self.troops.append(t)
            self.update()
            return

        if(c == 2):
            t = Troop(6, 42)
            self.troops.append(t)
            self.update()
            return

        # 3
        t = Troop(17, 41)
        self.troops.append(t)
        self.update()
        return

    def update(self):
        self.grid = []
        clear()

        self.empty_grid()
        print(self.draw_grid())
        self.display_king_health()

    def check_victory(self):
        if(self.townhall.destroyed == False):
            return(False)
        if(self.canon1.destroyed == False):
            return(False)
        if(self.canon2.destroyed == False):
            return(False)
        if(self.hut1.destroyed == False):
            return(False)
        if(self.hut2.destroyed == False):
            return(False)
        if(self.hut3.destroyed == False):
            return(False)
        if(self.hut4.destroyed == False):
            return(False)
        if(self.hut5.destroyed == False):
            return(False)

        return(True)

    def check_defeat(self):
        if(self.king.dead == False):
            return(False)
        for troop in self.troops:
            if(troop.dead == False):
                return(False)
        return(True)

    def draw_grid(self):
        print_s = "\n"
        self.townhall.render(self, 11, 21)
        self.hut1.render(self, 3, 3)
        self.hut2.render(self, 13, 34)
        self.hut3.render(self, 19, 19)
        self.hut4.render(self, 3, 29)
        self.hut5.render(self, 21, 7)
        self.canon1.render(self, 14, 10)
        self.canon2.render(self, 9, 30)
        self.king.render(self)

        if(self.num_troops > 0):
            for t in self.troops:
                t.render(self)

        for w in self.walls:
            w.render(self)

        for row in range(rows):
            for col in range(columns):
                print_s = print_s + self.grid[row][col]
            print_s = print_s + "\n"

        # print(self.buildings)

        return(print_s)

    def empty_grid(self):

        str = []
        for row in range(rows):
            str = []
            for col in range(columns):
                str.append(".")
            self.grid.append(str)

        for row in range(rows):
            for i in range(columns):

                # Grid boundary
                if(row == 0 and i == 0):
                    self.grid[row][i] = Fore.CYAN + "+" + Style.RESET_ALL
                    self.buildings[row][i] = 0
                    continue
                if(row == 0 and i == columns - 1):
                    self.grid[row][i] = Fore.CYAN + "+" + Style.RESET_ALL
                    self.buildings[row][i] = 0
                    continue
                if(row == rows - 1 and i == 0):
                    self.grid[row][i] = Fore.CYAN + "+" + Style.RESET_ALL
                    self.buildings[row][i] = 0
                    continue
                if(row == rows - 1 and i == columns - 1):
                    self.grid[row][i] = Fore.CYAN + "+" + Style.RESET_ALL
                    self.buildings[row][i] = 0
                    continue
                if(row == 0):
                    self.grid[row][i] = Fore.CYAN + "-" + Style.RESET_ALL
                    self.buildings[row][i] = 0
                    continue
                if(row == 0):
                    self.grid[row][i] = Fore.CYAN + "-" + Style.RESET_ALL
                    self.buildings[row][i] = 0
                    continue
                if(row == rows - 1):
                    self.grid[row][i] = Fore.CYAN + "-" + Style.RESET_ALL
                    self.buildings[row][i] = 0
                    continue
                if(i == 0):
                    self.grid[row][i] = Fore.CYAN + "|" + Style.RESET_ALL
                    self.buildings[row][i] = 0
                    continue

                if(i == columns - 1):
                    self.grid[row][i] = Fore.CYAN + "|" + Style.RESET_ALL
                    self.buildings[row][i] = 0
                    continue

                self.grid[row][i] = Back.CYAN + "." + Style.RESET_ALL
                self.buildings[row][i] = -1