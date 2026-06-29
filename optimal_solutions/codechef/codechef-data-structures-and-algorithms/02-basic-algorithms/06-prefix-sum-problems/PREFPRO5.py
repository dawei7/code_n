from math import gcd

def solve():
    n = int(input())
    pre = [0] * n
    suf = [0] * n
    v1 = list(map(int, input().split()))
    for i in range(n):
        pre[i] = v1[i] if i == 0 else gcd(v1[i], pre[i - 1])
    for i in range(n - 1, -1, -1):
        suf[i] = v1[i] if i == n - 1 else gcd(v1[i], suf[i + 1])
    fans = 0
    for i in range(n):
        if i == 0:
            fans = max(fans, suf[i + 1])
        elif i == n - 1:
            fans = max(fans, pre[i - 1])
        else:
            fans = max(fans, gcd(pre[i - 1], suf[i + 1]))
    print(fans)


if __name__ == "__main__":
    solve()
