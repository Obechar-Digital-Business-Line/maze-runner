class Location:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    @staticmethod
    def sort(locations):
        return sorted(locations, key=lambda loc: (loc.x, loc.y))
