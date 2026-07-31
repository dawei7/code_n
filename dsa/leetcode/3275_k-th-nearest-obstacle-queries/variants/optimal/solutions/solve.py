import heapq


def solve(queries: list[list[int]], k: int) -> list[int]:
    nearest: list[int] = []
    answer: list[int] = []

    for x, y in queries:
        heapq.heappush(nearest, -(abs(x) + abs(y)))
        if len(nearest) > k:
            heapq.heappop(nearest)

        answer.append(-nearest[0] if len(nearest) == k else -1)

    return answer
