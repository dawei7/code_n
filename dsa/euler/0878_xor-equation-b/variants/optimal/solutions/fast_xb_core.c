#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

static inline uint64_t xor_mul(uint64_t a, uint64_t b) {
    uint64_t res = 0;
    while (b > 0) {
        if (b & 1) res ^= a;
        a <<= 1;
        b >>= 1;
    }
    return res;
}

EXPORT int64_t compute_G(uint64_t N, uint64_t M) {
    int max_lim = 2048;
    int64_t total_solutions = 0;

    for (uint64_t b0 = 0; b0 < max_lim; b0++) {
        for (uint64_t a0 = 0; a0 <= b0; a0++) {
            uint64_t prev_b = (a0 << 1) ^ b0;
            if (a0 > 0 && prev_b <= a0) continue;

            uint64_t k = xor_mul(a0, a0) ^ (xor_mul(a0, b0) << 1) ^ xor_mul(b0, b0);
            if (k <= M) {
                if (a0 == 0 && b0 == 0) {
                    total_solutions++;
                    continue;
                }
                uint64_t b_prev = a0;
                uint64_t b_curr = b0;
                while (b_curr <= N) {
                    if (b_curr >= b_prev) {
                        total_solutions++;
                    }
                    uint64_t b_next = (b_curr << 1) ^ b_prev;
                    if (b_next <= b_curr) break;
                    b_prev = b_curr;
                    b_curr = b_next;
                }
            }
        }
    }
    return total_solutions;
}
