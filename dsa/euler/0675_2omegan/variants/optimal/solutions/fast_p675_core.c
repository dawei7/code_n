
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000087LL

int64_t power_mod(int64_t base, int64_t exp) {
    int64_t res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (__int128)res * base % MOD;
        base = (__int128)base * base % MOD;
        exp /= 2;
    }
    return res;
}

int64_t modInverse(int64_t n) {
    return power_mod(n, MOD - 2);
}

#define INV_PRECOMP 2000000
static int64_t inv_table[INV_PRECOMP];

void init_inv() {
    inv_table[1] = 1;
    for (int i = 2; i < INV_PRECOMP; ++i) {
        inv_table[i] = (MOD - (MOD / i) * inv_table[MOD % i] % MOD) % MOD;
    }
}

int64_t solve_c(int N) {
    init_inv();
    int* spf = (int*)malloc((N + 1) * sizeof(int));
    for (int i = 0; i <= N; ++i) spf[i] = i;
    for (int i = 2; i * i <= N; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= N; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }
    
    int* prime_exp = (int*)calloc(N + 1, sizeof(int));
    int64_t current_S = 1;
    int64_t F = 0;
    
    for (int i = 2; i <= N; ++i) {
        int temp = i;
        while (temp > 1) {
            int p = spf[temp];
            int count = 0;
            while (temp % p == 0) {
                count++;
                temp /= p;
            }
            int old_exp = prime_exp[p];
            int new_exp = old_exp + count;
            prime_exp[p] = new_exp;
            
            int64_t old_term = 2 * old_exp + 1;
            int64_t new_term = 2 * new_exp + 1;
            
            int64_t inv_old = (old_term < INV_PRECOMP) ? inv_table[old_term] : modInverse(old_term);
            
            current_S = (__int128)current_S * inv_old % MOD;
            current_S = (__int128)current_S * (new_term % MOD) % MOD;
        }
        F = (F + current_S) % MOD;
    }
    
    free(spf);
    free(prime_exp);
    return F;
}
