
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000007ULL

static inline uint64_t pow_mod(uint64_t base, uint64_t exp) {
    uint64_t res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) res = (uint64_t)((__int128)res * base % MOD);
        base = (uint64_t)((__int128)base * base % MOD);
        exp >>= 1;
    }
    return res;
}

static inline uint64_t inv_mod(uint64_t n) {
    return pow_mod(n, MOD - 2);
}

static uint32_t inv_arr[50000005];

int64_t solve_c(int64_t k, int64_t n) {
    int64_t M = n / k;
    uint64_t P = pow_mod(2, M % (MOD - 1));
    uint64_t inv_P2 = inv_mod((uint64_t)((__int128)P * P % MOD));
    
    int64_t max_a = k / 2;
    
    inv_arr[1] = 1;
    for (int64_t i = 2; i <= max_a + 1; ++i) {
        inv_arr[i] = (uint32_t)((uint64_t)(MOD - MOD / i) * inv_arr[MOD % i] % MOD);
    }
    
    uint64_t cur_term = pow_mod(P, k % (MOD - 1));
    uint64_t total = cur_term;
    
    for (int64_t a = 0; a < max_a; ++a) {
        uint64_t num1 = (k - 2 * a) % MOD;
        uint64_t num2 = (k - 2 * a - 1) % MOD;
        uint64_t num = (uint64_t)((__int128)num1 * num2 % MOD);
        
        uint64_t inv_a1 = inv_arr[a + 1];
        uint64_t den_inv = (uint64_t)((__int128)inv_a1 * inv_a1 % MOD);
        den_inv = (uint64_t)((__int128)den_inv * inv_P2 % MOD);
        
        cur_term = (uint64_t)((__int128)cur_term * num % MOD * den_inv % MOD);
        total = (total + cur_term) % MOD;
    }
    
    return (int64_t)total;
}
