
#include <stdint.h>
#include <math.h>

#define MOD 1000000007LL

int64_t solve_c(int64_t N) {
    int64_t max_k = (int64_t)((sqrt(8.0 * (double)N + 1.0) - 1.0) / 2.0);
    int64_t total = 0;
    
    for (int64_t k = 1; k <= max_k; ++k) {
        int64_t Tk = k * (k + 1) / 2;
        int64_t L = N - Tk;
        if (L < 0) break;
        
        int64_t q = L / k;
        int64_t r = L % k;
        
        int64_t q_mod = q % MOD;
        int64_t k_mod = k % MOD;
        int64_t r_mod = r % MOD;
        
        int64_t term1;
        if (q % 2 == 0) {
            term1 = (k_mod * ((q / 2) % MOD)) % MOD * ((q + 1) % MOD) % MOD;
        } else {
            term1 = (k_mod * q_mod) % MOD * (((q + 1) / 2) % MOD) % MOD;
        }
        
        int64_t term2 = (r_mod + 1) % MOD * ((q_mod + 1) % MOD) % MOD;
        
        total = (total + term1 + term2) % MOD;
    }
    return total;
}
