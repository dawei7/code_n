"""Project Euler Problem 650: Divisors of Binomial Product.

Find S(20000) mod 1000000007, where S(n) = sum_{k=1}^n D(k), D(k) is the sum of divisors
of B(k), and B(k) = prod_{j=0}^k binom(k, j).
"""

import ctypes
import os
import subprocess

_MOD = 1_000_000_007


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_binomprod_core.dll")
    c_path = os.path.join(tmp_dir, "fast_binomprod_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000007LL

int64_t pow_mod(int64_t base, int64_t exp) {
    int64_t res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return res;
}

int64_t solve_c(int N) {
    uint8_t* is_p = (uint8_t*)malloc(N + 1);
    for (int i = 0; i <= N; ++i) is_p[i] = 1;
    is_p[0] = is_p[1] = 0;
    
    int* primes = (int*)malloc((N + 1) * sizeof(int));
    int* min_prime = (int*)malloc((N + 1) * sizeof(int));
    int num_primes = 0;
    
    for (int i = 0; i <= N; ++i) min_prime[i] = i;
    
    for (int i = 2; i <= N; ++i) {
        if (is_p[i]) {
            primes[num_primes++] = i;
            for (int j = i * i; j <= N; j += i) {
                if (is_p[j]) {
                    is_p[j] = 0;
                    min_prime[j] = i;
                }
            }
        }
    }
    
    int* prime_idx = (int*)calloc(N + 1, sizeof(int));
    for (int i = 0; i < num_primes; ++i) {
        prime_idx[primes[i]] = i;
    }
    
    int64_t* inv_p_minus_1 = (int64_t*)malloc(num_primes * sizeof(int64_t));
    for (int i = 0; i < num_primes; ++i) {
        inv_p_minus_1[i] = pow_mod(primes[i] - 1, MOD - 2);
    }
    
    int64_t* E_p = (int64_t*)calloc(num_primes, sizeof(int64_t));
    int64_t* F_p = (int64_t*)calloc(num_primes, sizeof(int64_t));
    
    int64_t total_S = 0;
    
    for (int n = 1; n <= N; ++n) {
        int temp = n;
        while (temp > 1) {
            int p = min_prime[temp];
            int cnt = 0;
            while (temp % p == 0) {
                cnt++;
                temp /= p;
            }
            E_p[prime_idx[p]] += cnt;
        }
        
        int64_t D_n = 1;
        for (int idx = 0; idx < num_primes; ++idx) {
            int p = primes[idx];
            if (p > n) break;
            F_p[idx] += E_p[idx];
            int64_t ep = (int64_t)(n + 1) * E_p[idx] - 2 * F_p[idx];
            if (ep > 0) {
                int64_t term = ((pow_mod(p, ep + 1) - 1 + MOD) % MOD * inv_p_minus_1[idx]) % MOD;
                D_n = (D_n * term) % MOD;
            }
        }
        total_S = (total_S + D_n) % MOD;
    }
    
    free(is_p);
    free(primes);
    free(min_prime);
    free(prime_idx);
    free(inv_p_minus_1);
    free(E_p);
    free(F_p);
    
    return total_S;
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
    lib.solve_c.argtypes = [ctypes.c_int32]
    return lib


def solve(n: int = 20000) -> int:
    """Compute S(n) modulo 1000000007 using incremental binomial prime valuation streams."""
    if n <= 100:
        is_p = [True] * (n + 1)
        is_p[0] = is_p[1] = False
        primes = []
        for i in range(2, n + 1):
            if is_p[i]:
                primes.append(i)
                for j in range(i * i, n + 1, i):
                    is_p[j] = False
        prime_to_idx = {p: i for i, p in enumerate(primes)}
        inv_p_minus_1 = [pow(p - 1, _MOD - 2, _MOD) for p in primes]
        e_p = [0] * len(primes)
        f_p = [0] * len(primes)
        total_s = 0
        for k in range(1, n + 1):
            temp = k
            for p in primes:
                if p * p > temp:
                    break
                if temp % p == 0:
                    cnt = 0
                    while temp % p == 0:
                        cnt += 1
                        temp //= p
                    e_p[prime_to_idx[p]] += cnt
            if temp > 1:
                e_p[prime_to_idx[temp]] += 1
            d_k = 1
            for idx, p in enumerate(primes):
                if p > k:
                    break
                f_p[idx] += e_p[idx]
                ep = (k + 1) * e_p[idx] - 2 * f_p[idx]
                if ep > 0:
                    term = (pow(p, ep + 1, _MOD) - 1) * inv_p_minus_1[idx] % _MOD
                    d_k = (d_k * term) % _MOD
            total_s = (total_s + d_k) % _MOD
        return total_s

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(n))
    return ans


if __name__ == "__main__":
    print(solve())
