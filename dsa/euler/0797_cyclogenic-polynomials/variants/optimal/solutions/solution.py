"""Project Euler Problem 797: Cyclogenic Polynomials.

Compute Q_{10^7}(2) modulo 1_000_000_007, where P_n(x) is the sum of all
n-cyclogenic polynomials and Q_N(x) = sum_{n=1}^N P_n(x).
"""

import ctypes
import os
import subprocess
import sys

_MOD = 1_000_000_007

_C_SOURCE = r"""
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000007LL

static inline int64_t power(int64_t base, int64_t exp) {
    int64_t res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return res;
}

static inline int64_t modInverse(int64_t n) {
    return power(n, MOD - 2);
}

int64_t solve_c(int n) {
    int *spf = (int *)calloc(n + 1, sizeof(int));
    int8_t *mu = (int8_t *)calloc(n + 1, sizeof(int8_t));
    int *primes = (int *)malloc((n + 1) * sizeof(int));
    int prime_cnt = 0;
    
    spf[1] = 1; mu[1] = 1;
    for (int i = 2; i <= n; ++i) {
        if (spf[i] == 0) {
            spf[i] = i;
            primes[prime_cnt++] = i;
            mu[i] = -1;
        }
        for (int j = 0; j < prime_cnt; ++j) {
            int p = primes[j];
            int ip = i * p;
            if (ip > n) break;
            spf[ip] = p;
            if (i % p == 0) {
                mu[ip] = 0;
                break;
            }
            mu[ip] = -mu[i];
        }
    }
    
    int64_t *b = (int64_t *)malloc((n + 1) * sizeof(int64_t));
    int64_t *invb = (int64_t *)malloc((n + 1) * sizeof(int64_t));
    
    int64_t pow2 = 1;
    for (int k = 1; k <= n; ++k) {
        pow2 = (pow2 * 2) % MOD;
        b[k] = (pow2 - 1 + MOD) % MOD;
    }
    
    invb[0] = 1;
    int64_t acc = 1;
    for (int k = 1; k <= n; ++k) {
        acc = (acc * b[k]) % MOD;
        invb[k] = acc;
    }
    int64_t inv_total = modInverse(acc);
    for (int k = n; k >= 1; --k) {
        int64_t prev = invb[k - 1];
        invb[k] = (inv_total * prev) % MOD;
        inv_total = (inv_total * b[k]) % MOD;
    }
    invb[0] = 0;
    
    int64_t *T = (int64_t *)malloc((n + 1) * sizeof(int64_t));
    for (int i = 0; i <= n; ++i) T[i] = 1;
    T[0] = 0;
    
    for (int d = 1; d <= n; ++d) {
        int64_t phi_d = 1;
        if (d > 1) {
            int m = d;
            int p_distinct[15];
            int p_cnt = 0;
            while (m > 1) {
                int p = spf[m];
                p_distinct[p_cnt++] = p;
                while (m % p == 0) m /= p;
            }
            
            int num_divs = 1 << p_cnt;
            for (int mask = 0; mask < num_divs; ++mask) {
                int s = 1;
                int bits = 0;
                for (int bit = 0; bit < p_cnt; ++bit) {
                    if ((mask >> bit) & 1) {
                        s *= p_distinct[bit];
                        bits++;
                    }
                }
                int idx = d / s;
                if (bits % 2 == 0) {
                    phi_d = (phi_d * b[idx]) % MOD;
                } else {
                    phi_d = (phi_d * invb[idx]) % MOD;
                }
            }
        }
        
        int64_t fd = (phi_d + 1) % MOD;
        for (int m = d; m <= n; m += d) {
            T[m] = (T[m] * fd) % MOD;
        }
    }
    
    int64_t *prefT = (int64_t *)malloc((n + 1) * sizeof(int64_t));
    prefT[0] = 0;
    for (int i = 1; i <= n; ++i) {
        prefT[i] = (prefT[i - 1] + T[i]) % MOD;
    }
    
    int64_t ans = 0;
    for (int k = 1; k <= n; ++k) {
        if (mu[k] == 1) {
            ans = (ans + prefT[n / k]) % MOD;
        } else if (mu[k] == -1) {
            ans = (ans - prefT[n / k] + MOD) % MOD;
        }
    }
    
    free(spf); free(mu); free(primes); free(b); free(invb); free(T); free(prefT);
    return ans;
}
"""


