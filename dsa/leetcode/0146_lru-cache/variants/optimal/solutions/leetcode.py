class _Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}
        self.least = _Node()
        self.most = _Node()
        self.least.next = self.most
        self.most.previous = self.least

    def _remove(self, node: _Node) -> None:
        node.previous.next = node.next
        node.next.previous = node.previous

    def _append_most_recent(self, node: _Node) -> None:
        previous = self.most.previous
        previous.next = node
        node.previous = previous
        node.next = self.most
        self.most.previous = node

    def get(self, key: int) -> int:
        node = self.nodes.get(key)
        if node is None:
            return -1
        self._remove(node)
        self._append_most_recent(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        existing = self.nodes.get(key)
        if existing is not None:
            self._remove(existing)

        node = _Node(key, value)
        self.nodes[key] = node
        self._append_most_recent(node)

        if len(self.nodes) > self.capacity:
            oldest = self.least.next
            self._remove(oldest)
            del self.nodes[oldest.key]
