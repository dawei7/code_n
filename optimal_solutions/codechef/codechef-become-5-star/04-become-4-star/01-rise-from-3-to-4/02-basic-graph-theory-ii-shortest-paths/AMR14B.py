import heapq
import sys

class DSU:

    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = (self.find(a), self.find(b))
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = (rb, ra)
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    INF = 10 ** 30
    for _ in range(t):
        n, m = (data[idx], data[idx + 1])
        idx += 2
        graph = [[] for _ in range(n)]
        edges = []
        for _edge in range(m):
            u, v, w = (data[idx], data[idx + 1], data[idx + 2])
            idx += 3
            graph[u].append((v, w))
            graph[v].append((u, w))
            edges.append((w, u, v))
        dsu = DSU(n)
        mst = 0
        used = 0
        for w, u, v in sorted(edges):
            if dsu.union(u, v):
                mst += w
                used += 1
        if n and used != n - 1:
            out.append('NO')
            continue
        dist = [INF] * n
        last = [INF] * n
        dist[0] = 0
        last[0] = 0
        heap = [(0, 0, 0)]
        visited = [False] * n
        spt = 0
        reached = 0
        while heap:
            d, edge_w, u = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True
            reached += 1
            spt += edge_w
            for v, w in graph[u]:
                nd = d + w
                if not visited[v] and (nd < dist[v] or (nd == dist[v] and w < last[v])):
                    dist[v] = nd
                    last[v] = w
                    heapq.heappush(heap, (nd, w, v))
        out.append('YES' if reached == n and spt == mst else 'NO')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
