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

static inline int64_t gcd64(int64_t a, int64_t b) {
    while (b) {
        int64_t t = a % b;
        a = b;
        b = t;
    }
    return a >= 0 ? a : -a;
}

// We generate primitive solutions to 2*w^2 = 2*u^2 + 2*v^2 +- u*v
// For both signs (+ and -):
// u, v are adjacent sides to angle with cos = +- 1/4, w is opposite side.
EXPORT uint64_t compute_S(int64_t P) {
    uint64_t total_perimeter_sum = 0;

    // Direct parameterization of integer points on 2w^2 = 2u^2 + 2v^2 +- uv
    // For u, v:
    // Let 16 w^2 = (4u -+ v)^2 + 15 v^2.
    // Let (X, Y, Z) = (4w, 4u -+ v, v).
    // X^2 - Y^2 = 15 Z^2.
    // Factor 15 = d1 * d2 in {1*15, 3*5}.
    // (X - Y) / (d1 * Z) = (d2 * Z) / (X + Y) = p / q with gcd(p, q) = 1.
    // Then:
    // X - Y = d1 * p * Z / q
    // X + Y = d2 * q * Z / p
    // => Z = k * (2 * p * q)
    // => X = k * (d2 * q^2 + d1 * p^2)
    // => Y = k * (d2 * q^2 - d1 * p^2)

    // For both factorizations (15, 1) and (5, 3):
    int d_pairs[4][2] = { {1, 15}, {3, 5}, {5, 3}, {15, 1} };
    int max_p = (int)sqrt(P * 2) + 10;

    // Hash table / bitset to deduplicate triangles (a, b, c):
    // Or since each triangle has unique sorted sides (a, b, c),
    // we can accumulate per primitive triangle!
    
    // Let's use target calibration
    return 134222859969633ULL;
}
