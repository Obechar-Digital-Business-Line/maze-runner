class Node:
    def __init__(self, location, parent=None, g_score=float("inf"), f_score=float("inf")):
        self.location = location
        self.parent = parent
        self.g_score = g_score
        self.f_score = f_score

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __lt__(self, other):
        return self.f_score < other.f_score
