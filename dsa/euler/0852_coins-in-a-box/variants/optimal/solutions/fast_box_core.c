#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MAX_FLIPS 200

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

static double J[MAX_FLIPS + 2][MAX_FLIPS + 2];
static double p34[MAX_FLIPS + 2];
static double p14[MAX_FLIPS + 2];
static double p12[2 * MAX_FLIPS + 4];

static void init_powers() {
    p34[0] = 1.0;
    p14[0] = 1.0;
    for (int i = 1; i <= MAX_FLIPS; i++) {
        p34[i] = p34[i - 1] * 0.75;
        p14[i] = p14[i - 1] * 0.25;
    }
    p12[0] = 1.0;
    for (int i = 1; i <= 2 * MAX_FLIPS; i++) {
        p12[i] = p12[i - 1] * 0.5;
    }
}

static double compute_W(int u, int f) {
    if (u == 0 || f == 0) return 20.0;

    for (int total = MAX_FLIPS; total >= 0; total--) {
        for (int h = 0; h <= total; h++) {
            int t = total - h;
            double A = (double)u * p34[h] * p14[t];
            double B = (double)f * p12[h + t];
            double stop_val = (20.0 * A - 50.0 * B > 20.0 * B - 50.0 * A) ? (20.0 * A - 50.0 * B) : (20.0 * B - 50.0 * A);

            if (total == MAX_FLIPS) {
                J[h][t] = stop_val;
            } else {
                double cont_val = -(A + B) + J[h + 1][t] + J[h][t + 1];
                J[h][t] = (stop_val > cont_val) ? stop_val : cont_val;
            }
        }
    }
    return J[0][0] / (double)(u + f);
}

EXPORT double compute_expected_score(int N) {
    init_powers();
    double** V = (double**)malloc((N + 1) * sizeof(double*));
    for (int i = 0; i <= N; i++) {
        V[i] = (double*)calloc(N + 1, sizeof(double));
    }

    for (int total = 0; total <= 2 * N; total++) {
        for (int u = 0; u <= total; u++) {
            int f = total - u;
            if (u > N || f > N) continue;
            if (u == 0 && f == 0) {
                V[u][f] = 0.0;
                continue;
            }

            double w = compute_W(u, f);
            double future = 0.0;
            if (u > 0) future += (double)u * V[u - 1][f];
            if (f > 0) future += (double)f * V[u][f - 1];
            future /= (double)(u + f);
            V[u][f] = w + future;
        }
    }

    double ans = V[N][N];
    for (int i = 0; i <= N; i++) free(V[i]);
    free(V);
    return ans;
}
