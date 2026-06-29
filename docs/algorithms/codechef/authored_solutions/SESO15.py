import sys


def solve():
    arr = list(map(int, sys.stdin.buffer.read().split()))
    arr.sort()
    print(" ".join(map(str, arr)))


if __name__ == "__main__":
    solve()
