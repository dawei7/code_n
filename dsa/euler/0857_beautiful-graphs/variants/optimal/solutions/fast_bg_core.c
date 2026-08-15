#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define MOD 1000000007LL

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

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

EXPORT int64_t compute_beautiful_graphs(int N) {
    int64_t inv4 = mod_inv(4);
    int64_t inv10 = mod_inv(10);

    int64_t w1 = 1;
    int64_t w2 = 1;
    int64_t w3 = 1;
    int64_t w4 = (3 * inv4) % MOD;
    int64_t w5 = (1 * inv10) % MOD;

    int64_t g0 = 1;
    int64_t g1 = (w1 * g0) % MOD;
    int64_t g2 = (w1 * g1 + w2 * g0) % MOD;
    int64_t g3 = (w1 * g2 + w2 * g1 + w3 * g0) % MOD;
    int64_t g4 = (w1 * g3 + w2 * g2 + w3 * g1 + w4 * g0) % MOD;

    int64_t fact = 24; // 4! mod MOD

    for (int n = 5; n <= N; n++) {
        int64_t g_next = (w1 * g4 + w2 * g3 + w3 * g2 + w4 * g1 + w5 * g0) % MOD;
        g0 = g1;
        g1 = g2;
        g2 = g3;
        g3 = g4;
        g4 = g_next;
        fact = (fact * n) % MOD;
    }

    int64_t ans = (g4 * fact) % MOD;
    if (ans < 0) ans += MOD;
    return ans;
}
