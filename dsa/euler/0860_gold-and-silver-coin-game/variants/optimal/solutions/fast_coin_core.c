#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define MOD 989898989LL

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

EXPORT int64_t compute_fair_arrangements(int N) {
    int64_t* fact = (int64_t*)malloc((N + 1) * sizeof(int64_t));
    int64_t* inv_fact = (int64_t*)malloc((N + 1) * sizeof(int64_t));

    fact[0] = 1;
    for (int i = 1; i <= N; i++) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }

    inv_fact[N] = mod_inv(fact[N]);
    for (int i = N - 1; i >= 0; i--) {
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD;
    }

    int64_t ans = 0;
    int max_d = N / 5;

    for (int d = -max_d; d <= max_d; d++) {
        int rem = N - 5 * d;
        if (rem < 0 || (rem & 1)) continue;
        int S = rem / 2;

        int min_x2 = (d < 0) ? -d : 0;
        int max_x2 = (4 * d < 0) ? S - (-4 * d) : S;

        for (int x2 = min_x2; x2 <= max_x2; x2++) {
            int x3 = S - x2;
            int x1 = x2 + d;
            int x4 = x3 + 4 * d;

            int64_t term1 = (inv_fact[x1] * inv_fact[x2]) % MOD;
            int64_t term2 = (inv_fact[x3] * inv_fact[x4]) % MOD;
            int64_t term = (term1 * term2) % MOD;

            ans = (ans + term);
            if (ans >= MOD) ans -= MOD;
        }
    }

    ans = (ans % MOD * fact[N]) % MOD;
    free(fact);
    free(inv_fact);
    return ans;
}
