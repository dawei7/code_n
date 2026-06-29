import math
import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, a, b, k = (data[idx], data[idx + 1], data[idx + 2], data[idx + 3])
        idx += 4
        lcm = a // math.gcd(a, b) * b
        solved = n // a + n // b - 2 * (n // lcm)
        out.append('Win' if solved >= k else 'Lose')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
