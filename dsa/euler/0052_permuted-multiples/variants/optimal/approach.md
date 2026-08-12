# Permuted Multiples - Optimal Approach

## Algorithm Explanation

Find the smallest positive integer $x$ such that $x, 2x, 3x, 4x, 5x, 6x$ all consist of identical digit permutations.

### Digit Search Constraint
For $x$ and $6x$ to share the same digit length $D$:
$$x < \frac{10^D}{6} \approx 1.666 \dots \times 10^{D-1}$$
Thus, $x$ must always start with digit `'1'`.

### Strategy:
1. Incrementally iterate integers $x = 1, 2, 3 \dots$.
2. Canonicalize $x$'s digits using `sorted(str(x))`.
3. Compare sorted digit keys for $2x, 3x, 4x, 5x, 6x$ with short-circuit evaluation.
4. Return the first integer $x$ that satisfies all $5$ equality checks.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(X \cdot D \log D)$ where $X = 142857$ and $D = 6$. Runs in $< 0.05\text{s}$.
- **Space Complexity:** $\mathcal{O}(D)$ - Auxiliary sorted character arrays.
