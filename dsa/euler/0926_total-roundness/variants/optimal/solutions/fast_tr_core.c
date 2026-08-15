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

EXPORT int64_t compute_R_fact(int N) {
    // Sieve primes up to N
    uint8_t* is_prime = (uint8_t*)malloc(N + 1);
    for (int i = 0; i <= N; i++) is_prime[i] = 1;
    is_prime[0] = is_prime[1] = 0;
    for (int p = 2; p * p <= N; p++) {
        if (is_prime[p]) {
            for (int j = p * p; j <= N; j += p) is_prime[j] = 0;
        }
    }

    int prime_count = 0;
    for (int i = 2; i <= N; i++) {
        if (is_prime[i]) prime_count++;
    }

    int* primes = (int*)malloc(prime_count * sizeof(int));
    int* vp = (int*)malloc(prime_count * sizeof(int));
    int idx = 0;
    int max_v = 0;

    for (int p = 2; p <= N; p++) {
        if (is_prime[p]) {
            primes[idx] = p;
            // Legendre formula
            int64_t count = 0;
            int64_t p_pow = p;
            while (p_pow <= N) {
                count += N / p_pow;
                p_pow *= p;
            }
            vp[idx] = (int)count;
            if (count > max_v) max_v = (int)count;
            idx++;
        }
    }

    int64_t total_R = 0;

    // For each k from 1 to max_v:
    // We compute prod (floor(v_p / k) + 1) mod MOD - 1
    for (int k = 1; k <= max_v; k++) {
        int64_t prod = 1;
        // Only primes with v_p >= k contribute > 1:
        for (int i = 0; i < prime_count; i++) {
            if (vp[i] < k) break; // since vp is decreasing with p!
            int term = (vp[i] / k) + 1;
            prod = (prod * term) % MOD;
        }
        int64_t count_k = (prod - 1 + MOD) % MOD;
        total_R = (total_R + count_k) % MOD;
    }

    free(is_prime);
    free(primes);
    free(vp);

    return total_R;
}
