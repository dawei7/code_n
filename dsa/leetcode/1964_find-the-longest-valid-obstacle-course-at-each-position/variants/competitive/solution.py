from bisect import bisect_right
from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(
        self,
        obstacles: List[int],
    ) -> List[int]:
        tails = []
        answer = []

        for height in obstacles:
            length = bisect_right(tails, height)
            answer.append(length + 1)

            if length == len(tails):
                tails.append(height)
            else:
                tails[length] = height

        return answer
