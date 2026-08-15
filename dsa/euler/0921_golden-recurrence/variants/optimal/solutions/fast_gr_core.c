#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

#define MOD 398874989LL
#define PISANO 199437494LL
#define EXP_MOD 99718746LL

static inline int64_t power_mod(int64_t base, int64_t exp, int64_t mod) {
    int64_t res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) res = (res * base) % mod;
        base = (base * base) % mod;
        exp >>= 1;
    }
    return res;
}

// 2x2 matrix Fibonacci mod MOD
typedef struct {
    int64_t m00, m01, m10, m11;
} Mat2;

static inline Mat2 mat_mul(Mat2 A, Mat2 B) {
    Mat2 C;
    C.m00 = (A.m00 * B.m00 + A.m01 * B.m10) % MOD;
    C.m01 = (A.m00 * B.m01 + A.m01 * B.m11) % MOD;
    C.m10 = (A.m10 * B.m00 + A.m11 * B.m10) % MOD;
    C.m11 = (A.m10 * B.m01 + A.m11 * B.m11) % MOD;
    return C;
}

static inline Mat2 mat_pow(Mat2 A, int64_t p) {
    Mat2 res = {1, 0, 0, 1};
    Mat2 base = A;
    while (p > 0) {
        if (p & 1) res = mat_mul(res, base);
        base = mat_mul(base, base);
        p >>= 1;
    }
    return res;
}

static inline int64_t compute_s_E(int64_t E) {
    Mat2 T = {1, 1, 1, 0};
    Mat2 M = mat_pow(T, E);
    int64_t F_E = M.m01;
    int64_t L_E = (M.m11 + M.m00) % MOD;

    int64_t inv2 = (MOD + 1) / 2;
    int64_t p = (F_E * inv2) % MOD;
    int64_t q = (L_E * inv2) % MOD;

    int64_t p5 = power_mod(p, 5, MOD);
    int64_t q5 = power_mod(q, 5, MOD);

    return (p5 + q5) % MOD;
}

EXPORT int64_t compute_S_total(int m_max) {
    int64_t total_S = 0;

    int64_t f_prev = 1; // F_1 = 1
    int64_t f_curr = 1; // F_2 = 1

    for (int i = 2; i <= m_max; i++) {
        int64_t pow5 = power_mod(5, f_curr, 99718747LL);
        int64_t pow5_pisano = (pow5 % 2 != 0) ? pow5 : (pow5 + 99718747LL);
        int64_t E = (3 * pow5_pisano) % PISANO;

        int64_t s_val = compute_s_E(E);
        total_S = (total_S + s_val) % MOD;

        int64_t f_next = (f_prev + f_curr) % EXP_MOD;
        f_prev = f_curr;
        f_curr = f_next;
    }

    return total_S;
}
