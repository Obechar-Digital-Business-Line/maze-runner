import heapq
import json
import math
import os
from heapq import heappop
from typing import List

import location
from location import Location


class Map:
    width = None
    height = None
    obstacles: List[Location] = None
    bot: Location = None
    coin: Location = None
    locations = None
    map = None
    filename = 'output.txt'

    def init_file(self):
        filepath = os.path.join(os.getcwd(), self.filename)
        with open(filepath, 'w') as f:
            f.write('')

    def __init__(self):
        self.loadJson()
        self.loadLocs()
        self.loadMap()
        self.printMap()
        self.init_file()

    def loadJson(self):
        with open('map.json', 'r') as file:
            data = json.load(file)
            self.width = data['width']
            self.height = data['height']
            self.obstacles = [Location(*loc) for loc in sorted(data['obstacles'], key=lambda x: (x[0], x[1]))]
            self.bot = Location(*data['bot'])
            self.coin = Location(*data['coin'])
            self.obstacles = Location.sort(self.obstacles)

    def loadLocs(self):
        self.locations = self.obstacles.copy()
        self.locations.append(self.bot)
        self.locations.append(self.coin)

    def loadMap(self):
        self.map = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        for ll in self.obstacles:
            self.map[ll.x][ll.y] = '*'
        coin = self.coin
        self.map[coin.x][coin.y] = 'o'
        bot = self.bot
        self.map[bot.x][bot.y] = 'X'

    def printMap(self):
        print('*' * (self.width + 2))
        for i in range(self.height):
            print('*', end='')
            for j in range(self.width):
                print('{}'.format(self.map[i][j]), end='')
            print('*', end='')
            print()
        print('*' * (self.width + 2))
    # create a Map object and print its properties

    def moveBot(self, loc: Location):
        if self.map[loc.x][loc.y] == ' ' or self.map[loc.x][loc.y] == 'o':
            self.map[loc.x][loc.y] = 'X'
            self.map[self.bot.x][self.bot.y] = ' '
            self.bot = loc
            self.printMap()
            return True
        else:
            print('<', self.map[loc.x][loc.y], '>')
            return False
            # self.loadMap()

    def moveTo(self, loc: Location):
        tx = loc.x - self.bot.x
        ty = loc.y - self.bot.y

        flagA = True
        flagB = True
        if tx < 0:
            tx = -tx
            for i in range(tx):
                if not self.up():
                    flagA = False
                else:
                    flagA = True
        else:
            for i in range(tx):
                if not self.down():
                    flagA = False
                else:
                    flagA = True
        if ty < 0:
            ty = -ty
            for i in range(ty):
                if not self.left():
                    flagB = False
                else:
                    flagB = True
        else:
            for i in range(ty):
                if not self.right():
                    flagB = False
                else:
                    flagB = True

        if not flagA and not flagB:
            return False
        return True

    def left(self):
        if self.bot.y > 0:
            if self.moveBot(Location(self.bot.x, self.bot.y - 1)):
                self.write('left')
                return True
            return False

    def right(self):
        if self.bot.y < self.height - 1:
            if self.moveBot(Location(self.bot.x, self.bot.y + 1)):
                self.write('right')
                return True
            return False

    def up(self):
        if self.bot.x > 0:
            if self.moveBot(Location(self.bot.x - 1, self.bot.y)):
                self.write('up')
                return True
            return False

    def down(self):
        if self.bot.x < self.width - 1:
            if self.moveBot(Location(self.bot.x + 1, self.bot.y)):
                self.write('down')
                return True
            return False

    def write(self, a):
        with open(self.filename, mode='a') as file:
            file.write(a +'\n')



