for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in reversed(range(n//2)):
        a[i] += ans
        if a[i] > a[n-1-i]:
            ans = -1
            break
        ans += a[n-1-i] - a[i]
    print(ans)
