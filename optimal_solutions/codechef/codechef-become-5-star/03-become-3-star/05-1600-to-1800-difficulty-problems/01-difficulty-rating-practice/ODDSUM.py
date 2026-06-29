import sys


def solve():
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        N = int(input())
        # Minimum sum formula
        print((N - 1) * (N - 2) + 1)


if __name__ == "__main__":
    solve()
