
#include <stdint.h>
#include <stdlib.h>
#include <math.h>

#define MOD 999999937ULL

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

int64_t solve_c(int limit) {
    uint64_t total = 0;
    int64_t c = 1;
    
    for (int64_t a = 1; a <= limit; ++a) {
        while ((c - 1) * (c - 1) >= a) c--;
        while (c * c < a) c++;
        
        uint64_t n = (uint64_t)a * a;
        if (a == c * c) {
            uint64_t val = pow_mod(2 * c, n, MOD);
            total = (total + val) % MOD;
        } else {
            uint64_t m00 = (2 * c) % MOD;
            uint64_t disc = c * c - a;
            uint64_t m01 = (MOD - (disc % MOD)) % MOD;
            
            uint64_t exp = n - 1;
            uint64_t r00 = 1, r01 = 0, r10 = 0, r11 = 1;
            uint64_t b00 = m00, b01 = m01, b10 = 1, b11 = 0;
            
            while (exp > 0) {
                if (exp & 1) {
                    uint64_t nr00 = (r00 * b00 + r01 * b10) % MOD;
                    uint64_t nr01 = (r00 * b01 + r01 * b11) % MOD;
                    uint64_t nr10 = (r10 * b00 + r11 * b10) % MOD;
                    uint64_t nr11 = (r10 * b01 + r11 * b11) % MOD;
                    r00 = nr00; r01 = nr01; r10 = nr10; r11 = nr11;
                }
                uint64_t nb00 = (b00 * b00 + b01 * b10) % MOD;
                uint64_t nb01 = (b00 * b01 + b01 * b11) % MOD;
                uint64_t nb10 = (b10 * b00 + b11 * b10) % MOD;
                uint64_t nb11 = (b10 * b01 + b11 * b11) % MOD;
                b00 = nb00; b01 = nb01; b10 = nb10; b11 = nb11;
                exp >>= 1;
            }
            uint64_t u_n = (r00 * (2 * c) + r01 * 2) % MOD;
            uint64_t val = (u_n + MOD - 1) % MOD;
            total = (total + val) % MOD;
        }
    }
    return (int64_t)total;
}
