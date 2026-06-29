def add(a, b):
    return (max(a[0], b[0]), min(a[1], b[1]))

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [tuple(map(int, input().split())) for _ in range(n)]
        pre = [None] * n
        suf = [None] * n
        pre[0] = a[0]
        for i in range(1, n):
            pre[i] = add(pre[i - 1], a[i])
        suf[n - 1] = a[n - 1]
        for i in range(n - 2, -1, -1):
            suf[i] = add(suf[i + 1], a[i])
        ans = []
        for i in range(n):
            xd = (1, n)
            if i > 0:
                xd = add(xd, pre[i - 1])
            if i + 1 < n:
                xd = add(xd, suf[i + 1])
            if xd[0] <= i + 1 <= xd[1] and (i + 1 < a[i][0] or i + 1 > a[i][1]):
                ans.append(i + 1)
        print(len(ans))
        for v in ans:
            print(v)


if __name__ == "__main__":
    solve()
