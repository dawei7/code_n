from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def maxWalls(
        self, robots: List[int], distance: List[int], walls: List[int]
    ) -> int:
        ordered = sorted(zip(robots, distance))
        positions = [position for position, _ in ordered]
        ranges = [shot_range for _, shot_range in ordered]
        robot_positions = set(positions)
        fixed = sum(wall in robot_positions for wall in walls)
        free_walls = sorted(wall for wall in walls if wall not in robot_positions)

        def count_between(left: int, right: int) -> int:
            if left > right:
                return 0
            return bisect_right(free_walls, right) - bisect_left(free_walls, left)

        left_exterior = count_between(positions[0] - ranges[0], positions[0])
        dp_left = left_exterior
        dp_right = 0

        for i in range(1, len(positions)):
            left_robot = positions[i - 1]
            right_robot = positions[i]

            right_end = min(left_robot + ranges[i - 1], right_robot)
            left_start = max(right_robot - ranges[i], left_robot)
            from_left = count_between(left_robot, right_end)
            from_right = count_between(left_start, right_robot)
            overlap = count_between(left_start, right_end)
            both = from_left + from_right - overlap

            next_left = max(dp_left + from_right, dp_right + both)
            next_right = max(dp_left, dp_right + from_left)
            dp_left, dp_right = next_left, next_right

        right_exterior = count_between(
            positions[-1], positions[-1] + ranges[-1]
        )
        return fixed + max(dp_left, dp_right + right_exterior)
