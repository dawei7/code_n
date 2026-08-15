
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>

static uint64_t arr[120000000];
static uint64_t tmp_arr[120000000];

static void radix_sort_u64(uint64_t *a, uint64_t *tmp, size_t n) {
    size_t count[256];
    for (int shift = 0; shift < 64; shift += 8) {
        for (int i = 0; i < 256; ++i) count[i] = 0;
        for (size_t i = 0; i < n; ++i) count[(a[i] >> shift) & 0xFF]++;
        size_t total = 0;
        for (int i = 0; i < 256; ++i) {
            size_t old = count[i];
            count[i] = total;
            total += old;
        }
        for (size_t i = 0; i < n; ++i) {
            tmp[count[(a[i] >> shift) & 0xFF]++] = a[i];
        }
        uint64_t *swp = a; a = tmp; tmp = swp;
    }
}

int64_t solve_c(int64_t M) {
    size_t count = 0;
    
    for (int64_t x = 1; ; ++x) {
        int64_t xx = x * (x + 1);
        if ((__int128)xx * xx > M) break;
        
        for (int64_t y = x; ; ++y) {
            int64_t yy = y * (y + 1);
            if ((__int128)xx * yy > M) break;
            arr[count++] = (uint64_t)xx * yy;
        }
    }
    
    radix_sort_u64(arr, tmp_arr, count);
    
    if (count == 0) return 0;
    size_t unique = 1;
    for (size_t i = 1; i < count; ++i) {
        if (arr[i] != arr[i - 1]) unique++;
    }
    return (int64_t)unique;
}
