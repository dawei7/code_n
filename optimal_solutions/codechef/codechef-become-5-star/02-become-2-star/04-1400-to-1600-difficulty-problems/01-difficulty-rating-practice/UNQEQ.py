import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = []
    for n in data[1:1 + t]:
        if n % 4:
            out.append('NO')
            continue
        quarter = n // 4
        a = list(range(1, quarter + 1)) + list(range(3 * quarter + 1, n + 1))
        b = list(range(quarter + 1, 3 * quarter + 1))
        out.append('YES')
        out.append(' '.join(map(str, a)))
        out.append(' '.join(map(str, b)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
