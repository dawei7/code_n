#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>

#define MOD 1000000007LL

static int64_t FACT[100];
static int64_t POW2[100];
static int64_t C_TABLE[100][100];
static int initialized = 0;

static void init_tables() {
    if (initialized) return;
    FACT[0] = POW2[0] = 1;
    for (int i = 1; i < 100; i++) {
        FACT[i] = (FACT[i-1] * i) % MOD;
        POW2[i] = (POW2[i-1] * 2) % MOD;
    }
    for (int i = 0; i < 100; i++) {
        C_TABLE[i][0] = 1;
        for (int j = 1; j <= i; j++) {
            C_TABLE[i][j] = (C_TABLE[i-1][j-1] + C_TABLE[i-1][j]) % MOD;
        }
    }
    initialized = 1;
}

static int64_t H(int n, int j) {
    if (n - j - 1 < 0) return 0;
    return (FACT[n - j - 1] * POW2[j - 1]) % MOD;
}

static int64_t N_nk(int n, int k) {
    int64_t res = 0;
    for (int j = 2; j <= k; j++) {
        int64_t c = C_TABLE[k][j];
        int64_t term = ((j - 1) * c) % MOD * H(n, j) % MOD;
        if ((j - 2) % 2 == 1) {
            res = (res - term + MOD) % MOD;
        } else {
            res = (res + term) % MOD;
        }
    }
    return res;
}

typedef struct {
    double x, y;
    int orig_idx;
} Point;

typedef struct {
    int u, v;
} Chord;

static int pt_x_cmp(const void* a, const void* b) {
    const Point* p1 = (const Point*)a;
    const Point* p2 = (const Point*)b;
    if (p1->x < p2->x) return -1;
    if (p1->x > p2->x) return 1;
    return 0;
}

static int parent_arr[600000];
static int size_arr[600000];

static int find_set(int v) {
    if (v == parent_arr[v]) return v;
    return parent_arr[v] = find_set(parent_arr[v]);
}

static void union_sets(int a, int b) {
    a = find_set(a);
    b = find_set(b);
    if (a != b) {
        if (size_arr[a] < size_arr[b]) {
            int t = a; a = b; b = t;
        }
        parent_arr[b] = a;
        size_arr[a] += size_arr[b];
    }
}

int64_t compute_T(int n) {
    if (n < 4) return 0;
    init_tables();
    double PI = 3.14159265358979323846;
    double* cos_w = (double*)malloc(n * sizeof(double));
    double* sin_w = (double*)malloc(n * sizeof(double));
    for (int i = 0; i < n; i++) {
        cos_w[i] = cos(2.0 * PI * i / n);
        sin_w[i] = sin(2.0 * PI * i / n);
    }

    int num_chords = n * (n - 1) / 2;
    Chord* chords = (Chord*)malloc(num_chords * sizeof(Chord));
    int chord_idx = 0;
    for (int u = 0; u < n; u++) {
        for (int v = u + 1; v < n; v++) {
            chords[chord_idx].u = u;
            chords[chord_idx].v = v;
            chord_idx++;
        }
    }

    int max_pts = 600000;
    Point* pts = (Point*)malloc(max_pts * sizeof(Point));
    int num_pts = 0;

    for (int i = 0; i < num_chords; i++) {
        int u1 = chords[i].u, v1 = chords[i].v;
        double w1x = cos_w[u1], w1y = sin_w[u1];
        double w2x = cos_w[v1], w2y = sin_w[v1];
        double p1x = w1x * w2x - w1y * w2y;
        double p1y = w1x * w2y + w1y * w2x;
        double s1x = w1x + w2x;
        double s1y = w1y + w2y;

        for (int j = i + 1; j < num_chords; j++) {
            int u2 = chords[j].u, v2 = chords[j].v;
            if (u1 == u2 || u1 == v2 || v1 == u2 || v1 == v2) continue;
            int in1 = (u1 < u2 && u2 < v1);
            int in2 = (u1 < v2 && v2 < v1);
            if (in1 == in2) continue;

            double w3x = cos_w[u2], w3y = sin_w[u2];
            double w4x = cos_w[v2], w4y = sin_w[v2];
            double p2x = w3x * w4x - w3y * w4y;
            double p2y = w3x * w4y + w3y * w4x;
            double s2x = w3x + w4x;
            double s2y = w3y + w4y;

            double dx = p1x - p2x;
            double dy = p1y - p2y;
            double denom_sq = dx * dx + dy * dy;
            if (denom_sq < 1e-24) continue;

            double numx = (p1x * s2x - p1y * s2y) - (p2x * s1x - p2y * s1y);
            double numy = (p1x * s2y + p1y * s2x) - (p2x * s1y + p2y * s1x);
            double zx = (numx * dx + numy * dy) / denom_sq;
            double zy = (numy * dx - numx * dy) / denom_sq;

            pts[num_pts].x = zx;
            pts[num_pts].y = zy;
            pts[num_pts].orig_idx = num_pts;
            num_pts++;
        }
    }

    for (int i = 0; i < num_pts; i++) {
        parent_arr[i] = i;
        size_arr[i] = 1;
    }

    qsort(pts, num_pts, sizeof(Point), pt_x_cmp);

    double eps = 1e-7;
    double eps_sq = eps * eps;

    for (int i = 0; i < num_pts; i++) {
        for (int j = i + 1; j < num_pts; j++) {
            if (pts[j].x - pts[i].x > eps) break;
            double dy = pts[j].y - pts[i].y;
            if (dy > eps || dy < -eps) continue;
            double d_sq = (pts[j].x - pts[i].x) * (pts[j].x - pts[i].x) + dy * dy;
            if (d_sq < eps_sq) {
                union_sets(pts[i].orig_idx, pts[j].orig_idx);
            }
        }
    }

    int64_t total_T = 0;
    for (int i = 0; i < num_pts; i++) {
        if (parent_arr[i] == i) {
            int C = size_arr[i];
            int k = (int)round((1.0 + sqrt(1.0 + 8.0 * C)) / 2.0);
            total_T = (total_T + N_nk(n, k)) % MOD;
        }
    }

    free(cos_w);
    free(sin_w);
    free(chords);
    free(pts);
    return total_T;
}

int64_t solve_842(int n_min, int n_max) {
    init_tables();
    int64_t sum = 0;
    for (int n = n_min; n <= n_max; n++) {
        sum = (sum + compute_T(n)) % MOD;
    }
    return sum;
}
