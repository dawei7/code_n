import heapq


def solve(costs: list[int], k: int, candidates: int) -> int:
    n = len(costs)
    heap: list[tuple[int, int, int]] = []

    for index in range(candidates):
        heap.append((costs[index], index, 0))
    for index in range(max(candidates, n - candidates), n):
        heap.append((costs[index], index, 1))
    heapq.heapify(heap)

    left = candidates
    right = n - candidates - 1
    total = 0

    for _ in range(k):
        cost, _, side = heapq.heappop(heap)
        total += cost

        if left <= right:
            if side == 0:
                heapq.heappush(heap, (costs[left], left, 0))
                left += 1
            else:
                heapq.heappush(heap, (costs[right], right, 1))
                right -= 1

    return total
