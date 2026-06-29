from functools import cmp_to_key
import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        pieces = []
        internal = 0
        for _ in range(n):
            s = data[idx]
            idx += 1
            ones = 0
            inv = 0
            for ch in s:
                if ch == 49:
                    ones += 1
                else:
                    inv += ones
            zeros = m - ones
            pieces.append((ones, zeros))
            internal += inv

        def compare(a, b):
            left = a[0] * b[1]
            right = b[0] * a[1]
            return (left > right) - (left < right)
        pieces.sort(key=cmp_to_key(compare))
        total = internal
        ones_before = 0
        for ones, zeros in pieces:
            total += ones_before * zeros
            ones_before += ones
        out.append(str(total))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
