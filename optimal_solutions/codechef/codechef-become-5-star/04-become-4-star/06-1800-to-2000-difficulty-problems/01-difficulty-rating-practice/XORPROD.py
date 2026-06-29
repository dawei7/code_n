


def solve():
    mod = 998244353
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        evens, odds = sorted([x for x in a if x%2 == 0]), sorted([x for x in a if x%2 == 1])
        p = q = 0
        while p < len(odds) and q < len(evens):
            if odds[p] != 1: break
            evens[q] += 1
            p += 1
            q += 1
        ans = 1
        for i in range(p, len(odds)): ans = (ans * odds[i])%mod
        for x in evens: ans = (ans * x)%mod
        print(ans)


if __name__ == "__main__":
    solve()
