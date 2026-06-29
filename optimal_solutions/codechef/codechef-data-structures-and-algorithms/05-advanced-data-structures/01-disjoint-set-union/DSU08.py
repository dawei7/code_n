


def solve():
    parent = []
    setSize = []

    def dsu_find(a):
        if parent[a] == a:
            return a
        #fill in the blanks for the optimized find in DSU
        parent[a] = dsu_find(parent[a])
        return parent[a]

    def dsu_union(a, b):
        leader_a = dsu_find(a)
        leader_b = dsu_find(b)
        if leader_a != leader_b:
            #fill in the blanks for the optimized union in DSU
            if setSize[leader_b] < setSize[leader_a]:
                leader_a, leader_b = leader_b, leader_a
            parent[leader_b] = leader_a
            setSize[leader_a] += setSize[leader_b]


    if __name__ == "__main__":
        n, m = map(int, input().split())

        for i in range(n):
            parent.append(i)
            setSize.append(1)

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
