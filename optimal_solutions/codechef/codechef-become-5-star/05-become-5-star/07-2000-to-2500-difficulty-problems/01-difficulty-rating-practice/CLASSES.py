import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, m, s, k = (data[idx], data[idx + 1], data[idx + 2], data[idx + 3])
        idx += 4
        graph = [[] for _ in range(n + 1)]
        for _edge in range(m):
            u, v = (data[idx], data[idx + 1])
            idx += 2
            graph[u].append(v)
            graph[v].append(u)
        subjects = data[idx:idx + s]
        idx += s
        dist = [-1] * (n + 1)
        dist[0] = 0
        queue = deque([0])
        while queue:
            node = queue.popleft()
            for nxt in graph[node]:
                if dist[nxt] == -1:
                    dist[nxt] = dist[node] + 1
                    queue.append(nxt)
        chosen = sorted((dist[building] for building in subjects))[:k]
        out.append(str(2 * sum(chosen)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
