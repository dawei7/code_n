import heapq
import sys

def solve_case(n: int, hospitals: list[tuple[int, int]], roads: list[tuple[int, int, int]]) -> list[int]:
    graph = [[] for _ in range(n)]
    for u, v, distance in roads:
        u -= 1
        v -= 1
        graph[u].append((v, distance))
        graph[v].append((u, distance))
    inf = 10 ** 30
    dist = [inf] * n
    heap: list[tuple[int, int]] = []
    for city, cost in hospitals:
        city -= 1
        if cost < dist[city]:
            dist[city] = cost
            heapq.heappush(heap, (cost, city))
    while heap:
        current, node = heapq.heappop(heap)
        if current != dist[node]:
            continue
        for nxt, weight in graph[node]:
            nd = current + weight
            if nd < dist[nxt]:
                dist[nxt] = nd
                heapq.heappush(heap, (nd, nxt))
    return dist

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n, m, k = (data[idx], data[idx + 1], data[idx + 2])
        idx += 3
        hospitals = []
        for _ in range(k):
            hospitals.append((data[idx], data[idx + 1]))
            idx += 2
        roads = []
        for _ in range(m):
            roads.append((data[idx], data[idx + 1], data[idx + 2]))
            idx += 3
        out.append(' '.join(map(str, solve_case(n, hospitals, roads))))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
