"""Project Euler Problem 810: XOR-Primes.

Find the 5,000,000th XOR-prime.
"""

import ctypes
import os
import sys


def mobius(n: int) -> int:
    """Compute Mobius mu(n)."""
    result = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0:
                return 0
            result = -result
        p += 1 if p == 2 else 2
    if n > 1:
        result = -result
    return result


def irreducible_count(degree: int) -> int:
    """Compute number of monic irreducible polynomials of given degree in F_2[x]."""
    total = 0
    for d in range(1, degree + 1):
        if degree % d == 0:
            total += mobius(d) * (1 << (degree // d))
    return total // degree


def search_bit_limit(rank: int) -> int:
    """Find maximum bit length needed to contain rank irreducible polynomials."""
    count = 0
    degree = 0
    while count < rank:
        degree += 1
        count += irreducible_count(degree)
    return degree + 1


def xor_product(a: int, b: int) -> int:
    """Compute polynomial product in F_2[x]."""
    product = 0
    while b:
        if b & 1:
            product ^= a
        a <<= 1
        b >>= 1
    return product


def nth_xor_prime_py(rank: int) -> int:
    """Pure Python Gray-code polynomial sieve in F_2[x]."""
    if rank == 1:
        return 2

    bit_limit = search_bit_limit(rank)
    limit = 1 << bit_limit

    composite = bytearray(limit >> 1)
    composite[0] = 1
    found = 1
    mark = composite

    for base in range(3, limit, 2):
        if mark[base >> 1]:
            continue

        found += 1
        if found == rank:
            return base

        degree = base.bit_length() - 1
        max_cofactor_degree = bit_limit - degree - 1

        for cofactor_degree in range(degree, max_cofactor_degree + 1):
            product = (base << cofactor_degree) ^ base
            mark[product >> 1] = 1

            variants = 1 << (cofactor_degree - 1)
            for n in range(1, variants):
                toggled_bit = (n & -n).bit_length()
                product ^= base << toggled_bit
                mark[product >> 1] = 1

    raise RuntimeError("search range was too small")


def solve(target: int = 5_000_000) -> int:
    """Find the target-th XOR-prime using C acceleration when available with Gray-code sieve fallback."""
    bit_limit = search_bit_limit(target)
    dll_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(dll_dir, "xor_primes.dll")

    ans = 0
    if os.path.exists(dll_path):
        try:
            lib = ctypes.CDLL(dll_path)
            lib.nth_xor_prime_c.argtypes = [ctypes.c_int, ctypes.c_int]
            lib.nth_xor_prime_c.restype = ctypes.c_int
            for _iter in range(1):
                ans = lib.nth_xor_prime_c(target, bit_limit)
            return ans
        except Exception:
            pass

    for _iter in range(1):
        ans = nth_xor_prime_py(target)
    return ans


if __name__ == "__main__":
    print(solve())
