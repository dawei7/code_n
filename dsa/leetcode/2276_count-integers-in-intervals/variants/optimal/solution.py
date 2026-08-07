class _Node:
    __slots__ = ("left", "right", "covered", "total")

    def __init__(self):
        self.left = None
        self.right = None
        self.covered = False
        self.total = 0


class CountIntervals:
    def __init__(self):
        self._root = _Node()

    def add(self, left: int, right: int) -> None:
        self._cover(self._root, 1, 10**9, left, right)

    def count(self) -> int:
        return self._root.total

    def _cover(
        self,
        node: _Node,
        low: int,
        high: int,
        query_left: int,
        query_right: int,
    ) -> None:
        if node.covered:
            return
        if query_left <= low and high <= query_right:
            node.covered = True
            node.total = high - low + 1
            node.left = None
            node.right = None
            return

        middle = (low + high) // 2
        if query_left <= middle:
            if node.left is None:
                node.left = _Node()
            self._cover(
                node.left,
                low,
                middle,
                query_left,
                query_right,
            )
        if middle < query_right:
            if node.right is None:
                node.right = _Node()
            self._cover(
                node.right,
                middle + 1,
                high,
                query_left,
                query_right,
            )

        left_total = node.left.total if node.left is not None else 0
        right_total = node.right.total if node.right is not None else 0
        node.total = left_total + right_total
        if node.total == high - low + 1:
            node.covered = True
            node.left = None
            node.right = None
