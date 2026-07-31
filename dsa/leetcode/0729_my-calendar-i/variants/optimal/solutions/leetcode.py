class _Node:
    def __init__(self):
        self.covered = False
        self.left = None
        self.right = None


class MyCalendar:
    DOMAIN_LEFT = 0
    DOMAIN_RIGHT = 10**9 - 1

    def __init__(self):
        self.root = _Node()

    def _overlaps(self, node, left, right, query_left, query_right):
        if node is None:
            return False
        if node.covered:
            return True

        middle = (left + right) // 2
        if query_right <= middle:
            return self._overlaps(node.left, left, middle, query_left, query_right)
        if query_left > middle:
            return self._overlaps(node.right, middle + 1, right, query_left, query_right)
        return self._overlaps(node.left, left, middle, query_left, middle) or self._overlaps(
            node.right, middle + 1, right, middle + 1, query_right
        )

    def _cover(self, node, left, right, query_left, query_right):
        if query_left <= left and right <= query_right:
            node.covered = True
            node.left = None
            node.right = None
            return

        middle = (left + right) // 2
        if query_left <= middle:
            if node.left is None:
                node.left = _Node()
            self._cover(node.left, left, middle, query_left, query_right)
        if query_right > middle:
            if node.right is None:
                node.right = _Node()
            self._cover(node.right, middle + 1, right, query_left, query_right)

    def book(self, start: int, end: int) -> bool:
        query_right = end - 1
        if self._overlaps(
            self.root,
            self.DOMAIN_LEFT,
            self.DOMAIN_RIGHT,
            start,
            query_right,
        ):
            return False
        self._cover(
            self.root,
            self.DOMAIN_LEFT,
            self.DOMAIN_RIGHT,
            start,
            query_right,
        )
        return True
