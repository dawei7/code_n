import sys


def solve():
    input = sys.stdin.read
    sys.setrecursionlimit(100000)
    from functools import reduce

    a = int(1e18)
    b = int(1e9 + 7)

    def c(d, e):
        while e:
            d, e = e, d % e
        return d

    def f(g):
        print(' '.join(map(str, g)))

    def h(i, j, k):
        i %= k
        l = 1
        while j > 0:
            if j & 1:
                l = (l * i) % k
            i = (i * i) % k
            j //= 2
        return l

    m = [0, 1, 0, -1]
    n = [1, 0, -1, 0]

    def o(p, q):
        p %= b
        q %= b
        return p * q % b

    data = input().split()
    n = int(data[0])
    k = int(data[1])
    v = list(map(int, data[2:n + 2]))

    res = 0
    hash_map = [-1] * (int(1e5) + 10)

    r = 0
    p = -1
    mx = 0

    for l in range(n):
        while p < l:
            mx = max(mx, v[r])
            hash_map[v[r]] = r
            r += 1

            if r == n:
                length = n - l
                res += (length + 1) * length // 2
                print(res)
                sys.exit()

            if v[r] > k:
                for x in range(k, mx + 1, v[r]):
                    if hash_map[x] != -1 and hash_map[x] > p and hash_map[x] >= l:
                        p = hash_map[x]

        res += r - l
    print(res)


if __name__ == "__main__":
    solve()
