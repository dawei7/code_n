class _Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.previous: _Node | None = None
        self.next: _Node | None = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes: dict[int, _Node] = {}
        self.least = _Node()
        self.most = _Node()
        self.least.next = self.most
        self.most.previous = self.least

    def _remove(self, node: _Node) -> None:
        previous = node.previous
        following = node.next
        assert previous is not None and following is not None
        previous.next = following
        following.previous = previous

    def _append_most_recent(self, node: _Node) -> None:
        previous = self.most.previous
        assert previous is not None
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
            assert oldest is not None and oldest is not self.most
            self._remove(oldest)
            del self.nodes[oldest.key]


def solve(operations: list[str], arguments: list[list[int]]) -> list[int | None]:
    cache: LRUCache | None = None
    output: list[int | None] = []
    for operation, args in zip(operations, arguments):
        if operation == "LRUCache":
            cache = LRUCache(args[0])
            output.append(None)
        elif operation == "put":
            assert cache is not None
            cache.put(args[0], args[1])
            output.append(None)
        elif operation == "get":
            assert cache is not None
            output.append(cache.get(args[0]))
        else:
            raise ValueError(f"unknown operation: {operation}")
    return output
