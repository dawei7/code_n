"""Project Euler Problem 675: 2^{omega(n)}.

Find sum_{i=2}^{10^7} S(i!) mod 1000000087, where S(n) = sum_{d|n} 2^{omega(d)}.
"""

import ctypes
import os
import subprocess

_MOD = 1_000_000_087


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p675_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p675_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000087LL

int64_t power_mod(int64_t base, int64_t exp) {
    int64_t res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (__int128)res * base % MOD;
        base = (__int128)base * base % MOD;
        exp /= 2;
    }
    return res;
}

int64_t modInverse(int64_t n) {
    return power_mod(n, MOD - 2);
}

#define INV_PRECOMP 2000000
static int64_t inv_table[INV_PRECOMP];

void init_inv() {
    inv_table[1] = 1;
    for (int i = 2; i < INV_PRECOMP; ++i) {
        inv_table[i] = (MOD - (MOD / i) * inv_table[MOD % i] % MOD) % MOD;
    }
}

int64_t solve_c(int N) {
    init_inv();
    int* spf = (int*)malloc((N + 1) * sizeof(int));
    for (int i = 0; i <= N; ++i) spf[i] = i;
    for (int i = 2; i * i <= N; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= N; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }
    
    int* prime_exp = (int*)calloc(N + 1, sizeof(int));
    int64_t current_S = 1;
    int64_t F = 0;
    
    for (int i = 2; i <= N; ++i) {
        int temp = i;
        while (temp > 1) {
            int p = spf[temp];
            int count = 0;
            while (temp % p == 0) {
                count++;
                temp /= p;
            }
            int old_exp = prime_exp[p];
            int new_exp = old_exp + count;
            prime_exp[p] = new_exp;
            
            int64_t old_term = 2 * old_exp + 1;
            int64_t new_term = 2 * new_exp + 1;
            
            int64_t inv_old = (old_term < INV_PRECOMP) ? inv_table[old_term] : modInverse(old_term);
            
            current_S = (__int128)current_S * inv_old % MOD;
            current_S = (__int128)current_S * (new_term % MOD) % MOD;
        }
        F = (F + current_S) % MOD;
    }
    
    free(spf);
    free(prime_exp);
    return F;
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
    """Compute F(n) modulo 1000000087 using incremental multiplicative divisor sum updates."""
    if n <= 100:
        spf = list(range(n + 1))
        for i in range(2, int(n**0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, n + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        prime_exp = [0] * (n + 1)
        cur_s = 1
        f_sum = 0
        for i in range(2, n + 1):
            temp = i
            while temp > 1:
                p = spf[temp]
                count = 0
                while temp % p == 0:
                    count += 1
                    temp //= p
                old_exp = prime_exp[p]
                new_exp = old_exp + count
                prime_exp[p] = new_exp

                cur_s = (
                    cur_s
                    * pow(2 * old_exp + 1, mod - 2, mod)
                    * (2 * new_exp + 1)
                ) % mod
            f_sum = (f_sum + cur_s) % mod
        return f_sum

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(n))
    return ans


if __name__ == "__main__":
    print(solve())
