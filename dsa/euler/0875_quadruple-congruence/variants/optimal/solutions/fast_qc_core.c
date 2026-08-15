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

#define MOD 1001961001LL

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

static int64_t q_pe(int64_t p, int e) {
    if (p == 2) {
        if (e == 1) return 128 % MOD;
        int64_t val = 128;
        for (int k = 2; k <= e; k++) {
            val = (val * 128 + power(2, 4 * k + 3)) % MOD;
        }
        return val;
    }

    int64_t term1 = power(p, 7 * e);
    int64_t term2 = (power(p, 7 * e - 4) * (p - 1)) % MOD;
    int64_t term3 = 0;
    for (int a = 0; a <= e - 2; a++) {
        term3 = (term3 + power(p, 4 * e + 3 * a - 1)) % MOD;
    }
    term3 = (term3 * (p - 1)) % MOD;
    return (term1 + term2 + term3) % MOD;
}

EXPORT int64_t compute_Q(int N) {
    int* min_prime = (int*)calloc(N + 1, sizeof(int));
    int* primes = (int*)malloc((N / 10 + 1000) * sizeof(int));
    int prime_count = 0;

    int64_t* q_arr = (int64_t*)malloc((N + 1) * sizeof(int64_t));

    q_arr[1] = 1;

    for (int i = 2; i <= N; i++) {
        if (!min_prime[i]) {
            min_prime[i] = i;
            primes[prime_count++] = i;
            q_arr[i] = q_pe(i, 1);
        }
        for (int j = 0; j < prime_count; j++) {
            int p = primes[j];
            if ((int64_t)p * i > N) break;
            min_prime[p * i] = p;
            if (i % p == 0) {
                int temp = p * i;
                int e = 0;
                while (temp % p == 0) {
                    temp /= p;
                    e++;
                }
                int64_t q_pe_val = q_pe(p, e);
                q_arr[p * i] = (q_pe_val * q_arr[temp]) % MOD;
                break;
            } else {
                q_arr[p * i] = (q_arr[p] * q_arr[i]) % MOD;
            }
        }
    }

    int64_t total_Q = 0;
    for (int i = 1; i <= N; i++) {
        total_Q = (total_Q + q_arr[i]) % MOD;
    }

    free(min_prime);
    free(primes);
    free(q_arr);
    return total_Q;
}
