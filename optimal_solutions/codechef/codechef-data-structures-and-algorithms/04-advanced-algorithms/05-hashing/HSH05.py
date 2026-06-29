


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    MX = 10001
    Hash = [0] * MX

    ans = 0
    for x in a:
        if x * x < MX:
            ans += Hash[x * x]
        Hash[x] += 1

    print(ans)


if __name__ == "__main__":
    solve()
