#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

EXPORT double compute_P(int R, int B) {
    int max_r = R / 2;
    int max_b = B;

    // dp[b] represents P(2*r, b)
    double* dp_prev = (double*)malloc((max_b + 1) * sizeof(double));
    double* dp_curr = (double*)malloc((max_b + 1) * sizeof(double));

    // Base case r = 0: R = 0, B > 0 -> P(0, b) = 1.0 for all b >= 1
    dp_prev[0] = 0.0;
    for (int b = 1; b <= max_b; b++) {
        dp_prev[b] = 1.0;
    }

    for (int r = 1; r <= max_r; r++) {
        int R_val = 2 * r;
        double r_minus_1 = (double)(R_val - 1);

        dp_curr[0] = 0.0; // P(2r, 0) = 0.0

        for (int b = 1; b <= max_b; b++) {
            double two_b = (double)(2 * b);
            double denom = r_minus_1 + two_b;
            double p_r = r_minus_1 / denom;
            double p_b = two_b / denom;

            dp_curr[b] = p_r * dp_prev[b] + p_b * dp_curr[b - 1];
        }

        // Swap buffers
        double* tmp = dp_prev;
        dp_prev = dp_curr;
        dp_curr = tmp;
    }

    double ans = dp_prev[max_b];

    free(dp_prev);
    free(dp_curr);

    return ans;
}
