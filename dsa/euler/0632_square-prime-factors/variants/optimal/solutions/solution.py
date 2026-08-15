"""Project Euler Problem 632: Square Prime Factors.

Find the product of all non-zero C_k(10^16) mod 1000000007, where C_k(N) is the number
of integers 1 <= n <= N with exactly k square prime factors.
"""

import ctypes
import os
import subprocess

_MOD = 1_000_000_007


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_sq_core.dll")
    c_path = os.path.join(tmp_dir, "fast_sq_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>
#include <math.h>

#define MOD 1000000007LL

int64_t solve_c(int64_t N) {
    int64_t lim = (int64_t)sqrt((double)N);
    int8_t* omega = (int8_t*)calloc(lim + 1, sizeof(int8_t));
    uint8_t* is_prime = (uint8_t*)malloc(lim + 1);
    for (int64_t i = 0; i <= lim; ++i) is_prime[i] = 1;
    is_prime[0] = is_prime[1] = 0;
    
    int* primes = (int*)malloc((lim / 10) * sizeof(int));
    int num_primes = 0;
    
    for (int64_t i = 2; i <= lim; ++i) {
        if (is_prime[i]) {
            primes[num_primes++] = i;
            omega[i] = 1;
        }
        for (int p_idx = 0; p_idx < num_primes; ++p_idx) {
            int p = primes[p_idx];
            int64_t ip = i * p;
            if (ip > lim) break;
            is_prime[ip] = 0;
            if (i % p == 0) {
                omega[ip] = -1;
                break;
            } else {
                if (omega[i] == -1) {
                    omega[ip] = -1;
                } else {
                    omega[ip] = omega[i] + 1;
                }
            }
        }
    }
    
    int64_t S[15] = {0};
    for (int64_t m = 1; m <= lim; ++m) {
        int r = (m == 1) ? 0 : omega[m];
        if (r >= 0) {
            S[r] += N / (m * m);
        }
    }
    
    int64_t binom[15][15] = {0};
    for (int i = 0; i < 15; ++i) {
        binom[i][0] = 1;
        for (int j = 1; j <= i; ++j) {
            binom[i][j] = binom[i-1][j-1] + binom[i-1][j];
        }
    }
    
    int64_t C[15] = {0};
    for (int k = 0; k < 15; ++k) {
        int64_t val = 0;
        for (int r = k; r < 15; ++r) {
            int64_t term = binom[r][k] * S[r];
            if ((r - k) % 2 == 1) {
                val -= term;
            } else {
                val += term;
            }
        }
        C[k] = val;
    }
    
    int64_t prod = 1;
    for (int k = 0; k < 15; ++k) {
        if (C[k] > 0) {
            prod = (prod * (C[k] % MOD)) % MOD;
        }
    }
    
    free(omega);
    free(is_prime);
    free(primes);
    return prod;
}
"""
        with open(c_path, "w", encoding="utf-8") as f:
            f.write(c_code)

        subprocess.run(
            ["gcc", "-O3", "-shared", "-o", dll_path, c_path], check=True
        )

    lib = ctypes.CDLL(dll_path)
    lib.solve_c.restype = ctypes.c_int64
    lib.solve_c.argtypes = [ctypes.c_int64]
    return lib


def solve(n: int = 10**16) -> int:
    """Compute the modular product of non-zero C_k(N) using squarefree binomial inclusion-exclusion."""
    if n <= 10000:
        lim = int(n**0.5)
        omega = [0] * (lim + 1)
        primes = []
        is_p = [True] * (lim + 1)
        is_p[0] = is_p[1] = False
        for i in range(2, lim + 1):
            if is_p[i]:
                primes.append(i)
                omega[i] = 1
            for p in primes:
                if i * p > lim:
                    break
                is_p[i * p] = False
                if i % p == 0:
                    omega[i * p] = -1
                    break
                else:
                    omega[i * p] = -1 if omega[i] == -1 else omega[i] + 1

        s_arr = [0] * 15
        for m in range(1, lim + 1):
            r = 0 if m == 1 else omega[m]
            if r >= 0:
                s_arr[r] += n // (m * m)

        import math

        c_arr = [0] * 15
        for k in range(15):
            val = 0
            for r in range(k, 15):
                term = math.comb(r, k) * s_arr[r]
                val = val - term if (r - k) % 2 == 1 else val + term
            c_arr[k] = val

        prod = 1
        for k in range(15):
            if c_arr[k] > 0:
                prod = (prod * (c_arr[k] % _MOD)) % _MOD
        return prod

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(n))
    return ans


if __name__ == "__main__":
    print(solve())
