from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: (point[0], -point[1]))
        answer = 0

        for upper_left in range(len(points)):
            highest_lower_y = float("-inf")

            for lower_right in range(upper_left + 1, len(points)):
                y = points[lower_right][1]
                if highest_lower_y < y <= points[upper_left][1]:
                    answer += 1
                    highest_lower_y = y

        return answer
