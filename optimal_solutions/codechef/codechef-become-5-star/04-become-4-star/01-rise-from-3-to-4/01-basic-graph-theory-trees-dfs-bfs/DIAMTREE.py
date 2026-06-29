from collections import deque


def solve():
    def bfs(start, adj):
        queue = deque([start])
        dist = [-1] * len(adj)
        dist[start] = 0
        farthest = start
        max_dist = 0

        while queue:
            node = queue.popleft()
            for neigh in adj[node]:
                if dist[neigh] == -1:
                    dist[neigh] = dist[node] + 1
                    queue.append(neigh)
                    if dist[neigh] > max_dist:
                        max_dist = dist[neigh]
                        farthest = neigh

        return (farthest, max_dist)

    t = int(input())
    for _ in range(t):
        n = int(input())
        adj_list = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u, v = map(int, input().split())
            adj_list[u].append(v)
            adj_list[v].append(u)

        leaf = bfs(1, adj_list)
        diameter = bfs(leaf[0], adj_list)
        print(diameter[1])


if __name__ == "__main__":
    solve()
