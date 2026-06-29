import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    high_a = 1 << 29
    high_b = 1 << 28
    out = []
    for x in data[1:1 + t]:
        out.append(f'{x | high_a} {x | high_b} {x}')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
