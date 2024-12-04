import math
from config import TIME_STEP

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, vector):
        return Position(self.x + vector.x * TIME_STEP, self.y + vector.y * TIME_STEP)

    def distance_to(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)
