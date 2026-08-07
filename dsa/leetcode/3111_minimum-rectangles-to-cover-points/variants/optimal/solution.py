class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort()
        rectangles = 0
        covered_through = -1

        for x, _ in points:
            if x > covered_through:
                rectangles += 1
                covered_through = x + w

        return rectangles
