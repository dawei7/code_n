
#include <stdint.h>
#include <stdlib.h>
#include <math.h>

#define MOD 1000000007ULL

static int64_t V[2000005];
static int64_t S_pi[2000005];
static int total_v;
static int64_t N_val;
static int64_t lim;

static inline int get_idx(int64_t v) {
    if (v <= lim) {
        return (int)(total_v - v);
    } else {
        return (int)(N_val / v - 1);
    }
}

int64_t solve_c(int64_t N) {
    N_val = N;
    lim = (int64_t)sqrt((double)N);
    while ((lim + 1) * (lim + 1) <= N) lim++;
    while (lim * lim > N) lim--;
    
    total_v = 0;
    for (int64_t i = 1; i <= lim; ++i) {
        V[total_v++] = N / i;
    }
    for (int64_t s = V[total_v - 1] - 1; s >= 1; --s) {
        V[total_v++] = s;
    }
    
    for (int i = 0; i < total_v; ++i) {
        S_pi[i] = V[i] - 1;
    }
    
    for (int64_t p = 2; p <= lim; ++p) {
        if (S_pi[get_idx(p)] > S_pi[get_idx(p - 1)]) {
            int64_t sp = S_pi[get_idx(p - 1)];
            int64_t p2 = p * p;
            for (int i = 0; i < total_v; ++i) {
                int64_t v = V[i];
                if (v < p2) break;
                S_pi[i] -= (S_pi[get_idx(v / p)] - sp);
            }
        }
    }
    
    uint64_t ans = 0;
    
    for (int64_t p = 2; p <= lim; ++p) {
        if (S_pi[get_idx(p)] > S_pi[get_idx(p - 1)]) {
            int64_t c[70];
            int num_c = 0;
            int64_t pk = 1;
            while (pk <= N) {
                int64_t next_pk = (pk <= N / p) ? pk * p : N + 1;
                c[num_c++] = (N / pk) - (N / next_pk);
                if (next_pk > N) break;
                pk = next_pk;
            }
            
            uint64_t p_contrib = 0;
            for (int j = 0; j < num_c; ++j) {
                for (int k = j + 1; k < num_c; ++k) {
                    uint64_t term = ((uint64_t)(k - j) * (c[j] % MOD)) % MOD;
                    term = (term * (c[k] % MOD)) % MOD;
                    p_contrib = (p_contrib + term) % MOD;
                }
            }
            ans = (ans + 2 * p_contrib) % MOD;
        }
    }
    
    for (int64_t v = 1; v <= lim; ++v) {
        int64_t upper_p = N / v;
        int64_t lower_p = N / (v + 1);
        if (lower_p < lim) lower_p = lim;
        if (upper_p <= lim) continue;
        
        int64_t count_primes = S_pi[get_idx(upper_p)] - S_pi[get_idx(lower_p)];
        if (count_primes > 0) {
            uint64_t c0 = (N - v) % MOD;
            uint64_t c1 = v % MOD;
            uint64_t pair_term = (2 * c0 * c1) % MOD;
            uint64_t block = (pair_term * (count_primes % MOD)) % MOD;
            ans = (ans + block) % MOD;
        }
    }
    
    return (int64_t)ans;
}
