import math
import sys

def multiply(z1, z2):
    a, b = z1
    c, d = z2
    return (abs(a * c - b * d), abs(a * d + b * c))

def prime_representation(p: int):
    limit = math.isqrt(p)
    for a in range(limit + 1):
        b2 = p - a * a
        b = math.isqrt(b2)
        if b * b == b2:
            return (a, b)
    return None

def solve(n: int):
    original = n
    two_power = 0
    while n % 2 == 0:
        n //= 2
        two_power += 1
    factors = []
    d = 3
    while d * d <= n:
        if n % d == 0:
            exp = 0
            while n % d == 0:
                n //= d
                exp += 1
            factors.append((d, exp))
        d += 2
    if n > 1:
        factors.append((n, 1))
    ans = (1, 0)
    if two_power:
        for _ in range(two_power):
            ans = multiply(ans, (1, 1))
    for p, exp in factors:
        if p % 4 == 3:
            if exp % 2:
                return None
            scale = p ** (exp // 2)
            ans = (ans[0] * scale, ans[1] * scale)
        else:
            rep = prime_representation(p)
            if rep is None:
                return None
            for _ in range(exp):
                ans = multiply(ans, rep)
    return ans if ans[0] * ans[0] + ans[1] * ans[1] == original else None

def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = []
    for n in data[1:1 + t]:
        ans = solve(n)
        if ans is None:
            out.append('-1')
        else:
            out.append(f'{ans[0]} {ans[1]}')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
