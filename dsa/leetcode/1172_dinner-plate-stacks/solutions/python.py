import heapq


class DinnerPlates:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.available = []

    def push(self, val: int) -> None:
        while self.available and (
            self.available[0] >= len(self.stacks)
            or len(self.stacks[self.available[0]]) == self.capacity
        ):
            heapq.heappop(self.available)

        if not self.available:
            index = len(self.stacks)
            self.stacks.append([])
            heapq.heappush(self.available, index)

        index = self.available[0]
        self.stacks[index].append(val)
        if len(self.stacks[index]) == self.capacity:
            heapq.heappop(self.available)

    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        if not self.stacks:
            return -1
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index: int) -> int:
        if index < 0 or index >= len(self.stacks) or not self.stacks[index]:
            return -1

        was_full = len(self.stacks[index]) == self.capacity
        value = self.stacks[index].pop()
        if was_full:
            heapq.heappush(self.available, index)

        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        return value


def solve(capacity: int, operations: list[list]) -> list:
    plates = DinnerPlates(capacity)
    output = []
    for method, arguments in operations:
        if method == "push":
            output.append(plates.push(*arguments))
        elif method == "pop":
            output.append(plates.pop())
        elif method == "popAtStack":
            output.append(plates.popAtStack(*arguments))
        else:
            raise ValueError(f"unknown operation: {method}")
    return output
