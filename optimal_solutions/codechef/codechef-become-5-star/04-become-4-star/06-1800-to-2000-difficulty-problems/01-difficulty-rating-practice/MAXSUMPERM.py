import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        q = data[idx + 1]
        idx += 2
        arr = data[idx:idx + n]
        idx += n
        diff = [0] * (n + 1)
        for _ in range(q):
            left = data[idx] - 1
            right = data[idx + 1] - 1
            idx += 2
            diff[left] += 1
            diff[right + 1] -= 1
        freq = [0] * n
        cur = 0
        for i in range(n):
            cur += diff[i]
            freq[i] = cur
        positions = sorted(range(n), key=lambda i: freq[i])
        values = sorted(arr)
        arranged = [0] * n
        for pos, value in zip(positions, values):
            arranged[pos] = value
        total = sum((value * count for value, count in zip(arranged, freq)))
        out.append(str(total))
        out.append(' '.join(map(str, arranged)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
