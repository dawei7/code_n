import math
import sys

def connected(values):
    n = len(values)
    seen = [False] * n
    stack = [0]
    seen[0] = True
    while stack:
        i = stack.pop()
        for j in range(n):
            if not seen[j] and math.gcd(values[i], values[j]) == 1:
                seen[j] = True
                stack.append(j)
    return all(seen)

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out = []
    safe_primes = [47, 43, 41, 37, 31, 29]
    for _ in range(t):
        n = data[idx]
        idx += 1
        values = data[idx:idx + n]
        idx += n
        if connected(values):
            out.append('0')
            out.append(' '.join(map(str, values)))
            continue
        remaining = set(values[1:])
        replacement = next((prime for prime in safe_primes if prime not in remaining), safe_primes[0])
        values[0] = replacement
        out.append('1')
        out.append(' '.join(map(str, values)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
