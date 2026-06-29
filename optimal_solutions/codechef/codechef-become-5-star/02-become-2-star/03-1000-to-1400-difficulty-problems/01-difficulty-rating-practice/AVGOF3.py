import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = []
    for x in data[1:1 + t]:
        out.append(f'{x - 1} {x} {x + 1}')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
