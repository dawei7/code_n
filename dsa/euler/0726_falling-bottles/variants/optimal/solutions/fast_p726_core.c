
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000033ULL

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

static uint64_t inv_odd[20005];

int64_t solve_c(int n) {
    for (int k = 1; k <= n; ++k) {
        inv_odd[k] = pow_mod(2 * k - 1, MOD - 2, MOD);
    }
    
    uint64_t cur_f = 1;
    uint64_t total = 1;
    uint64_t curN = 1;
    uint64_t pow2 = 2;
    uint64_t mers_prefix = 1;
    uint64_t odd_inv_prefix = 1;
    
    for (int layer = 2; layer <= n; ++layer) {
        uint64_t start = curN + 1;
        uint64_t end = curN + layer;
        for (uint64_t x = start; x <= end; ++x) {
            cur_f = (uint64_t)((__int128)cur_f * (x % MOD) % MOD);
        }
        curN = end;
        
        pow2 = (pow2 * 2) % MOD;
        mers_prefix = (uint64_t)((__int128)mers_prefix * (pow2 + MOD - 1) % MOD);
        odd_inv_prefix = (uint64_t)((__int128)odd_inv_prefix * inv_odd[layer] % MOD);
        
        cur_f = (uint64_t)((__int128)cur_f * mers_prefix % MOD);
        cur_f = (uint64_t)((__int128)cur_f * odd_inv_prefix % MOD);
        
        total = (total + cur_f) % MOD;
    }
    return (int64_t)total;
}
