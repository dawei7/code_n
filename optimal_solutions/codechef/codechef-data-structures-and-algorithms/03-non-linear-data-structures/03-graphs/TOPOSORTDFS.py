import sys
from collections import deque


def solve():
    sys.setrecursionlimit(10**6)

    N = 200005
    adj = [[] for _ in range(N)]
    vis = [False] * N
    col = [0] * N
    topological_order = []
    n = 0

    def dfs(v):
        if vis[v]:
            return

        vis[v] = True

        for i in adj[v]:
            dfs(i)

        topological_order.append(v)

    def cycle(s):
        col[s] = 1
        for i in adj[s]:
            if col[i] == 0:
                if cycle(i):
                    return True
            elif col[i] == 1:
                return True
        col[s] = 2
        return False

    def find_topological_sort():
        global topological_order

        for i in range(1, n + 1):
            if col[i] == 0 and cycle(i):
                print(-1)
                return
            if not vis[i]:
                dfs(i)

        topological_order.reverse()
        print(' '.join(map(str, topological_order)))

    if __name__ == "__main__":
        input = sys.stdin.read
        data = input().split()

        idx = 0
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2

        for _ in range(m):
            a = int(data[idx])
            b = int(data[idx + 1])
            adj[a].append(b)
            idx += 2

        find_topological_sort()


if __name__ == "__main__":
    solve()
