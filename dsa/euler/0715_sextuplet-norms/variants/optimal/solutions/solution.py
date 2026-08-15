"""Project Euler Problem 715: Sextuplet Norms.

Find G(10^12) mod 1000000007, where G(n) = sum_{k=1}^n f(k) / (k^2 * phi(k)) and
f(n) is the number of 6-tuples with sum(x_i^2) coprime to n^2.
"""

import ctypes
import math
import os
import subprocess

_MOD = 1_000_000_007


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p715_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p715_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>
#include <math.h>

#define MOD 1000000007ULL

static int64_t V[2000005];
static uint64_t Gcube[2000005];
static int64_t Gchi[2000005];
static uint64_t Gprime[2000005];
static int total_v;
static int64_t N_val;
static int64_t lim;

static int primes[100000];
static int64_t prime_squares[100000];
static uint64_t prime_cubes[100000];
static int prime_chi[100000];
static uint64_t prime_weights[100000];
static uint64_t prefix_prime_sums[100000];
static int P;
static uint8_t is_comp[1000005 / 8 + 1];

static inline int get_idx(int64_t v) {
    if (v <= lim) {
        return (int)(total_v - v);
    } else {
        return (int)(N_val / v - 1);
    }
}

static inline uint64_t sum_cubes_mod(int64_t n) {
    uint64_t a = (n % MOD) * ((n + 1) % MOD) % MOD;
    a = (a * 500000004ULL) % MOD;
    return (a * a) % MOD;
}

static inline int64_t prefix_chi(int64_t n) {
    if (n <= 0) return 0;
    int r = n & 3;
    return (r == 1 || r == 2) ? 1 : 0;
}

static inline uint64_t prime_sum_upto(int64_t x) {
    if (x < 2) return 0;
    return Gprime[get_idx(x)];
}

static inline uint64_t tail_prime_sum(int64_t x, int idx) {
    if (idx >= P) {
        if (P == 0 || x <= primes[P - 1]) return 0;
    } else if (x < primes[idx]) {
        return 0;
    }
    uint64_t sum_x = prime_sum_upto(x);
    uint64_t pref = prefix_prime_sums[idx];
    return (sum_x + MOD - pref) % MOD;
}

