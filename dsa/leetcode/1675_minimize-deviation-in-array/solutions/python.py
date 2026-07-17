import heapq


def solve(nums: list[int]) -> int:
    heap: list[int] = []
    minimum = float("inf")

    for value in nums:
        normalized = value * 2 if value % 2 else value
        heapq.heappush(heap, -normalized)
        minimum = min(minimum, normalized)

    answer = float("inf")
    while heap:
        maximum = -heapq.heappop(heap)
        answer = min(answer, maximum - minimum)
        if maximum % 2:
            break
        reduced = maximum // 2
        minimum = min(minimum, reduced)
        heapq.heappush(heap, -reduced)

    return int(answer)
