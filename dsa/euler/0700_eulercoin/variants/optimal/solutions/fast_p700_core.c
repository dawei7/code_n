
#include <stdint.h>
#include <stdlib.h>

int64_t solve_c(int64_t a, int64_t m) {
    int64_t total = 0;
    int64_t cur_min = m;
    int64_t v = 0;
    int64_t threshold = 20000000;
    
    while (1) {
        v += a;
        if (v >= m) v -= m;
        if (v < cur_min) {
            cur_min = v;
            total += v;
            if (cur_min < threshold) break;
        }
    }
    
    int64_t last_forward = cur_min;
    
    int64_t t = 0, newt = 1;
    int64_t r = m, newr = a;
    while (newr != 0) {
        int64_t q = r / newr;
        int64_t tmp = t - q * newt; t = newt; newt = tmp;
        tmp = r - q * newr; r = newr; newr = tmp;
    }
    if (t < 0) t += m;
    int64_t inv_a = t;
    
    int64_t min_n = m;
    for (int64_t val = 1; val < last_forward; ++val) {
        int64_t n_v = (int64_t)(((unsigned __int128)val * inv_a) % m);
        if (n_v < min_n) {
            min_n = n_v;
            total += val;
        }
    }
    
    return total;
}