static uint64_t S(int64_t n, int idx) {
    if (n < 2) return 1;
    if (idx >= P) return (1 + tail_prime_sum(n, idx)) % MOD;
    int64_t p0 = primes[idx];
    if (p0 > n) return 1;
    if (prime_squares[idx] > n) return (1 + tail_prime_sum(n, idx)) % MOD;
    
    uint64_t res = (1 + tail_prime_sum(n, idx)) % MOD;
    
    for (int j = idx; j < P; ++j) {
        int64_t p = primes[j];
        int64_t pp = prime_squares[j];
        if (pp > n) break;
        
        int64_t q = n / p;
        int next_idx = j + 1;
        uint64_t gp1 = prime_weights[j];
        
        uint64_t rest;
        if (next_idx >= P || prime_squares[next_idx] > q) {
            rest = tail_prime_sum(q, next_idx);
        } else {
            rest = (S(q, next_idx) + MOD - 1) % MOD;
        }
        res = (res + gp1 * rest) % MOD;
        
        int sign = prime_chi[j];
        uint64_t p3 = prime_cubes[j];
        uint64_t prev = p3;
        uint64_t cur = (prev * p3) % MOD;
        int64_t pe_int = pp;
        
        while (pe_int <= n) {
            uint64_t gp;
            if (sign >= 0) {
                gp = (cur + MOD - (uint64_t)sign * prev) % MOD;
            } else {
                gp = (cur + prev) % MOD;
            }
            int64_t q_pe = n / pe_int;
            
            uint64_t rest_pe;
            if (next_idx >= P || prime_squares[next_idx] > q_pe) {
                rest_pe = (1 + tail_prime_sum(q_pe, next_idx)) % MOD;
            } else {
                rest_pe = S(q_pe, next_idx);
            }
            res = (res + gp * rest_pe) % MOD;
            
            if (pe_int > n / p) break;
            pe_int *= p;
            prev = cur;
            cur = (cur * p3) % MOD;
        }
    }
    
    return res % MOD;
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
    
    P = 0;
    for (int i = 0; i <= lim / 8 + 1; ++i) is_comp[i] = 0;
    for (int p = 2; p * p <= lim; ++p) {
        if (!((is_comp[p >> 3] >> (p & 7)) & 1)) {
            for (int j = p * p; j <= lim; j += p) {
                is_comp[j >> 3] |= (1 << (j & 7));
            }
        }
    }
    for (int p = 2; p <= lim; ++p) {
        if (!((is_comp[p >> 3] >> (p & 7)) & 1)) {
            primes[P] = p;
            prime_squares[P] = (int64_t)p * p;
            uint64_t p3 = (uint64_t)(p % MOD) * (p % MOD) % MOD * (p % MOD) % MOD;
            prime_cubes[P] = p3;
            int ch = (p == 2) ? 0 : ((p & 3) == 1 ? 1 : -1);
            prime_chi[P] = ch;
            if (ch >= 0) {
                prime_weights[P] = (p3 + MOD - (uint64_t)ch) % MOD;
            } else {
                prime_weights[P] = (p3 + 1) % MOD;
            }
            P++;
        }
    }
    
    for (int i = 0; i < total_v; ++i) {
        Gcube[i] = (sum_cubes_mod(V[i]) + MOD - 1) % MOD;
        Gchi[i] = prefix_chi(V[i]) - 1;
    }
    
    for (int idx = 0; idx < P; ++idx) {
        int64_t p = primes[idx];
        int64_t p2 = prime_squares[idx];
        if (p2 > N) break;
        
        int ipm1 = get_idx(p - 1);
        uint64_t gc_pm1 = Gcube[ipm1];
        int64_t gh_pm1 = Gchi[ipm1];
        
        uint64_t p3 = prime_cubes[idx];
        int chip = prime_chi[idx];
        
        for (int i = 0; i < total_v; ++i) {
            int64_t v = V[i];
            if (v < p2) break;
            
            int iu = get_idx(v / p);
            Gcube[i] = (Gcube[i] + MOD - (p3 * ((Gcube[iu] + MOD - gc_pm1) % MOD)) % MOD) % MOD;
            if (chip != 0) {
                Gchi[i] = Gchi[i] - chip * (Gchi[iu] - gh_pm1);
            }
        }
    }
    
    for (int i = 0; i < total_v; ++i) {
        int64_t chi_val = Gchi[i];
        uint64_t chi_mod = (chi_val % (int64_t)MOD + MOD) % MOD;
        Gprime[i] = (Gcube[i] + MOD - chi_mod) % MOD;
    }
    
    prefix_prime_sums[0] = 0;
    for (int i = 0; i < P; ++i) {
        prefix_prime_sums[i + 1] = prime_sum_upto(primes[i]);
    }
    
    uint64_t ans = S(N, 0);
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
    """Compute G(N) modulo 1000000007 using Min_25 prime-sum sieve and Dirichlet character convolution."""
    if n <= 10:
        # Multiplicative g(k) for small k
        g_vals = [0] * (n + 1)
        g_vals[1] = 1
        for i in range(1, n + 1):
            if g_vals[i] == 0:
                continue
            # small primes
            for p in (2, 3, 5, 7):
                if p * i <= n and math.gcd(i, p) == 1:
                    pe = p
                    e = 1
                    while pe * i <= n:
                        if p == 2:
                            g_pe = 1 << (3 * e)
                        else:
                            ch = 1 if (p % 4 == 1) else -1
                            g_pe = p ** (3 * e) - ch * p ** (3 * e - 3)
                        g_vals[pe * i] = g_vals[i] * g_pe
                        pe *= p
                        e += 1
        return sum(g_vals[1 : n + 1]) % _MOD

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(n))
    return ans


if __name__ == "__main__":
    print(solve())
