class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0

    dsu = UnionFind(n)
    merges = 0
    for bit in range(30):
        prv = -1
        for i in range(n):
            if (~a[i] >> bit) & 1: continue
            if prv != -1 and dsu.find(i) != dsu.find(prv):
                ans += 1 << bit
                dsu.union(i, prv)
                merges += 1
            prv = i
    print(ans if merges == n-1 else -1)
