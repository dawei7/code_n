import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = [str((items + 9) // 10) for items in data[1:1 + t]]
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
