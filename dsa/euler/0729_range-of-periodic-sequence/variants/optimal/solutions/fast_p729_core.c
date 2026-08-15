
#include <stdint.h>
#include <stdlib.h>
#include <math.h>

static int a[30];
static double total_sum;
static int cur_n;

static inline void handle_one_necklace() {
    double x = 0.0;
    for (int iter = 0; iter < 4; ++iter) {
        double y = x;
        double dy = 1.0;
        for (int i = 1; i <= cur_n; ++i) {
            double s = sqrt(y * y + 4.0);
            if (a[i] == 0) {
                dy *= 0.5 * (1.0 + y / s);
                y = 0.5 * (y + s);
            } else {
                dy *= 0.5 * (1.0 - y / s);
                y = 0.5 * (y - s);
            }
        }
        double next_x = x - (y - x) / (dy - 1.0);
        if (fabs(next_x - x) <= 1e-15 * (1.0 + fabs(next_x))) {
            x = next_x;
            break;
        }
        x = next_x;
    }
    
    double y = x;
    double mn = y;
    double mx = y;
    for (int i = 1; i < cur_n; ++i) {
        double s = sqrt(y * y + 4.0);
        if (a[i] == 0) {
            y = 0.5 * (y + s);
        } else {
            y = 0.5 * (y - s);
        }
        if (y < mn) mn = y;
        if (y > mx) mx = y;
    }
    total_sum += cur_n * (mx - mn);
}

static void rec(int t, int p) {
    if (t > cur_n) {
        if (p == cur_n) {
            handle_one_necklace();
        }
        return;
    }
    a[t] = a[t - p];
    rec(t + 1, p);
    if (a[t - p] == 0) {
        a[t] = 1;
        rec(t + 1, t);
    }
}

double solve_c(int P) {
    total_sum = 0.0;
    for (int n = 2; n <= P; ++n) {
        cur_n = n;
        rec(1, 1);
    }
    return total_sum;
}
