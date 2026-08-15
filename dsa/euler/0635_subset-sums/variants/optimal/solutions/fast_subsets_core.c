
#include <stdint.h>
#include <stdlib.h>
#include <math.h>

#define MOD 1000000009LL
#define INV2 ((MOD + 1) / 2)
#define K9 ((9 * INV2) % MOD)

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

int64_t solve_c(int64_t L) {
    if (L < 2) return 0;
    
    int64_t size = L / 2 + 1;
    uint8_t* is_prime = (uint8_t*)malloc(size);
    for (int64_t i = 0; i < size; ++i) is_prime[i] = 1;
    is_prime[0] = 0;
    
    int64_t r = (int64_t)sqrt((double)L);
    for (int64_t p = 3; p <= r; p += 2) {
        if (is_prime[p / 2]) {
            int64_t start = (p * p) / 2;
            int64_t step = p;
            for (int64_t j = start; j < size; j += step) {
                is_prime[j] = 0;
            }
        }
    }
    
    int64_t max_odd = 2 * L + 3;
    int64_t odd_count = max_odd / 2 + 1;
    uint32_t* inv_odd = (uint32_t*)malloc(odd_count * sizeof(uint32_t));
    
    int64_t max_half = (L + 1) / 2;
    uint32_t* inv_half = (uint32_t*)malloc((max_half + 1) * sizeof(uint32_t));
    
    int64_t block = 1000000;
    int64_t* pref = (int64_t*)malloc((block + 1) * sizeof(int64_t));
    
    for (int64_t s = 1; s <= max_half; s += block) {
        int64_t cnt = block;
        if (s + cnt - 1 > max_half) cnt = max_half - s + 1;
        pref[0] = 1;
        int64_t x = s;
        for (int64_t i = 0; i < cnt; ++i) {
            pref[i + 1] = (pref[i] * x) % MOD;
            x++;
        }
        int64_t inv_total = pow_mod(pref[cnt], MOD - 2);
        x = s + cnt - 1;
        for (int64_t i = cnt - 1; i >= 0; --i) {
            inv_half[x] = (uint32_t)((pref[i] * inv_total) % MOD);
            inv_total = (inv_total * x) % MOD;
            x--;
        }
    }
    
    for (int64_t idx = 0; idx < odd_count; idx += block) {
        int64_t cnt = block;
        if (idx + cnt > odd_count) cnt = odd_count - idx;
        pref[0] = 1;
        int64_t x = 2 * idx + 1;
        for (int64_t i = 0; i < cnt; ++i) {
            pref[i + 1] = (pref[i] * x) % MOD;
            x += 2;
        }
        int64_t inv_total = pow_mod(pref[cnt], MOD - 2);
        x = 2 * (idx + cnt - 1) + 1;
        for (int64_t i = cnt - 1; i >= 0; --i) {
            inv_odd[idx + i] = (uint32_t)((pref[i] * inv_total) % MOD);
            inv_total = (inv_total * x) % MOD;
            x -= 2;
        }
    }
    
    int64_t S2 = (L >= 2) ? 2 : 0;
    int64_t S3 = (L >= 2) ? 6 : 0;
    
    int64_t max_i = (L - 1) / 2;
    int64_t C = 2;
    int64_t D = 3;
    
    int64_t a1 = 3;
    int64_t a3 = 5;
    int64_t idx_a1 = 1;
    int64_t idx_a3 = 2;
    
    int64_t t1 = 2;
    int64_t t2 = 5;
    int64_t t3 = 7;
    int64_t t4 = 4;
    
    for (int64_t i = 0; i <= max_i; ++i) {
        if (i >= 1 && is_prime[i]) {
            int64_t invp = inv_odd[i];
            S2 = (S2 + (C + 4 * i) % MOD * invp) % MOD;
            S3 = (S3 + (D + 6 * i) % MOD * invp) % MOD;
        }
        
        int64_t invh = inv_half[i + 1];
        int64_t invn2 = inv_odd[i + 1];
        
        C = (C * a1) % MOD;
        C = (C * a3) % MOD;
        C = (C * invh) % MOD;
        C = (C * invn2) % MOD;
        C = (C * 2) % MOD;
        
        D = (D * K9) % MOD;
        D = (D * t1) % MOD;
        D = (D * t2) % MOD;
        D = (D * t3) % MOD;
        D = (D * t4) % MOD;
        D = (D * invh) % MOD;
        D = (D * invn2) % MOD;
        D = (D * inv_odd[idx_a1]) % MOD;
        D = (D * inv_odd[idx_a3]) % MOD;
        
        a1 += 4;
        a3 += 4;
        idx_a1 += 2;
        idx_a3 += 2;
        t1 += 3;
        t2 += 6;
        t3 += 6;
        t4 += 3;
    }
    
    free(is_prime);
    free(inv_odd);
    free(inv_half);
    free(pref);
    
    return (S2 + S3) % MOD;
}
