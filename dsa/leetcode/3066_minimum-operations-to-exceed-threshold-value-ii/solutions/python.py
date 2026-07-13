import heapq
from typing import List

def solve(nums: List[int], k: int) -> int:
    """
    Calculates the minimum operations to make all elements >= k.
    Uses a min-heap to greedily combine the two smallest elements.
    """
    heap = list(nums)
    heapq.heapify(heap)

    operations = 0

    # Continue until the smallest element is at least k
    while len(heap) > 1 and heap[0] < k:
        # Extract the two smallest elements
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)

        # Calculate the new value and push it back
        new_val = x * 2 + y
        heapq.heappush(heap, new_val)

        operations += 1

    return operations
