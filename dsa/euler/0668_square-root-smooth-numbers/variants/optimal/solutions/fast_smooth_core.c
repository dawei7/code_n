
#include <stdint.h>
#include <stdlib.h>
#include <math.h>

int64_t solve_c(int64_t N) {
    int64_t sqrtN = (int64_t)sqrt(N);
    int64_t num_vals = 2 * sqrtN;
    
    int64_t* V = (int64_t*)malloc(num_vals * sizeof(int64_t));
    int64_t* S = (int64_t*)malloc(num_vals * sizeof(int64_t));
    
    for (int64_t i = 1; i <= sqrtN; ++i) {
        V[i - 1] = N / i;
        S[i - 1] = V[i - 1] - 1;
    }
    for (int64_t i = sqrtN + 1; i <= 2 * sqrtN; ++i) {
        V[i - 1] = 2 * sqrtN - i + 1;
        S[i - 1] = V[i - 1] - 1;
    }
    
    for (int64_t p = 2; p <= sqrtN; ++p) {
        if (S[2 * sqrtN - p] > S[2 * sqrtN - (p - 1)]) {
            int64_t sp = S[2 * sqrtN - (p - 1)];
            int64_t p2 = p * p;
            
            for (int64_t i = 0; i < num_vals; ++i) {
                int64_t v = V[i];
                if (v < p2) break;
                
                int64_t div = v / p;
                int64_t idx = (div <= sqrtN) ? (2 * sqrtN - div) : (N / div - 1);
                S[i] -= (S[idx] - sp);
            }
        }
    }
    
    int64_t non_smooth = 0;
    for (int64_t k = 1; k <= sqrtN; ++k) {
        int64_t pi_Nk = S[k - 1];
        int64_t pi_k_minus_1 = (k == 1) ? 0 : S[2 * sqrtN - (k - 1)];
        non_smooth += (pi_Nk - pi_k_minus_1);
    }
    
    int64_t ans = N - non_smooth;
    free(V);
    free(S);
    return ans;
}
