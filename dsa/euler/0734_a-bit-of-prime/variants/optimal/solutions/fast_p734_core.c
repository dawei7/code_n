
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000007ULL
#define SIZE (1 << 20)

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

static uint32_t A[SIZE];
static uint8_t is_comp[SIZE / 8 + 1];

int64_t solve_c(int n, int k) {
    for (int i = 0; i < SIZE; ++i) A[i] = 0;
    for (int i = 0; i <= n / 8 + 1; ++i) is_comp[i] = 0;
    
    for (int p = 2; p * p <= n; ++p) {
        if (!((is_comp[p >> 3] >> (p & 7)) & 1)) {
            for (int j = p * p; j <= n; j += p) {
                is_comp[j >> 3] |= (1 << (j & 7));
            }
        }
    }
    
    for (int p = 2; p <= n; ++p) {
        if (!((is_comp[p >> 3] >> (p & 7)) & 1)) {
            A[p] = 1;
        }
    }
    
    for (int i = 0; i < 20; ++i) {
        for (int mask = 0; mask < SIZE; ++mask) {
            if (mask & (1 << i)) {
                A[mask] += A[mask ^ (1 << i)];
            }
        }
    }
    
    for (int mask = 0; mask < SIZE; ++mask) {
        A[mask] = (uint32_t)pow_mod(A[mask], k, MOD);
    }
    
    for (int i = 0; i < 20; ++i) {
        for (int mask = 0; mask < SIZE; ++mask) {
            if (mask & (1 << i)) {
                uint32_t sub = A[mask ^ (1 << i)];
                A[mask] = (A[mask] >= sub) ? (A[mask] - sub) : (A[mask] + MOD - sub);
            }
        }
    }
    
    uint64_t total = 0;
    for (int p = 2; p <= n; ++p) {
        if (!((is_comp[p >> 3] >> (p & 7)) & 1)) {
            total = (total + A[p]) % MOD;
        }
    }
    return (int64_t)total;
}
