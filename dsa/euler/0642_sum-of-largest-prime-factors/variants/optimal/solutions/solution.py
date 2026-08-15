"""Project Euler Problem 642: Sum of Largest Prime Factors.

Find F(201820182018) mod 10^9, where F(n) = sum_{i=2}^n f(i) and f(i) is the largest prime factor of i.
"""

import ctypes
import os
import subprocess

_MOD = 1_000_000_000


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_lpf_core.dll")
    c_path = os.path.join(tmp_dir, "fast_lpf_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>
#include <math.h>

#define MOD 1000000000LL
#define HASH_SIZE 2000003

typedef struct HashNode {
    int64_t key;
    int64_t val;
    struct HashNode* next;
} HashNode;

static int64_t G_N;
static int64_t G_root;
static int* G_primes;
static int G_num_primes;
static int* G_pi;
static int64_t* G_prime_sums;
static int32_t* G_idx_small;
static int32_t* G_idx_large;
static int64_t* G_lower_prime_sum;
static int64_t G_key_base;

static HashNode** G_table;
static HashNode* G_node_pool;
static int G_pool_ptr;

static inline int64_t prime_sum_upto(int64_t x) {
    if (x <= G_root) return G_prime_sums[G_idx_small[x]];
    return G_prime_sums[G_idx_large[G_N / x]];
}

static inline int64_t terminal_prime_sum(int64_t x, int idx) {
    if (idx >= G_num_primes) {
        if (x <= G_primes[G_num_primes - 1]) return 0;
    } else if (x < G_primes[idx]) {
        return 0;
    }
    return (prime_sum_upto(x) - G_lower_prime_sum[idx] + MOD) % MOD;
}

static int64_t contribution(int64_t bound, int idx) {
    int end = G_pi[(int)sqrt((double)bound)];
    int64_t total = terminal_prime_sum(bound, idx);
    if (idx >= end) return total;
    
    int64_t key = bound * G_key_base + idx;
    uint32_t h = (uint32_t)(((uint64_t)key ^ ((uint64_t)key >> 16)) % HASH_SIZE);
    for (HashNode* curr = G_table[h]; curr; curr = curr->next) {
        if (curr->key == key) return curr->val;
    }
    
    for (int i = idx; i < end; ++i) {
        int p = G_primes[i];
        int64_t power = p;
        int64_t power_limit = bound / p;
        int next_idx = i + 1;
        while (power <= power_limit) {
            int64_t child_bound = bound / power;
            int child_end = G_pi[(int)sqrt((double)child_bound)];
            int64_t child;
            if (next_idx >= child_end) {
                child = terminal_prime_sum(child_bound, next_idx);
            } else {
                child = contribution(child_bound, next_idx);
            }
            total = (total + child + p) % MOD;
            if (power > bound / p) break;
            power *= p;
        }
    }
    
    HashNode* node = &G_node_pool[G_pool_ptr++];
    node->key = key;
    node->val = total;
    node->next = G_table[h];
    G_table[h] = node;
    
    return total;
}

int64_t solve_c(int64_t N) {
    G_N = N;
    int64_t root = (int64_t)sqrt((double)N);
    G_root = root;
    
    int64_t num_values = 2 * root + 10;
    int64_t* values = (int64_t*)malloc(num_values * sizeof(int64_t));
    G_prime_sums = (int64_t*)malloc(num_values * sizeof(int64_t));
    
    G_idx_small = (int32_t*)malloc((root + 10) * sizeof(int32_t));
    G_idx_large = (int32_t*)malloc((root + 10) * sizeof(int32_t));
    
    int v_idx = 0;
    for (int64_t i = 1; i <= root; ++i) {
        int64_t val = N / i;
        values[v_idx] = val;
        if (val <= root) {
            G_idx_small[val] = v_idx;
        } else {
            G_idx_large[i] = v_idx;
        }
        v_idx++;
    }
    int64_t last_large = values[root - 1];
    for (int64_t val = last_large - 1; val >= 1; --val) {
        values[v_idx] = val;
        G_idx_small[val] = v_idx;
        v_idx++;
    }
    int total_values = v_idx;
    
    for (int i = 0; i < total_values; ++i) {
        int64_t v = values[i];
        __int128 sum = (__int128)v * (v + 1) / 2 - 1;
        G_prime_sums[i] = (int64_t)(sum % MOD);
    }
    
    uint8_t* is_p = (uint8_t*)malloc(root + 10);
    for (int i = 0; i <= root + 9; ++i) is_p[i] = 1;
    is_p[0] = is_p[1] = 0;
    for (int64_t i = 2; i * i <= root; ++i) {
        if (is_p[i]) {
            for (int64_t j = i * i; j <= root; j += i) is_p[j] = 0;
        }
    }
    G_primes = (int*)malloc((root + 10) * sizeof(int));
    int num_primes = 0;
    for (int i = 2; i <= root; ++i) {
        if (is_p[i]) G_primes[num_primes++] = i;
    }
    G_num_primes = num_primes;
    
    int limit = total_values;
    for (int p_idx = 0; p_idx < num_primes; ++p_idx) {
        int p = G_primes[p_idx];
        int64_t p2 = (int64_t)p * p;
        while (limit > 0 && values[limit - 1] < p2) {
            limit--;
        }
        int64_t sum_before_p = G_prime_sums[G_idx_small[p - 1]];
        for (int idx = 0; idx < limit; ++idx) {
            int64_t value = values[idx];
            int64_t q = value / p;
            int qidx = (q <= root) ? G_idx_small[q] : G_idx_large[N / q];
            int64_t term = (p * ((G_prime_sums[qidx] - sum_before_p) % MOD)) % MOD;
            G_prime_sums[idx] = (G_prime_sums[idx] - term + MOD) % MOD;
        }
    }
    
    G_pi = (int*)malloc((root + 10) * sizeof(int));
    int count = 0;
    int p_curr = 0;
    for (int v = 0; v <= root; ++v) {
        if (p_curr < num_primes && G_primes[p_curr] == v) {
            count++;
            p_curr++;
        }
        G_pi[v] = count;
    }
    
    G_lower_prime_sum = (int64_t*)malloc((num_primes + 10) * sizeof(int64_t));
    for (int idx = 0; idx < num_primes; ++idx) {
        G_lower_prime_sum[idx] = G_prime_sums[G_idx_small[G_primes[idx] - 1]];
    }
    if (num_primes > 0) {
        G_lower_prime_sum[num_primes] = G_prime_sums[G_idx_small[G_primes[num_primes - 1]]];
    }
    
    G_table = (HashNode**)calloc(HASH_SIZE, sizeof(HashNode*));
    G_node_pool = (HashNode*)malloc(5000000 * sizeof(HashNode));
    G_pool_ptr = 0;
    G_key_base = num_primes + 1;
    
    int64_t ans = contribution(N, 0);
    
    free(values);
    free(G_prime_sums);
    free(G_idx_small);
    free(G_idx_large);
    free(is_p);
    free(G_primes);
    free(G_pi);
    free(G_lower_prime_sum);
    free(G_table);
    free(G_node_pool);
    
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


def solve(n: int = 201820182018) -> int:
    """Compute F(n) modulo 10^9 using sublinear Lucy prime sum sieve and sparse Min_25 recursion."""
    if n <= 10000:
        lpf = [0] * (n + 1)
        for p in range(2, n + 1):
            if lpf[p] == 0:
                for j in range(p, n + 1, p):
                    lpf[j] = p
        return sum(lpf[2:]) % _MOD

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(n))
    return ans


if __name__ == "__main__":
    print(solve())
