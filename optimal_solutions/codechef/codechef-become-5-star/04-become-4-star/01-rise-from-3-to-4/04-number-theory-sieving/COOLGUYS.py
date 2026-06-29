import math
import sys

def divisor_pair_count(n: int) -> int:
    total = 0
    left = 1
    while left <= n:
        quotient = n // left
        right = n // quotient
        total += quotient * (right - left + 1)
        left = right + 1
    return total

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    out: list[str] = []
    for i in range(1, t + 1):
        n = data[i]
        numerator = divisor_pair_count(n)
        denominator = n * n
        common = math.gcd(numerator, denominator)
        out.append(f'{numerator // common}/{denominator // common}')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
