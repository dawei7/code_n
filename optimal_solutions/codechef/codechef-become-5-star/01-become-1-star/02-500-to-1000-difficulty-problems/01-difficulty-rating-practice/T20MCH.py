import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    target, overs, current = data[:3]
    possible = current + (20 - overs) * 36
    sys.stdout.write('YES' if possible > target else 'NO')


if __name__ == "__main__":
    solve()
