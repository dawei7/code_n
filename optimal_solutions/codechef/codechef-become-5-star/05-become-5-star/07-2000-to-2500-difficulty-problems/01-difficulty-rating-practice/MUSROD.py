from functools import cmp_to_key
import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        lengths = data[idx:idx + n]
        idx += n
        beauties = data[idx:idx + n]
        idx += n
        rods = list(zip(lengths, beauties))

        def cmp(a, b):
            left = a[0] * b[1]
            right = b[0] * a[1]
            return (right > left) - (right < left)
        rods.sort(key=cmp_to_key(cmp))
        pos = 0
        ans = 0
        for length, beauty in rods:
            ans += pos * beauty
            pos += length
        out.append(str(ans))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
