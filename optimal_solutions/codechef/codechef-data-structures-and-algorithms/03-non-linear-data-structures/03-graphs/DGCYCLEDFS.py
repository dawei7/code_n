


def solve():
    class Solution:
        def DFS(self, node, adj, color):
            if color[node] == 1:
                return True  # Cycle detected (node is in the current path)
            if color[node] == 0:
                color[node] = 1  # Mark the node as visiting
                for neighbor in adj[node]:  # Recur for all neighbors
                    if self.DFS(neighbor, adj, color):
                        return True  # Cycle detected in the recursion
            color[node] = 2  # Mark the node as fully processed
            return False  # No cycle detected from this node

        def findCycle(self, n, adj):
            color = [0] * (n + 1)  # Initialize color array, 0 represents unvisited

            for v in range(1, n + 1):  # Iterate through all nodes
                if color[v] == 0 and self.DFS(v, adj, color):
                    return True  # Cycle detected
            return False  # No cycle detected in the entire graph

    if __name__ == "__main__":
        # Read the number of nodes and edges
        n, m = map(int, input().split())

        # Initialize the adjacency list for the graph
        adj = [[] for _ in range(n + 1)]

        # Read the edges and build the graph
        for _ in range(m):
            u, v = map(int, input().split())
            adj[u].append(v)  # Add edge to the adjacency list

        # Create an instance of Solution class and check for cycle
        sol = Solution()
        if sol.findCycle(n, adj):
            print("YES")  # Print YES if a cycle is detected
        else:
            print("NO")   # Print NO if no cycle is detected


if __name__ == "__main__":
    solve()
