import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        q = int(data[idx + 1])
        a = data[idx + 2]
        b = data[idx + 3]
        idx += 4
        pref = [0] * (n + 1)
        for i in range(1, n + 1):
            diff = (b[i - 1] - a[i - 1]) % 26
            sign = 1 if i % 2 == 0 else -1
            pref[i] = (pref[i - 1] + sign * diff) % 26
        for _ in range(q):
            left = int(data[idx])
            right = int(data[idx + 1])
            idx += 2
            value = (pref[right] - pref[left - 1]) % 26
            out.append('Yes' if value == 0 else 'No')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
