# Pandigital Multiples - Optimal Approach

## Algorithm Explanation

Find the largest 1-to-9 pandigital 9-digit number formed by concatenating products of an integer $X$ with $(1, 2, \dots, n)$ where $n > 1$.

### Mathematical Bounds
1. The problem gives a candidate $918273645$ for $X = 9, n = 5$. Thus any larger answer must start with digit `'9'`.
2. For $n = 2$, $X$ must be a $4$-digit number starting with $9$: $X \in [9214, 9876]$.
   - $X \times 1$ gives $4$ digits.
   - $X \times 2$ gives $5$ digits.
   - Total length $= 4 + 5 = 9$ digits.

### Search Strategy:
- Loop $X$ downwards from $9876$ to $9214$.
- Form concatenated string $S = \text{str}(X) + \text{str}(2X)$.
- Test $\text{len}(S) = 9$ and $\text{set}(S) = \{'1', \dots, '9'\}$.
- The first valid candidate is guaranteed to be maximal.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$ - Iterates at most $663$ numbers. Operates in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
