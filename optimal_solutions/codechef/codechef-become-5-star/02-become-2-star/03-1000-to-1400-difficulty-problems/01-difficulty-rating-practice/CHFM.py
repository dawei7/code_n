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
        total = sum(values)
        if total % n:
            out.append('Impossible')
            continue
        mean = total // n
        answer = next((i + 1 for i, value in enumerate(values) if value == mean), None)
        out.append(str(answer) if answer is not None else 'Impossible')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
