"""Project Euler Problem 752: Powers of 1 + sqrt(7).

Find G(10^6), where G(N) = sum_{x=2}^N g(x) and g(x) is the multiplicative order
of 1 + sqrt(7) modulo x in Z[sqrt(7)]/(x).
"""

import ctypes
import math
import os
import subprocess


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p752_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p752_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>

#define MAX_N 1000005

static int spf[MAX_N];
static int primes[100000];
static uint64_t orders[MAX_N];
static uint64_t values[MAX_N];

static inline uint64_t gcd_64(uint64_t a, uint64_t b) {
    while (b) {
        uint64_t t = b;
        b = a % b;
        a = t;
    }
    return a;
}

static inline uint64_t lcm_64(uint64_t a, uint64_t b) {
    if (a == 0 || b == 0) return 0;
    return (a / gcd_64(a, b)) * b;
}

static void quadratic_power(uint64_t exp, uint64_t mod, uint64_t *res_a, uint64_t *res_b) {
    uint64_t ra = 1, rb = 0;
    uint64_t ba = 1, bb = 1;
    
    while (exp > 0) {
        if (exp & 1) {
            uint64_t n_ra = (uint64_t)(((__int128)ba * ra + 7 * (__int128)bb * rb) % mod);
            uint64_t n_rb = (uint64_t)(((__int128)ba * rb + (__int128)bb * ra) % mod);
            ra = n_ra; rb = n_rb;
        }
        uint64_t n_ba = (uint64_t)(((__int128)ba * ba + 7 * (__int128)bb * bb) % mod);
        uint64_t n_bb = (uint64_t)((2 * (__int128)ba * bb) % mod);
        ba = n_ba; bb = n_bb;
        exp >>= 1;
    }
    *res_a = ra;
    *res_b = rb;
}

static uint64_t pow_mod(uint64_t base, uint64_t exp, uint64_t mod) {
    uint64_t res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) res = (uint64_t)((__int128)res * base % mod);
        base = (uint64_t)((__int128)base * base % mod);
        exp >>= 1;
    }
    return res;
}

static uint64_t prime_order(int p) {
    if (p == 7) return 7;
    uint64_t order;
    int factors[30];
    int F = 0;
    
    if (pow_mod(7, (p - 1) / 2, p) == 1) {
        order = p - 1;
    } else {
        order = (uint64_t)(p - 1) * (p + 1);
    }
    
    uint64_t temp = order;
    for (int d = 2; (uint64_t)d * d <= temp; ++d) {
        if (temp % d == 0) {
            factors[F++] = d;
            while (temp % d == 0) temp /= d;
        }
    }
    if (temp > 1) factors[F++] = (int)temp;
    
    for (int i = 0; i < F; ++i) {
        int q = factors[i];
        while (order % q == 0) {
            uint64_t ra, rb;
            quadratic_power(order / q, p, &ra, &rb);
            if (ra == 1 && rb == 0) {
                order /= q;
            } else {
                break;
            }
        }
    }
    return order;
}

int64_t solve_c(int limit) {
    for (int i = 0; i <= limit; ++i) {
        spf[i] = 0;
        orders[i] = 0;
        values[i] = 0;
    }
    int P = 0;
    for (int i = 2; i <= limit; ++i) {
        if (spf[i] == 0) {
            spf[i] = i;
            primes[P++] = i;
        }
        for (int j = 0; j < P; ++j) {
            int p = primes[j];
            if (i * p > limit || p > spf[i]) break;
            spf[i * p] = p;
        }
    }
    
    for (int j = 0; j < P; ++j) {
        int p = primes[j];
        if (p < 5) continue;
        uint64_t order = prime_order(p);
        int64_t prime_power = p;
        uint64_t lifted_order = order;
        orders[prime_power] = lifted_order;
        
        while (prime_power <= limit / p) {
            prime_power *= p;
            uint64_t ra, rb;
            quadratic_power(lifted_order, prime_power, &ra, &rb);
            if (ra != 1 || rb != 0) {
                lifted_order *= p;
            }
            orders[prime_power] = lifted_order;
        }
    }
    
    uint64_t total = 0;
    for (int n = 2; n <= limit; ++n) {
        if (n % 2 == 0 || n % 3 == 0) continue;
        
        int p = spf[n];
        int remaining = n;
        int prime_power = 1;
        while (remaining % p == 0) {
            remaining /= p;
            prime_power *= p;
        }
        uint64_t prev = (remaining > 1) ? values[remaining] : 1;
        uint64_t comp_order = orders[prime_power];
        uint64_t val = lcm_64(prev, comp_order);
        values[n] = val;
        total += val;
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
    lib.solve_c.argtypes = [ctypes.c_int]
    return lib


def solve(limit: int = 1_000_000) -> int:
    """Compute G(limit) using quadratic field multiplicative order sieving."""
    if limit <= 100:
        total = 0
        for x in range(2, limit + 1):
            if x % 2 == 0 or x % 3 == 0:
                continue
            a, b = 1, 0
            for step in range(1, x * x + 1):
                a, b = (a + 7 * b) % x, (a + b) % x
                if a == 1 and b == 0:
                    total += step
                    break
        return total

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(limit))
    return ans


if __name__ == "__main__":
    print(solve())
