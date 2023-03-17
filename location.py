import math


class Location:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g_score = 1
        self.f_score = 1
        self.parent = None

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Location):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))

    @staticmethod
    def sort(locations):
        return sorted(locations, key=lambda loc: (loc.x, loc.y))

    @staticmethod
    def heuristic(a, b) -> float:
        return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)