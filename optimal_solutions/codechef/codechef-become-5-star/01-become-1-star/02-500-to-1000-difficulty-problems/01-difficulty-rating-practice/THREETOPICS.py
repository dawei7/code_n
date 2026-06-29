import sys

def solve():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return
    a, b, c, x = values[:4]
    sys.stdout.write('Yes' if x in {a, b, c} else 'No')


if __name__ == "__main__":
    solve()
