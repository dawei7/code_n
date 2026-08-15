#include <math.h>
#include <stdlib.h>
#include <stdio.h>

#define PI 3.14159265358979323846

static inline double H(int a, int b, double x) {
    return 0.5 - 0.5 / (a + b) * (b * cos(a * PI * x) + a * cos(b * PI * x));
}

typedef struct {
    double x1, x2, z1, z2;
} Branch;

static int cmp_double(const void* a, const void* b) {
    double da = *(const double*)a;
    double db = *(const double*)b;
    if (da < db) return -1;
    if (da > db) return 1;
    return 0;
}

int get_branches(int a, int b, Branch* branches) {
    static double raw_pts[5000];
    int num_pts = 0;
    raw_pts[num_pts++] = 0.0;
    
    int limit_k1 = (a + b + 1) / 2;
    for (int k = 1; k < limit_k1; ++k) {
        double x = 2.0 * k / (a + b);
        if (x > 0.0 && x < 1.0) raw_pts[num_pts++] = x;
    }
    if (b > a) {
        int limit_k2 = b - a + 1;
        for (int k = 1; k < limit_k2; ++k) {
            double x = (2.0 * k - 1.0) / (b - a);
            if (x > 0.0 && x < 1.0) raw_pts[num_pts++] = x;
        }
    }
    raw_pts[num_pts++] = 1.0;
    
    qsort(raw_pts, num_pts, sizeof(double), cmp_double);
    
    static double u_pts[5000];
    int u_cnt = 0;
    for (int i = 0; i < num_pts; ++i) {
        if (u_cnt == 0 || fabs(raw_pts[i] - u_pts[u_cnt - 1]) > 1e-11) {
            u_pts[u_cnt++] = raw_pts[i];
        }
    }
    
    static double extrema[5000];
    int ext_cnt = 0;
    extrema[ext_cnt++] = u_pts[0];
    for (int i = 1; i < u_cnt - 1; ++i) {
        double z_prev = H(a, b, u_pts[i - 1]);
        double z_curr = H(a, b, u_pts[i]);
        double z_next = H(a, b, u_pts[i + 1]);
        if ((z_curr - z_prev) * (z_next - z_curr) < -1e-12) {
            extrema[ext_cnt++] = u_pts[i];
        }
    }
    extrema[ext_cnt++] = u_pts[u_cnt - 1];
    
    int num_b = 0;
    for (int i = 0; i < ext_cnt - 1; ++i) {
        branches[num_b].x1 = extrema[i];
        branches[num_b].x2 = extrema[i + 1];
        branches[num_b].z1 = H(a, b, extrema[i]);
        branches[num_b].z2 = H(a, b, extrema[i + 1]);
        num_b++;
    }
    return num_b;
}

double trace_F(int a, int b, int c, int d) {
    static Branch b_x[5000];
    static Branch b_y[5000];
    int nb_x = get_branches(a, b, b_x);
    int nb_y = get_branches(c, d, b_y);
    
    int ix = 0, iy = 0;
    double cur_z = 0.0;
    double total_variation = 0.0;
    int dir_z = 1;
    
    for (int step = 0; step < 500000; ++step) {
        double zx1 = b_x[ix].z1, zx2 = b_x[ix].z2;
        double zy1 = b_y[iy].z1, zy2 = b_y[iy].z2;
        
        if (dir_z == 1) {
            double lim_x = (zx1 > zx2) ? zx1 : zx2;
            double lim_y = (zy1 > zy2) ? zy1 : zy2;
            double next_z = (lim_x < lim_y) ? lim_x : lim_y;
            total_variation += (next_z - cur_z);
            cur_z = next_z;
            
            if (fabs(cur_z - 1.0) < 1e-9 && ix == nb_x - 1 && iy == nb_y - 1) {
                break;
            }
            
            if (fabs(lim_x - next_z) < 1e-9) {
                if (zx2 >= zx1) ix++; else ix--;
                dir_z = -1;
            } else {
                if (zy2 >= zy1) iy++; else iy--;
                dir_z = -1;
            }
        } else {
            double lim_x = (zx1 < zx2) ? zx1 : zx2;
            double lim_y = (zy1 < zy2) ? zy1 : zy2;
            double next_z = (lim_x > lim_y) ? lim_x : lim_y;
            total_variation += (cur_z - next_z);
            cur_z = next_z;
            
            if (fabs(lim_x - next_z) < 1e-9) {
                if (zx1 <= zx2) ix--; else ix++;
                dir_z = 1;
            } else {
                if (zy1 <= zy2) iy--; else iy++;
                dir_z = 1;
            }
        }
    }
    return total_variation;
}

double compute_G(int m, int n) {
    int primes[300];
    int p_cnt = 0;
    for (int p = m; p <= n; ++p) {
        int is_p = 1;
        if (p < 2) is_p = 0;
        for (int d = 2; d * d <= p; ++d) {
            if (p % d == 0) { is_p = 0; break; }
        }
        if (is_p) primes[p_cnt++] = p;
    }
    
    double total = 0.0;
    for (int i = 0; i < p_cnt; ++i) {
        for (int j = i + 1; j < p_cnt; ++j) {
            int p = primes[i];
            int q = primes[j];
            total += trace_F(p, q, p, 2 * q - p);
        }
    }
    return total;
}
