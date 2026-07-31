class Node:
    def __init__(self, value: int, height: int):
        self.value = value
        self.forward: list[Node | None] = [None] * height


class Skiplist:
    MAX_LEVEL = 32

    def __init__(self):
        self.head = Node(-1, self.MAX_LEVEL)
        self.random_state = 0x6D2B79F5

    def nextBit(self) -> int:
        state = self.random_state
        state ^= (state << 13) & 0xFFFFFFFF
        state ^= state >> 17
        state ^= (state << 5) & 0xFFFFFFFF
        self.random_state = state & 0xFFFFFFFF
        return state & 1

    def randomHeight(self) -> int:
        height = 1
        while height < self.MAX_LEVEL and self.nextBit():
            height += 1
        return height

    def predecessors(self, target: int) -> list[Node]:
        update = [self.head] * self.MAX_LEVEL
        current = self.head
        for level in range(self.MAX_LEVEL - 1, -1, -1):
            while current.forward[level] is not None and current.forward[level].value < target:
                current = current.forward[level]
            update[level] = current
        return update

    def search(self, target: int) -> bool:
        candidate = self.predecessors(target)[0].forward[0]
        return candidate is not None and candidate.value == target

    def add(self, num: int) -> None:
        update = self.predecessors(num)
        node = Node(num, self.randomHeight())
        for level in range(len(node.forward)):
            node.forward[level] = update[level].forward[level]
            update[level].forward[level] = node

    def erase(self, num: int) -> bool:
        update = self.predecessors(num)
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
