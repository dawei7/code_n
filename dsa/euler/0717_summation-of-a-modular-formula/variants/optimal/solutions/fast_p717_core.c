
#include <stdint.h>
#include <stdlib.h>

static inline uint64_t pow_mod(uint64_t base, uint64_t exp, uint64_t mod) {
    uint64_t res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) {
            __int128 prod = (__int128)res * base;
            res = (uint64_t)(prod % mod);
        }
        __int128 prod = (__int128)base * base;
        base = (uint64_t)(prod % mod);
        exp >>= 1;
    }
    return res;
}

static uint8_t is_comp[10000005 / 8 + 1];

int64_t solve_c(int limit) {
    for (int i = 0; i <= limit / 8 + 1; ++i) is_comp[i] = 0;
    for (int p = 2; p * p < limit; ++p) {
        if (!((is_comp[p >> 3] >> (p & 7)) & 1)) {
            for (int j = p * p; j < limit; j += p) {
                is_comp[j >> 3] |= (1 << (j & 7));
            }
        }
    }
    
    int64_t total = 0;
    for (int p = 3; p < limit; ++p) {
        if (!((is_comp[p >> 3] >> (p & 7)) & 1)) {
            uint64_t E = pow_mod(2, p, p - 1);
            uint64_t r = pow_mod(2, E, p);
            uint64_t k = (r & 1) ? (r + p) / 2 : r / 2;
            
            uint64_t p2 = (uint64_t)p * p;
            uint64_t pow2_p1 = pow_mod(2, p - 1, p2);
            uint64_t q = (pow2_p1 - 1) / p;
            uint64_t m = (2 * q) % p;
            
            uint64_t odd_flag = r & 1;
            uint64_t gp = (odd_flag + k * m) % p;
            total += gp;
        }
    }
    return total;
}
