import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        _, position, swaps = data[idx:idx + 3]
        idx += 3
        for _ in range(swaps):
            a, b = (data[idx], data[idx + 1])
            idx += 2
            if position == a:
                position = b
            elif position == b:
                position = a
        out.append(str(position))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
