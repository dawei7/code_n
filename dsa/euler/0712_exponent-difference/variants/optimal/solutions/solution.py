"""Project Euler Problem 712: Exponent Difference.

Find S(10^12) mod 1000000007, where S(N) = sum_{1 <= n, m <= N} D(n, m) and
D(n, m) = sum_p |v_p(n) - v_p(m)|.
"""

import ctypes
import math
import os
import subprocess

_MOD = 1_000_000_007


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p712_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p712_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>
#include <math.h>

#define MOD 1000000007ULL

static int64_t V[2000005];
static int64_t S_pi[2000005];
static int total_v;
static int64_t N_val;
static int64_t lim;

static inline int get_idx(int64_t v) {
    if (v <= lim) {
        return (int)(total_v - v);
    } else {
        return (int)(N_val / v - 1);
    }
}

int64_t solve_c(int64_t N) {
    N_val = N;
    lim = (int64_t)sqrt((double)N);
    while ((lim + 1) * (lim + 1) <= N) lim++;
    while (lim * lim > N) lim--;
    
    total_v = 0;
    for (int64_t i = 1; i <= lim; ++i) {
        V[total_v++] = N / i;
    }
    for (int64_t s = V[total_v - 1] - 1; s >= 1; --s) {
        V[total_v++] = s;
    }
    
    for (int i = 0; i < total_v; ++i) {
        S_pi[i] = V[i] - 1;
    }
    
    for (int64_t p = 2; p <= lim; ++p) {
        if (S_pi[get_idx(p)] > S_pi[get_idx(p - 1)]) {
            int64_t sp = S_pi[get_idx(p - 1)];
            int64_t p2 = p * p;
            for (int i = 0; i < total_v; ++i) {
                int64_t v = V[i];
                if (v < p2) break;
                S_pi[i] -= (S_pi[get_idx(v / p)] - sp);
            }
        }
    }
    
    uint64_t ans = 0;
    
    for (int64_t p = 2; p <= lim; ++p) {
        if (S_pi[get_idx(p)] > S_pi[get_idx(p - 1)]) {
            int64_t c[70];
            int num_c = 0;
            int64_t pk = 1;
            while (pk <= N) {
                int64_t next_pk = (pk <= N / p) ? pk * p : N + 1;
                c[num_c++] = (N / pk) - (N / next_pk);
                if (next_pk > N) break;
                pk = next_pk;
            }
            
            uint64_t p_contrib = 0;
            for (int j = 0; j < num_c; ++j) {
                for (int k = j + 1; k < num_c; ++k) {
                    uint64_t term = ((uint64_t)(k - j) * (c[j] % MOD)) % MOD;
                    term = (term * (c[k] % MOD)) % MOD;
                    p_contrib = (p_contrib + term) % MOD;
                }
            }
            ans = (ans + 2 * p_contrib) % MOD;
        }
    }
    
    for (int64_t v = 1; v <= lim; ++v) {
        int64_t upper_p = N / v;
        int64_t lower_p = N / (v + 1);
        if (lower_p < lim) lower_p = lim;
        if (upper_p <= lim) continue;
        
        int64_t count_primes = S_pi[get_idx(upper_p)] - S_pi[get_idx(lower_p)];
        if (count_primes > 0) {
            uint64_t c0 = (N - v) % MOD;
            uint64_t c1 = v % MOD;
            uint64_t pair_term = (2 * c0 * c1) % MOD;
            uint64_t block = (pair_term * (count_primes % MOD)) % MOD;
            ans = (ans + block) % MOD;
        }
    }
    
    return (int64_t)ans;
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
    lib.solve_c.argtypes = [ctypes.c_int64]
    return lib


def solve(n: int = 1_000_000_000_000) -> int:
    """Compute S(N) modulo 1000000007 using Lucy's prime counting algorithm and hyperbolic block grouping."""
    if n <= 100:
        primes = [
            2,
            3,
            5,
            7,
            11,
            13,
            17,
            19,
            23,
            29,
            31,
            37,
            41,
            43,
            47,
            53,
            59,
            61,
            67,
            71,
            73,
            79,
            83,
            89,
            97,
        ]
        primes = [p for p in primes if p <= n]
        total = 0
        for p in primes:
            c = []
            k = 0
            while (p**k) <= n:
                cnt = (n // (p**k)) - (n // (p ** (k + 1)))
                c.append(cnt)
                k += 1
            p_contrib = 0
            for j in range(len(c)):
                for k in range(j + 1, len(c)):
                    p_contrib += (k - j) * c[j] * c[k]
            total += 2 * p_contrib
        return total % _MOD

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(n))
    return ans


if __name__ == "__main__":
    print(solve())
