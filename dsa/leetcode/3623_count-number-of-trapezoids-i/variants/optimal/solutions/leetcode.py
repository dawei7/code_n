from collections import defaultdict
from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        modulus = 1_000_000_007
        points_per_height = defaultdict(int)
        for _, y in points:
            points_per_height[y] += 1

        answer = 0
        earlier_sides = 0
        for count in points_per_height.values():
            sides = count * (count - 1) // 2
            answer = (answer + sides * earlier_sides) % modulus
            earlier_sides = (earlier_sides + sides) % modulus

        return answer
