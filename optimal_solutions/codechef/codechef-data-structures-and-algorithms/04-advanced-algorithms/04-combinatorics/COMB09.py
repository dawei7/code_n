


def solve():
    MOD = 10**9 + 7

    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        ways = 1
        for i in range(n):
            # Can pick 0 or 1 or 2 .... a[i] number of i-th fruit
            # So we can pick the i-th fruit in a[i] + 1 number of ways
            ways = (ways * (a[i] + 1)) % MOD

        print(ways)


if __name__ == "__main__":
    solve()
