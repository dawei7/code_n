"""Project Euler Problem 625: Gcd Sum.

Find G(10^11) mod 998244353, where G(N) = sum_{j=1}^N sum_{i=1}^j gcd(i, j).
"""

from typing import Dict, List

_MOD = 998244353
_INV2 = (_MOD + 1) // 2


def _sieve_phi_pref(b_limit: int) -> List[int]:
    phi = list(range(b_limit + 1))
    primes: List[int] = []
    is_prime = bytearray(b"\x01") * (b_limit + 1)
    is_prime[0:2] = b"\x00\x00"

    for i in range(2, b_limit + 1):
        if is_prime[i]:
            primes.append(i)
            phi[i] = i - 1
        for p in primes:
            ip = i * p
            if ip > b_limit:
                break
            is_prime[ip] = 0
            if i % p == 0:
                phi[ip] = phi[i] * p
                break
            phi[ip] = phi[i] * (p - 1)

    pref_phi = [0] * (b_limit + 1)
    s = 0
    for i in range(1, b_limit + 1):
        s = (s + phi[i]) % _MOD
        pref_phi[i] = s
    return pref_phi


def solve(n: int = 100_000_000_000) -> int:
    """Compute G(N) mod 998244353 using the sublinear Du Sieve on Euler's totient function."""
    b_limit = min(int(n ** (2 / 3)) + 100, 20_000_000)
    pref_phi = _sieve_phi_pref(b_limit)
    memo_phi: Dict[int, int] = {}

    def phi_summatory(x: int) -> int:
        if x <= b_limit:
            return pref_phi[x]
        if x in memo_phi:
            return memo_phi[x]

        total = (x % _MOD) * ((x + 1) % _MOD) % _MOD * _INV2 % _MOD
        l = 2
        while l <= x:
            q = x // l
            r = x // q
            cnt = (r - l + 1) % _MOD
            total = (total - cnt * phi_summatory(q)) % _MOD
            l = r + 1

        memo_phi[x] = total
        return total

    ans = 0
    l = 1
    while l <= n:
        q = n // l
        r = n // q
        phi_interval = (phi_summatory(r) - phi_summatory(l - 1)) % _MOD
        t_q = (q % _MOD) * ((q + 1) % _MOD) % _MOD * _INV2 % _MOD
        ans = (ans + phi_interval * t_q) % _MOD
        l = r + 1

    return ans


if __name__ == "__main__":
    print(solve())
