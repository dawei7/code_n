


def solve():
    class Solution:
        def getMinimumServers(self, n, serverConnections):
            # Initialize the distance array with a large number
            distance = [float('inf')] * (n + 1)

            # Create an adjacency list for the graph
            graph = defaultdict(list)
            for a, b in serverConnections:
                graph[a].append(b)
                graph[b].append(a)

            # BFS setup
            queue = deque([1])  # Start from server 1
            distance[1] = 0  # Distance to itself is 0

            # Perform BFS to find the shortest path
            while queue:
                v = queue.popleft()

                # If we reached server n, return the distance
                if v == n:
                    return 1 + distance[n]

                # Check all adjacent servers
                for neighbor in graph[v]:
                    # If visiting this neighbor is better, update its distance and enqueue it
                    if 1 + distance[v] < distance[neighbor]:
                        distance[neighbor] = 1 + distance[v]
                        queue.append(neighbor)

            # If we can't reach server n, return -1
            return -1


if __name__ == "__main__":
    solve()
