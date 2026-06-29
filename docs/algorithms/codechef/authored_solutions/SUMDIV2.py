import math
import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        x, y = data[idx], data[idx + 1]
        idx += 2
        answer = x * y - x - y
        step = x // math.gcd(x, y) * y
        if answer <= 0:
            answer += ((1 - answer + step - 1) // step) * step
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
