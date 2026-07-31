import heapq


class NumberContainers:
    def __init__(self) -> None:
        self.index_to_number = {}
        self.number_to_indices = {}

    def change(self, index: int, number: int) -> None:
        if self.index_to_number.get(index) == number:
            return
        self.index_to_number[index] = number
        heap = self.number_to_indices.setdefault(number, [])
        heapq.heappush(heap, index)

    def find(self, number: int) -> int:
        heap = self.number_to_indices.get(number, [])
        while heap and self.index_to_number.get(heap[0]) != number:
            heapq.heappop(heap)
        return heap[0] if heap else -1


def solve(operations, arguments):
    containers = None
    output = []
    for operation, values in zip(operations, arguments):
        if operation == "NumberContainers":
            containers = NumberContainers()
            output.append(None)
        elif operation == "change":
            output.append(containers.change(*values))
        elif operation == "find":
            output.append(containers.find(*values))
    return output
