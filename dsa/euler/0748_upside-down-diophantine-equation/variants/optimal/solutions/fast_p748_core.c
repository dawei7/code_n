
#include <stdint.h>
#include <stdlib.h>
#include <math.h>

#define MOD 1000000000ULL

static inline int gcd(int a, int b) {
    while (b) {
        int t = b;
        b = a % b;
        a = t;
    }
    return a;
}

static inline int64_t isqrt_64(int64_t n) {
    if (n <= 0) return 0;
    int64_t x = (int64_t)sqrt((double)n);
    while ((x + 1) * (x + 1) <= n) x++;
    while (x * x > n) x--;
    return x;
}

int64_t solve_c(int64_t N, int64_t mod) {
    __int128 N2 = (__int128)N * N;
    __int128 target = 2 * N2 / 13;
    int64_t r_max = isqrt_64((int64_t)isqrt_64((int64_t)target));
    while ((__int128)(r_max + 1) * (r_max + 1) * (r_max + 1) * (r_max + 1) <= target) r_max++;
    while ((__int128)r_max * r_max * r_max * r_max > target) r_max--;
    
    int64_t m_max = isqrt_64(r_max);
    
    uint64_t total = 0;
    
    for (int64_t m = 1; m <= m_max; ++m) {
        int64_t mm = m * m;
        int64_t n_max = isqrt_64(r_max - mm);
        int64_t n_start = (m & 1) ? 0 : 1;
        
        for (int64_t n = n_start; n <= n_max; n += 2) {
            if (gcd((int)m, (int)n) != 1) continue;
            
            int64_t nn = n * n;
            int64_t r = mm + nn;
            
            int64_t u = mm - nn;
            int64_t v = 2 * m * n;
            
            int64_t a = 3 * u - 2 * v;
            if (a < 0) a = -a;
            int64_t b = 3 * v + 2 * u;
            if (b < 0) b = -b;
            
            int64_t p = (a < b) ? b : a;
            int64_t q = (a < b) ? a : b;
            
            if (p % 13 == 0 && q % 13 == 0) continue;
            
            __int128 x = (__int128)q * r;
            __int128 y = (__int128)p * r;
            if (x > N || y > N) continue;
            __int128 z = (__int128)p * q;
            if (z > N) continue;
            
            __int128 s = x + y + z;
            if (mod > 0) {
                total = (total + (uint64_t)(s % mod)) % mod;
            } else {
                total += (uint64_t)s;
            }
        }
    }
    return (int64_t)total;
}
