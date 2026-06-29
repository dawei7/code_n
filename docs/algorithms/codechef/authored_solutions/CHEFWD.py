import sys


MOD = 1_000_000_007


def berlekamp_massey(sequence: list[int]) -> list[int]:
    c = [1]
    b = [1]
    length = 0
    m = 1
    bb = 1
    for n in range(len(sequence)):
        discrepancy = sequence[n]
        for i in range(1, length + 1):
            discrepancy = (discrepancy + c[i] * sequence[n - i]) % MOD
        if discrepancy == 0:
            m += 1
            continue
        old = c[:]
        coef = discrepancy * pow(bb, MOD - 2, MOD) % MOD
        if len(c) < len(b) + m:
            c.extend([0] * (len(b) + m - len(c)))
        for i, value in enumerate(b):
            c[i + m] = (c[i + m] - coef * value) % MOD
        if 2 * length <= n:
            length = n + 1 - length
            b = old
            bb = discrepancy
            m = 1
        else:
            m += 1
    return [(-c[i]) % MOD for i in range(1, length + 1)]


def combine(a: list[int], b: list[int], recurrence: list[int]) -> list[int]:
    k = len(recurrence)
    tmp = [0] * (2 * k)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    tmp[i + j] = (tmp[i + j] + x * y) % MOD
    for i in range(2 * k - 2, k - 1, -1):
        if tmp[i]:
            for j, coef in enumerate(recurrence):
                tmp[i - 1 - j] = (tmp[i - 1 - j] + tmp[i] * coef) % MOD
    return tmp[:k]


def linear_nth(initial: list[int], recurrence: list[int], n: int) -> int:
    if n < len(initial):
        return initial[n]
    k = len(recurrence)
    pol = [1] + [0] * (k - 1)
    e = [0, 1] + [0] * (k - 2) if k > 1 else [recurrence[0]]
    while n:
        if n & 1:
            pol = combine(pol, e, recurrence)
        e = combine(e, e, recurrence)
        n >>= 1
    return sum(pol[i] * initial[i] for i in range(k)) % MOD


def brute_value(n: int) -> int:
    fib = [0, 1]
    for _ in range(2, n + 5):
        fib.append((fib[-1] + fib[-2]) % MOD)
    total = 0
    for x in range(1, n):
        total += fib[x + 1] * (fib[n - x + 2] + fib[n - x + 3])
    return total % MOD


BASE = [brute_value(n) for n in range(5)]
TRANSITION = [
    [2, 1, MOD - 2, MOD - 1, 0],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
]


def mat_mul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    size = 5
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        ri = result[i]
        for k in range(size):
            if a[i][k]:
                aik = a[i][k]
                bk = b[k]
                for j in range(size):
                    ri[j] = (ri[j] + aik * bk[j]) % MOD
    return result


POWERS = [TRANSITION]
for _ in range(60):
    POWERS.append(mat_mul(POWERS[-1], POWERS[-1]))


def fast_value(n: int) -> int:
    if n < len(BASE):
        return BASE[n]
    power = n - 4
    vector = [BASE[4], BASE[3], BASE[2], BASE[1], BASE[0]]
    bit = 0
    while power:
        if power & 1:
            matrix = POWERS[bit]
            vector = [
                sum(matrix[i][j] * vector[j] for j in range(5)) % MOD
                for i in range(5)
            ]
        power >>= 1
        bit += 1
    return vector[0]


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    out = [str(fast_value(n)) for n in data[1:]]
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
