


def solve():
    def dfs(v, par):
        visited[v] = True  # Mark the current node as visited
        for u in adjList[v]:  # Iterate over all adjacent nodes
            if not visited[u]:  # If the neighbor node has not been visited
                if dfs(u, v):  # Recursively perform DFS on the neighbor
                    return True  # Cycle detected in recursive DFS
            elif u != par:  # If the neighbor is not the parent, a back edge is detected
                return True  # Cycle detected
        return False  # No cycle detected in this path

    def hasCycle(n):
        for v in range(1, n + 1):  # Iterate over all nodes
            if not visited[v]:  # If the node has not been visited
                if dfs(v, -1):  # Perform DFS starting from this node
                    return True  # Cycle detected
        return False  # No cycle found

    if __name__ == "__main__":
        import sys
        sys.setrecursionlimit(10**6)  # Increase recursion limit for large graphs

        # Input fast I/O
        input = sys.stdin.read
        data = input().splitlines()  # Read all input lines

        # Reading n (nodes) and m (edges)
        n, m = map(int, data[0].split())

        # Initialize visited array and adjacency list
        visited = [False] * (n + 1)
        adjList = [[] for _ in range(n + 1)]

        # Reading edges and building the adjacency list
        for i in range(1, m + 1):
            u, v = map(int, data[i].split())
            adjList[u].append(v)  # Add edge from u to v
            adjList[v].append(u)  # Add edge from v to u (undirected graph)

        # Check for cycle and print result
        if hasCycle(n):
            print("YES")  # Print YES if a cycle is detected
        else:
            print("NO")   # Print NO if no cycle is detected


if __name__ == "__main__":
    solve()
