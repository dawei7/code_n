from collections import defaultdict


def solve():
    def dfs(node, parent, level, largest_values):
        largest_values[level] = max(largest_values.get(level, -1), node)

        for v in adj[node]:
            if v != parent:
                dfs(v, node, level + 1, largest_values)

    if __name__ == "__main__":
        n = int(input())

        adj = defaultdict(list)

        for _ in range(n - 1):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)

        largest_values = {}
        dfs(1, -1, 1, largest_values)

        print(len(largest_values))
        for level in sorted(largest_values):
            print(largest_values[level], end=' ')


if __name__ == "__main__":
    solve()
