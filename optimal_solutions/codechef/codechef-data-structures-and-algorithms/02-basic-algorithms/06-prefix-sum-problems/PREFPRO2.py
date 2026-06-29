def solve():
    len = int(input())
    ar = list(map(int, input().split()))
    pre = [0] * len
    for i in range(len):
        if i != 0:
            pre[i] += pre[i - 1]
        pre[i] += ar[i]
    q = int(input())
    while q > 0:
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if a == 0:
            print(pre[b])
        else:
            print(pre[b] - pre[a - 1])
        q -= 1


if __name__ == "__main__":
    solve()
