# import imp
from time import sleep
from os import system, name
# from typing_extensions import Self
from colorama import init, Fore, Back, Style
# import random
from zmq import BACKLOG
from src.input import *
from src.building import Building, Tower, Townhall, Hut, Canon, Wall
from src.queen import Queen
from src.spell import Spell, Rage, Heal
from src.globals import *
from src.king import King
from src.queen import Queen
from src.enemy import Enemy
from src.queen import Queen
from src.archer import Archer
from src.barbarian import Barbarian
from src.balloon import Balloon


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


class Game:
    def __init__(self, player, level):
        self.grid = []
        self.player = player
        self.level = level

        if(player == 1):
            self.king = King(26, 23)
        else:
            self.king = Queen(26, 23)

        self.troops = []
        self.barbarians = []
        self.archers = []
        self.balloons = []

        self.num_troops = 0
        self.num_archers = 0
        self.num_barbarians = 0
        self.num_balloons = 0
        self.total_barbarians = 6
        self.total_archers = 6
        self.total_balloons = 3

        self.buildings = []

        self.townhall = Townhall()
        # number of huts are fixed(5)
        self.hut1 = Hut()
        self.hut2 = Hut()
        self.hut3 = Hut()
        self.hut4 = Hut()
        self.hut5 = Hut()

        # number of canons and wizard towers depend on level
        self.canons = []
        self.towers = []

        if(self.level == 1):
            self.num_canons = 2
            self.num_towers = 2
        elif(self.level == 2):
            self.num_canons = 3
            self.num_towers = 3
        elif(self.level == 3):
            self.num_canons = 4
            self.num_towers = 4

        for i in range(self.num_canons):
            self.canons.append(Canon())

        for i in range(self.num_towers):
            self.towers.append(Tower())

        # self.canon1 = Canon()
        # self.canon2 = Canon()

        # self.tower1 = Tower()
        # self.tower2 = Tower()

        self.walls = []

        self.create_walls()
        # self.create_canons(level)

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

        if(self.player == 1):
            print("     King's Health")
        else:
            print("     Queen's Health")

        print("|" + healthDisplay + remainingDisplay + "|")
        print("         " + percent)

        print("Barbarians " + str(self.total_barbarians))
        print("Archers " + str(self.total_archers))
        print("Balloons " + str(self.total_balloons))
        
        # print(self.level)
        # if(self.num_barbarians > 0):
        #     for t in self.barbarians:
        #         print(t)
        #         print(t.char)
        #         print(t.get_char())
        
    # def update_canon_tile(self, row, column, char, building):
    #     self.grid[row][column] = Fore.BLUE + char + Style.RESET_ALL
    #     self.buildings[row][column] = building
    #     return

    def update_wall_tile(self, row, column, char, building):
        self.grid[row][column] = Back.WHITE + \
            Fore.BLACK + char + Style.RESET_ALL
        self.buildings[row][column] = building
        return

    def update_troop_tile(self, row, column, char, health):
        # print(char)
        # sleep(5)

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

    def eagle_attack_queen(self):
        self.king.eagle_attack(self)
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

        # spawning points for troops
        # (13, 2), (6, 42), (17, 41)

        if(c == 1 or c == 2 or c == 3):

            # spawn barbarian

            if(self.num_barbarians >= limit_barbarian):
                print("Barbarians are at limit")
                return

            self.num_barbarians = self.num_barbarians + 1
            self.num_troops = self.num_troops + 1

            if(c == 1):
                b = Barbarian(13, 2)
                b.update()

            if(c == 2):
                b = Barbarian(6, 42)
                b.update()

            if(c == 3):
                b = Barbarian(17, 41)
                b.update()

            # t = Troop(13, 2)
            # self.troops.append(t)

            self.barbarians.append(b)
            self.troops.append(b)
            self.update()
            return

        if(c == 4 or c == 5 or c == 6):
            # spawn archer
            if(self.num_archers >= limit_archer):
                print("Archers are at limit")
                return

            self.num_archers = self.num_archers + 1
            self.num_troops = self.num_troops + 1

            if(c == 4):
                a = Archer(13, 2)
                a.update()

            if(c == 5):
                a = Archer(6, 42)
                a.update()

            if(c == 6):
                a = Archer(17, 41)
                a.update()

            # t = Troop(13, 2)
            # self.troops.append(t)

            self.archers.append(a)
            self.troops.append(a)
            self.update()
            return

        if(c == 7 or c == 8 or c == 9):
            # spawn balloon
            if(self.num_balloons >= limit_balloon):
                print("Balloons are at limit")
                return

            self.num_balloons = self.num_balloons + 1
            self.num_troops = self.num_troops + 1

            if(c == 7):
                b = Balloon(13, 2)
                b.update()

            if(c == 8):
                b = Balloon(6, 42)
                b.update()

            if(c == 9):
                b = Balloon(17, 41)
                b.update()

            # t = Troop(13, 2)
            # self.troops.append(t)

            self.balloons.append(b)
            self.troops.append(b)
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

        for i in range(self.num_canons):
            if(self.canons[i].destroyed == False):
                return(False)

        for i in range(self.num_towers):
            if(self.towers[i].destroyed == False):
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

        # for troop in self.troops:
        #     if(troop.dead == False):
        #         return(False)

        if self.total_balloons == 0 and self.total_archers == 0 and self.total_barbarians == 0:
            return True
        else:
            return False

        # return(True)

    def draw_grid(self):

        print_s = "\n"
        self.townhall.render(self, 11, 21)
        self.hut1.render(self, 3, 3)
        self.hut2.render(self, 13, 34)
        self.hut3.render(self, 19, 19)
        self.hut4.render(self, 3, 29)
        self.hut5.render(self, 21, 7)

        if(self.level == 1):
            self.canons[0].render(self, 4, 10)
            self.canons[1].render(self, 15, 25)
            self.towers[0].render(self, 5, 30)
            self.towers[1].render(self, 21, 9)
        elif(self.level == 2):
            self.canons[0].render(self, 14, 10)
            self.canons[1].render(self, 18, 30)
            self.towers[0].render(self, 5, 30)

            self.towers[1].render(self, 21, 9)
            self.towers[2].render(self, 15, 25)
            self.canons[2].render(self, 2, 2)

        elif(self.level == 3):

            self.canons[0].render(self, 14, 10)
            self.canons[1].render(self, 18, 30)
            self.towers[0].render(self, 5, 30)

            self.towers[1].render(self, 21, 9)
            self.towers[2].render(self, 10, 19)

            self.canons[2].render(self, 2, 2)
            self.canons[3].render(self, 14, 33)
            self.towers[3].render(self, 15, 25)

        # self.canon1.render(self, 4, 10)
        # self.canon2.render(self, 18, 30)
        # self.tower1.render(self, 5, 11)
        # self.tower2.render(self, 17, 31)

        self.king.render(self)

        for w in self.walls:
            w.render(self)

        self.num_barbarians = 0
        for t in self.barbarians:
            if(t.dead == False):
                self.num_barbarians = self.num_barbarians + 1

        self.num_archers = 0
        for t in self.archers:
            if(t.dead == False):
                self.num_archers = self.num_archers + 1

        self.num_balloons = 0
        for t in self.balloons:
            if(t.dead == False):
                self.num_balloons = self.num_balloons + 1

        if(self.num_barbarians > 0):
            for t in self.barbarians:
                if(t.dead == False):
                    t.render(self)

        if(self.num_archers > 0):
            for a in self.archers:
                if(a.dead == False):
                    a.render(self)

        if(self.num_balloons > 0):
            for b in self.balloons:
                if(b.dead == False):
                    b.render(self)

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
