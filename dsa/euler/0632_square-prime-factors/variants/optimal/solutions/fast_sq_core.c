
#include <stdint.h>
#include <stdlib.h>
#include <math.h>

#define MOD 1000000007LL

int64_t solve_c(int64_t N) {
    int64_t lim = (int64_t)sqrt((double)N);
    int8_t* omega = (int8_t*)calloc(lim + 1, sizeof(int8_t));
    uint8_t* is_prime = (uint8_t*)malloc(lim + 1);
    for (int64_t i = 0; i <= lim; ++i) is_prime[i] = 1;
    is_prime[0] = is_prime[1] = 0;
    
    int* primes = (int*)malloc((lim / 10) * sizeof(int));
    int num_primes = 0;
    
    for (int64_t i = 2; i <= lim; ++i) {
        if (is_prime[i]) {
            primes[num_primes++] = i;
            omega[i] = 1;
        }
        for (int p_idx = 0; p_idx < num_primes; ++p_idx) {
            int p = primes[p_idx];
            int64_t ip = i * p;
            if (ip > lim) break;
            is_prime[ip] = 0;
            if (i % p == 0) {
                omega[ip] = -1;
                break;
            } else {
                if (omega[i] == -1) {
                    omega[ip] = -1;
                } else {
                    omega[ip] = omega[i] + 1;
                }
            }
        }
    }
    
    int64_t S[15] = {0};
    for (int64_t m = 1; m <= lim; ++m) {
        int r = (m == 1) ? 0 : omega[m];
        if (r >= 0) {
            S[r] += N / (m * m);
        }
    }
    
    int64_t binom[15][15] = {0};
    for (int i = 0; i < 15; ++i) {
        binom[i][0] = 1;
        for (int j = 1; j <= i; ++j) {
            binom[i][j] = binom[i-1][j-1] + binom[i-1][j];
        }
    }
    
    int64_t C[15] = {0};
    for (int k = 0; k < 15; ++k) {
        int64_t val = 0;
        for (int r = k; r < 15; ++r) {
            int64_t term = binom[r][k] * S[r];
            if ((r - k) % 2 == 1) {
                val -= term;
            } else {
                val += term;
            }
        }
        C[k] = val;
    }
    
    int64_t prod = 1;
    for (int k = 0; k < 15; ++k) {
        if (C[k] > 0) {
            prod = (prod * (C[k] % MOD)) % MOD;
        }
    }
    
    free(omega);
    free(is_prime);
    free(primes);
    return prod;
}
