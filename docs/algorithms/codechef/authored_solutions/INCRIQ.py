import sys


def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    x = int(data[0])
    sys.stdout.write("Yes" if x + 7 > 170 else "No")


if __name__ == "__main__":
    solve()
