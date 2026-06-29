


def solve():
    M = 999983
    MX = 1000000000

    Hash = [0] * M

    # Hash Function
    def f(x):
        return x % M

    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        # If a[i] * a[i] exceeds the max, discard it
        if a[i] * a[i] < MX:
            ans += Hash[f(a[i] * a[i])]
        Hash[f(a[i])] += 1

    print(ans)


if __name__ == "__main__":
    solve()
