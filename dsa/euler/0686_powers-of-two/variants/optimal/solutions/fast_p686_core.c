
#include <stdio.h>
#include <math.h>
#include <stdint.h>

int64_t solve_c(int64_t L, int64_t n) {
    double alpha = log10(2.0);
    double scale = pow(10.0, floor(log10((double)L)));
    double low = log10((double)L / scale);
    double high = log10(((double)L + 1.0) / scale);
    
    int64_t count = 0;
    int64_t j = 0;
    double frac = 0.0;
    
    while (count < n) {
        j++;
        frac += alpha;
        if (frac >= 1.0) frac -= 1.0;
        
        if (frac >= low && frac < high) {
            count++;
            if (count == n) return j;
        }
    }
    return j;
}
