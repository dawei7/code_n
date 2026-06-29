from bisect import bisect_left as lb


def solve():
    mod = 10**9 + 7

    a = [0]

    for i in range (1,5*10**4 + 10) :
        a.append(a[-1] + i)

    fact = [1]
    inv = [1]

    for i in range (1,5*10**4 + 10) :
        fact.append((fact[-1] * i )%mod)
        inv.append(pow(fact[-1],mod-2,mod))

    for i in range(int(input())) :
        s,e = [int(x) for x in input().split()]
        x = lb(a,s)
        y = lb(a,e)
        t = x - (a[x] - s)
        t1 = y - (a[y] - e)
        if (t1 < t) :
            print(0)
            continue
        n = y - x
        r = t1 - t
        if (r > n) :
            print(0)
            continue
        ans = (fact[n] * inv[r] * inv[n-r])%mod
        print(ans)


if __name__ == "__main__":
    solve()
