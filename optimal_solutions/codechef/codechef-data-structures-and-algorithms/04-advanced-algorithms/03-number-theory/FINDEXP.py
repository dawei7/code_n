


def solve():
    def modexp(a, b, m):
        a %= m
        res = 1
        while b > 0:
            if b & 1:
                res = (res * a) % m
            a = (a * a) % m
            b >>= 1
        return res

    t = int(input())

    for _ in range(t):
        a, b, m = map(int, input().split())
        print(modexp(a, b, m))


if __name__ == "__main__":
    solve()
