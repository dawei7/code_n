"""Project Euler Problem 798: Card Stacking Game.

Compute C(10^7, 10^7) modulo 1_000_000_007, where C(n, s) is the number of
initial visible card configurations that are losing for the first player.
"""

import ctypes
import os
import subprocess

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

void fwht_xor(int64_t *a, int n) {
    for (int h = 1; h < n; h <<= 1) {
        for (int i = 0; i < n; i += (h << 1)) {
            for (int j = i; j < i + h; ++j) {
                int64_t x = a[j];
                int64_t y = a[j + h];
                int64_t u = x + y;
                if (u >= MOD) u -= MOD;
                int64_t v = x - y;
                if (v < 0) v += MOD;
                a[j] = u;
                a[j + h] = v;
            }
        }
    }
}

int64_t solve_c(int n, int s) {
    if (n == 0) return 1;
    int L = 1;
    while (L < n) L <<= 1;
    
    int64_t *fact = (int64_t *)malloc((n + 1) * sizeof(int64_t));
    int64_t *inv_fact = (int64_t *)malloc((n + 1) * sizeof(int64_t));
    fact[0] = 1;
    for (int i = 1; i <= n; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    inv_fact[n] = modInverse(fact[n]);
    for (int i = n; i >= 1; --i) inv_fact[i - 1] = (inv_fact[i] * i) % MOD;
    
    int64_t *a = (int64_t *)calloc(L, sizeof(int64_t));
    if (n == 1) {
        a[0] = 2;
    } else {
        int64_t a0 = (power(2, n - 2) + 2) % MOD;
        int64_t a1 = (power(2, n - 2) + (n - 2)) % MOD;
        a[0] = a0;
        if (n > 1) a[1] = a1;
        if (n > 2) a[2] = (power(2, n - 3) + (n - 3)) % MOD;
        
        int64_t inv4 = modInverse(4);
        
        #define nCk(nn, kk) (((kk) < 0 || (kk) > (nn)) ? 0 : ((fact[nn] * inv_fact[kk] % MOD) * inv_fact[(nn) - (kk)] % MOD))
        #define Q_of(X, k) (( (X) * nCk((X) + (k) + 1, (k) + 1) - ((k) + 1) * nCk((X) + (k) + 1, (k) + 2) ) % MOD)
        
        int X0 = n - 4;
        if (3 < n && X0 >= 0) {
            int k = 0;
            int X = X0;
            int64_t F = (power(2, X + 1) - 1 + MOD) % MOD;
            while (1) {
                int g = 2 * k + 3;
                if (g >= n || X < 0) break;
                int64_t qv = Q_of(X, k);
                a[g] = (F + qv) % MOD;
                if (a[g] < 0) a[g] += MOD;
                if (X < 2) break;
                int64_t c_xk_1 = nCk(X + k - 1, k);
                int64_t c_xk = nCk(X + k, k);
                int64_t tmp = (F - 2 * c_xk_1 - c_xk) % MOD;
                if (tmp < 0) tmp += MOD;
                tmp = (tmp * inv4) % MOD;
                int64_t c_next = nCk(X + k - 1, k + 1);
                F = (2 * tmp - c_next) % MOD;
                if (F < 0) F += MOD;
                k++;
                X -= 2;
            }
        }
        
        X0 = n - 5;
        if (4 < n && X0 >= 0) {
            int k = 0;
            int X = X0;
            int64_t F = (power(2, X + 1) - 1 + MOD) % MOD;
            while (1) {
                int g = 2 * k + 4;
                if (g >= n || X < 0) break;
                int64_t qv = Q_of(X, k);
                a[g] = (F + qv) % MOD;
                if (a[g] < 0) a[g] += MOD;
                if (X < 2) break;
                int64_t c_xk_1 = nCk(X + k - 1, k);
                int64_t c_xk = nCk(X + k, k);
                int64_t tmp = (F - 2 * c_xk_1 - c_xk) % MOD;
                if (tmp < 0) tmp += MOD;
                tmp = (tmp * inv4) % MOD;
                int64_t c_next = nCk(X + k - 1, k + 1);
                F = (2 * tmp - c_next) % MOD;
                if (F < 0) F += MOD;
                k++;
                X -= 2;
            }
        }
    }
    
    fwht_xor(a, L);
    
    int64_t total = 0;
    for (int i = 0; i < L; ++i) {
        total = (total + power(a[i], s)) % MOD;
    }
    
    int64_t inv_L = modInverse(L);
    int64_t ans = (total * inv_L) % MOD;
    if (ans < 0) ans += MOD;
    
    free(fact); free(inv_fact); free(a);
    return ans;
}
"""


def _load_c_solver():
    dll_path = os.path.join(os.path.dirname(__file__), "solver798.dll")
    if not os.path.exists(dll_path):
        c_path = os.path.join(os.path.dirname(__file__), "solver798.c")
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
    lib.solve_c.argtypes = [ctypes.c_int32, ctypes.c_int32]
    return lib.solve_c


def solve(n: int = 10_000_000, s: int = 10_000_000) -> int:
    """Compute C(n, s) mod 10^9+7 using Sprague-Grundy theorem and Fast Walsh-Hadamard Transform."""
    ans = 0
    for _iter in range(1):
        try:
            c_solve = _load_c_solver()
            ans = int(c_solve(n, s))
        except Exception:
            from array import array

            # Python fallback
            L = 1 << (n - 1).bit_length() if n > 0 else 1
            if n == 0:
                ans = 1
                break

            fact = array("I", [1]) * (n + 1)
            for i in range(2, n + 1):
                fact[i] = (fact[i - 1] * i) % _MOD
            inv_fact = array("I", [1]) * (n + 1)
            inv_fact[n] = pow(int(fact[n]), _MOD - 2, _MOD)
            for i in range(n, 0, -1):
                inv_fact[i - 1] = (inv_fact[i] * i) % _MOD

            def nCk(nn, kk):
                if kk < 0 or kk > nn:
                    return 0
                return (int(fact[nn]) * int(inv_fact[kk]) % _MOD) * int(inv_fact[nn - kk]) % _MOD

            def Q_of(X, k):
                return (X * nCk(X + k + 1, k + 1) - (k + 1) * nCk(X + k + 1, k + 2)) % _MOD

            a = array("I", [0]) * L
            if n == 1:
                a[0] = 2
            else:
                a[0] = (pow(2, n - 2, _MOD) + 2) % _MOD
                if n > 1:
                    a[1] = (pow(2, n - 2, _MOD) + (n - 2)) % _MOD
                if n > 2:
                    a[2] = (pow(2, n - 3, _MOD) + (n - 3)) % _MOD

                inv4 = pow(4, _MOD - 2, _MOD)
                for start_g, parity_offset in [(3, 4), (4, 5)]:
                    X0 = n - parity_offset
                    if start_g < n and X0 >= 0:
                        k = 0
                        X = X0
                        F = (pow(2, X + 1, _MOD) - 1) % _MOD
                        while True:
                            g = 2 * k + start_g
                            if g >= n or X < 0:
                                break
                            a[g] = (F + Q_of(X, k)) % _MOD
                            if X < 2:
                                break
                            c_xk_1 = nCk(X + k - 1, k)
                            c_xk = nCk(X + k, k)
                            tmp = (F - 2 * c_xk_1 - c_xk) % _MOD
                            tmp = (tmp * inv4) % _MOD
                            c_next = nCk(X + k - 1, k + 1)
                            F = (2 * tmp - c_next) % _MOD
                            k += 1
                            X -= 2

            h = 1
            while h < L:
                step = h << 1
                for i in range(0, L, step):
                    for j in range(i, i + h):
                        x = a[j]
                        y = a[j + h]
                        u = (x + y) % _MOD
                        v = (x - y + _MOD) % _MOD
                        a[j] = u
                        a[j + h] = v
                h = step

            total = 0
            for v in a:
                total = (total + pow(int(v), s, _MOD)) % _MOD
            inv_L = pow(L, _MOD - 2, _MOD)
            ans = (total * inv_L) % _MOD

    return ans


if __name__ == "__main__":
    print(solve())
