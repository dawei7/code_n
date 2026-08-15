#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

static inline uint64_t power_mod(uint64_t base, uint64_t exp, uint64_t mod) {
    uint64_t res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) res = (uint64_t)((__int128)res * base % mod);
        base = (uint64_t)((__int128)base * base % mod);
        exp >>= 1;
    }
    return res;
}

static int* visited_stamp;
static int current_stamp = 0;

static int prime_in_S_fast(int q, const int* test_primes, int num_test_primes) {
    if (q == 2 || q == 5) return 1;
    if (q % 2 == 0) return 0;

    for (int i = 0; i < num_test_primes; i++) {
        int p = test_primes[i];
        current_stamp++;

        int x = 1 % q;
        int reaches_zero = 0;
        while (visited_stamp[x] != current_stamp) {
            if (x == 0) {
                reaches_zero = 1;
                break;
            }
            visited_stamp[x] = current_stamp;
            x = (int)((power_mod(x, p, q) + 1) % q);
        }
        if (!reaches_zero) return 0;
    }
    return 1;
}

EXPORT uint64_t compute_R(int N) {
    uint8_t* is_prime = (uint8_t*)malloc(N + 1);
    for (int i = 0; i <= N; i++) is_prime[i] = 1;
    is_prime[0] = is_prime[1] = 0;
    for (int p = 2; p * p <= N; p++) {
        if (is_prime[p]) {
            for (int j = p * p; j <= N; j += p) is_prime[j] = 0;
        }
    }

    visited_stamp = (int*)calloc(N + 1, sizeof(int));
    current_stamp = 0;

    int test_primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199};
    int num_test = sizeof(test_primes) / sizeof(test_primes[0]);

    int* S_primes = (int*)malloc(100000 * sizeof(int));
    int s_prime_count = 0;

    for (int p = 2; p <= N; p++) {
        if (is_prime[p]) {
            if (prime_in_S_fast(p, test_primes, num_test)) {
                S_primes[s_prime_count++] = p;
            }
        }
    }

    uint64_t total_R = 0;

    void dfs_prod(int idx, uint64_t cur_val) {
        total_R += cur_val;
        for (int i = idx; i < s_prime_count; i++) {
            uint64_t nxt = cur_val * S_primes[i];
            if (nxt > (uint64_t)N) break;
            dfs_prod(i + 1, nxt);
        }
    }

    dfs_prod(0, 1);

    free(is_prime);
    free(visited_stamp);
    free(S_primes);

    return total_R;
}
