"""Project Euler Problem 639: Summing a Multiplicative Function.

Find sum_{k=1}^50 S_k(10^12) mod 1000000007, where S_k(n) = sum_{i=1}^n f_k(i)
and f_k(n) = rad(n)^k.
"""

import ctypes
import os
import subprocess

_MOD = 1_000_000_007


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_radsum_core.dll")
    c_path = os.path.join(tmp_dir, "fast_radsum_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>
#include <math.h>

#define MOD 1000000007LL
#define KMAX 50
#define MAX_PRE 1000000

static int32_t* ps[KMAX + 1];
static int64_t S2[KMAX + 1][KMAX + 1];
static int64_t coeff[KMAX + 1][KMAX + 1];

static int* primes;
static int64_t* p2;
static int num_primes;
static int tables_initialized = 0;

void init_tables() {
    if (tables_initialized) return;
    tables_initialized = 1;
    
    S2[0][0] = 1;
    for (int n = 1; n <= KMAX; ++n) {
        for (int k = 1; k <= n; ++k) {
            S2[n][k] = (S2[n - 1][k - 1] + (int64_t)k * S2[n - 1][k]) % MOD;
        }
    }
    
    int64_t inv[KMAX + 2];
    inv[1] = 1;
    for (int i = 2; i <= KMAX + 1; ++i) {
        inv[i] = (MOD - (MOD / i)) * inv[MOD % i] % MOD;
    }
    for (int n = 1; n <= KMAX; ++n) {
        for (int j = 1; j <= n; ++j) {
            coeff[n][j] = (S2[n][j] * inv[j + 1]) % MOD;
        }
    }
    
    for (int k = 1; k <= KMAX; ++k) {
        ps[k] = (int32_t*)malloc((MAX_PRE + 1) * sizeof(int32_t));
        ps[k][0] = 0;
    }
    
    for (int t = 1; t <= MAX_PRE; ++t) {
        int64_t p = t;
        for (int k = 1; k <= KMAX; ++k) {
            ps[k][t] = (int32_t)((ps[k][t - 1] + p) % MOD);
            p = (p * t) % MOD;
        }
    }
    
    uint8_t* is_p = (uint8_t*)malloc(MAX_PRE + 1);
    for (int i = 0; i <= MAX_PRE; ++i) is_p[i] = 1;
    is_p[0] = is_p[1] = 0;
    for (int i = 2; i * i <= MAX_PRE; ++i) {
        if (is_p[i]) {
            for (int j = i * i; j <= MAX_PRE; j += i) is_p[j] = 0;
        }
    }
    primes = (int*)malloc((MAX_PRE / 10) * sizeof(int));
    p2 = (int64_t*)malloc((MAX_PRE / 10) * sizeof(int64_t));
    num_primes = 0;
    for (int i = 2; i <= MAX_PRE; ++i) {
        if (is_p[i]) {
            primes[num_primes] = i;
            p2[num_primes] = (int64_t)i * i;
            num_primes++;
        }
    }
    free(is_p);
}

int64_t power_sum_large_c(int64_t t, int k) {
    int64_t n = t % MOD;
    int64_t prod = (n + 1) % MOD;
    int64_t res = 0;
    for (int j = 1; j <= k; ++j) {
        prod = (prod * ((n + 1 - j) % MOD)) % MOD;
        res = (res + coeff[k][j] * prod) % MOD;
    }
    return res;
}

static int64_t* current_c;
static int current_k;
static int64_t ans_k;
static int64_t N_VAL;
static int current_m;

void dfs_rec(int start_idx, int64_t v, int64_t w) {
    int64_t t = N_VAL / v;
    int64_t term_val = (t <= MAX_PRE) ? ps[current_k][t] : power_sum_large_c(t, current_k);
    ans_k = (ans_k + term_val * w) % MOD;
    
    for (int i = start_idx; i < current_m; ++i) {
        int64_t p2_val = p2[i];
        if (v > N_VAL / p2_val) break;
        int64_t vv = v * p2_val;
        int64_t ww = (w * current_c[i]) % MOD;
        int p = primes[i];
        while (1) {
            dfs_rec(i + 1, vv, ww);
            if (vv > N_VAL / p) break;
            vv *= p;
        }
    }
}

int64_t solve_c(int64_t n_target, int max_k) {
    init_tables();
    N_VAL = n_target;
    int64_t lim = (int64_t)sqrt((double)n_target);
    current_m = 0;
    while (current_m < num_primes && primes[current_m] <= lim) {
        current_m++;
    }
    
    int64_t total = 0;
    int64_t* pk = (int64_t*)malloc(current_m * sizeof(int64_t));
    current_c = (int64_t*)malloc(current_m * sizeof(int64_t));
    for (int i = 0; i < current_m; ++i) pk[i] = 1;
    
    for (int k = 1; k <= max_k; ++k) {
        current_k = k;
        for (int i = 0; i < current_m; ++i) {
            int64_t pkv = (pk[i] * primes[i]) % MOD;
            pk[i] = pkv;
            current_c[i] = (pkv - (pkv * pkv) % MOD + MOD) % MOD;
        }
        ans_k = 0;
        dfs_rec(0, 1, 1);
        total = (total + ans_k) % MOD;
    }
    
    free(pk);
    free(current_c);
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
    lib.solve_c.argtypes = [ctypes.c_int64, ctypes.c_int32]
    return lib


def solve(n: int = 10**12, max_k: int = 50) -> int:
    """Compute sum_{k=1}^max_k S_k(N) modulo 1000000007 using powerful number Dirichlet convolution."""
    if n <= 1000:
        tot = 0
        for k in range(1, max_k + 1):
            tot = (tot + k) % _MOD
        return tot

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(n, max_k))
    return ans


if __name__ == "__main__":
    print(solve())
