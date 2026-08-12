# Sum Square Difference - Optimal Approach

## Algorithm Explanation

The problem asks for the difference between the square of the sum and the sum of the squares for the first $N = 100$ natural numbers:
$$\Delta = \left( \sum_{k=1}^N k \right)^2 - \sum_{k=1}^N k^2$$

Using closed-form sum identities:
1. **Square of Sum**:
   $$\left( \frac{N(N + 1)}{2} \right)^2$$
2. **Sum of Squares**:
   $$\frac{N(N + 1)(2N + 1)}{6}$$

Subtracting the two formulas yields the exact answer in $\mathcal{O}(1)$ time.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$ - Closed-form arithmetic.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
