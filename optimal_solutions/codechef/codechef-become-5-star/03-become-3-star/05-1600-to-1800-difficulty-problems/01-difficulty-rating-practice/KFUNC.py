import sys

def digital_root(value):
    return 9 if value % 9 == 0 else value % 9

def prefix_sum(first, diff, count):
    if count <= 0:
        return 0
    cycle = [digital_root(first + i * diff) for i in range(9)]
    full, rem = divmod(count, 9)
    return full * sum(cycle) + sum(cycle[:rem])

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        first, diff, left, right = data[idx:idx + 4]
        idx += 4
        out.append(str(prefix_sum(first, diff, right) - prefix_sum(first, diff, left - 1)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
