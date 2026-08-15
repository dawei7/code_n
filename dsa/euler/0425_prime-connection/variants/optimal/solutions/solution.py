"""Project Euler Problem 425: Prime Connection.

Find F(10^7), the sum of primes <= 10^7 which are not 2's relatives.
A prime P is a 2's relative if there is a chain of connected primes from 2 to P with max prime <= P.
"""

from heapq import heappop, heappush
from typing import Dict, List, Set


def _build_odd_prime_sieve(limit: int) -> bytearray:
    half = limit >> 1
    sieve = bytearray(b"\x01") * half
    if half > 0:
        sieve[0] = 0

    i = 1
    while 2 * i * i < half:
        if sieve[i]:
            current = 3 * i + 1
            step = 2 * i + 1
            while current < half:
                sieve[current] = 0
                current += step
        i += 1
    return sieve


def solve(limit: int = 10_000_000) -> int:
    """Compute F(limit) using Dijkstra minimax path search over connected prime graph."""
    sieve = _build_odd_prime_sieve(limit)

    def is_prime(x: int) -> bool:
        if (x & 1) == 0:
            return x == 2
        return bool(sieve[x >> 1])

    connected: Dict[int, Set[int]] = {}

    for i in range(2, limit):
        if not is_prime(i):
            continue

        max_pos = 7
        split = [0] * max_pos
        shift = 1
        reduced = i
        for pos in range(max_pos):
            shift *= 10
            split[pos] = reduced % shift
            reduced -= reduced % shift

        shift = 1
        pos = 0
        while shift < 10 * i and shift < limit:
            current = i
            digit = split[pos] + shift
            while digit <= 9 * shift:
                current += shift
                if is_prime(current):
                    connected.setdefault(i, set()).add(current)
                    connected.setdefault(current, set()).add(i)
                digit += shift
            pos += 1
            shift *= 10

    best: Dict[int, int] = {}
    todo: List[int] = [2]

    while todo:
        current = heappop(todo)
        top = best.get(current, 0)
        if top < current:
            top = current

        if current not in connected:
            continue

        for edge in connected[current]:
            high = best.get(edge, 0)
            if high == 0 or top < high:
                best[edge] = top
                heappush(todo, edge)

    result = 0
    for i in range(3, limit, 2):
        if is_prime(i) and (best.get(i, 0) == 0 or best[i] > i):
            result += i

    return result


if __name__ == "__main__":
    print(solve())
