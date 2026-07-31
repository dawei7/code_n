from bisect import bisect_left
from typing import List


class Solution:
    def countRectangles(
        self, rectangles: List[List[int]], points: List[List[int]]
    ) -> List[int]:
        widths_by_height = [[] for _ in range(101)]
        for width, height in rectangles:
            widths_by_height[height].append(width)
        for widths in widths_by_height:
            widths.sort()

        answer = []
        for x, y in points:
            count = 0
            for height in range(y, 101):
                widths = widths_by_height[height]
                count += len(widths) - bisect_left(widths, x)
            answer.append(count)
        return answer
