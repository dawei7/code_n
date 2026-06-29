


def solve():
    parent = []
    size = []

    def dsu_find(a):
        if parent[a] == a:
            return a
        parent[a] = dsu_find(parent[a])
        return parent[a]

    def dsu_union(a, b):
        leader_a = dsu_find(a)
        leader_b = dsu_find(b)
        if leader_a != leader_b:
            if size[leader_b] < size[leader_a]:
                leader_a, leader_b = leader_b, leader_a
            parent[leader_b] = leader_a
            size[leader_b] += size[leader_a]

    if __name__ == '__main__':
        n, m = map(int, input().split())
        parent = [i for i in range(n)]
        size = [1] * n

        for _ in range(m):
            a, b = map(int, input().split())
            dsu_union(a, b)

        q = int(input())
        for _ in range(q):
            x, y = map(int, input().split())
            if dsu_find(x) == dsu_find(y):
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    solve()
