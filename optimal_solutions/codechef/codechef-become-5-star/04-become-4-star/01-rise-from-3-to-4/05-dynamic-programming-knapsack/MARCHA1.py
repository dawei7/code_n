import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, target = (data[idx], data[idx + 1])
        idx += 2
        possible = 1
        for value in data[idx:idx + n]:
            possible |= possible << value
        idx += n
        out.append('Yes' if possible >> target & 1 else 'No')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
