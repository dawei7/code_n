import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    res = []
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        start = int(data[index + 2])
        index += 3
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            u = int(data[index])
            v = int(data[index + 1])
            index += 2
            graph[u].append(v)
            graph[v].append(u)
        for i in range(1, n + 1):
            graph[i].sort()
        visited = [False] * (n + 1)
        order = []
        dq = deque()
        dq.append(start)
        visited[start] = True
        while dq:
            node = dq.popleft()
            order.append(node)
            for adj in graph[node]:
                if not visited[adj]:
                    visited[adj] = True
                    dq.append(adj)
        res.append(' '.join(map(str, order)))
    sys.stdout.write('\n'.join(res))


if __name__ == "__main__":
    solve()
