from AStar import AStarFinder
from map import Map

print("def")
my_map = Map()

path = AStarFinder().find_path(my_map.bot, my_map.coin, my_map.obstacles)
print(path)

