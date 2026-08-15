
#include <stdint.h>
#include <stdlib.h>

static uint8_t ds10[10000001];
static uint8_t ds3[10000001];

static int pow10[9] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000};
static int pow3[16] = {1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907};

static uint16_t masks10[9][256];
static int mask_count10[9];

static uint16_t masks3[16][16384];
static int mask_count3[16];

int cmp_popcount_desc(const void* a, const void* b) {
    uint16_t ma = *(const uint16_t*)a;
    uint16_t mb = *(const uint16_t*)b;
    int ca = __builtin_popcount(ma);
    int cb = __builtin_popcount(mb);
    if (ca != cb) return cb - ca;
    return (int)ma - (int)mb;
}

void init_masks() {
    for (int len = 2; len <= 8; ++len) {
        int cnt = 1 << (len - 1);
        mask_count10[len] = cnt;
        for (int m = 0; m < cnt; ++m) {
            masks10[len][m] = (uint16_t)m;
        }
        qsort(masks10[len], cnt, sizeof(uint16_t), cmp_popcount_desc);
    }
    for (int len = 2; len <= 15; ++len) {
        int cnt = 1 << (len - 1);
        mask_count3[len] = cnt;
        for (int m = 0; m < cnt; ++m) {
            masks3[len][m] = (uint16_t)m;
        }
        qsort(masks3[len], cnt, sizeof(uint16_t), cmp_popcount_desc);
    }
}

int64_t solve_c(int limit) {
    init_masks();
    for (int i = 1; i <= limit; ++i) {
        ds10[i] = ds10[i / 10] + (i % 10);
        ds3[i] = ds3[i / 3] + (i % 3);
    }
    
    int digits10[10] = {0};
    int digits3[20] = {0};
    int len10 = 1, len3 = 1;
    int sum10 = 0, sum3 = 0;
    int prefix10[10] = {0};
    int prefix3[20] = {0};
    
    int64_t total = 0;
    
    for (int n = 1; n <= limit; ++n) {
        // Increment base-10
        int i = 0;
        while (i < len10 && digits10[i] == 9) {
            sum10 -= 9;
            digits10[i] = 0;
            i++;
        }
        if (i == len10) {
            digits10[i] = 1;
            len10++;
            sum10++;
        } else {
            digits10[i]++;
            sum10++;
        }
        
        // Increment base-3
        i = 0;
        while (i < len3 && digits3[i] == 2) {
            sum3 -= 2;
            digits3[i] = 0;
            i++;
        }
        if (i == len3) {
            digits3[i] = 1;
            len3++;
            sum3++;
        } else {
            digits3[i]++;
            sum3++;
        }
        
        // f(n, 10)
        int f10;
        if (len10 == 1) {
            f10 = 0;
        } else if (sum10 < 10) {
            f10 = 1;
        } else {
            int p = 0;
            prefix10[0] = 0;
            int pos = 0;
            for (int idx = len10 - 1; idx >= 0; --idx) {
                p = p * 10 + digits10[idx];
                pos++;
                prefix10[pos] = p;
            }
            int good = 0;
            int cnt = mask_count10[len10];
            for (int mi = 0; mi < cnt; ++mi) {
                int mask = masks10[len10][mi];
                int s = 0;
                int start = 0;
                for (int bit = 0; bit < len10 - 1; ++bit) {
                    if ((mask >> (len10 - 2 - bit)) & 1) {
                        int ln = bit - start + 1;
                        s += prefix10[start + ln] - prefix10[start] * pow10[ln];
                        start = bit + 1;
                    }
                }
                int ln = len10 - start;
                s += prefix10[start + ln] - prefix10[start] * pow10[ln];
                if (ds10[s] < 10) {
                    good = 1;
                    break;
                }
            }
            f10 = good ? 2 : 3;
        }
        
        // f(n, 3)
        int f3;
        if (len3 == 1) {
            f3 = 0;
        } else if (sum3 < 3) {
            f3 = 1;
        } else {
            int p = 0;
            prefix3[0] = 0;
            int pos = 0;
            for (int idx = len3 - 1; idx >= 0; --idx) {
                p = p * 3 + digits3[idx];
                pos++;
                prefix3[pos] = p;
            }
            int good = 0;
            int cnt = mask_count3[len3];
            for (int mi = 0; mi < cnt; ++mi) {
                int mask = masks3[len3][mi];
                int s = 0;
                int start = 0;
                for (int bit = 0; bit < len3 - 1; ++bit) {
                    if ((mask >> (len3 - 2 - bit)) & 1) {
                        int ln = bit - start + 1;
                        s += prefix3[start + ln] - prefix3[start] * pow3[ln];
                        start = bit + 1;
                    }
                }
                int ln = len3 - start;
                s += prefix3[start + ln] - prefix3[start] * pow3[ln];
                if (ds3[s] < 3) {
                    good = 1;
                    break;
                }
            }
            f3 = good ? 2 : 3;
        }
        
        if (f10 == f3) {
            total += n;
        }
    }
    return total;
}
