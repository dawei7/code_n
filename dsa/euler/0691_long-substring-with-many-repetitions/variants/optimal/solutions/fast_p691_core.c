
#include <stdint.h>
#include <stdlib.h>
#include <math.h>

#define MAX_STATES 10000005

typedef struct {
    int nxt0, nxt1;
    int link;
    int maxlen;
    int occ;
} State;

static State sam[MAX_STATES];
static int order[MAX_STATES];
static int cnt_len[5000005];
static int best[5000005];

int64_t solve_c(int n) {
    sam[1].nxt0 = 0;
    sam[1].nxt1 = 0;
    sam[1].link = 0;
    sam[1].maxlen = 0;
    sam[1].occ = 0;
    
    int last = 1;
    int sz = 1;
    
    unsigned __int128 scale = (unsigned __int128)1 << 60;
    unsigned __int128 s5 = (unsigned __int128)5 * scale * scale;
    unsigned __int128 r = 0;
    for (int b = 62; b >= 0; --b) {
        unsigned __int128 cand = r | ((unsigned __int128)1 << b);
        if (cand * cand <= s5) r = cand;
    }
    unsigned __int128 inv_phi = (r - scale) / 2;
    
    unsigned __int128 acc = 0;
    uint64_t prev_floor = 0;
    
    for (int i = 0; i < n; ++i) {
        acc += inv_phi;
        uint64_t cur_floor = (uint64_t)(acc >> 60);
        int b = (int)(cur_floor - prev_floor);
        prev_floor = cur_floor;
        
        int a = __builtin_parity(i);
        int c = a ^ b;
        
        int cur = ++sz;
        sam[cur].nxt0 = 0;
        sam[cur].nxt1 = 0;
        sam[cur].link = 0;
        sam[cur].maxlen = sam[last].maxlen + 1;
        sam[cur].occ = 1;
        
        int p = last;
        if (c == 0) {
            while (p && sam[p].nxt0 == 0) {
                sam[p].nxt0 = cur;
                p = sam[p].link;
            }
            if (p == 0) {
                sam[cur].link = 1;
            } else {
                int q = sam[p].nxt0;
                if (sam[p].maxlen + 1 == sam[q].maxlen) {
                    sam[cur].link = q;
                } else {
                    int clone = ++sz;
                    sam[clone] = sam[q];
                    sam[clone].maxlen = sam[p].maxlen + 1;
                    sam[clone].occ = 0;
                    while (p && sam[p].nxt0 == q) {
                        sam[p].nxt0 = clone;
                        p = sam[p].link;
                    }
                    sam[q].link = clone;
                    sam[cur].link = clone;
                }
            }
        } else {
            while (p && sam[p].nxt1 == 0) {
                sam[p].nxt1 = cur;
                p = sam[p].link;
            }
            if (p == 0) {
                sam[cur].link = 1;
            } else {
                int q = sam[p].nxt1;
                if (sam[p].maxlen + 1 == sam[q].maxlen) {
                    sam[cur].link = q;
                } else {
                    int clone = ++sz;
                    sam[clone] = sam[q];
                    sam[clone].maxlen = sam[p].maxlen + 1;
                    sam[clone].occ = 0;
                    while (p && sam[p].nxt1 == q) {
                        sam[p].nxt1 = clone;
                        p = sam[p].link;
                    }
                    sam[q].link = clone;
                    sam[cur].link = clone;
                }
            }
        }
        last = cur;
    }
    
    for (int i = 0; i <= n; ++i) cnt_len[i] = 0;
    for (int i = 1; i <= sz; ++i) cnt_len[sam[i].maxlen]++;
    for (int i = 1; i <= n; ++i) cnt_len[i] += cnt_len[i - 1];
    for (int i = 1; i <= sz; ++i) {
        order[cnt_len[sam[i].maxlen]--] = i;
    }
    
    for (int i = sz; i >= 2; --i) {
        int u = order[i];
        sam[sam[u].link].occ += sam[u].occ;
    }
    
    for (int i = 0; i <= n; ++i) best[i] = 0;
    for (int i = 2; i <= sz; ++i) {
        int o = sam[i].occ;
        if (o <= n && sam[i].maxlen > best[o]) {
            best[o] = sam[i].maxlen;
        }
    }
    
    int cur_max = 0;
    int64_t total = 0;
    for (int k = n; k >= 1; --k) {
        if (best[k] > cur_max) cur_max = best[k];
        best[k] = cur_max;
        total += best[k];
    }
    
    return total;
}
