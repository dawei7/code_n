import sys
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def factor_counts(value: int):
    counts = [0] * len(PRIMES)
    if value <= 1:
        return counts
    for i, prime in enumerate(PRIMES):
        while value % prime == 0:
            counts[i] += 1
            value //= prime
    return counts
FACTORS = [factor_counts(x) for x in range(101)]

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    arr = data[1:1 + n]
    idx = 1 + n
    prefixes = [[0] * (n + 1) for _ in PRIMES]
    for pos, value in enumerate(arr, 1):
        factors = FACTORS[value]
        for p_idx in range(len(PRIMES)):
            prefixes[p_idx][pos] = prefixes[p_idx][pos - 1] + factors[p_idx]
    q = data[idx]
    idx += 1
    out = []
    for _ in range(q):
        left, right, mod = data[idx:idx + 3]
        idx += 3
        if mod == 1:
            out.append('0')
            continue
        ans = 1 % mod
        for p_idx, prime in enumerate(PRIMES):
            exp = prefixes[p_idx][right] - prefixes[p_idx][left - 1]
            if exp:
                ans = ans * pow(prime, exp, mod) % mod
        out.append(str(ans))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
