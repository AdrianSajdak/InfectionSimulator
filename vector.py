import math
from config import MAX_SPEED

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        magnitude = self.magnitude()
        if magnitude > MAX_SPEED:
            self.x = (self.x / magnitude) * MAX_SPEED
            self.y = (self.y / magnitude) * MAX_SPEED

    def magnitude(self):
        return math.hypot(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
