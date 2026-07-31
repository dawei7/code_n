from heapq import heapify, heappop, heappush


def solve(nums: list[int], k: int) -> int:
    heap = [-value for value in nums]
    heapify(heap)
    score = 0

    for _ in range(k):
        value = -heappop(heap)
        score += value
        heappush(heap, -((value + 2) // 3))

    return score
