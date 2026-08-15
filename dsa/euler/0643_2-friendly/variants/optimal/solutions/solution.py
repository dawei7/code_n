"""Project Euler Problem 643: 2-Friendly.

Find f(10^11) mod 1000000007, where f(n) is the number of pairs 1 <= p < q <= n
such that gcd(p, q) = 2^t for some t > 0.
"""

import ctypes
import os
import subprocess

_MOD = 1_000_000_007


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_friendly_core.dll")
    c_path = os.path.join(tmp_dir, "fast_friendly_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000007LL
#define INV2 ((MOD + 1) / 2)
#define PRE_LIMIT 10000000

static int32_t* phi_pref;
static int phi_initialized = 0;

void init_phi() {
    if (phi_initialized) return;
    phi_initialized = 1;
    
    int* phi = (int*)malloc((PRE_LIMIT + 1) * sizeof(int));
    for (int i = 0; i <= PRE_LIMIT; ++i) phi[i] = i;
    
    uint8_t* is_p = (uint8_t*)malloc(PRE_LIMIT + 1);
    for (int i = 0; i <= PRE_LIMIT; ++i) is_p[i] = 1;
    is_p[0] = is_p[1] = 0;
    
    int* primes = (int*)malloc((PRE_LIMIT / 10) * sizeof(int));
    int num_primes = 0;
    
    for (int i = 2; i <= PRE_LIMIT; ++i) {
        if (is_p[i]) {
            primes[num_primes++] = i;
            phi[i] = i - 1;
        }
        for (int p_idx = 0; p_idx < num_primes; ++p_idx) {
            int p = primes[p_idx];
            if ((int64_t)i * p > PRE_LIMIT) break;
            is_p[i * p] = 0;
            if (i % p == 0) {
                phi[i * p] = phi[i] * p;
                break;
            } else {
                phi[i * p] = phi[i] * (p - 1);
            }
        }
    }
    
    phi_pref = (int32_t*)malloc((PRE_LIMIT + 1) * sizeof(int32_t));
    phi_pref[0] = 0;
    for (int i = 1; i <= PRE_LIMIT; ++i) {
        phi_pref[i] = (int32_t)(((int64_t)phi_pref[i - 1] + phi[i]) % MOD);
    }
    
    free(phi);
    free(is_p);
    free(primes);
}

#define HASH_SIZE 1000003
typedef struct HashNode {
    int64_t key;
    int64_t val;
    struct HashNode* next;
} HashNode;

static HashNode** table;
static HashNode* pool;
static int pool_ptr;

int64_t Phi_c(int64_t x) {
    if (x <= PRE_LIMIT) return phi_pref[x];
    
    uint32_t h = (uint32_t)(((uint64_t)x ^ ((uint64_t)x >> 16)) % HASH_SIZE);
    for (HashNode* curr = table[h]; curr; curr = curr->next) {
        if (curr->key == x) return curr->val;
    }
    
    int64_t xm = x % MOD;
    int64_t total = (((xm * ((xm + 1) % MOD)) % MOD) * INV2) % MOD;
    
    int64_t l = 2;
    while (l <= x) {
        int64_t q = x / l;
        int64_t r = x / q;
        int64_t count = (r - l + 1) % MOD;
        total = (total - (count * Phi_c(q)) % MOD + MOD) % MOD;
        l = r + 1;
    }
    
    HashNode* node = &pool[pool_ptr++];
    node->key = x;
    node->val = total;
    node->next = table[h];
    table[h] = node;
    
    return total;
}

int64_t solve_c(int64_t n) {
    init_phi();
    
    table = (HashNode**)calloc(HASH_SIZE, sizeof(HashNode*));
    pool = (HashNode*)malloc(1000000 * sizeof(HashNode));
    pool_ptr = 0;
    
    int64_t ans = 0;
    int64_t p2 = 2;
    while (p2 <= n) {
        int64_t m = n / p2;
        int64_t phi_m = Phi_c(m);
        ans = (ans + phi_m - 1 + MOD) % MOD;
        if (p2 > n / 2) break;
        p2 *= 2;
    }
    
    free(table);
    free(pool);
    return ans;
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


def solve(n: int = 10**11) -> int:
    """Compute f(n) modulo 1000000007 using the sublinear Du Sieve for Euler's totient summatory function."""
    if n <= 100:
        ans = 0
        p2 = 2
        while p2 <= n:
            m = n // p2
            count = 0
            for y in range(2, m + 1):
                import math

                count += sum(1 for x in range(1, y) if math.gcd(x, y) == 1)
            ans = (ans + count) % _MOD
            p2 *= 2
        return ans

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(n))
    return ans


if __name__ == "__main__":
    print(solve())
