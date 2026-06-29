import heapq
import sys

def solve_case(n: int, budget: int, ratings: list[int], intervals: list[tuple[int, int, int]]) -> int:
    starts: list[list[tuple[int, int]]] = [[] for _ in range(n + 2)]
    for left, right, cost in intervals:
        starts[left].append((cost, right))
    cheapest = [10 ** 9] * (n + 1)
    heap: list[tuple[int, int]] = []
    for pos in range(1, n + 1):
        for item in starts[pos]:
            heapq.heappush(heap, item)
        while heap and heap[0][1] < pos:
            heapq.heappop(heap)
        if heap:
            cheapest[pos] = heap[0][0]
    total = sum(ratings)
    dp = [0] * (budget + 1)
    for pos, rating in enumerate(ratings, 1):
        if rating >= 0:
            continue
        cost = cheapest[pos]
        value = -rating
        if cost > budget:
            continue
        for money in range(budget, cost - 1, -1):
            candidate = dp[money - cost] + value
            if candidate > dp[money]:
                dp[money] = candidate
    return total + max(dp)

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n, budget, m = (data[idx], data[idx + 1], data[idx + 2])
        idx += 3
        ratings = data[idx:idx + n]
        idx += n
        intervals = []
        for _ in range(m):
            intervals.append((data[idx], data[idx + 1], data[idx + 2]))
            idx += 3
        out.append(str(solve_case(n, budget, ratings, intervals)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
