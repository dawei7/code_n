


def solve():
    class Solution:
        def getMinimumDistance(self, n, edges, x, y):
            # Initialize the distance array with a large value
            dis = [float('inf')] * (n + 1)

            # Initialize the adjacency list for the graph
            g = [[] for _ in range(n + 1)]

            # Build the graph
            for a, b in edges:
                g[a].append(b)
                g[b].append(a)

            # BFS setup
            q = deque([x])
            dis[x] = 0

            # Perform BFS
            while q:
                v = q.popleft()

                if v == y:
                    break

                for adj in g[v]:
                    if 1 + dis[v] < dis[adj]:
                        dis[adj] = 1 + dis[v]
                        q.append(adj)

            # If the distance to y is still infinity, return -1
            return -1 if dis[y] == float('inf') else dis[y]


if __name__ == "__main__":
    solve()
