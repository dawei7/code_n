
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>

#define MOD 1000000000ULL

static int offset[200];
static int lens[200];
static uint32_t *u[200];
static uint32_t *v[200];
static uint64_t f0[20000];
static uint64_t a2[20000];

int64_t solve_c(int M) {
    int n_tmp = 0;
    while ((n_tmp + 1) * (n_tmp + 2) / 2 <= M) n_tmp++;
    int max_n = n_tmp - 1;
    int N = max_n + 3;
    
    for (int n = 0; n <= N + 1; ++n) {
        int off = (n + 1) * (n + 2) / 2;
        offset[n] = off;
        int ln = M - off + 1;
        lens[n] = (ln > 0) ? ln : 0;
    }
    
    for (int n = 1; n <= N + 1; ++n) {
        int ln = lens[n];
        if (ln > 0) {
            u[n] = (uint32_t *)calloc(n * ln, sizeof(uint32_t));
            v[n] = (uint32_t *)calloc(n * ln, sizeof(uint32_t));
        } else {
            u[n] = NULL;
            v[n] = NULL;
        }
    }
    
    for (int m = 0; m <= M; ++m) {
        f0[m] = 0;
        a2[m] = 0;
    }
    a2[0] = 1;
    
    int n_active = 0;
    for (int m = 0; m <= M; ++m) {
        while (n_active + 1 < N + 1 && offset[n_active + 1] <= m) {
            n_active++;
        }
        
        for (int n = 1; n <= n_active; ++n) {
            int off = offset[n];
            int ln = lens[n];
            int idx_cur = m - off;
            
            int mp1 = m - n - 2;
            int idx1 = mp1 - off;
            
            int mp2 = m - n - 3;
            int idx2 = mp2 - offset[n + 1];
            int lnp = lens[n + 1];
            
            int mp3 = m - n - 1;
            int idx3 = mp3 - offset[n - 1];
            int lnm = lens[n - 1];
            
            if (n == 1) {
                uint64_t val_u = 0;
                if (idx1 >= 0) val_u += 2 * u[1][idx1] + v[1][idx1];
                if (idx2 >= 0 && lnp > 0) val_u += v[2][idx2] + u[2][lnp + idx2];
                if (mp3 >= 0) val_u += f0[mp3];
                u[1][idx_cur] = (uint32_t)(val_u % MOD);
                
                uint64_t val_v = 0;
                if (idx1 >= 0) val_v += 2 * v[1][idx1] + 2 * u[1][idx1];
                if (idx2 >= 0 && lnp > 0) val_v += v[2][lnp + idx2] + 2 * u[2][idx2];
                if (mp3 >= 0) val_v += f0[mp3];
                v[1][idx_cur] = (uint32_t)(val_v % MOD);
                continue;
            }
            
            uint32_t *u_n = u[n];
            uint32_t *v_n = v[n];
            uint32_t *u_p = u[n + 1];
            uint32_t *v_p = v[n + 1];
            uint32_t *u_m = u[n - 1];
            uint32_t *v_m = v[n - 1];
            
            uint32_t u_n1 = (idx1 >= 0) ? u_n[idx1] : 0;
            uint32_t v_n1 = (idx1 >= 0) ? v_n[idx1] : 0;
            uint32_t u_p1 = (idx2 >= 0 && lnp > 0) ? u_p[idx2] : 0;
            uint32_t v_p1 = (idx2 >= 0 && lnp > 0) ? v_p[idx2] : 0;
            
            int base = 0;
            int base_next = ln;
            int base_p = lnp;
            int base_m = 0;
            
            if (idx1 < 0) {
                for (int k = 1; k < n; ++k) {
                    u_n[base + idx_cur] = u_m[base_m + idx3];
                    v_n[base + idx_cur] = v_m[base_m + idx3];
                    base = base_next;
                    base_next += ln;
                    base_m += lnm;
                }
                u_n[(n - 1) * ln + idx_cur] = u_m[(n - 2) * lnm + idx3];
                v_n[(n - 1) * ln + idx_cur] = v_m[(n - 2) * lnm + idx3];
                continue;
            }
            
            if (idx2 >= 0 && lnp > 0) {
                for (int k = 1; k < n; ++k) {
                    u_n[base + idx_cur] = (uint32_t)(((uint64_t)u_n[base + idx1] + v_p1 + u_p[base_p + idx2] + u_m[base_m + idx3] + v_n1 + u_n[base_next + idx1]) % MOD);
                    v_n[base + idx_cur] = (uint32_t)(((uint64_t)v_n[base + idx1] + v_p[base_p + idx2] + u_p1 + v_m[base_m + idx3] + v_n[base_next + idx1] + u_n1) % MOD);
                    base = base_next;
                    base_next += ln;
                    base_p += lnp;
                    base_m += lnm;
                }
                int base_last = (n - 1) * ln;
                u_n[base_last + idx_cur] = (uint32_t)(((uint64_t)2 * u_n[base_last + idx1] + v_n1 + v_p1 + u_p[base_p + idx2] + u_m[(n - 2) * lnm + idx3]) % MOD);
                v_n[base_last + idx_cur] = (uint32_t)(((uint64_t)2 * v_n[base_last + idx1] + 2ULL * u_n1 + v_p[base_p + idx2] + 2ULL * u_p1 + v_m[(n - 2) * lnm + idx3]) % MOD);
            } else {
                for (int k = 1; k < n; ++k) {
                    u_n[base + idx_cur] = (uint32_t)(((uint64_t)u_n[base + idx1] + u_m[base_m + idx3] + v_n1 + u_n[base_next + idx1]) % MOD);
                    v_n[base + idx_cur] = (uint32_t)(((uint64_t)v_n[base + idx1] + v_m[base_m + idx3] + v_n[base_next + idx1] + u_n1) % MOD);
                    base = base_next;
                    base_next += ln;
                    base_m += lnm;
                }
                int base_last = (n - 1) * ln;
                u_n[base_last + idx_cur] = (uint32_t)(((uint64_t)2 * u_n[base_last + idx1] + v_n1 + u_m[(n - 2) * lnm + idx3]) % MOD);
                v_n[base_last + idx_cur] = (uint32_t)(((uint64_t)2 * v_n[base_last + idx1] + 2ULL * u_n1 + v_m[(n - 2) * lnm + idx3]) % MOD);
            }
        }
        
        uint64_t val_f = 0;
        if (m - 1 >= 0) val_f += a2[m - 1];
        if (m - 2 >= 0) val_f += 4 * f0[m - 2];
        int mp = m - 3;
        if (mp >= offset[1] && lens[1] > 0) {
            int id1 = mp - offset[1];
            val_f += 2 * u[1][id1] + v[1][id1];
        }
        f0[m] = val_f % MOD;
        
        if (m >= 1) {
            uint64_t val_a = 3 * a2[m - 1];
            if (m - 2 >= 0) val_a += 3 * f0[m - 2];
            a2[m] = val_a % MOD;
        }
    }
    
    int64_t ans = a2[M];
    
    for (int n = 1; n <= N + 1; ++n) {
        if (u[n]) free(u[n]);
        if (v[n]) free(v[n]);
    }
    
    return ans;
}
