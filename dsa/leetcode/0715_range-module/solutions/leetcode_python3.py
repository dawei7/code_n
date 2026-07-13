class _Node:
    def __init__(self, state: int = 0):
        self.state = state
        self.left = None
        self.right = None


class RangeModule:
    DOMAIN_LEFT = 1
    DOMAIN_RIGHT = 10**9

    def __init__(self):
        self.root = _Node()

    @staticmethod
    def _children(node: _Node) -> None:
        if node.left is None:
            node.left = _Node(node.state)
            node.right = _Node(node.state)

    def _assign(self, node, left, right, query_left, query_right, state):
        if query_left <= left and right <= query_right:
            node.state = state
            node.left = None
            node.right = None
            return
        self._children(node)
        middle = (left + right) // 2
        if query_left <= middle:
            self._assign(node.left, left, middle, query_left, query_right, state)
        if query_right > middle:
            self._assign(node.right, middle + 1, right, query_left, query_right, state)
        if node.left.state == node.right.state and node.left.state != -1:
            node.state = node.left.state
            node.left = None
            node.right = None
        else:
            node.state = -1

    def _query(self, node, left, right, query_left, query_right):
        if node.state != -1:
            return node.state == 1
        if query_left <= left and right <= query_right:
            return False
        middle = (left + right) // 2
        if query_right <= middle:
            return self._query(node.left, left, middle, query_left, query_right)
        if query_left > middle:
            return self._query(node.right, middle + 1, right, query_left, query_right)
        return (
            self._query(node.left, left, middle, query_left, query_right)
            and self._query(node.right, middle + 1, right, query_left, query_right)
        )

    def addRange(self, left: int, right: int) -> None:
        self._assign(self.root, self.DOMAIN_LEFT, self.DOMAIN_RIGHT, left, right - 1, 1)

    def queryRange(self, left: int, right: int) -> bool:
        return self._query(self.root, self.DOMAIN_LEFT, self.DOMAIN_RIGHT, left, right - 1)

    def removeRange(self, left: int, right: int) -> None:
        self._assign(self.root, self.DOMAIN_LEFT, self.DOMAIN_RIGHT, left, right - 1, 0)
