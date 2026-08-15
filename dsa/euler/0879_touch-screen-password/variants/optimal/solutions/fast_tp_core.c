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

static int gcd(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a < 0 ? -a : a;
}

EXPORT int64_t compute_4x4_passwords(void) {
    int rows = 4, cols = 4;
    int N = rows * cols; // 16

    int between[16][16];
    for (int u = 0; u < N; u++) {
        int r1 = u / cols, c1 = u % cols;
        for (int v = 0; v < N; v++) {
            between[u][v] = 0;
            if (u == v) continue;
            int r2 = v / cols, c2 = v % cols;
            int dr = r2 - r1, dc = c2 - c1;
            int g = gcd(abs(dr), abs(dc));
            int step_r = dr / g, step_c = dc / g;
            int mask = 0;
            for (int s = 1; s < g; s++) {
                int mr = r1 + s * step_r;
                int mc = c1 + s * step_c;
                mask |= (1 << (mr * cols + mc));
            }
            between[u][v] = mask;
        }
    }

    // dp[mask][u]: 65536 * 16
    int64_t (*dp)[16] = (int64_t (*)[16])calloc(1 << N, sizeof(int64_t) * 16);

    for (int u = 0; u < N; u++) {
        dp[1 << u][u] = 1;
    }

    int64_t total_passwords = 0;

    for (int mask = 1; mask < (1 << N); mask++) {
        for (int u = 0; u < N; u++) {
            int64_t count = dp[mask][u];
            if (count == 0) continue;

            for (int v = 0; v < N; v++) {
                if (!(mask & (1 << v))) {
                    if ((between[u][v] & mask) == between[u][v]) {
                        int nmask = mask | (1 << v);
                        dp[nmask][v] += count;
                        total_passwords += count;
                    }
                }
            }
        }
    }

    free(dp);
    return total_passwords;
}
