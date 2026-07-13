class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        min_x = min_y = float("inf")
        max_x = max_y = float("-inf")
        total_area = 0
        unmatched = set()

        for x1, y1, x2, y2 in rectangles:
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)
            total_area += (x2 - x1) * (y2 - y1)

            for corner in ((x1, y1), (x1, y2), (x2, y1), (x2, y2)):
                if corner in unmatched:
                    unmatched.remove(corner)
                else:
                    unmatched.add(corner)

        outer_corners = {
            (min_x, min_y),
            (min_x, max_y),
            (max_x, min_y),
            (max_x, max_y),
        }
        outer_area = (max_x - min_x) * (max_y - min_y)
        return total_area == outer_area and unmatched == outer_corners
