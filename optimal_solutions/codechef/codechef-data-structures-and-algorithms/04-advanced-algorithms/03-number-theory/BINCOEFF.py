


def solve():
    MOD = 1000000007
    MAXN = 1000000

    def exp(x, n, m):
        x %= m
        res = 1
        while n > 0:
            if n % 2 == 1:
                res = (res * x) % m
            x = (x * x) % m
            n //= 2
        return res

    def factorial(m):
        fac = [0] * (MAXN + 1)
        fac[0] = 1
        for i in range(1, MAXN + 1):
            fac[i] = (fac[i - 1] * i) % m
        return fac

    def inverses(m, fac):
        inv = [0] * (MAXN + 1)
        inv[MAXN] = exp(fac[MAXN], m - 2, m)
        for i in range(MAXN, 0, -1):
            inv[i - 1] = (inv[i] * i) % m
        return inv

    def choose1(n, k, m, fac, inv):
        return ((fac[n] * inv[k] % m) * inv[n - k]) % m

    t = int(input())
    fac = factorial(MOD)
    inv = inverses(MOD, fac)

    for _ in range(t):
        a, b = map(int, input().split())
        result = choose1(a, b, MOD, fac, inv)
        print(result)


if __name__ == "__main__":
    solve()
