# Multiples of 3 or 5 - Optimal Approach

## Algorithm Explanation

The problem asks for the sum of all natural numbers below $N = 1000$ that are divisible by $3$ or $5$.

Instead of iterating through numbers $1$ to $999$ in $\mathcal{O}(N)$ time, we use the **Inclusion-Exclusion Principle** alongside the arithmetic series sum formula in $\mathcal{O}(1)$ time.

### Arithmetic Series Formula
The sum of multiples of $k$ up to $M = N - 1$ is:
$$S(k) = k \cdot (1 + 2 + \dots + p) = k \cdot \frac{p(p + 1)}{2}$$
where $p = \lfloor \frac{M}{k} \rfloor$.

### Inclusion-Exclusion
Numbers divisible by both $3$ and $5$ are multiples of $\text{lcm}(3, 5) = 15$. Adding $S(3)$ and $S(5)$ double-counts multiples of $15$, so we subtract $S(15)$:
$$\text{Total Sum} = S(3) + S(5) - S(15)$$

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$ - Fixed arithmetic operations.
- **Space Complexity:** $\mathcal{O}(1)$ - Constant memory.
