class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets

mod = 10**9 + 7
maxn = 2*10**5 + 5
fac = [1]*(maxn)
for i in range(2, maxn): fac[i] = fac[i-1] * i % mod
def C(n, r):
    if n < r or r < 0: return 0
    return fac[n] * pow(fac[r] * fac[n-r], mod-2, mod) % mod

for _ in range(int(input())):
    n, m = map(int, input().split())
    D = DisjointSetUnion(n)
    for i in range(m):
        u, v = map(int, input().split())
        D.union(u-1, v-1)
    a = list(map(int, input().split()))
    comps = [ [] for _ in range(n)]
    for i in range(n): comps[D.find(i)].append(a[i])
    rem = n
    ans = 1
    for i in range(n):
        freq = {}
        for x in comps[i]:
            if x not in freq: freq[x] = 0
            freq[x] += 1
        ans = ans * C(rem, len(comps[i])) % mod
        rem -= len(comps[i])
        for x in freq.values():
            ans = ans * fac[x] % mod
    print(ans)
