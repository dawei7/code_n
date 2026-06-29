# cook your dish here
from bisect import bisect_left as bl, bisect_right as br


def solve():
    for i in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        hi = 1
        for num in arr[1:]:
            pos = br(arr, num, hi=hi)
            hi = max(pos + 1, hi)
            arr[pos] = num
        print(hi, *arr[:hi])


if __name__ == "__main__":
    solve()
