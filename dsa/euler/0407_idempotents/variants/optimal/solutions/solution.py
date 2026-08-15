"""Project Euler Problem 407: Idempotents.

Find sum_{n=1..10^7} M(n), where M(n) is the largest value of a < n such that a^2 = a (mod n).
"""

from array import array


def solve(limit: int = 10_000_000) -> int:
    """Compute sum_{n=1..limit} M(n) using SPF prime-power decomposition and CRT idempotent generation."""
    spf = array("I", range(limit + 1))
    if limit >= 0:
        spf[0] = 0
    if limit >= 1:
        spf[1] = 1

    root = int(limit**0.5)
    for i in range(2, root + 1):
        if spf[i] == i:
            start = i * i
            step = i
            for j in range(start, limit + 1, step):
                if spf[j] == j:
                    spf[j] = i

    total = 0
    spf_local = spf
    pow_local = pow

    for n in range(2, limit + 1):
        t = n
        p = spf_local[t]
        pk = 1
        while t % p == 0:
            t //= p
            pk *= p

        if t == 1:
            total += 1
            continue

        sums = [0]
        min_gt = n
        q = pk
        n_div = n // q
        inv = pow_local(n_div, -1, q)
        e = n_div * inv
        v = e
        if 1 < v < min_gt:
            min_gt = v
        sums.append(v)

        while t > 1:
            p = spf_local[t]
            pk = 1
            while t % p == 0:
                t //= p
                pk *= p
            q = pk
            n_div = n // q
            inv = pow_local(n_div, -1, q)
            e = n_div * inv
            new_sums = []
            for s in sums:
                v = s + e
                if v >= n:
                    v -= n
                if 1 < v < min_gt:
                    min_gt = v
                new_sums.append(v)
            sums += new_sums

        total += n + 1 - min_gt

    return total


if __name__ == "__main__":
    print(solve())
