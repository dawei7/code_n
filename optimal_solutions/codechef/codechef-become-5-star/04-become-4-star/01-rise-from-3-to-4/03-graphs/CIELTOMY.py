import heapq
import sys

def count_shortest_paths(n: int, edges: list[tuple[int, int, int]]) -> int:
    graph = [[] for _ in range(n)]
    for u, v, weight in edges:
        u -= 1
        v -= 1
        graph[u].append((v, weight))
        graph[v].append((u, weight))
    inf = 10 ** 18
    dist = [inf] * n
    ways = [0] * n
    dist[0] = 0
    ways[0] = 1
    heap = [(0, 0)]
    while heap:
        current, node = heapq.heappop(heap)
        if current != dist[node]:
            continue
        for nxt, weight in graph[node]:
            nd = current + weight
            if nd < dist[nxt]:
                dist[nxt] = nd
                ways[nxt] = ways[node]
                heapq.heappush(heap, (nd, nxt))
            elif nd == dist[nxt]:
                ways[nxt] += ways[node]
    return ways[-1]

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n, m = (data[idx], data[idx + 1])
        idx += 2
        edges = []
        for _ in range(m):
            edges.append((data[idx], data[idx + 1], data[idx + 2]))
            idx += 3
        out.append(str(count_shortest_paths(n, edges)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
