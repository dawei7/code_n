from heapq import heapify, heapreplace


def solve(nums: list[int], k: int, multiplier: int) -> list[int]:
    heap = [(value, index) for index, value in enumerate(nums)]
    heapify(heap)

    for _ in range(k):
        value, index = heap[0]
        updated = value * multiplier
        nums[index] = updated
        heapreplace(heap, (updated, index))

    return nums
