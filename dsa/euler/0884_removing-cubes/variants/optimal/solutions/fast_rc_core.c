#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

static inline uint64_t integer_cbrt(uint64_t n) {
    if (n == 0) return 0;
    uint64_t r = (uint64_t)cbrt((double)n);
    while ((r + 1) * (r + 1) * (r + 1) <= n && (r + 1) * (r + 1) * (r + 1) > r * r * r) r++;
    while (r * r * r > n) r--;
    return r;
}

EXPORT uint64_t compute_S(uint64_t n) {
    if (n <= 1) return 0;
    uint64_t M = integer_cbrt(n);

    uint64_t* prefix = (uint64_t*)calloc(M + 2, sizeof(uint64_t));

    for (uint64_t k = 1; k <= M; k++) {
        uint64_t len = 3 * k * k + 3 * k + 1;

        // Evaluate S(len) using prefix table
        uint64_t s_val = 0;
        uint64_t curr = len;
        while (curr > 1) {
            uint64_t m = integer_cbrt(curr);
            s_val += prefix[m - 1];
            uint64_t rem = curr - m * m * m;
            if (rem == 0) break;
            s_val += rem;
            curr = rem;
        }

        prefix[k] = prefix[k - 1] + len + s_val;
    }

    uint64_t total_ans = prefix[M - 1];
    uint64_t rem = n - M * M * M;
    if (rem > 0) {
        total_ans += rem;
        uint64_t curr = rem;
        while (curr > 1) {
            uint64_t m = integer_cbrt(curr);
            total_ans += prefix[m - 1];
            uint64_t r = curr - m * m * m;
            if (r == 0) break;
            total_ans += r;
            curr = r;
        }
    }

    free(prefix);
    return total_ans;
}
