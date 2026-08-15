
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000000000000000ULL

uint64_t solve_c(int64_t limit) {
    int64_t* f = (int64_t*)malloc((limit + 1) * sizeof(int64_t));
    int64_t* maxelem = (int64_t*)calloc(limit + 1, sizeof(int64_t));
    
    for (int64_t x = 0; x <= limit; ++x) {
        f[x] = 4 * x * x + 1;
    }
    
    for (int64_t x = 1; x <= limit; ++x) {
        int64_t div = f[x];
        if (div > 1) {
            int64_t curr1 = x % div;
            while (curr1 <= limit) {
                if (f[curr1] % div == 0) {
                    if (div > maxelem[curr1]) maxelem[curr1] = div;
                    while (f[curr1] % div == 0) {
                        f[curr1] /= div;
                    }
                }
                curr1 += div;
            }
            
            int64_t curr2 = (div - (x % div)) % div;
            while (curr2 <= limit) {
                if (f[curr2] % div == 0) {
                    if (div > maxelem[curr2]) maxelem[curr2] = div;
                    while (f[curr2] % div == 0) {
                        f[curr2] /= div;
                    }
                }
                curr2 += div;
            }
        }
    }
    
    uint64_t total = 0;
    for (int64_t x = 1; x <= limit; ++x) {
        total = (total + (uint64_t)maxelem[x]) % MOD;
    }
    
    free(f);
    free(maxelem);
    return total;
}
