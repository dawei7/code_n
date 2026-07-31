import heapq


def solve(nums: list[int], k: int) -> int:
    heap = nums.copy()
    heapq.heapify(heap)
    operations = 0

    while heap[0] < k:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        heapq.heappush(heap, first * 2 + second)
        operations += 1

    return operations
