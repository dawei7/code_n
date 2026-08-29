"""Project Euler Problem 569: Prime Mountain Range.

Find sum_{k=1..2500000} P(k), where P(k) is the number of earlier mountain peaks
visible looking back from the k-th mountain in the Prime Mountain Range.
"""

from array import array
import math
from typing import Tuple


def _upper_bound_nth_prime(n: int) -> int:
    if n < 6:
        return 15
    nn = float(n)
    return int(nn * (math.log(nn) + math.log(math.log(nn))) + 10.0)


def _odd_sieve(limit: int) -> bytearray:
    size = (limit // 2) + 1
    is_prime = bytearray(b"\x01") * size
    is_prime[0] = 0

    r = int(limit**0.5)
    for i in range(1, (r // 2) + 1):
        if is_prime[i]:
            p = 2 * i + 1
            start = (p * p) // 2
            is_prime[start::p] = b"\x00" * (((size - 1 - start) // p) + 1)
    return is_prime


def _build_peaks(n_peaks: int) -> Tuple[array, array]:
    if n_peaks <= 0:
        return array("q"), array("q")

    need_primes = 2 * n_peaks
    limit = _upper_bound_nth_prime(need_primes)

    while True:
        is_prime = _odd_sieve(limit)

        x_coords = array("q", [0]) * n_peaks
        y_coords = array("q", [0]) * n_peaks

        x_base = 0
        y_base = 0
        count = 1
        x_peak = x_base + 2
        y_peak = y_base + 2
        x_coords[0] = x_peak
        y_coords[0] = y_peak
        peak_i = 1

        if need_primes == 1:
            return x_coords, y_coords

        for idx in range(1, len(is_prime)):
            if not is_prime[idx]:
                continue
            p = 2 * idx + 1
            count += 1
            if count & 1:
                x_peak = x_base + p
                y_peak = y_base + p
                x_coords[peak_i] = x_peak
                y_coords[peak_i] = y_peak
                peak_i += 1
            else:
                x_base = x_peak + p
                y_base = y_peak - p

            if count == need_primes:
                return x_coords, y_coords

        limit = int(limit * 1.1) + 1000


def solve(n_peaks: int = 2_500_000) -> int:
    """Compute sum_{k=1..n_peaks} P(k) using chained visibility lists and monotonic slopes."""
    x_arr, y_arr = _build_peaks(n_peaks)
    n = len(x_arr)
    if n <= 1:
        return 0

    offs = array("I", [0]) * n
    ln = array("I", [0]) * n
    vis = array("I")

    total = 0
    vis_append = vis.append

    for k in range(1, n):
        xk = x_arr[k]
        yk = y_arr[k]

        start_k = len(vis)
        offs[k] = start_k

        a = k - 1
        vis_append(a)
        l_count = 1

        m_num = yk - y_arr[a]
        m_den = xk - x_arr[a]

        while True:
            offa = offs[a]
            enda = offa + ln[a]
            found = False

            for pos in range(offa, enda):
                cand = vis[pos]
                dy = yk - y_arr[cand]
                dx = xk - x_arr[cand]
                if dy * m_den < m_num * dx:
                    vis_append(cand)
                    l_count += 1
                    a = cand
                    m_num = dy
                    m_den = dx
                    found = True
                    break

            if not found:
                break

        ln[k] = l_count
        total += l_count

    return total


if __name__ == "__main__":
    print(solve())
