
#include <stdint.h>
#include <stdlib.h>

int gcd(int a, int b) {
    if (a < 0) a = -a;
    if (b < 0) b = -b;
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

typedef struct {
    int dx;
    int dy;
    int64_t c;
} Line;

int cmp_lines(const void* a, const void* b) {
    const Line* la = (const Line*)a;
    const Line* lb = (const Line*)b;
    if (la->dx != lb->dx) return la->dx - lb->dx;
    if (la->dy != lb->dy) return la->dy - lb->dy;
    if (la->c < lb->c) return -1;
    if (la->c > lb->c) return 1;
    return 0;
}

int64_t solve_c(int num_points) {
    int* px = (int*)malloc(num_points * sizeof(int));
    int* py = (int*)malloc(num_points * sizeof(int));
    
    int64_t s = 290797;
    int64_t mod_bbs = 50515093;
    for (int i = 0; i < num_points; ++i) {
        s = (s * s) % mod_bbs;
        px[i] = (int)(s % 2000) - 1000;
        s = (s * s) % mod_bbs;
        py[i] = (int)(s % 2000) - 1000;
    }
    
    int64_t total_pairs = (int64_t)num_points * (num_points - 1) / 2;
    Line* lines = (Line*)malloc(total_pairs * sizeof(Line));
    
    int64_t idx = 0;
    for (int i = 0; i < num_points; ++i) {
        int x1 = px[i];
        int y1 = py[i];
        for (int j = i + 1; j < num_points; ++j) {
            int dx = px[j] - x1;
            int dy = py[j] - y1;
            int g = gcd(dx, dy);
            dx /= g;
            dy /= g;
            if (dx < 0 || (dx == 0 && dy < 0)) {
                dx = -dx;
                dy = -dy;
            }
            int a = -dy;
            int b = dx;
            int64_t c = -((int64_t)a * x1 + (int64_t)b * y1);
            lines[idx].dx = dx;
            lines[idx].dy = dy;
            lines[idx].c = c;
            idx++;
        }
    }
    
    qsort(lines, total_pairs, sizeof(Line), cmp_lines);
    
    int64_t total_m = 0;
    int* slope_counts = (int*)malloc(total_pairs * sizeof(int));
    int num_slopes = 0;
    
    int current_slope_count = 0;
    for (int64_t i = 0; i < total_pairs; ++i) {
        if (i == 0 || lines[i].dx != lines[i-1].dx || lines[i].dy != lines[i-1].dy || lines[i].c != lines[i-1].c) {
            total_m++;
            if (i > 0 && (lines[i].dx != lines[i-1].dx || lines[i].dy != lines[i-1].dy)) {
                slope_counts[num_slopes++] = current_slope_count;
                current_slope_count = 0;
            }
            current_slope_count++;
        }
    }
    if (current_slope_count > 0) {
        slope_counts[num_slopes++] = current_slope_count;
    }
    
    int64_t total_s = 0;
    for (int i = 0; i < num_slopes; ++i) {
        int64_t cnt = slope_counts[i];
        total_s += cnt * (total_m - cnt);
    }
    
    free(px);
    free(py);
    free(lines);
    free(slope_counts);
    return total_s;
}
