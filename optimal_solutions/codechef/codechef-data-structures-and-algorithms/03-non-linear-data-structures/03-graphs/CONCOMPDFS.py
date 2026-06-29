def DFS(node, visited, adj_list):
    stack = [node]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            for neighbor in adj_list[v]:
                if not visited[neighbor]:
                    stack.append(neighbor)

def FindConnectedComponents(adj_list, n):
    visited = [False] * (n + 1)
    components = 0
    for i in range(1, n + 1):
        if not visited[i]:
            DFS(i, visited, adj_list)
            components += 1
    return components

def solve():
    n, m = map(int, input().split())
    adj_list = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)
    components = FindConnectedComponents(adj_list, n)
    print(components)


if __name__ == "__main__":
    solve()
