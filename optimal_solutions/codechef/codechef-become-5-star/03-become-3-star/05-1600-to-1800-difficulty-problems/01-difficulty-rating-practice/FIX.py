from heapq import *


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        maxi = max(arr)
        vis = set()
        ans = [-1] * n
        for i in range(n):
            if arr[i] in vis:
                ans[i] = maxi
            else:
                ans[i] = arr[i]
            vis.add(arr[i])
        print(*ans)


if __name__ == "__main__":
    solve()
