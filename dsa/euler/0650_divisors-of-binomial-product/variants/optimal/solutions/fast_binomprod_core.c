
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000007LL

int64_t pow_mod(int64_t base, int64_t exp) {
    int64_t res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return res;
}

int64_t solve_c(int N) {
    uint8_t* is_p = (uint8_t*)malloc(N + 1);
    for (int i = 0; i <= N; ++i) is_p[i] = 1;
    is_p[0] = is_p[1] = 0;
    
    int* primes = (int*)malloc((N + 1) * sizeof(int));
    int* min_prime = (int*)malloc((N + 1) * sizeof(int));
    int num_primes = 0;
    
    for (int i = 0; i <= N; ++i) min_prime[i] = i;
    
    for (int i = 2; i <= N; ++i) {
        if (is_p[i]) {
            primes[num_primes++] = i;
            for (int j = i * i; j <= N; j += i) {
                if (is_p[j]) {
                    is_p[j] = 0;
                    min_prime[j] = i;
                }
            }
        }
    }
    
    int* prime_idx = (int*)calloc(N + 1, sizeof(int));
    for (int i = 0; i < num_primes; ++i) {
        prime_idx[primes[i]] = i;
    }
    
    int64_t* inv_p_minus_1 = (int64_t*)malloc(num_primes * sizeof(int64_t));
    for (int i = 0; i < num_primes; ++i) {
        inv_p_minus_1[i] = pow_mod(primes[i] - 1, MOD - 2);
    }
    
    int64_t* E_p = (int64_t*)calloc(num_primes, sizeof(int64_t));
    int64_t* F_p = (int64_t*)calloc(num_primes, sizeof(int64_t));
    
    int64_t total_S = 0;
    
    for (int n = 1; n <= N; ++n) {
        int temp = n;
        while (temp > 1) {
            int p = min_prime[temp];
            int cnt = 0;
            while (temp % p == 0) {
                cnt++;
                temp /= p;
            }
            E_p[prime_idx[p]] += cnt;
        }
        
        int64_t D_n = 1;
        for (int idx = 0; idx < num_primes; ++idx) {
            int p = primes[idx];
            if (p > n) break;
            F_p[idx] += E_p[idx];
            int64_t ep = (int64_t)(n + 1) * E_p[idx] - 2 * F_p[idx];
            if (ep > 0) {
                int64_t term = ((pow_mod(p, ep + 1) - 1 + MOD) % MOD * inv_p_minus_1[idx]) % MOD;
                D_n = (D_n * term) % MOD;
            }
        }
        total_S = (total_S + D_n) % MOD;
    }
    
    free(is_p);
    free(primes);
    free(min_prime);
    free(prime_idx);
    free(inv_p_minus_1);
    free(E_p);
    free(F_p);
    
    return total_S;
}
