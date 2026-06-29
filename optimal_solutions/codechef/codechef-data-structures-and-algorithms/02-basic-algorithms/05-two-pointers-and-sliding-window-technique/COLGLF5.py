def solve():
    n, m = map(int, input().split())
    f = list(map(int, input().split()))
    c = list(map(int, input().split()))
    l1, l2 = (0, 0)
    flag = 0
    ans = 0
    while l1 < n and l2 < m:
        if f[l1] < c[l2]:
            if flag:
                ans += 1
                flag = 0
            l1 += 1
        else:
            if not flag:
                ans += 1
                flag = 1
            l2 += 1
    ans += 1
    print(ans)


if __name__ == "__main__":
    solve()
