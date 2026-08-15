#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

#define MOD 1234567891LL

static inline int64_t power(int64_t base, int64_t exp) {
    int64_t res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return res;
}

static inline int64_t modInverse(int64_t n) {
    return power(n, MOD - 2);
}

EXPORT int64_t compute_sum_D(int64_t N) {
    // We compute sum_{n=1}^N D(n) mod MOD
    // D(2m) = (1/2) * binom(2m, m)^2 mod MOD
    // D(2m + 1) = (m / (2m + 1)) * binom(2m, m) * binom(2m + 2, m + 1) mod MOD
    // Let M_max = N / 2
    int64_t M_max = (N + 1) / 2;

    int64_t* C = (int64_t*)malloc((M_max + 2) * sizeof(int64_t));
    int64_t* inv = (int64_t*)malloc((2 * M_max + 5) * sizeof(int64_t));

    // Linear inverse precomputation
    inv[1] = 1;
    for (int64_t i = 2; i <= 2 * M_max + 3; i++) {
        inv[i] = (MOD - MOD / i) * inv[MOD % i] % MOD;
    }

    C[0] = 1;
    for (int64_t m = 1; m <= M_max + 1; m++) {
        C[m] = (C[m - 1] * (4 * m - 2) % MOD) * inv[m] % MOD;
    }

    int64_t inv2 = inv[2];
    int64_t total_sum = 0;

    for (int64_t m = 1; 2 * m <= N; m++) {
        // D(2m)
        int64_t d_even = (C[m] * C[m] % MOD) * inv2 % MOD;
        total_sum = (total_sum + d_even) % MOD;

        // D(2m + 1) if 2m + 1 <= N
        if (2 * m + 1 <= N) {
            int64_t coeff = (m * inv[2 * m + 1]) % MOD;
            int64_t d_odd = ((C[m] * C[m + 1] % MOD) * coeff) % MOD;
            total_sum = (total_sum + d_odd) % MOD;
        }
    }

    free(C);
    free(inv);
    return total_sum;
}
