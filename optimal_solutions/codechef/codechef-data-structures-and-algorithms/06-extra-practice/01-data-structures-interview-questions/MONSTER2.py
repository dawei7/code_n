def solve():
    import sys
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        A, B, X, Y = map(int, input().split())
        if X <= Y:
            print(0)
            continue
        hits_needed = (A + (X - Y) - 1) // (X - Y)
        max_hits = (B - 1) // Y
        if hits_needed <= max_hits:
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    solve()
