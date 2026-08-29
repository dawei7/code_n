"""Project Euler Problem 771: Pseudo Geometric Sequences.

Find G(10^18) mod 10^9+7, the number of strictly increasing integer sequences
a_0 < a_1 < ... < a_n <= N (n >= 4) satisfying |a_i^2 - a_{i-1} a_{i+1}| <= 2.
"""

from bisect import bisect_right
from typing import List, Tuple

_MOD = 1_000_000_007


def _iroot4(n: int) -> int:
    x = int(n**0.25)
    while (x + 1) ** 4 <= n:
        x += 1
    while x**4 > n:
        x -= 1
    return x


def _phi_sieve(n: int) -> List[int]:
    phi = list(range(n + 1))
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    return phi


def _count_consecutive(n: int) -> int:
    if n < 5:
        return 0
    return (n - 4) * (n - 3) // 2


def _count_geometric(n: int, phi: List[int]) -> int:
    max_p = _iroot4(n)
    total = 0
    for p in range(2, max_p + 1):
        ph = phi[p]
        if ph == 0:
            continue
        p_pow = p * p * p * p
        while p_pow <= n:
            total += ph * (n // p_pow)
            p_pow *= p
    return total


def _seq_len_limit(a0: int, a1: int, m: int, s: int, n: int) -> int:
    length = 2
    prev, cur = a0, a1
    while True:
        nxt = m * cur + s * prev
        if nxt > n:
            break
        prev, cur = cur, nxt
        length += 1
    return length


def _count_seq_from_recurrence(a0: int, a1: int, m: int, s: int, n: int) -> int:
    length = _seq_len_limit(a0, a1, m, s, n)
    if length < 5:
        return 0
    return (length - 4) * (length - 3) // 2


def _count_regular(n: int) -> int:
    total = 0
    total += _count_seq_from_recurrence(1, 2, 1, 1, n)

    max_m = _iroot4(n) + 2
    for m in range(2, max_m + 1):
        length = _seq_len_limit(1, m, m, 1, n)
        if length >= 5:
            total += (length - 4) * (length - 3) // 2

    total += _count_seq_from_recurrence(1, 3, 2, 1, n)

    for m in range(3, max_m + 1):
        length = _seq_len_limit(1, m, m, -1, n)
        if length >= 5:
            total += (length - 4) * (length - 3) // 2

    total += _count_seq_from_recurrence(1, 2, 3, -1, n)
    total += _count_seq_from_recurrence(1, 3, 4, -1, n)
    return total


def _is_consecutive(seq: List[int]) -> bool:
    return all(seq[i + 1] == seq[i] + 1 for i in range(len(seq) - 1))


def _is_geometric(seq: List[int]) -> bool:
    return all(seq[i + 1] * seq[0] == seq[i] * seq[1] for i in range(1, len(seq) - 1))


def _is_rec(seq: List[int], m: int, s: int) -> bool:
    return all(
        seq[i + 1] == m * seq[i] + s * seq[i - 1] for i in range(1, len(seq) - 1)
    )


def _in_families(seq: List[int]) -> bool:
    if len(seq) < 3:
        return False
    if _is_consecutive(seq) or _is_geometric(seq):
        return True
    a0, a1, a2 = seq[0], seq[1], seq[2]
    if (a2 - a0) % a1 == 0:
        m = (a2 - a0) // a1
        if m >= 1 and _is_rec(seq, m, 1):
            k = a1 * a1 - a0 * (m * a1 + a0)
            if abs(k) <= 2:
                return True
    if (a2 + a0) % a1 == 0:
        m = (a2 + a0) // a1
        if m >= 2 and _is_rec(seq, m, -1):
            k = a1 * a1 - a0 * (m * a1 - a0)
            if abs(k) <= 2:
                return True
    return False


def _compute_finite_exception_maxes(bound: int) -> List[int]:
    starts = [(1, 2), (2, 3)]
    found: List[List[int]] = []
    for start in starts:
        stack = [list(start)]
        while stack:
            seq = stack.pop()
            if seq[-1] > bound:
                continue
            if len(seq) >= 5 and not _in_families(seq):
                found.append(seq)
            a, b = seq[-2], seq[-1]
            t = b * b
            for k in (-2, -1, 0, 1, 2):
                num = t + k
                if num % a == 0:
                    c = num // a
                    if c > b and c <= bound and -2 <= t - a * c <= 2:
                        stack.append(seq + [c])

    inf = [1, 2, 6]
    while True:
        nxt = inf[-1] * 3
        if nxt > bound:
            break
        inf.append(nxt)
    inf_prefixes = {tuple(inf[:i]) for i in range(5, len(inf) + 1)}
    maxes = [seq[-1] for seq in found if tuple(seq) not in inf_prefixes]
    maxes.sort()
    return maxes


def _infinite_exception_prefix_count(n: int) -> int:
    if n < 1:
        return 0
    length = 1
    if n >= 2:
        val = 2
        while val <= n:
            length += 1
            val *= 3
    return max(0, length - 4)


def _count_exceptions(n: int, finite_maxes: List[int]) -> int:
    return bisect_right(finite_maxes, n) + _infinite_exception_prefix_count(n)


def solve(N: int = 1_000_000_000_000_000_000) -> int:
    """Compute G(N) modulo 10^9+7 by classifying all valid pseudo-geometric sequence families."""
    phi = _phi_sieve(_iroot4(N) + 2)
    finite_maxes = _compute_finite_exception_maxes(1000)

    ans = 0
    for _iter in range(1):
        total = (
            _count_consecutive(N)
            + _count_geometric(N, phi)
            + _count_regular(N)
            + _count_exceptions(N, finite_maxes)
        )
        ans = total % _MOD
    return ans


if __name__ == "__main__":
    print(solve())
