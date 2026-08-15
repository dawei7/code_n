
#include <stdint.h>
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

int64_t c_val_c(int64_t N, int64_t k) {
    if (k == 1) {
        int64_t num = 1, den = 1;
        for (int64_t i = 1; i <= N; ++i) {
            num = (num * ((N + i) % MOD)) % MOD;
            den = (den * (i % MOD)) % MOD;
        }
        return (num * pow_mod(den, MOD - 2)) % MOD;
    }
    
    int64_t num = 1, den = 1;
    int64_t curr_k = 1;
    for (int64_t j = 1; j <= N; ++j) {
        curr_k = (curr_k * k) % MOD;
        den = (den * (curr_k - 1)) % MOD;
    }
    for (int64_t j = N + 1; j <= 2 * N; ++j) {
        curr_k = (curr_k * k) % MOD;
        num = (num * (curr_k - 1)) % MOD;
    }
    return (num * pow_mod(den, MOD - 2)) % MOD;
}

int64_t solve_c() {
    int64_t total = 0;
    int64_t p10 = 10;
    for (int64_t k = 1; k <= 7; ++k) {
        int64_t N = p10 + k;
        int64_t val = c_val_c(N, k);
        total = (total + val) % MOD;
        p10 *= 10;
    }
    return total;
}
