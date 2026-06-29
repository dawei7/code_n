from collections import Counter
import sys

def possible(shorter: Counter, longer: Counter) -> bool:
    odd = 0
    for ch in set(shorter) | set(longer):
        remaining = longer[ch] - shorter[ch]
        if remaining < 0:
            return False
        odd += remaining & 1
    return odd <= 1

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        a = data[idx]
        b = data[idx + 1]
        idx += 2
        ca = Counter(a)
        cb = Counter(b)
        if n <= m:
            ok = possible(ca, cb)
        else:
            ok = possible(cb, ca)
        out.append('YES' if ok else 'NO')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
