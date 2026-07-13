from collections import defaultdict
from math import gcd
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        count = len(points)
        if count <= 2:
            return count

        answer = 2
        for index, (x1, y1) in enumerate(points):
            directions = defaultdict(int)
            for x2, y2 in points[index + 1 :]:
                dx = x2 - x1
                dy = y2 - y1
                if dx == 0:
                    direction = (0, 1)
                elif dy == 0:
                    direction = (1, 0)
                else:
                    divisor = gcd(abs(dx), abs(dy))
                    dx //= divisor
                    dy //= divisor
                    if dx < 0:
                        dx = -dx
                        dy = -dy
                    direction = (dx, dy)
                directions[direction] += 1
            answer = max(answer, max(directions.values(), default=0) + 1)
        return answer
