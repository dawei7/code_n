


def solve():
    class Solution:
        # Function to perform DFS and mark visited nodes
        def dfs(self, node, adjList, visited):
            stack = [node]
            while stack:
                current = stack.pop()
                if not visited[current]:
                    visited[current] = True
                    for neighbor in adjList[current]:
                        if not visited[neighbor]:
                            stack.append(neighbor)

        # Function to count the number of connected components
        def countComponents(self, n, m, edges):
            # Initialize adjacency list and visited array
            adjList = defaultdict(list)
            visited = [False] * (n + 1)

            # Build the adjacency list from the edges
            for u, v in edges:
                adjList[u].append(v) # Add edge from u to v
                adjList[v].append(u) # Add edge from v to u (undirected graph)

            components = 0 # Variable to count the number of connected components

            # Iterate through all nodes to count connected components
            for i in range(1, n + 1):
                if not visited[i]: # If the node has not been visited
                    self.dfs(i, adjList, visited) # Perform DFS to visit all nodes in the component
                    components += 1 # Increment the count of connected components

            return components # Return the number of connected components


if __name__ == "__main__":
    solve()
