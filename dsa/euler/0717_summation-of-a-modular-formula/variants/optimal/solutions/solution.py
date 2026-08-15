"""Project Euler Problem 717: Summation of a Modular Formula.

Find G(10^7), where G(N) = sum_{3 <= p < N, p prime} g(p), g(p) = f(p) mod p, and
f(p) = floor(2^(2^p) / p) mod 2^p.
"""

import ctypes
import os
import subprocess


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p717_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p717_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>

static inline uint64_t pow_mod(uint64_t base, uint64_t exp, uint64_t mod) {
    uint64_t res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) {
            __int128 prod = (__int128)res * base;
            res = (uint64_t)(prod % mod);
        }
        __int128 prod = (__int128)base * base;
        base = (uint64_t)(prod % mod);
        exp >>= 1;
    }
    return res;
}

static uint8_t is_comp[10000005 / 8 + 1];

int64_t solve_c(int limit) {
    for (int i = 0; i <= limit / 8 + 1; ++i) is_comp[i] = 0;
    for (int p = 2; p * p < limit; ++p) {
        if (!((is_comp[p >> 3] >> (p & 7)) & 1)) {
            for (int j = p * p; j < limit; j += p) {
                is_comp[j >> 3] |= (1 << (j & 7));
            }
        }
    }
    
    int64_t total = 0;
    for (int p = 3; p < limit; ++p) {
        if (!((is_comp[p >> 3] >> (p & 7)) & 1)) {
            uint64_t E = pow_mod(2, p, p - 1);
            uint64_t r = pow_mod(2, E, p);
            uint64_t k = (r & 1) ? (r + p) / 2 : r / 2;
            
            uint64_t p2 = (uint64_t)p * p;
            uint64_t pow2_p1 = pow_mod(2, p - 1, p2);
            uint64_t q = (pow2_p1 - 1) / p;
            uint64_t m = (2 * q) % p;
            
            uint64_t odd_flag = r & 1;
            uint64_t gp = (odd_flag + k * m) % p;
            total += gp;
        }
    }
    return total;
}
"""
        with open(c_path, "w", encoding="utf-8") as f:
            f.write(c_code)

        subprocess.run(
            [
                "gcc",
                "-O3",
                "-shared",
                "-static",
                "-static-libgcc",
                "-o",
                dll_path,
                c_path,
            ],
            check=True,
        )

    lib = ctypes.CDLL(dll_path)
    lib.solve_c.restype = ctypes.c_int64
    lib.solve_c.argtypes = [ctypes.c_int]
    return lib


def solve(limit: int = 10_000_000) -> int:
    """Compute G(limit) using Fermat quotient decomposition and fast modular arithmetic."""
    if limit <= 10000:
        is_prime = [True] * limit
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(limit**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, limit, i):
                    is_prime[j] = False

        total = 0
        for p in range(3, limit):
            if is_prime[p]:
                e_exp = pow(2, p, p - 1)
                r = pow(2, e_exp, p)
                k = (r + p) // 2 if (r % 2 == 1) else (r // 2)
                q = (pow(2, p - 1, p * p) - 1) // p
                m = (2 * q) % p
                odd_flag = 1 if (r % 2 == 1) else 0
                gp = (odd_flag + k * m) % p
                total += gp
        return total

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(limit))
    return ans


if __name__ == "__main__":
    print(solve())
