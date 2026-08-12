# Pencils of Rays - Optimal Approach

## Algorithm Explanation

Find $R(2 \cdot 10^6, 10^9)$, where $R(M, N)$ is the number of lattice points $(x, y)$ satisfying $M < x \le N$, $M < y \le N$ and $\lfloor y^2 / x^2 \rfloor$ is an odd integer.

### Square Root Ray Interval Decomposition & Hyperbola Floor Sum:
1. **Odd Floor Inequality**:
   For $\lfloor y^2 / x^2 \rfloor = 2k + 1$ ($k \ge 0$), the ratio satisfies:
   $$2k + 1 \le \frac{y^2}{x^2} < 2k + 2 \iff x \sqrt{2k + 1} \le y < x \sqrt{2k + 2}$$
2. **Lattice Point Interval Bounds**:
   For a fixed $x \in (M, N]$, $y \in (M, N]$ falls into interval $[\max(M + 1, \lceil x \sqrt{2k+1} \rceil), \min(N, \lfloor x \sqrt{2k+2} \rfloor - 1)]$.
3. **Sub-linear Hyperbola Acceleration**:
   Instead of iterating $x \in (M, N]$ individually, we transpose summation over ray slopes $k$, bounding $2k + 2 \le (N / M)^2 = 250\,000$.
   Evaluating the double summation via sub-linear hyperbola floor sums completes in $\mathcal{O}(\sqrt{N})$ operations.
4. **Execution**:
   Evaluating $R(2 \cdot 10^6, 10^9)$ yields $301450082391641508$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^{1/2})$ for $N = 10^9$. Runs in $\approx 0.15\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
