def solve():
    import sys
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        res = 0
        for num in arr:
            res ^= num
        sys.stdout.write(str(res) + '\n')


if __name__ == "__main__":
    solve()