def _load_c_solver():
    dll_path = os.path.join(os.path.dirname(__file__), "solver797.dll")
    if not os.path.exists(dll_path):
        c_path = os.path.join(os.path.dirname(__file__), "solver797.c")
        with open(c_path, "w", encoding="utf-8") as f:
            f.write(_C_SOURCE)
        subprocess.run(
            ["gcc", "-O3", "-shared", "-static", "-o", dll_path, c_path],
            check=True,
            capture_output=True,
        )
        if os.path.exists(c_path):
            os.remove(c_path)
    lib = ctypes.CDLL(dll_path)
    lib.solve_c.restype = ctypes.c_int64
    lib.solve_c.argtypes = [ctypes.c_int32]
    return lib.solve_c


def solve(N: int = 10_000_000) -> int:
    """Compute Q_N(2) mod 10^9+7 using cyclotomic evaluation and Mobius Dirichlet convolution."""
    ans = 0
    for _iter in range(1):
        try:
            c_solve = _load_c_solver()
            ans = int(c_solve(N))
        except Exception:
            from array import array

            # Pure Python fallback for smaller samples
            spf = array("I", [0]) * (N + 1)
            mu = array("b", [0]) * (N + 1)
            primes = []
            spf[1] = 1
            mu[1] = 1
            for i in range(2, N + 1):
                if spf[i] == 0:
                    spf[i] = i
                    primes.append(i)
                    mu[i] = -1
                for p in primes:
                    ip = i * p
                    if ip > N:
                        break
                    spf[ip] = p
                    if i % p == 0:
                        mu[ip] = 0
                        break
                    mu[ip] = -mu[i]

            b = array("I", [0]) * (N + 1)
            invb = array("I", [0]) * (N + 1)
            pow2 = 1
            for k in range(1, N + 1):
                pow2 = (pow2 * 2) % _MOD
                b[k] = pow2 - 1
            invb[0] = 1
            acc = 1
            for k in range(1, N + 1):
                acc = (acc * b[k]) % _MOD
                invb[k] = acc
            inv_total = pow(acc, _MOD - 2, _MOD)
            for k in range(N, 0, -1):
                prev = invb[k - 1]
                invb[k] = (inv_total * prev) % _MOD
                inv_total = (inv_total * b[k]) % _MOD
            invb[0] = 0

            T = array("I", [1]) * (N + 1)
            T[0] = 0
            for d in range(1, N + 1):
                phi_d = 1
                if d > 1:
                    m = d
                    p_distinct = []
                    while m > 1:
                        p = spf[m]
                        p_distinct.append(p)
                        while m % p == 0:
                            m //= p
                    num_divs = 1 << len(p_distinct)
                    for mask in range(num_divs):
                        s = 1
                        bits = 0
                        for bit in range(len(p_distinct)):
                            if (mask >> bit) & 1:
                                s *= p_distinct[bit]
                                bits += 1
                        idx = d // s
                        if bits % 2 == 0:
                            phi_d = (phi_d * b[idx]) % _MOD
                        else:
                            phi_d = (phi_d * invb[idx]) % _MOD
                fd = (phi_d + 1) % _MOD
                for m in range(d, N + 1, d):
                    T[m] = (T[m] * fd) % _MOD

            prefT = array("I", [0]) * (N + 1)
            for i in range(1, N + 1):
                prefT[i] = (prefT[i - 1] + T[i]) % _MOD

            res = 0
            for k in range(1, N + 1):
                if mu[k] == 1:
                    res = (res + prefT[N // k]) % _MOD
                elif mu[k] == -1:
                    res = (res - prefT[N // k] + _MOD) % _MOD
            ans = res

    return ans


if __name__ == "__main__":
    print(solve())
