from typing import List


class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        min_x = min(x for x, _ in points)
        max_x = max(x for x, _ in points)
        axis_sum = min_x + max_x
        point_set = {(x, y) for x, y in points}
        return all((axis_sum - x, y) in point_set for x, y in point_set)
