#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#define MOD 1000000007LL

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

static int primes[5000];
static int num_primes = 0;
static char is_p[10005];

static void sieve(int limit) {
    memset(is_p, 1, sizeof(char) * (limit + 1));
    is_p[0] = is_p[1] = 0;
    for (int p = 2; p * p <= limit; p++) {
        if (is_p[p]) {
            for (int i = p * p; i <= limit; i += p) is_p[i] = 0;
        }
    }
    num_primes = 0;
    for (int p = 2; p <= limit; p++) {
        if (is_p[p]) primes[num_primes++] = p;
    }
}

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

EXPORT int64_t compute_r6_factorial(int K) {
    sieve(K);

    // 1. sigma_1 for m <= K
    int* sigma_1 = (int*)calloc(K + 1, sizeof(int));
    for (int i = 1; i <= K; i++) {
        for (int j = i; j <= K; j += i) {
            sigma_1[j] += i;
        }
    }

    // 2. tau(m) for m <= K using log-derivative:
    int* a = (int*)calloc(K + 1, sizeof(int));
    a[0] = 1;
    for (int m = 1; m <= K; m++) {
        int64_t s = 0;
        for (int j = 1; j <= m; j++) {
            s = (s + (int64_t)sigma_1[j] * a[m - j]) % MOD;
        }
        int64_t term = (-24LL * s) % MOD;
        if (term < 0) term += MOD;
        a[m] = (int)((term * mod_inv(m)) % MOD);
    }

    int* tau_vals = (int*)calloc(K + 1, sizeof(int));
    for (int m = 1; m <= K; m++) {
        tau_vals[m] = a[m - 1];
    }

    // 3. tau(K!) mod MOD
    int64_t tau_M = 1;
    for (int idx = 0; idx < num_primes; idx++) {
        int p = primes[idx];
        int e = 0;
        int temp = K;
        while (temp > 0) {
            e += temp / p;
            temp /= p;
        }

        int64_t t0_val = 1;
        int64_t t1_val = tau_vals[p];
        int64_t p11 = power_mod(p, 11);

        for (int step = 2; step <= e; step++) {
            int64_t t2_val = (t1_val * tau_vals[p] - p11 * t0_val) % MOD;
            if (t2_val < 0) t2_val += MOD;
            t0_val = t1_val;
            t1_val = t2_val;
        }

        int64_t t_pe = (e >= 1) ? t1_val : t0_val;
        tau_M = (tau_M * t_pe) % MOD;
    }

    // 4. M = K! mod MOD
    int64_t M = 1;
    for (int i = 1; i <= K; i++) M = (M * i) % MOD;

    // 5. sigma_k(K!) mod MOD
    #define GET_SIGMA_FACT(k) ({ \
        int64_t ans_sig = 1; \
        for (int idx = 0; idx < num_primes; idx++) { \
            int p = primes[idx]; \
            int e = 0; \
            int temp = K; \
            while (temp > 0) { \
                e += temp / p; \
                temp /= p; \
            } \
            int64_t pk = power_mod(p, k); \
            int64_t term; \
            if (pk == 1) { \
                term = (e + 1) % MOD; \
            } else { \
                term = (power_mod(p, (int64_t)(e + 1) * (k)) - 1 + MOD) % MOD; \
                term = (term * mod_inv(pk - 1 + MOD)) % MOD; \
            } \
            ans_sig = (ans_sig * term) % MOD; \
        } \
        ans_sig; \
    })

    int64_t sig11 = GET_SIGMA_FACT(11);
    int64_t sig9  = GET_SIGMA_FACT(9);
    int64_t sig7  = GET_SIGMA_FACT(7);
    int64_t sig5  = GET_SIGMA_FACT(5);
    int64_t sig3  = GET_SIGMA_FACT(3);
    int64_t sig1  = GET_SIGMA_FACT(1);

    #define MOD_FRAC(num, den) (((int64_t)(num) % MOD + MOD) % MOD * mod_inv(((int64_t)(den) % MOD + MOD) % MOD) % MOD)

    int64_t c_sig11 = MOD_FRAC(455, 14328576);
    int64_t c_tau   = MOD_FRAC(-1, 15671880);

    int64_t M2 = (M * M) % MOD;
    int64_t M3 = (M2 * M) % MOD;
    int64_t M4 = (M3 * M) % MOD;
    int64_t M5 = (M4 * M) % MOD;

    int64_t P9 = (MOD_FRAC(11, 20736) + MOD_FRAC(-11, 17280) * M) % MOD;
    int64_t P7 = (MOD_FRAC(25, 10368) + MOD_FRAC(-25, 3456) * M + MOD_FRAC(25, 5184) * M2) % MOD;
    int64_t P5 = (MOD_FRAC(35, 10368) + MOD_FRAC(-35, 1728) * M + MOD_FRAC(5, 144) * M2 + MOD_FRAC(-5, 288) * M3) % MOD;
    int64_t P3 = (MOD_FRAC(25, 20736) + MOD_FRAC(-25, 1728) * M + MOD_FRAC(5, 96) * M2 + MOD_FRAC(-5, 72) * M3 + MOD_FRAC(5, 168) * M4) % MOD;
    int64_t P1 = (MOD_FRAC(1, 20736) + MOD_FRAC(-5, 3456) * M + MOD_FRAC(5, 432) * M2 + MOD_FRAC(-5, 144) * M3 + MOD_FRAC(1, 24) * M4 + MOD_FRAC(-1, 60) * M5) % MOD;

    int64_t ans = (c_sig11 * sig11 + c_tau * tau_M + P9 * sig9 + P7 * sig7 + P5 * sig5 + P3 * sig3 + P1 * sig1) % MOD;
    if (ans < 0) ans += MOD;

    free(sigma_1);
    free(a);
    free(tau_vals);
    return ans;
}
