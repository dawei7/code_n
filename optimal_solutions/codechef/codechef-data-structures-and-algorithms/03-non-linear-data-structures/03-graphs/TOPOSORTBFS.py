from collections import deque, defaultdict


def solve():
    def topo_sort(n, adj, indegree):
        q = deque()
        topo_order = []

        # Initialize queue with nodes having zero indegree
        for i in range(1, n + 1):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            topo_order.append(node)
            for v in adj[node]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        if len(topo_order) == n:
            print(" ".join(map(str, topo_order)))
        else:
            print(-1)

    if __name__ == "__main__":
        import sys
        input = sys.stdin.read
        data = input().split()

        index = 0
        n = int(data[index])
        m = int(data[index + 1])
        index += 2

        # Initialize adjacency list and indegree array
        adj = defaultdict(list)
        indegree = [0] * (n + 1)

        for _ in range(m):
            u = int(data[index])
            v = int(data[index + 1])
            index += 2
            adj[u].append(v)
            indegree[v] += 1

        topo_sort(n, adj, indegree)


if __name__ == "__main__":
    solve()
