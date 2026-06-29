import sys

def solve():
    input = sys.stdin.readline
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        arr = list(map(int, input().split()))
        distinct = []
        prev = None
        for num in arr:
            if prev is None or num != prev:
                distinct.append(num)
                prev = num
        print(len(distinct))
        print(' '.join(map(str, distinct)))


if __name__ == "__main__":
    solve()
