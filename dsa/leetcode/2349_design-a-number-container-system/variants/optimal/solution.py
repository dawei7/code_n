import heapq


class NumberContainers:
    def __init__(self):
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
