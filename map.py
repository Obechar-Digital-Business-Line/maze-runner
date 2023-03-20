import heapq
import json
import math
import os
from heapq import heappop
from typing import List

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


