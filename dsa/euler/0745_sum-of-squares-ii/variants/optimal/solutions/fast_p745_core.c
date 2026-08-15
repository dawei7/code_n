
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000007ULL
#define MAX_K 10000005

static uint32_t J2[MAX_K];
static int primes[700000];
static uint8_t is_comp[MAX_K];

int64_t solve_c(int64_t N) {
    int64_t limit = 1;
    while ((limit + 1) * (limit + 1) <= N) limit++;
    
    for (int i = 0; i <= limit; ++i) {
        J2[i] = 0;
        is_comp[i] = 0;
    }
    
    J2[1] = 1;
    int P = 0;
    
    for (int i = 2; i <= limit; ++i) {
        if (!is_comp[i]) {
            primes[P++] = i;
            uint64_t p2 = (uint64_t)i * i % MOD;
            J2[i] = (uint32_t)((p2 + MOD - 1) % MOD);
        }
        for (int j = 0; j < P; ++j) {
            int p = primes[j];
            int64_t ip = (int64_t)i * p;
            if (ip > limit) break;
            is_comp[ip] = 1;
            uint64_t p2 = (uint64_t)p * p % MOD;
            if (i % p == 0) {
                J2[ip] = (uint32_t)((uint64_t)J2[i] * p2 % MOD);
                break;
            } else {
                J2[ip] = (uint32_t)((uint64_t)J2[i] * J2[p] % MOD);
            }
        }
    }
    
    uint64_t total = 0;
    for (int64_t k = 1; k <= limit; ++k) {
        uint64_t cnt = (N / (k * k)) % MOD;
        total = (total + (uint64_t)J2[k] * cnt) % MOD;
    }
    
    return (int64_t)total;
}
