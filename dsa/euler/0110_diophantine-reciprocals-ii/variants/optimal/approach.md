# Diophantine Reciprocals II - Optimal Approach

## Algorithm Explanation

Find the least positive integer $n$ for which the number of distinct positive integer solutions $(x, y)$ to $\frac{1}{x} + \frac{1}{y} = \frac{1}{n}$ exceeds $4,000,000$.

### Fundamental Prime Factorization Structure:
As derived in Problem 108:
$$\text{Solutions}(n) = \frac{d(n^2) + 1}{2} > 4,000,000 \implies d(n^2) > 7,999,999$$

For $n = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k}$:
$$d(n^2) = (2e_1 + 1)(2e_2 + 1) \cdots (2e_k + 1)$$

To minimize $n$ for a given divisor count $d(n^2)$:
1. Primes $p_1 < p_2 < \dots < p_k$ must be the smallest consecutive primes $\{2, 3, 5, 7, 11, 13 \dots\}$.
2. Exponents must be non-increasing: $e_1 \ge e_2 \ge \dots \ge e_k \ge 1$.

### Pruned Backtracking Search:
Perform Depth-First Search (DFS) over valid exponent sequences $(e_1, e_2, \dots, e_k)$ assigned to prime factors $p_1 < p_2 < \dots$.
Prune any search branch where candidate $n \ge \text{best\_n}$ so far.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\text{Exponent Vectors})$ with branch-and-bound pruning ($< 2000$ states explored). Runs in $< 0.005\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary stack memory.
