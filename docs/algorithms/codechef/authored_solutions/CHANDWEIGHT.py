for _ in range(int(input())):
    n = int(input())
    w = list(map(int, input().split()))
    a = list(map(int, input().split()))
    pref, suf = [0]*n, [0]*n
    for i in range(n):
        pref[i] = a[i] - w[i]
        if i > 0:
            if a[i] < pref[i-1]: pref[i] += pref[i-1] - a[i]
    for i in reversed(range(n)):
        suf[i] = a[i] - w[i]
        if i+1 < n:
            if a[i] < suf[i+1]: suf[i] += suf[i+1] - a[i]
    ans = [0]*n
    for i in range(n):
        L, R = 0, 0
        if i > 0: L = pref[i-1]
        if i+1 < n: R = suf[i+1]
        ans[i] = max(L+R - w[i], a[i] - w[i])
    print(*ans)
