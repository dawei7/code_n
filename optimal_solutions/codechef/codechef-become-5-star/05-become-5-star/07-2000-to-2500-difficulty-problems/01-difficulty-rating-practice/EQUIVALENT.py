import math
import sys

def factor_signature(n: int):
    factors = []
    exps = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            factors.append(d)
            exps.append(e)
        d += 1 if d == 2 else 2
    if n > 1:
        factors.append(n)
        exps.append(1)
    g = 0
    for e in exps:
        g = math.gcd(g, e)
    return tuple(((p, e // g) for p, e in zip(factors, exps)))

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        a, b = data[idx:idx + 2]
        idx += 2
        out.append('YES' if factor_signature(a) == factor_signature(b) else 'NO')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
