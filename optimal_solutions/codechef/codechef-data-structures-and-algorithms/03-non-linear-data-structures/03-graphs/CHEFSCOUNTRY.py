from collections import deque


def solve():
    class Solution:
        # Function to perform BFS and mark visited nodes
        def bfs(self, start, adjList, visited):
            q = deque([start])  # Initialize the queue with the starting node
            visited[start] = True  # Mark the starting node as visited

            while q:
                node = q.popleft()  # Dequeue the front node
                for neighbor in adjList[node]:
                    if not visited[neighbor]:  # Check if the neighbor has not been visited
                        q.append(neighbor)  # Enqueue the neighbor
                        visited[neighbor] = True  # Mark the neighbor as visited

        # Function to find the number of connected components
        def findConnectedComponents(self, n, m, edges):
            # Initialize the adjacency list and visited array
            adjList = [[] for _ in range(n + 1)]
            visited = [False] * (n + 1)

            # Build the adjacency list from edges
            for u, v in edges:
                adjList[u].append(v)  # Add edge u-v
                adjList[v].append(u)  # Add edge v-u (undirected graph)

            components = 0
            # Iterate through all nodes
            for i in range(1, n + 1):
                if not visited[i]:  # If the node is not visited
                    components += 1  # Increment the count of connected components
                    self.bfs(i, adjList, visited)  # Perform BFS starting from this node

            return components - 1  # As required by the problem statement

    if __name__ == "__main__":
        n, m = map(int, input().split())  # Read number of nodes and edges
        edges = [list(map(int, input().split())) for _ in range(m)]  # Read edges

        sol = Solution()
        result = sol.findConnectedComponents(n, m, edges)  # Find the number of connected components
        print(result)  # Output the result


if __name__ == "__main__":
    solve()
