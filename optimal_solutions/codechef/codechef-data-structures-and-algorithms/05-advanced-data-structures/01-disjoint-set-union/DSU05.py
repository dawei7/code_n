


def solve():
    parent = []

    def dsu_find(a):
        if parent[a] == a:
            return a
        return dsu_find(parent[a])

    def dsu_union(a, b):
        leader_a = dsu_find(a)
        leader_b = dsu_find(b)
        if leader_a != leader_b:
            parent[leader_b] = leader_a

    if __name__ == "__main__":
        n, m = map(int, input().split())

        for i in range(n):
            parent.append(i)

        for i in range(m):
            command = list(map(str, input().split()))
            if command[0] == "union":
                a, b = int(command[1]), int(command[2])
                dsu_union(a, b)
            elif command[0] == "find":
                a = int(command[1])
                print(dsu_find(a))


if __name__ == "__main__":
    solve()
