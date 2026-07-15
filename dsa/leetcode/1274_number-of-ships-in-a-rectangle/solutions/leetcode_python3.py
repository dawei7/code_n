class Solution:
    def countShips(
        self, sea: "Sea", topRight: "Point", bottomLeft: "Point"
    ) -> int:
        def count(right: int, top: int, left: int, bottom: int) -> int:
            if left > right or bottom > top:
                return 0
            if not sea.hasShips(Point(right, top), Point(left, bottom)):
                return 0
            if left == right and bottom == top:
                return 1

            mid_x = (left + right) // 2
            mid_y = (bottom + top) // 2
            return (
                count(mid_x, mid_y, left, bottom)
                + count(right, mid_y, mid_x + 1, bottom)
                + count(mid_x, top, left, mid_y + 1)
                + count(right, top, mid_x + 1, mid_y + 1)
            )

        return count(topRight.x, topRight.y, bottomLeft.x, bottomLeft.y)
