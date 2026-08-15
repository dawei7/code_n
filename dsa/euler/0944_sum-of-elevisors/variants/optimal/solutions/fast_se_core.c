#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

static inline int64_t power_mod(int64_t base, int64_t exp, int64_t mod) {
    int64_t res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) res = (__int128)res * base % mod;
        base = (__int128)base * base % mod;
        exp >>= 1;
    }
    return res;
}

EXPORT int64_t compute_S(int64_t n, int64_t mod) {
    int64_t m = n / 2;
    int64_t inv2 = (mod + 1) / 2;

    // Term 1: 2^{n - 1} * m(m + 1)/2 mod mod
    int64_t sum_all_x = ((__int128)(m % mod) * ((m + 1) % mod) % mod) * inv2 % mod;
    int64_t term1 = ((__int128)power_mod(2, n - 1, mod) * sum_all_x) % mod;

    // Term 2: sum_{k >= 2} (sum_{x in [L_k, R_k]} x) * 2^{n - k} mod mod
    int64_t term2 = 0;
    int64_t cur_x = 1;

    while (cur_x <= m) {
        int64_t k = n / cur_x;
        int64_t next_x = n / k;
        if (next_x > m) next_x = m;

        // Sum x for x in [cur_x, next_x]
        int64_t count = (next_x - cur_x + 1) % mod;
        int64_t sum_ends = (cur_x + next_x) % mod;
        int64_t sum_x_range = ((__int128)count * sum_ends % mod) * inv2 % mod;

        int64_t pow2 = power_mod(2, n - k, mod);
        term2 = (term2 + (__int128)sum_x_range * pow2) % mod;

        cur_x = next_x + 1;
    }

    int64_t ans = (term1 - term2 + mod) % mod;
    return ans;
}
