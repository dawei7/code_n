


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    mp = {}

    ans = 0
    for i in range(n):
        if (a[i] * a[i]) < 10**9: 
            ans += mp.get(a[i] * a[i], 0)
        mp[a[i]] = mp.get(a[i], 0) + 1

    print(ans)


if __name__ == "__main__":
    solve()
