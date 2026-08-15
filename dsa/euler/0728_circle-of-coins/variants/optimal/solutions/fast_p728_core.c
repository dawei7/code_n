
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000007ULL

static inline uint64_t pow_mod(uint64_t base, uint64_t exp, uint64_t mod) {
    uint64_t res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) res = (uint64_t)((__int128)res * base % mod);
        base = (uint64_t)((__int128)base * base % mod);
        exp >>= 1;
    }
    return res;
}

static uint32_t phi[10000005];
static uint8_t is_comp[10000005 / 8 + 1];
static int primes[700000];

int64_t solve_c(int N) {
    phi[1] = 1;
    int P = 0;
    for (int i = 0; i <= N / 8 + 1; ++i) is_comp[i] = 0;
    
    for (int i = 2; i <= N; ++i) {
        if (!((is_comp[i >> 3] >> (i & 7)) & 1)) {
            primes[P++] = i;
            phi[i] = i - 1;
        }
        for (int j = 0; j < P; ++j) {
            int p = primes[j];
            int64_t ip = (int64_t)i * p;
            if (ip > N) break;
            is_comp[ip >> 3] |= (1 << (ip & 7));
            if (i % p == 0) {
                phi[ip] = phi[i] * p;
                break;
            } else {
                phi[ip] = phi[i] * (p - 1);
            }
        }
    }
    
    uint64_t inv2 = (MOD + 1) / 2;
    uint64_t ans = 0;
    
    for (int m = 1; m <= N; ++m) {
        int L = N / m;
        int t = m - 1;
        
        uint64_t ph = phi[m];
        uint64_t A;
        if (m == 1 || (m & 1) == 0) {
            A = (2 * ph) % MOD;
        } else {
            A = (3 * ph) % MOD;
            A = (uint64_t)((__int128)A * inv2 % MOD);
        }
        
        uint64_t G;
        if (t == 0) {
            G = (uint64_t)(L % MOD);
        } else {
            uint64_t r = pow_mod(2, t, MOD);
            uint64_t den = (r + MOD - 1) % MOD;
            if (den == 0) {
                G = (uint64_t)(L % MOD);
            } else {
                uint64_t rL = pow_mod(2, (uint64_t)t * L, MOD);
                uint64_t num = (uint64_t)((__int128)r * (rL + MOD - 1) % MOD);
                uint64_t den_inv = pow_mod(den, MOD - 2, MOD);
                G = (uint64_t)((__int128)num * den_inv % MOD);
            }
        }
        ans = (ans + (__int128)A * G) % MOD;
    }
    return (int64_t)ans;
}
