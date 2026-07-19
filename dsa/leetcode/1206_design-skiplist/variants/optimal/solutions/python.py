class _Node:
    def __init__(self, value: int, height: int):
        self.value = value
        self.forward: list[_Node | None] = [None] * height


class Skiplist:
    _MAX_LEVEL = 32

    def __init__(self):
        self._head = _Node(-1, self._MAX_LEVEL)
        self._random_state = 0x6D2B79F5

    def _next_bit(self) -> int:
        state = self._random_state
        state ^= (state << 13) & 0xFFFFFFFF
        state ^= state >> 17
        state ^= (state << 5) & 0xFFFFFFFF
        self._random_state = state & 0xFFFFFFFF
        return state & 1

    def _random_height(self) -> int:
        height = 1
        while height < self._MAX_LEVEL and self._next_bit():
            height += 1
        return height

    def _predecessors(self, target: int) -> list[_Node]:
        update = [self._head] * self._MAX_LEVEL
        current = self._head
        for level in range(self._MAX_LEVEL - 1, -1, -1):
            while current.forward[level] is not None and current.forward[level].value < target:
                current = current.forward[level]
            update[level] = current
        return update

    def search(self, target: int) -> bool:
        predecessor = self._predecessors(target)[0]
        candidate = predecessor.forward[0]
        return candidate is not None and candidate.value == target

    def add(self, num: int) -> None:
        update = self._predecessors(num)
        node = _Node(num, self._random_height())
        for level in range(len(node.forward)):
            node.forward[level] = update[level].forward[level]
            update[level].forward[level] = node

    def erase(self, num: int) -> bool:
        update = self._predecessors(num)
        target = update[0].forward[0]
        if target is None or target.value != num:
            return False
        for level in range(len(target.forward)):
            if update[level].forward[level] is target:
                update[level].forward[level] = target.forward[level]
        return True


def solve(operations: list[str], arguments: list[list[int]]) -> list[object]:
    skiplist: Skiplist | None = None
    output: list[object] = []
    for operation, args in zip(operations, arguments):
        if operation == "Skiplist":
            skiplist = Skiplist()
            output.append(None)
        elif operation == "add":
            assert skiplist is not None
            skiplist.add(args[0])
            output.append(None)
        elif operation == "search":
            assert skiplist is not None
            output.append(skiplist.search(args[0]))
        elif operation == "erase":
            assert skiplist is not None
            output.append(skiplist.erase(args[0]))
    return output
