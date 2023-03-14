import json

from location import Location


class Map:
    width = None
    height = None
    obstacles = None
    bot = None
    coin = None
    locations = None
    map = None

    def __init__(self):
        self.loadJson()
        self.loadLocs()
        self.loadMap()
        self.printMap()

    def loadJson(self):
        with open('map.json', 'r') as file:
            data = json.load(file)
            self.width = data['width']
            self.height = data['height']
            self.obstacles = [Location(*loc) for loc in data['obstacles']]
            self.bot = Location(*data['bot'])
            self.coin = Location(*data['coin'])
            self.obstacles = Location.sort(self.obstacles)

    def loadLocs(self):
        self.locations = self.obstacles.copy()
        self.locations.append(self.bot)
        self.locations.append(self.coin)

    def loadMap(self):
        self.map = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        for l in self.obstacles:
            self.map[l.x][l.y] += '*'
        coin = self.coin
        self.map[coin.x][coin.y] += 'o'
        bot = self.bot
        self.map[bot.x][bot.y] += 'X'

    def printMap(self):
        print('*' * (self.width + 2))
        for row in self.map:
            print('*', end="")
            for loc in row:
                if loc != " ":
                    print(str(loc).lstrip(), end="")
                else:
                    print(str(loc), end="")
            print('*', end="")
            print()

        print('*' * (self.width + 2))
# create a Map object and print its properties
