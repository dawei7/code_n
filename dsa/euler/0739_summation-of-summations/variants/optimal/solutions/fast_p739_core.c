
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

static uint32_t L[100000005];

int64_t solve_c(int n) {
    if (n <= 1) return 0;
    
    L[1] = 1;
    L[2] = 3;
    for (int k = 3; k <= n; ++k) {
        uint32_t val = L[k - 1] + L[k - 2];
        if (val >= MOD) val -= MOD;
        L[k] = val;
    }
    
    uint64_t inv_n_minus_1 = inv_mod(n - 1);
    
    uint32_t *inv_arr = (uint32_t *)malloc((n + 5) * sizeof(uint32_t));
    inv_arr[1] = 1;
    for (int i = 2; i <= n; ++i) {
        inv_arr[i] = (uint32_t)((uint64_t)(MOD - MOD / i) * inv_arr[MOD % i] % MOD);
    }
    
    uint64_t total = 0;
    uint64_t B_j = 1;
    
    for (int j = 0; j <= n - 2; ++j) {
        int k = n - j;
        uint64_t coeff = (uint64_t)(n - j - 1) * inv_n_minus_1 % MOD;
        coeff = (uint64_t)((__int128)coeff * B_j % MOD);
        
        uint64_t term = (uint64_t)((__int128)coeff * L[k] % MOD);
        total = (total + term) % MOD;
        
        uint64_t num = n + j - 1;
        uint64_t den_inv = inv_arr[j + 1];
        B_j = (uint64_t)((__int128)B_j * (num % MOD) % MOD * den_inv % MOD);
    }
    
    free(inv_arr);
    return (int64_t)total;
}
