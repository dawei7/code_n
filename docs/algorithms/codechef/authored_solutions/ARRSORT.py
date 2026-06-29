import math
import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        perm = data[idx:idx + n]
        idx += n
        answer = 0
        for pos, value in enumerate(perm, start=1):
            answer = math.gcd(answer, abs(value - pos))
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
