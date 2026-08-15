
#include <stdint.h>
#include <stdlib.h>

static inline int dsu_find(int* parent, int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

static inline void dsu_mark(int* parent, int x) {
    if (parent[x] == x) {
        parent[x] = dsu_find(parent, x + 1);
    }
}

int64_t solve_c(int64_t M) {
    int64_t half = M / 2;
    int max_coord = (int)(M * 1.25) + 100;
    
    int* coord_parent = (int*)malloc((max_coord + 2) * sizeof(int));
    int* diff_parent = (int*)malloc((max_coord + 2) * sizeof(int));
    for (int i = 0; i <= max_coord + 1; ++i) {
        coord_parent[i] = i;
        diff_parent[i] = i;
    }
    
    int v_min = -2 * max_coord;
    int v_offset = -v_min;
    int v_len = 3 * max_coord + 1;
    int* v_parent = (int*)malloc((v_len + 2) * sizeof(int));
    for (int i = 0; i <= v_len + 1; ++i) {
        v_parent[i] = i;
    }
    
    dsu_mark(coord_parent, 0);
    dsu_mark(diff_parent, 0);
    dsu_mark(v_parent, 0 + v_offset);
    
    int64_t total = 0;
    int a = 1;
    
    while (1) {
        a = dsu_find(coord_parent, a);
        if (a > half) break;
        
        int b = a + 1;
        int d = 0, v1 = 0, v2 = 0;
        
        while (1) {
            b = dsu_find(coord_parent, b);
            
            d = b - a;
            if (diff_parent[d] != d) {
                int nd = dsu_find(diff_parent, d);
                b = a + nd;
                continue;
            }
            
            v1 = b - 2 * a;
            int i1 = v1 + v_offset;
            if (v_parent[i1] != i1) {
                int ni = dsu_find(v_parent, i1);
                int next_v = ni - v_offset;
                b = 2 * a + next_v;
                continue;
            }
            
            v2 = a - 2 * b;
            int i2 = v2 + v_offset;
            if (v_parent[i2] != i2) {
                b++;
                continue;
            }
            
            break;
        }
        
        dsu_mark(coord_parent, a);
        dsu_mark(coord_parent, b);
        dsu_mark(diff_parent, d);
        dsu_mark(v_parent, v1 + v_offset);
        dsu_mark(v_parent, v2 + v_offset);
        
        if (a + b <= M) {
            total += (int64_t)(a + b);
        }
    }
    
    free(coord_parent);
    free(diff_parent);
    free(v_parent);
    return total;
}
