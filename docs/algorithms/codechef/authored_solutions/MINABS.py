for _ in range(int(input())):
    n, a, b = int(input()), input(), input()
    ans = 0
    for i in range(n):
        ans += ord(a[i]) - ord(b[i]) + 26
    print(min(ans%26, (-ans)%26))
