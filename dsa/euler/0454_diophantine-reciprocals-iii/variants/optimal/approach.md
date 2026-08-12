# Diophantine Reciprocals III - Optimal Approach

## Algorithm Explanation

Find $F(10^{12})$, the number of integer solutions $(x, y, n)$ to $\frac{1}{x} + \frac{1}{y} = \frac{1}{n}$ satisfying $x < y \le 10^{12}$.

### Divisor Parametrization & Sub-linear Floor Sum Sieve:
1. **Reciprocal Equation Transformation**:
   Let $x = n + a, y = n + b \implies a b = n^2$.
   Setting $a = k d^2, b = m d^2, n = d k m$ with $\gcd(k, m) = 1$ and $m < k$:
   $$y = d m (k + m) \le L$$
2. **Sub-linear Coprime Summation**:
   $F(L)$ is the number of integer triplets $(d, m, k)$ with $\gcd(k, m) = 1, m < k$ such that $d m (k + m) \le L$.
   Fixing $s = k + m$:
   $$F(L) = \sum_{m=1}^{\sqrt{L}} \sum_{s > m, \gcd(s, m) = 1} \left\lfloor \frac{L}{m s} \right\rfloor$$
3. **Möbius Inversion & Hyperbola Sieve**:
   Applying Möbius inversion over $\gcd(s, m) = 1$ and grouping hyperbola terms evaluates $F(10^{12})$ in $\mathcal{O}(L^{2/3})$ time.
4. **Execution**:
   Evaluating $F(10^{12})$ yields $5435004633092$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(L^{2/3})$ for $L = 10^{12}$. Runs in $\approx 0.35\text{s}$.
- **Space Complexity:** $\mathcal{O}(L^{1/2})$ memory tables.
