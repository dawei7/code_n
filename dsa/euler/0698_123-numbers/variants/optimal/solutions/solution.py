"""Project Euler Problem 698: 123 Numbers.

Find F(111111111111222333) mod 123123123, where F(n) is the n-th 123-number
(numbers composed of digits 1, 2, 3 whose non-zero digit frequencies are themselves 123-numbers).
"""

from functools import lru_cache
from typing import List, Tuple

_MOD = 123_123_123


@lru_cache(None)
def _is_123_number(x: int) -> bool:
    if x == 1:
        return True
    if x <= 0:
        return False
    s = str(x)
    for ch in s:
        if ch not in "123":
            return False
    c1 = s.count("1")
    c2 = s.count("2")
    c3 = s.count("3")
    if c1 and not _is_123_number(c1):
        return False
    if c2 and not _is_123_number(c2):
        return False
    if c3 and not _is_123_number(c3):
        return False
    return True


def _factorials_up_to(n: int) -> List[int]:
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i
    return fact


def _valid_total_triples(
    length: int, allowed: List[int]
) -> List[Tuple[int, int, int]]:
    poss = [0] + allowed
    poss_set = set(poss)
    triples: List[Tuple[int, int, int]] = []
    for a in poss:
        for b in poss:
            s = a + b
            if s > length:
                continue
            c = length - s
            if c in poss_set:
                if a == 0 and b == 0 and c == 0:
                    continue
                triples.append((a, b, c))
    return triples


def _count_completions(
    length: int,
    fact: List[int],
    triples: List[Tuple[int, int, int]],
    used1: int,
    used2: int,
    used3: int,
) -> int:
    used = used1 + used2 + used3
    rem = length - used
    total = 0
    for a, b, c in triples:
        if used1 <= a and used2 <= b and used3 <= c:
            ra = a - used1
            rb = b - used2
            rc = c - used3
            if ra + rb + rc == rem:
                total += fact[rem] // (fact[ra] * fact[rb] * fact[rc])
    return total


def solve(n: int = 111_111_111_111_222_333, mod: int = _MOD) -> int:
    """Find F(n) modulo mod using length search and digit unranking."""
    fact = [1]
    allowed: List[int] = []
    cumulative = 0
    target_length = 0
    rank_in_len = 0

    for length in range(1, 1000):
        fact.append(fact[-1] * length)
        if _is_123_number(length):
            allowed.append(length)

        triples = _valid_total_triples(length, allowed)
        cnt_l = sum(
            fact[length] // (fact[a] * fact[b] * fact[c]) for a, b, c in triples
        )

        if cumulative + cnt_l >= n:
            target_length = length
            rank_in_len = n - cumulative
            break
        cumulative += cnt_l

    fact = _factorials_up_to(target_length)
    allowed = [i for i in range(1, target_length + 1) if _is_123_number(i)]
    triples = _valid_total_triples(target_length, allowed)

    used1 = used2 = used3 = 0
    k = rank_in_len
    ans_val = 0

    for _ in range(target_length):
        for digit in (1, 2, 3):
            n1 = used1 + (1 if digit == 1 else 0)
            n2 = used2 + (1 if digit == 2 else 0)
            n3 = used3 + (1 if digit == 3 else 0)

            cnt = _count_completions(target_length, fact, triples, n1, n2, n3)
            if k > cnt:
                k -= cnt
            else:
                ans_val = (ans_val * 10 + digit) % mod
                used1, used2, used3 = n1, n2, n3
                break

    return ans_val


if __name__ == "__main__":
    print(solve())
