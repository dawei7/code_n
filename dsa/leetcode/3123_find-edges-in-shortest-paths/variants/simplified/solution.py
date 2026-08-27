from collections import deque
from heapq import heappop, heappush
from typing import List


class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        g = [[] for _ in range(n)]
        for i, (a, b, w) in enumerate(edges):
            g[a].append((b, w, i))
            g[b].append((a, w, i))

        dist = [float('inf')] * n
        dist[0] = 0
        q = [(0, 0)]
        while q:
            da, a = heappop(q)
            if da > dist[a]:
                continue
            for b, w, _ in g[a]:
                if dist[b] > da + w:
                    dist[b] = da + w
                    heappush(q, (dist[b], b))

        m = len(edges)
        ans = [False] * m
        if dist[n - 1] == float('inf'):
            return ans

        visited = [False] * n
        visited[n - 1] = True
        bfs_q = deque([n - 1])
        while bfs_q:
            a = bfs_q.popleft()
            for b, w, i in g[a]:
                if dist[a] == dist[b] + w:
                    ans[i] = True
                    if not visited[b]:
                        visited[b] = True
                        bfs_q.append(b)
        return ans
