import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        values = data[idx:idx + n]
        idx += n
        if n < 3:
            out.append('NO')
            continue
        values.sort()
        max_count = values.count(values[-1])
        if max_count >= 2:
            out.append('YES' if max_count <= (n + 1) // 2 else 'NO')
        else:
            second_largest = values[-2]
            out.append('YES' if values[0] < second_largest else 'NO')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
