
#include <stdint.h>
#include <stdlib.h>

int64_t solve_c(int64_t N) {
    int64_t total = 0;
    for (int64_t k = 1; k < N; ++k) {
        int64_t q = N / k;
        int64_t r = N % k;
        int64_t intra = r * (q + 1) * q / 2 + (k - r) * q * (q - 1) / 2;
        total += intra;
    }
    return total;
}
