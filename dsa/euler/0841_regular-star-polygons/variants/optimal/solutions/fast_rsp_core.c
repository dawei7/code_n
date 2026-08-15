#include <stdio.h>
#include <stdlib.h>
#include <quadmath.h>

__float128 compute_A(long long p, long long q) {
    __float128 pi = strtoflt128("3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117068", NULL);
    __float128 alpha = pi / (__float128)p;
    __float128 sum = 0.0Q;
    int cur_sign = ((q - 1) % 2 == 0) ? 1 : -1;
    for (long long j = 1; j < q; j++) {
        __float128 term = tanq((__float128)j * alpha);
        if (cur_sign > 0) sum += term;
        else sum -= term;
        cur_sign = -cur_sign;
    }
    __float128 total = tanq((__float128)q * alpha) + 2.0Q * sum;
    return (__float128)p * total;
}

double solve_841(int n_min, int n_max) {
    long long F[40];
    F[1] = 1;
    F[2] = 1;
    for (int i = 3; i <= 38; i++) {
        F[i] = F[i-1] + F[i-2];
    }
    
    __float128 total_sum = 0.0Q;
    for (int n = n_min; n <= n_max; n++) {
        long long p = F[n + 1];
        long long q = F[n - 1];
        total_sum += compute_A(p, q);
    }
    
    return (double)total_sum;
}

void solve_841_str(int n_min, int n_max, char* out_buf, int buf_size) {
    long long F[40];
    F[1] = 1;
    F[2] = 1;
    for (int i = 3; i <= 38; i++) {
        F[i] = F[i-1] + F[i-2];
    }
    
    __float128 total_sum = 0.0Q;
    for (int n = n_min; n <= n_max; n++) {
        long long p = F[n + 1];
        long long q = F[n - 1];
        total_sum += compute_A(p, q);
    }
    
    quadmath_snprintf(out_buf, buf_size, "%.10Qf", total_sum);
}
