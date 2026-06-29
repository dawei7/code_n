def solve():
    n = int(input())
    tree = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        tree[u].append(v)
    for i in range(n):
        for j in range(len(tree[i])):
            print(tree[i][j], end=' ')
        print()


if __name__ == "__main__":
    solve()
