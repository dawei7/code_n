import heapq
import sys

def minimum_travel_cost(heights: list[int], costs: list[int], roads: list[tuple[int, int]]) -> int:
    n = len(heights)
    graph = [[] for _ in range(n)]
    for u, v in roads:
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    inf = 10 ** 30
    up = [inf] * n
    down = [inf] * n
    up[0] = costs[0]
    down[0] = costs[0]
    heap: list[tuple[int, int, int]] = [(costs[0], 0, 0), (costs[0], 1, 0)]
    while heap:
        current, mode, node = heapq.heappop(heap)
        dist = up if mode == 0 else down
        if current != dist[node]:
            continue
        if node == n - 1:
            return current
        other_dist = down if mode == 0 else up
        switched = current + costs[node]
        if switched < other_dist[node]:
            other_dist[node] = switched
            heapq.heappush(heap, (switched, 1 - mode, node))
        for nxt in graph[node]:
            if mode == 0:
                if heights[node] <= heights[nxt] and current < up[nxt]:
                    up[nxt] = current
                    heapq.heappush(heap, (current, 0, nxt))
            elif heights[node] >= heights[nxt] and current < down[nxt]:
                down[nxt] = current
                heapq.heappush(heap, (current, 1, nxt))
    return -1

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, r = (data[0], data[1])
    idx = 2
    heights = data[idx:idx + n]
    idx += n
    costs = data[idx:idx + n]
    idx += n
    roads = [(data[idx + 2 * i], data[idx + 2 * i + 1]) for i in range(r)]
    print(minimum_travel_cost(heights, costs, roads))


if __name__ == "__main__":
    solve()
