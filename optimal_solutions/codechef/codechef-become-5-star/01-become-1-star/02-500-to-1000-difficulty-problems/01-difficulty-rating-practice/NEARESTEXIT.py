import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = ['LEFT' if x <= 50 else 'RIGHT' for x in data[1:1 + t]]
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
