"""Project Euler Problem 586: Binary Quadratic Form.

Find f(10^15, 40), where f(n, r) is the number of integers k <= n that can be
expressed as k = a^2 + 3ab + b^2 with a > b > 0 in exactly r different ways.
"""

import bisect
from collections import Counter
import math
from typing import List, Tuple


def _sieve_primes_upto(n: int) -> List[int]:
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    lim = int(math.isqrt(n))
    for p in range(2, lim + 1):
        if sieve[p]:
            start = p * p
            step = p
            sieve[start : n + 1 : step] = b"\x00" * (((n - start) // step) + 1)
    return [i for i in range(n + 1) if sieve[i]]


def _iroot(n: int, k: int) -> int:
    if k == 1:
        return n
    if k == 2:
        return int(math.isqrt(n))
    x = int(n ** (1.0 / k))
    if x < 1:
        x = 1
    while pow(x + 1, k) <= n:
        x += 1
    while pow(x, k) > n:
        x -= 1
    return x


def _factor_multisets(target: int) -> List[List[int]]:
    res: List[List[int]] = []

    def rec(rem: int, start: int, cur: List[int]) -> None:
        if rem == 1:
            res.append(cur.copy())
            return
        for f in range(start, rem + 1):
            if f < 2:
                continue
            if rem % f == 0:
                cur.append(f)
                rec(rem // f, f, cur)
                cur.pop()

    rec(target, 2, [])
    return res


def _unique_permutations(multiset: List[int]) -> List[Tuple[int, ...]]:
    c = Counter(multiset)
    keys = sorted(c)
    out: List[Tuple[int, ...]] = []
    seq = [0] * len(multiset)

    def backtrack(pos: int) -> None:
        if pos == len(multiset):
            out.append(tuple(seq))
            return
        prev = None
        for k in keys:
            if c[k] == 0:
                continue
            if prev == k:
                continue
            prev = k
            c[k] -= 1
            seq[pos] = k
            backtrack(pos + 1)
            c[k] += 1

    backtrack(0)
    return out


def _multipliers_prefix(qmax: int) -> List[int]:
    if qmax <= 0:
        return [0]

    inert_primes = [
        p for p in _sieve_primes_upto(int(math.isqrt(qmax)) + 1) if p % 5 in (2, 3)
    ]

    vals: List[int] = []

    def rec(idx: int, cur: int) -> None:
        t = cur
        while t <= qmax:
            vals.append(t)
            t *= 5

        for j in range(idx, len(inert_primes)):
            p = inert_primes[j]
            p2 = p * p
            if cur * p2 > qmax:
                break
            x = cur * p2
            while x <= qmax:
                rec(j + 1, x)
                x *= p2

    rec(0, 1)
    vals = sorted(set(vals))

    w_arr = [0] * (qmax + 1)
    c = 0
    i = 0
    for x in range(1, qmax + 1):
        while i < len(vals) and vals[i] == x:
            c += 1
            i += 1
        w_arr[x] = c
    return w_arr


def _build_sequences(
    n: int, r: int, first_split_primes: List[int]
) -> List[Tuple[int, ...]]:
    seqs: List[Tuple[int, ...]] = []
    for d in (2 * r, 2 * r + 1):
        for facs in _factor_multisets(d):
            exps = [f - 1 for f in facs]
            for seq in _unique_permutations(exps):
                if len(seq) > len(first_split_primes):
                    continue
                prod = 1
                ok = True
                for p, e in zip(first_split_primes, seq):
                    prod *= pow(p, e)
                    if prod > n:
                        ok = False
                        break
                if ok:
                    seqs.append(seq)
    return seqs


def solve(n: int = 10**15, r: int = 40) -> int:
    """Compute f(n, r) using prime ideal splitting in Z[(1+sqrt(5))/2] and quotient grouping."""
    small_primes = _sieve_primes_upto(20000)
    first_split = [p for p in small_primes if p % 5 in (1, 4)]
    seqs = _build_sequences(n, r, first_split)
    if not seqs:
        return 0

    min_core = None
    for seq in seqs:
        prod = 1
        for p, e in zip(first_split, seq):
            prod *= pow(p, e)
        if min_core is None or prod < min_core:
            min_core = prod

    qmax = n // min_core
    w_prefix = _multipliers_prefix(qmax)

    max_need = 0
    for seq in seqs:
        if len(seq) == 1:
            bound = _iroot(n, seq[0])
        else:
            prod = 1
            for p, e in zip(first_split, seq[:-1]):
                prod *= pow(p, e)
            bound = _iroot(n // prod, seq[-1])
        if bound > max_need:
            max_need = bound

    primes = _sieve_primes_upto(max_need + 10)
    split_primes = [p for p in primes if p % 5 in (1, 4)]

    def sum_last(a_val: int, start_idx: int, e: int) -> int:
        max_p = _iroot(n // a_val, e)
        end_idx = bisect.bisect_right(split_primes, max_p)
        if end_idx <= start_idx:
            return 0

        total = 0
        idx = start_idx
        while idx < end_idx:
            p = split_primes[idx]
            pe = p if e == 1 else (p * p if e == 2 else pow(p, e))
            q = n // (a_val * pe)
            high_p = _iroot(n // (a_val * q), e)
            if high_p > max_p:
                high_p = max_p
            idx2 = bisect.bisect_right(split_primes, high_p, idx, end_idx)
            total += (idx2 - idx) * w_prefix[q]
            idx = idx2
        return total

    def sum_for_sequence(seq: Tuple[int, ...]) -> int:
        k_len = len(seq)
        total = 0

        def rec(pos: int, start_idx: int, a_val: int) -> None:
            nonlocal total
            if pos == k_len - 1:
                total += sum_last(a_val, start_idx, seq[pos])
                return

            e = seq[pos]
            max_p_here = _iroot(n // a_val, e)
            for idx in range(start_idx, len(split_primes)):
                if idx + (k_len - 1 - pos) >= len(split_primes):
                    break

                p = split_primes[idx]
                if p > max_p_here:
                    break

                pe = p if e == 1 else (p * p if e == 2 else pow(p, e))
                new_a = a_val * pe
                if new_a > n:
                    break

                max_rem = n // new_a
                prod_min = 1
                ok = True
                for j in range(pos + 1, k_len):
                    pj = split_primes[idx + (j - pos)]
                    ej = seq[j]
                    prod_min *= (
                        pj if ej == 1 else (pj * pj if ej == 2 else pow(pj, ej))
                    )
                    if prod_min > max_rem:
                        ok = False
                        break
                if not ok:
                    break

                rec(pos + 1, idx + 1, new_a)

        rec(0, 0, 1)
        return total

    ans = 0
    for seq in seqs:
        ans += sum_for_sequence(seq)
    return ans


if __name__ == "__main__":
    print(solve())
