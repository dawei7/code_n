import math

def TorF(v, val, h):
    time = 0
    for x in v:
        time += math.ceil(x / val)
    return time <= h

def solve():
    t = int(input())
    while t > 0:
        n, h = map(int, input().split())
        v = list(map(int, input().split()))
        first, last = (1, int(1000000000.0))
        while first < last:
            mid = (first + last) // 2
            if TorF(v, mid, h):
                last = mid
            else:
                first = mid + 1
        print(first)
        t -= 1


if __name__ == "__main__":
    solve()
