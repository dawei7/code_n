"""Project Euler 343: Fractional Sequences

Find sum_{k=1}^{2*10^6} f(k^3), where f(k) is the stopping value of the fractional sequence a_1 = 1/k.
"""

from __future__ import annotations


def solve(limit_k: int = 2_000_000) -> str:
    """Calculates sum_{k=1}^{limit_k} f(k^3) in pure Python in O(N log log N) time

    using the invariant f(k) = LPF(k + 1) - 1, algebraic factorization
    k^3 + 1 = (k + 1)(k^2 - k + 1), and polynomial sieve of k^2 - k + 1 with Tonelli-Shanks.
    """
    # 1. Sieve LPF of (k + 1) for k <= limit_k
    lpf_k = [0] * (limit_k + 2)
    for p in range(2, limit_k + 2):
        if lpf_k[p] == 0:
            for mult in range(p, limit_k + 2, p):
                lpf_k[mult] = p

    # 2. Sieve polynomial P(k) = k^2 - k + 1 for k in 1..limit_k
    v_arr = [k * k - k + 1 for k in range(limit_k + 1)]
    max_prime_poly = [1] * (limit_k + 1)

    # Prime p = 3: k^2 - k + 1 = 0 mod 3 => k = 2 mod 3
    for k in range(2, limit_k + 1, 3):
        max_prime_poly[k] = 3
        while v_arr[k] % 3 == 0:
            v_arr[k] //= 3

    # Primes p = 6m + 1 <= limit_k
    for p in range(7, limit_k + 1, 6):
        if lpf_k[p] == p:  # p is prime
            # Find square root of -3 mod p
            if p % 4 == 3:
                r = pow(-3 % p, (p + 1) // 4, p)
            else:
                # Tonelli-Shanks algorithm for p = 1 mod 4
                z = 2
                while pow(z, (p - 1) // 2, p) != p - 1:
                    z += 1
                q = p - 1
                s = 0
                while (q & 1) == 0:
                    s += 1
                    q >>= 1
                r = pow(-3 % p, (q + 1) // 2, p)
                t = pow(-3 % p, q, p)
                c = pow(z, q, p)
                while t != 1:
                    i = 1
                    cur = (t * t) % p
                    while cur != 1:
                        cur = (cur * cur) % p
                        i += 1
                    b = pow(c, 1 << (s - i - 1), p)
                    r = (r * b) % p
                    c = (b * b) % p
                    t = (t * c) % p
                    s = i

            inv2 = (p + 1) // 2
            k1 = ((r + 1) * inv2) % p
            k2 = ((-r + 1) * inv2) % p

            for k_root in (k1, k2):
                start = k_root if k_root > 0 else k_root + p
                for k in range(start, limit_k + 1, p):
                    if p > max_prime_poly[k]:
                        max_prime_poly[k] = p
                    while v_arr[k] % p == 0:
                        v_arr[k] //= p

    # 3. Sum total f(k^3) = max(LPF(k + 1), LPF(k^2 - k + 1)) - 1
    total_sum = 0
    for k in range(1, limit_k + 1):
        lpf1 = lpf_k[k + 1]
        lpf2 = max_prime_poly[k]
        if v_arr[k] > 1:
            lpf2 = max(lpf2, v_arr[k])
        total_sum += max(lpf1, lpf2) - 1

    return str(total_sum)


if __name__ == "__main__":
    print(solve())
