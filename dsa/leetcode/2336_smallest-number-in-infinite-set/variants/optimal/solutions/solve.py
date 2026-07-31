import heapq


class SmallestInfiniteSet:
    def __init__(self) -> None:
        self.next_fresh = 1
        self.restored = []
        self.restored_values = set()

    def popSmallest(self) -> int:
        if self.restored:
            value = heapq.heappop(self.restored)
            self.restored_values.remove(value)
            return value
        value = self.next_fresh
        self.next_fresh += 1
        return value

    def addBack(self, num: int) -> None:
        if num < self.next_fresh and num not in self.restored_values:
            heapq.heappush(self.restored, num)
            self.restored_values.add(num)


def solve(operations, arguments):
    infinite_set = None
    output = []

    for operation, values in zip(operations, arguments):
        if operation == "SmallestInfiniteSet":
            infinite_set = SmallestInfiniteSet()
            output.append(None)
        elif operation == "popSmallest":
            output.append(infinite_set.popSmallest())
        elif operation == "addBack":
            output.append(infinite_set.addBack(*values))

    return output
