for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    left, right = [1]*n, [1]*n
    for i in range(1, n):
        if p[i] < p[i-1]: left[i] += left[i-1]
        if p[n-1-i] < p[n-i]: right[n-1-i] += right[n-i]
    print(sum(left[i] * right[i] for i in range(n)))
