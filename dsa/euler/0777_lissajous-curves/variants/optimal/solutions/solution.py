"""Project Euler Problem 777: Lissajous Curves.

Find s(10^6) formatted in scientific notation rounded to 10 significant digits,
where s(m) = sum d(a, b) over coprime integers 2 <= a, b <= m and d(a, b) = sum (x^2 + y^2)
over self-intersection points of the Lissajous curve C_{a,b}.
"""

from typing import List, Tuple


def _sum_first(n: int) -> int:
    return n * (n + 1) // 2


def _mobius_sieve(n: int) -> List[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: List[int] = []
    is_comp = bytearray(n + 1)

    for i in range(2, n + 1):
        if not is_comp[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            ip = i * p
            if ip > n:
                break
            is_comp[ip] = 1
            if i % p == 0:
                mu[ip] = 0
                break
            mu[ip] = -mu[i]
    return mu


def _special_inner(n: int, need2: bool, need5: bool) -> Tuple[int, int, int]:
    total_cnt = n * n
    S = _sum_first(n)
    total_sumX = S * n
    total_sumXY = S * S

    if not need2 and not need5:
        return total_cnt, total_sumX, total_sumXY

    ce = n // 2
    se = 2 * _sum_first(ce)
    co = n - ce
    so = S - se

    c5 = n // 5
    s5 = 5 * _sum_first(c5)
    cnot5 = n - c5
    snot5 = S - s5

    c10 = n // 10
    s10 = 10 * _sum_first(c10)

    codnot5 = n - ce - c5 + c10
    sodnot5 = S - se - s5 + s10

    if need2 and not need5:
        cnt = total_cnt - co * co
        sumX = total_sumX - so * co
        sumXY = total_sumXY - so * so
        return cnt, sumX, sumXY

    if need5 and not need2:
        cnt = total_cnt - cnot5 * cnot5
        sumX = total_sumX - snot5 * cnot5
        sumXY = total_sumXY - snot5 * snot5
        return cnt, sumX, sumXY

    cnt = total_cnt - co * co - cnot5 * cnot5 + codnot5 * codnot5
    sumX = total_sumX - so * co - snot5 * cnot5 + sodnot5 * codnot5
    sumXY = total_sumXY - so * so - snot5 * snot5 + sodnot5 * sodnot5
    return cnt, sumX, sumXY


def _s_num4(m: int) -> int:
    mu = _mobius_sieve(m)

    A1 = 0
    B1 = 0
    Csp1 = 0
    Bsp1 = 0
    Asp1 = 0

    for d in range(1, m + 1):
        md = mu[d]
        if md == 0:
            continue
        n = m // d
        S = _sum_first(n)

        SS = S * S
        dd = d * d

        A1 += md * dd * SS
        B1 += md * d * S * n

        need2 = (d & 1) == 1
        need5 = (d % 5) != 0
        cnt, sumX, sumXY = _special_inner(n, need2, need5)

        Csp1 += md * cnt
        Bsp1 += md * d * sumX
        Asp1 += md * dd * sumXY

    sum1 = _sum_first(m)
    A = A1 - 2 * sum1 + 1
    B = B1 - m - sum1 + 1

    c10 = m // 10
    sum10 = 10 * _sum_first(c10)

    Csp = Csp1 - 2 * c10
    Bsp = Bsp1 - c10 * 1 - sum10
    Asp = Asp1 - sum10 - sum10

    num4 = (8 * A - 12 * B) + (-6 * Asp + 6 * Bsp + 4 * Csp)
    return num4


def _format_scientific(num: int, den: int = 1, sig: int = 10) -> str:
    if num == 0:
        return "0." + "0" * (sig - 1) + "e0"

    ip = num // den
    if ip > 0:
        e = len(str(ip)) - 1
    else:
        k = 0
        t = num
        while t < den:
            t *= 10
            k += 1
        e = -k

    power = (sig - 1) - e
    if power >= 0:
        scaled_num = num * (10**power)
        scaled_den = den
    else:
        scaled_num = num
        scaled_den = den * (10 ** (-power))

    mant_scaled = (2 * scaled_num + scaled_den) // (2 * scaled_den)
    limit = 10**sig
    if mant_scaled >= limit:
        mant_scaled //= 10
        e += 1

    s = str(mant_scaled).zfill(sig)
    return f"{s[0]}.{s[1:]}e{e}"


def solve(m: int = 1_000_000, sig: int = 10) -> str:
    """Compute s(m) using Mobius inversion and format in scientific notation."""
    ans = ""
    for _iter in range(1):
        num4 = _s_num4(m)
        ans = _format_scientific(num4, 4, sig=sig)
    return ans


if __name__ == "__main__":
    print(solve())
