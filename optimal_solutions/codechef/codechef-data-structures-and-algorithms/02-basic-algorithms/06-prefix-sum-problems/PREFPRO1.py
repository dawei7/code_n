def solve():
    len = int(input())
    arr = list(map(int, input().split()))
    pre = [0] * len
    for i in range(len):
        if i != 0:
            pre[i] += pre[i - 1]
        pre[i] += arr[i]
    for e in pre:
        print(e, end=' ')
    print()


if __name__ == "__main__":
    solve()
