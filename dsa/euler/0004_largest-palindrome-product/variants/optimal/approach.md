# Largest Palindrome Product - Optimal Approach

## Algorithm Explanation

A palindromic number reads the same forwards and backwards. We want the largest product $P = i \times j$ of two $3$-digit numbers ($100 \le i, j \le 999$).

1. Iterate outer factor $i$ from $999$ down to $100$.
2. Prune outer loop if $i \times 999 \le \text{max\_pal}$.
3. Iterate inner factor $j$ from $i$ down to $100$.
4. Prune inner loop if $i \times j \le \text{max\_pal}$.
5. Test if product string $S = \text{str}(P)$ is palindromic ($S = S^R$).
6. Track maximum palindrome encountered.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(D^2)$ where $D = 900$. With double pruning, it evaluates only a tiny fraction of products.
- **Space Complexity:** $\mathcal{O}(1)$ - Memory overhead is negligible.
