
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000007LL

static inline int64_t pow_mod(int64_t base, int64_t exp) {
    int64_t res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return res;
}

int64_t solve_c(int64_t alpha, int64_t n) {
    int64_t* inv = (int64_t*)malloc((alpha + 1) * sizeof(int64_t));
    inv[1] = 1;
    for (int i = 2; i <= alpha; ++i) {
        inv[i] = (MOD - MOD / i) * inv[MOD % i] % MOD;
    }
    
    int64_t total = 0;
    int64_t comb = 1;
    int64_t exp_n_plus_1 = n + 1;
    
    for (int64_t j = 0; j < alpha; ++j) {
        int64_t term;
        if (j == 0) {
            term = 1;
        } else if (j == 1) {
            term = (n + 1) % MOD;
        } else {
            term = ((pow_mod(j, exp_n_plus_1) - 1 + MOD) % MOD) * inv[j - 1] % MOD;
        }
        
        int64_t signed_term = (comb * term) % MOD;
        if ((alpha - 1 - j) & 1) {
            total = (total - signed_term + MOD) % MOD;
        } else {
            total = (total + signed_term) % MOD;
        }
        
        comb = ((comb * ((alpha - j) % MOD)) % MOD) * inv[j + 1] % MOD;
    }
    
    free(inv);
    return total;
}
