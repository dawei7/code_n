#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

#define MOD 1000000007LL

static inline int64_t power_mod(int64_t base, int64_t exp) {
    int64_t res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return res;
}

static inline int64_t mod_inv(int64_t n) {
    return power_mod(n, MOD - 2);
}

EXPORT int64_t compute_P(int64_t n) {
    // We need C_n = 1/(n+1) * binom(2n, n) mod MOD
    // and f_{(n+1, n-1)} = 3/(n+2) * binom(2n, n-1) mod MOD
    // binom(2n, n) = (2n)! / (n!)^2
    // We can compute fact(2n) and fact(n) mod MOD:
    int64_t fact_n = 1;
    int64_t fact_2n = 1;

    for (int64_t i = 1; i <= n; i++) {
        fact_n = (fact_n * i) % MOD;
    }

    fact_2n = fact_n;
    for (int64_t i = n + 1; i <= 2 * n; i++) {
        fact_2n = (fact_2n * i) % MOD;
    }

    int64_t inv_fact_n = mod_inv(fact_n);
    int64_t inv_fact_n_sq = (inv_fact_n * inv_fact_n) % MOD;

    // binom(2n, n) = fact(2n) * inv_fact_n_sq
    int64_t binom_2n_n = (fact_2n * inv_fact_n_sq) % MOD;

    // C_n = binom(2n, n) * inv(n + 1)
    int64_t c_n = (binom_2n_n * mod_inv(n + 1)) % MOD;

    // binom(2n, n-1) = binom(2n, n) * n / (n + 1)
    int64_t binom_2n_n_minus_1 = ((binom_2n_n * (n % MOD)) % MOD * mod_inv(n + 1)) % MOD;

    // f_{(n+1, n-1)} = 3 * binom(2n, n-1) * inv(n + 2)
    int64_t f_hook = ((3 * binom_2n_n_minus_1) % MOD * mod_inv(n + 2)) % MOD;

    int64_t p_ans = (c_n * c_n + f_hook * f_hook) % MOD;

    return p_ans;
}
