class _Node:
    def __init__(self):
        self.maximum = 0
        self.lazy = 0
        self.left = None
        self.right = None


class MyCalendarThree:
    DOMAIN_LEFT = 0
    DOMAIN_RIGHT = 10**9 - 1

    def __init__(self):
        self.root = _Node()

    def _add(self, node, left, right, query_left, query_right):
        if query_left <= left and right <= query_right:
            node.maximum += 1
            node.lazy += 1
            return

        middle = (left + right) // 2
        if query_left <= middle:
            if node.left is None:
                node.left = _Node()
            self._add(node.left, left, middle, query_left, query_right)
        if query_right > middle:
            if node.right is None:
                node.right = _Node()
            self._add(node.right, middle + 1, right, query_left, query_right)

        left_maximum = node.left.maximum if node.left is not None else 0
        right_maximum = node.right.maximum if node.right is not None else 0
        node.maximum = node.lazy + max(left_maximum, right_maximum)

    def book(self, start: int, end: int) -> int:
        self._add(
            self.root,
            self.DOMAIN_LEFT,
            self.DOMAIN_RIGHT,
            start,
            end - 1,
        )
        return self.root.maximum
