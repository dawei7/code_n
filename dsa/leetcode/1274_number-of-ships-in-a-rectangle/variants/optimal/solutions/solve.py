class Point:
    """Local equivalent of the coordinate point supplied by LeetCode's judge."""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Sea:
    """Local equivalent of LeetCode's hidden ship-query interface."""

    def hasShips(self, topRight: Point, bottomLeft: Point) -> bool:
        raise NotImplementedError


def solve(sea: Sea, topRight: Point, bottomLeft: Point) -> int:
    def count(right, top, left, bottom):
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
