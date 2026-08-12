# Product-sum Numbers - Optimal Approach

## Algorithm Explanation

Find the sum of all distinct minimal product-sum numbers $N$ for sets of size $2 \le k \le 12000$.

### Factorization Equivalence
Consider a set of numbers $\{a_1, a_2, \dots, a_m, 1, 1, \dots, 1\}$ with $m \ge 2$ non-unit factors $a_i \ge 2$ and $k - m$ ones:
- Product $P = a_1 \times a_2 \times \cdots \times a_m$
- Sum $S = (a_1 + a_2 + \cdots + a_m) + (k - m)$

Equating $P = S$ yields the set size formula:
$$k = P - S + m$$

### Search Bound & Strategy:
1. Upper bound $N \le 2k$ (since $N = 2k$ can always be formed by $\{k, 2, 1, 1, \dots, 1\}$).
2. Recursively generate all factorizations with non-unit factors $\ge 2$ up to product $P \le 24000$.
3. Compute $k = P - S + m$ for each factorization and update `min_k[k] = min(min_k[k], P)`.
4. Sum all distinct values in `set(min_k[2:])`.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\text{Factorizations})$ for numbers $\le 24000$. Runs in $< 0.05\text{s}$.
- **Space Complexity:** $\mathcal{O}(K)$ - Minimal $N$ lookup array.
