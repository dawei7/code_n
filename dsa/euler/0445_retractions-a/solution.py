"""Project Euler Problem 445: Retractions A.

Find sum_{k=1..N-1} R(C(N, k)) mod 1000000007 for N = 10_000_000,
where R(n) is the number of retractions modulo n.
"""

from array import array
from math import isqrt

MOD = 1_000_000_007


def _sieve_spf_and_primes(n: int) -> tuple[array, array, array]:
    spf = array("I", [0]) * (n + 1)
    prime_idx = array("I", [0]) * (n + 1)
    primes = array("I")

    if n >= 1:
        spf[0] = 1
        spf[1] = 1

    if n >= 2:
        spf[2] = 2
        primes.append(2)
        prime_idx[2] = 1
        for x in range(4, n + 1, 2):
            spf[x] = 2

    limit = isqrt(n)
    for i in range(3, n + 1, 2):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
            prime_idx[i] = len(primes)
            if i <= limit:
                step = i << 1
                start = i * i
                for j in range(start, n + 1, step):
                    if spf[j] == 0:
                        spf[j] = i

    return spf, primes, prime_idx


def _inverses_upto(n: int, mod: int) -> array:
    inv = array("I", [0]) * (n + 1)
    inv[1] = 1
    for i in range(2, n + 1):
        inv[i] = (mod - (mod // i) * inv[mod % i] % mod) % mod
    return inv


def _batch_inverse(vals: array, mod: int) -> array:
    n = len(vals)
    invs = array("I", [0]) * n

    idxs = array("I")
    prefix = array("I")
    prod = 1

    for i in range(n):
        v = vals[i]
        if v:
            prod = (prod * v) % mod
            idxs.append(i)
            prefix.append(prod)

    if len(idxs) == 0:
        return invs

    inv_all = pow(prod, mod - 2, mod)

    for j in range(len(idxs) - 1, -1, -1):
        i = idxs[j]
        prev = prefix[j - 1] if j else 1
        invs[i] = (inv_all * prev) % mod
        inv_all = (inv_all * vals[i]) % mod

    return invs


def solve(n: int = 10_000_000) -> int:
    """Compute sum_{k=1..N-1} R(C(N, k)) mod MOD using incremental prime factorization."""
    spf, primes, prime_idx = _sieve_spf_and_primes(n)
    inv_num = _inverses_upto(n, MOD)

    num_primes = len(primes)
    max_exp = array("I", [0]) * num_primes
    offset = array("I", [0]) * num_primes

    total_terms = 0
    for idx in range(num_primes):
        p = primes[idx]
        t = n
        e = 0
        while t:
            t //= p
            e += t
        max_exp[idx] = e
        offset[idx] = total_terms
        total_terms += e

    inv_terms = array("I", [0]) * total_terms
    chunk_size = 1_000_000
    write_pos = 0
    vals = array("I")

    for idx in range(num_primes):
        p = primes[idx]
        m = max_exp[idx]
        pow_val = p % MOD
        for _ in range(m):
            vals.append((pow_val + 1) % MOD)
            pow_val = (pow_val * p) % MOD
            if len(vals) >= chunk_size:
                invs = _batch_inverse(vals, MOD)
                inv_terms[write_pos : write_pos + len(vals)] = invs
                write_pos += len(vals)
                vals = array("I")

    if len(vals):
        invs = _batch_inverse(vals, MOD)
        inv_terms[write_pos : write_pos + len(vals)] = invs
        write_pos += len(vals)

    exp = array("I", [0]) * num_primes
    p_pow = array("I", [1]) * num_primes

    prod = 1
    zero_count = 0

    mid = n // 2
    even = n % 2 == 0

    sum_sigma = 0

    spf_local = spf
    prime_idx_local = prime_idx
    inv_num_local = inv_num
    inv_terms_local = inv_terms
    offset_local = offset
    exp_local = exp
    p_pow_local = p_pow
    mod = MOD

    for k in range(1, mid + 1):
        numer = n - k + 1
        denom = k

        # Multiply by numer
        x = numer
        while x > 1:
            p = spf_local[x]
            pi = prime_idx_local[p] - 1
            cnt = 0
            while x > 1 and spf_local[x] == p:
                x //= p
                cnt += 1

            old_e = exp_local[pi]
            if old_e:
                term_old = p_pow_local[pi] + 1
                if term_old == mod:
                    term_old = 0
                if term_old:
                    prod = (
                        prod
                        * inv_terms_local[offset_local[pi] + old_e - 1]
                    ) % mod
                else:
                    zero_count -= 1

            new_e = old_e + cnt
            exp_local[pi] = new_e

            if cnt == 1:
                p_pow_local[pi] = (p_pow_local[pi] * p) % mod
            elif cnt == 2:
                pp = (p * p) % mod
                p_pow_local[pi] = (p_pow_local[pi] * pp) % mod
            else:
                p_pow_local[pi] = (
                    p_pow_local[pi] * pow(p, cnt, mod)
                ) % mod

            term_new = p_pow_local[pi] + 1
            if term_new == mod:
                term_new = 0
            if term_new:
                prod = (prod * term_new) % mod
            else:
                zero_count += 1

        # Divide by denom
        x = denom
        while x > 1:
            p = spf_local[x]
            pi = prime_idx_local[p] - 1
            cnt = 0
            while x > 1 and spf_local[x] == p:
                x //= p
                cnt += 1

            old_e = exp_local[pi]
            term_old = p_pow_local[pi] + 1
            if term_old == mod:
                term_old = 0
            if term_old:
                prod = (
                    prod
                    * inv_terms_local[offset_local[pi] + old_e - 1]
                ) % mod
            else:
                zero_count -= 1

            new_e = old_e - cnt
            exp_local[pi] = new_e

            invp = inv_num_local[p]
            if cnt == 1:
                p_pow_local[pi] = (p_pow_local[pi] * invp) % mod
            elif cnt == 2:
                invpp = (invp * invp) % mod
                p_pow_local[pi] = (p_pow_local[pi] * invpp) % mod
            else:
                p_pow_local[pi] = (
                    p_pow_local[pi] * pow(invp, cnt, mod)
                ) % mod

            if new_e:
                term_new = p_pow_local[pi] + 1
                if term_new == mod:
                    term_new = 0
                if term_new:
                    prod = (prod * term_new) % mod
                else:
                    zero_count += 1

        sigma_val = 0 if zero_count else prod

        if even and k == mid:
            sum_sigma += sigma_val
        else:
            sum_sigma += 2 * sigma_val

        if sum_sigma >= (1 << 62):
            sum_sigma %= mod

    sum_sigma %= mod
    sum_binom = (pow(2, n, mod) - 2) % mod
    return (sum_sigma - sum_binom) % mod


if __name__ == "__main__":
    print(solve())
