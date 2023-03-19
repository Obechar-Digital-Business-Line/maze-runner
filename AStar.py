import heapq

from Node import Node
from location import Location
from map import Map


class AStarFinder:

    def __init__(self):
        self.open_set = []
        self.closed_set = set()

    @staticmethod
    def heuristic(a, b):
        return abs(a.x - b.x) + abs(a.y - b.y)

    # @staticmethod
    # def heuristic(current_node, goal_node, obstacles):
    #     dx = abs(current_node.x - goal_node.x)
    #     dy = abs(current_node.y - goal_node.y)
    #     return dx + dy + min(abs(current_node.x - obs.x) + abs(current_node.y - obs.y) for obs in obstacles)

    @staticmethod
    def get_neighbors(node: Node, m: Map) -> list[Node]:
        neighbors = []
        for x_offset, y_offset in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            neighbor_location = Location(node.location.x + x_offset, node.location.y + y_offset)
            # print("[[[[[[[[[[[[[{} {}]]]]]]]]]]]]]", neighbor_location, obstacles)
            if neighbor_location in m.obstacles or neighbor_location.x < 0 or neighbor_location.x >= m.height \
                    or neighbor_location.y < 0 or neighbor_location.y >= m.width:
                continue
            neighbor_node = Node(location=neighbor_location, parent=node)
            neighbors.append(neighbor_node)
        return neighbors

    def find_path(self, m: Map):
        start_node = Node(location=m.bot, g_score=0, f_score=self.heuristic(m.bot, m.coin))
        self.open_set.append(start_node)

        while self.open_set:
            current_node = heapq.heappop(self.open_set)

            if current_node.location == m.coin:
                path = []
                while current_node is not None:
                    path.append(current_node.location)
                    current_node = current_node.parent
                return path[::-1]

            self.closed_set.add(current_node)

            for neighbor in self.get_neighbors(current_node, m):
                if neighbor in self.closed_set:
                    continue

                tentative_g_score = current_node.g_score + 1

                if neighbor not in self.open_set:
                    heapq.heappush(self.open_set, neighbor)
                elif tentative_g_score >= neighbor.g_score:
                    continue

                neighbor.g_score = tentative_g_score
                neighbor.f_score = tentative_g_score + self.heuristic(neighbor.location, m.coin)

        return None
