"""Project Euler Problem 734: A Bit of Prime.

Find T(10^6, 999983) mod 1000000007, where T(n, k) is the number of k-tuples (x_1, ..., x_k)
of primes <= n whose bitwise-OR is also a prime <= n.
"""

import ctypes
import os
import subprocess

_MOD = 1_000_000_007


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p734_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p734_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000007ULL
#define SIZE (1 << 20)

static inline uint64_t pow_mod(uint64_t base, uint64_t exp, uint64_t mod) {
    uint64_t res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) res = (uint64_t)((__int128)res * base % mod);
        base = (uint64_t)((__int128)base * base % mod);
        exp >>= 1;
    }
    return res;
}

static uint32_t A[SIZE];
static uint8_t is_comp[SIZE / 8 + 1];

int64_t solve_c(int n, int k) {
    for (int i = 0; i < SIZE; ++i) A[i] = 0;
    for (int i = 0; i <= n / 8 + 1; ++i) is_comp[i] = 0;
    
    for (int p = 2; p * p <= n; ++p) {
        if (!((is_comp[p >> 3] >> (p & 7)) & 1)) {
            for (int j = p * p; j <= n; j += p) {
                is_comp[j >> 3] |= (1 << (j & 7));
            }
        }
    }
    
    for (int p = 2; p <= n; ++p) {
        if (!((is_comp[p >> 3] >> (p & 7)) & 1)) {
            A[p] = 1;
        }
    }
    
    for (int i = 0; i < 20; ++i) {
        for (int mask = 0; mask < SIZE; ++mask) {
            if (mask & (1 << i)) {
                A[mask] += A[mask ^ (1 << i)];
            }
        }
    }
    
    for (int mask = 0; mask < SIZE; ++mask) {
        A[mask] = (uint32_t)pow_mod(A[mask], k, MOD);
    }
    
    for (int i = 0; i < 20; ++i) {
        for (int mask = 0; mask < SIZE; ++mask) {
            if (mask & (1 << i)) {
                uint32_t sub = A[mask ^ (1 << i)];
                A[mask] = (A[mask] >= sub) ? (A[mask] - sub) : (A[mask] + MOD - sub);
            }
        }
    }
    
    uint64_t total = 0;
    for (int p = 2; p <= n; ++p) {
        if (!((is_comp[p >> 3] >> (p & 7)) & 1)) {
            total = (total + A[p]) % MOD;
        }
    }
    return (int64_t)total;
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
    lib.solve_c.argtypes = [ctypes.c_int, ctypes.c_int]
    return lib


def solve(n: int = 1_000_000, k: int = 999_983) -> int:
    """Compute T(n, k) modulo 1000000007 using Fast Zeta Transform (SOS DP) for bitwise-OR convolution."""
    if n <= 1000:
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(n**0.5) + 1):
            if is_prime[p]:
                for j in range(p * p, n + 1, p):
                    is_prime[j] = False

        b_len = n.bit_length()
        size = 1 << b_len
        arr = [0] * size
        for p in range(2, n + 1):
            if is_prime[p]:
                arr[p] = 1

        for i in range(b_len):
            for mask in range(size):
                if mask & (1 << i):
                    arr[mask] += arr[mask ^ (1 << i)]

        for mask in range(size):
            arr[mask] = pow(arr[mask], k, _MOD)

        for i in range(b_len):
            for mask in range(size):
                if mask & (1 << i):
                    arr[mask] = (arr[mask] - arr[mask ^ (1 << i)]) % _MOD

        total = sum(arr[p] for p in range(2, n + 1) if is_prime[p]) % _MOD
        return total

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(n, k))
    return ans


if __name__ == "__main__":
    print(solve())
