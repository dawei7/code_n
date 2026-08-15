#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

static const int digit_cost[10] = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};

static inline int get_literal_cost(int n) {
    int cost = 0;
    while (n > 0) {
        cost += digit_cost[n % 10];
        n /= 10;
    }
    return cost;
}

typedef struct {
    int val;
    int cost;
} Atom;

static int compare_atoms(const void* a, const void* b) {
    return ((const Atom*)a)->cost - ((const Atom*)b)->cost;
}

EXPORT int64_t compute_T(int N) {
    int* P = (int*)malloc((N + 1) * sizeof(int));
    int* M = (int*)malloc((N + 1) * sizeof(int));

    P[0] = 0;
    for (int i = 1; i <= N; i++) {
        P[i] = get_literal_cost(i);
    }

    // Multiplication DP
    for (int a = 2; a <= N; a++) {
        int pa_plus_2 = P[a] + 2;
        int max_b = N / a;
        for (int b = 2; b <= max_b; b++) {
            int cost_prod = pa_plus_2 + P[b];
            if (cost_prod < P[a * b]) {
                P[a * b] = cost_prod;
            }
        }
    }

    for (int i = 1; i <= N; i++) {
        M[i] = P[i];
    }

    // Collect product atoms
    Atom* atoms = (Atom*)malloc((N + 1) * sizeof(Atom));
    int atom_count = 0;
    for (int b = 1; b <= N; b++) {
        if (P[b] <= 18) {
            atoms[atom_count].val = b;
            atoms[atom_count].cost = P[b] + 2;
            atom_count++;
        }
    }

    qsort(atoms, atom_count, sizeof(Atom), compare_atoms);

    // Addition DP: push updates via active atoms
    for (int it = 0; it < atom_count; it++) {
        int b = atoms[it].val;
        int cost_b = atoms[it].cost;
        for (int a = 1; a + b <= N; a++) {
            int val = M[a] + cost_b;
            if (val < M[a + b]) {
                M[a + b] = val;
            }
        }
    }

    int64_t total_sum = 0;
    for (int i = 1; i <= N; i++) {
        total_sum += M[i];
    }

    free(P);
    free(M);
    free(atoms);
    return total_sum;
}
