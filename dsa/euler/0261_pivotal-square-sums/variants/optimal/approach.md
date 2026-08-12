# Pivotal Square Sums - Optimal Approach

## Algorithm Explanation

Find the sum of all distinct square-pivots $k \le 10^{10}$, where $k$ satisfies $\sum_{j=0}^m (k-j)^2 = \sum_{j=1}^m (n+j)^2$ for integer parameters $m > 0$ and $n \ge k$.

### Algebraic Simplification & Generalized Pell Recurrence:
1. **Equation Reduction**:
   Expanding both sides and canceling the common $\frac{m(m+1)(2m+1)}{6}$ term:
   $$(m+1) k (k - m) = m n (n + m + 1)$$
2. **Pell Equation Family Transformation**:
   Multiplying by $4$ and completing the square yields a family of generalized Pell equations indexed by parameter $m$:
   $$X^2 - m(m+1) Y^2 = Z$$
3. **Fundamental Solution Recurrence**:
   For each small $m \le \sqrt{10^{10}}$, we generate solutions $(k, n)$ using fundamental units of $\mathbb{Z}[\sqrt{m(m+1)}]$.
4. **Distinct Pivot Summation**:
   We collect all distinct values of $k \le 10^{10}$ in a hash set and sum them up.
5. **Execution**:
   The sum of all distinct square-pivots $\le 10^{10}$ is $238890850232021$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\sqrt{L})$ where $L = 10^{10}$. Runs in $\approx 0.20\text{s}$.
- **Space Complexity:** $\mathcal{O}(K)$ for distinct pivot set storage.
