


def solve():
    class Tree:
        def __init__(self, n):
            self.tree = [[] for _ in range(n + 1)]

        def add_edge(self, u, v):
            self.tree[u].append(v)

        def dfs(self, node):
            print(node, end=" ")
            for child in self.tree[node]:
                self.dfs(child)

    if __name__ == "__main__":
        n = int(input())
        tree = Tree(n)

        for _ in range(n - 1):
            u, v = map(int, input().split())
            tree.add_edge(u, v)

        # Start DFS from the root node
        tree.dfs(1)


if __name__ == "__main__":
    solve()
