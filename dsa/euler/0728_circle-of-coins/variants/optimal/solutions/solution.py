"""Project Euler Problem 728: Circle of Coins.

Find S(10^7) mod 1000000007, where S(N) = sum_{n=1}^N sum_{k=1}^n F(n, k) and F(n, k)
is the number of solvable configurations when flipping k adjacent coins on a circle of n coins.
"""

import ctypes
import os
import subprocess

_MOD = 1_000_000_007


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p728_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p728_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000007ULL

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

static uint32_t phi[10000005];
static uint8_t is_comp[10000005 / 8 + 1];
static int primes[700000];

int64_t solve_c(int N) {
    phi[1] = 1;
    int P = 0;
    for (int i = 0; i <= N / 8 + 1; ++i) is_comp[i] = 0;
    
    for (int i = 2; i <= N; ++i) {
        if (!((is_comp[i >> 3] >> (i & 7)) & 1)) {
            primes[P++] = i;
            phi[i] = i - 1;
        }
        for (int j = 0; j < P; ++j) {
            int p = primes[j];
            int64_t ip = (int64_t)i * p;
            if (ip > N) break;
            is_comp[ip >> 3] |= (1 << (ip & 7));
            if (i % p == 0) {
                phi[ip] = phi[i] * p;
                break;
            } else {
                phi[ip] = phi[i] * (p - 1);
            }
        }
    }
    
    uint64_t inv2 = (MOD + 1) / 2;
    uint64_t ans = 0;
    
    for (int m = 1; m <= N; ++m) {
        int L = N / m;
        int t = m - 1;
        
        uint64_t ph = phi[m];
        uint64_t A;
        if (m == 1 || (m & 1) == 0) {
            A = (2 * ph) % MOD;
        } else {
            A = (3 * ph) % MOD;
            A = (uint64_t)((__int128)A * inv2 % MOD);
        }
        
        uint64_t G;
        if (t == 0) {
            G = (uint64_t)(L % MOD);
        } else {
            uint64_t r = pow_mod(2, t, MOD);
            uint64_t den = (r + MOD - 1) % MOD;
            if (den == 0) {
                G = (uint64_t)(L % MOD);
            } else {
                uint64_t rL = pow_mod(2, (uint64_t)t * L, MOD);
                uint64_t num = (uint64_t)((__int128)r * (rL + MOD - 1) % MOD);
                uint64_t den_inv = pow_mod(den, MOD - 2, MOD);
                G = (uint64_t)((__int128)num * den_inv % MOD);
            }
        }
        ans = (ans + (__int128)A * G) % MOD;
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
    lib.solve_c.argtypes = [ctypes.c_int]
    return lib


def solve(n: int = 10_000_000, mod: int = _MOD) -> int:
    """Compute S(N) modulo 1000000007 using Eulerian totient transformation and geometric series sum."""
    if n <= 10:
        # Small direct evaluation
        phi = list(range(n + 1))
        for i in range(2, n + 1):
            if phi[i] == i:
                for j in range(i, n + 1, i):
                    phi[j] -= phi[j] // i

        inv2 = (mod + 1) // 2
        ans = 0
        for m in range(1, n + 1):
            l_val = n // m
            t = m - 1
            ph = phi[m]
            if m == 1 or (m & 1) == 0:
                a_val = (2 * ph) % mod
            else:
                a_val = (3 * ph * inv2) % mod

            if t == 0:
                g_val = l_val % mod
            else:
                r = pow(2, t, mod)
                den = (r - 1) % mod
                if den == 0:
                    g_val = l_val % mod
                else:
                    rl = pow(2, t * l_val, mod)
                    num = (r * (rl - 1)) % mod
                    g_val = (num * pow(den, mod - 2, mod)) % mod
            ans = (ans + a_val * g_val) % mod
        return ans

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(n))
    return ans


if __name__ == "__main__":
    print(solve())
