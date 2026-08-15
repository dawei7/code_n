
#include <stdint.h>
#include <stdlib.h>
#include <math.h>

double solve_bob_c() {
    int N = 12;
    int num_states = 1 << N;
    int target = num_states - 1;
    
    double* V = (double*)calloc(num_states, sizeof(double));
    double* V_new = (double*)calloc(num_states, sizeof(double));
    
    int rolls_x[36];
    int rolls_y[36];
    int idx = 0;
    for (int x = 1; x <= 6; ++x) {
        for (int y = 1; y <= 6; ++y) {
            rolls_x[idx] = x;
            rolls_y[idx] = y;
            idx++;
        }
    }
    
    for (int it = 0; it < 20000; ++it) {
        double max_diff = 0.0;
        for (int s = 0; s < num_states; ++s) {
            if (s == target) {
                V_new[s] = 0.0;
                continue;
            }
            double sum_min = 0.0;
            for (int r = 0; r < 36; ++r) {
                int x = rolls_x[r];
                int y = rolls_y[r];
                double v1 = V[s ^ (1 << (x - 1))];
                double v2 = V[s ^ (1 << (y - 1))];
                double v3 = V[s ^ (1 << (x + y - 1))];
                double best = v1 < v2 ? (v1 < v3 ? v1 : v3) : (v2 < v3 ? v2 : v3);
                sum_min += best;
            }
            V_new[s] = 1.0 + sum_min / 36.0;
            double diff = fabs(V_new[s] - V[s]);
            if (diff > max_diff) max_diff = diff;
        }
        
        for (int s = 0; s < num_states; ++s) {
            V[s] = V_new[s];
        }
        
        if (max_diff < 1e-13) {
            break;
        }
    }
    
    double ans = V[0];
    free(V);
    free(V_new);
    return ans;
}
