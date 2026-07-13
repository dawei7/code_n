from math import cos, pi, sin, sqrt
from random import random
from typing import List


class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        distance = self.radius * sqrt(random())
        angle = 2 * pi * random()
        return [
            self.x_center + distance * cos(angle),
            self.y_center + distance * sin(angle),
        ]
