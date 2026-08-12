# Diophantine Equation - Optimal Approach

## Algorithm Explanation

Find the value of non-square $D \le 1000$ such that the minimal integer solution $x$ to **Pell's Equation** $x^2 - D y^2 = 1$ is maximized.

### Fundamental Theorem of Pell's Equation
By Lagrange's Theorem, the fundamental minimal solution $(x_1, y_1)$ to $x^2 - D y^2 = 1$ is always a convergent $\frac{p_k}{q_k}$ of the continued fraction expansion of $\sqrt{D}$.

1. For each non-square integer $D \in [2, 1000]$:
2. Generate convergents $\frac{p_k}{q_k}$ using the continued fraction recurrence for $\sqrt{D}$:
   - $p_k = a_k p_{k-1} + p_{k-2}$
   - $q_k = a_k q_{k-1} + q_{k-2}$
3. Check if $p_k^2 - D q_k^2 == 1$.
4. The first convergent that satisfies the equation gives the minimal $x = p_k$.
5. Track and return the parameter $D$ yielding the global maximum $x$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(D \cdot P)$ where $D = 1000$ and $P \le 250$ convergent steps. Runs in $< 0.03\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Memory overhead is constant.
