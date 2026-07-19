from collections import Counter, defaultdict
from typing import List


class DetectSquares:
    def __init__(self):
        self.points = Counter()
        self.rows = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1
        self.rows[y][x] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        squares = 0

        for other_x, horizontal_count in self.rows[y].items():
            side = other_x - x
            if side == 0:
                continue

            squares += (
                horizontal_count
                * self.points[(x, y + side)]
                * self.points[(other_x, y + side)]
            )
            squares += (
                horizontal_count
                * self.points[(x, y - side)]
                * self.points[(other_x, y - side)]
            )

        return squares
