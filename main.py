from AStar import AStarFinder
from map import Map

my_map = Map()

path = AStarFinder().find_path(my_map)
# path = bfs_().find(my_map)
print('My path: ', path)

for i in path:
    if not my_map.moveTo(i):
        continue

