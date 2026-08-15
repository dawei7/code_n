#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

static int64_t total_correct = 0;

static void recurse_partition(int* arr, int* buf, int L, int R, int bit) {
    if (L >= R) return;

    // Filter active primes (p >= (1 << bit))
    int mask = 1 << bit;
    int c0 = 0;
    int c1 = 0;

    int idx0 = L;
    int idx1 = R; // fill from right for 1s, from left for 0s

    for (int i = L; i < R; i++) {
        int p = arr[i];
        if (p >= mask) {
            if (!(p & mask)) {
                buf[idx0++] = p;
                c0++;
            } else {
                buf[--idx1] = p;
                c1++;
            }
        }
    }

    total_correct += (c0 > c1) ? c0 : c1;

    // Copy back to arr
    // 0s are in [L, L + c0)
    for (int i = 0; i < c0; i++) {
        arr[L + i] = buf[L + i];
    }
    // 1s are in [R - c1, R)
    for (int i = 0; i < c1; i++) {
        arr[L + c0 + i] = buf[R - 1 - i];
    }

    if (c0 > 0) recurse_partition(arr, buf, L, L + c0, bit + 1);
    if (c1 > 0) recurse_partition(arr, buf, L + c0, L + c0 + c1, bit + 1);
}

EXPORT double compute_expected_score(int N) {
    // 1. Bitwise sieve for primes <= N
    int size = (N >> 6) + 2;
    uint64_t* composite = (uint64_t*)calloc(size, sizeof(uint64_t));

    for (int p = 3; (int64_t)p * p <= N; p += 2) {
        if (!(composite[p >> 6] & (1ULL << (p & 63)))) {
            for (int64_t i = (int64_t)p * p; i <= N; i += (2 * p)) {
                composite[i >> 6] |= (1ULL << (i & 63));
            }
        }
    }

    int* primes = (int*)malloc(6000000 * sizeof(int));
    int* buf = (int*)malloc(6000000 * sizeof(int));
    int prime_count = 0;
    primes[prime_count++] = 2;

    for (int p = 3; p <= N; p += 2) {
        if (!(composite[p >> 6] & (1ULL << (p & 63)))) {
            primes[prime_count++] = p;
        }
    }
    free(composite);

    total_correct = 0;
    recurse_partition(primes, buf, 0, prime_count, 0);

    double ans = (double)total_correct / (double)prime_count;
    free(primes);
    free(buf);
    return ans;
}
