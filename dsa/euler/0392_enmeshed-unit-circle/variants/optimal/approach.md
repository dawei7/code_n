# Enmeshed Unit Circle - Optimal Approach

## Algorithm Explanation

Find the minimum area occupied by red cells overlapping the unit circle $x^2 + y^2 \le 1$ in an $(N+1) \times (N+1)$ rectilinear grid bounded by $[-1, 1] \times [-1, 1]$ for $N = 400$, rounded to 10 decimal places.

### 4-Fold Symmetry & Shooting Method Calculus Optimization:
1. **Symmetric Quadrant Grid Reduction**:
   By 4-fold Cartesian symmetry, we place $k = N / 2 = 200$ gridlines $0 < x_1 < x_2 < \dots < x_k < 1$ in the first quadrant.
   The total area of red cells overlapping $x^2 + y^2 \le 1$ is 4 times the first quadrant step-function area:
   $$\text{Area} = 4 \sum_{i=1}^{k+1} x_i (y_{i-1} - y_i)$$
   where $y_i = \sqrt{1 - x_i^2}$ with boundary conditions $x_0 = 0, x_{k+1} = 1$.
2. **First-Order Optimality Conditions & Recurrence**:
   Setting partial derivatives $\frac{\partial \text{Area}}{\partial x_i} = 0$ for $i = 1 \dots k$ yields a non-linear 3-term recurrence relation:
   $$x_{i+1} - x_{i-1} = 2 x_i \sqrt{\frac{1 - x_i^2}{1 - x_{i+1}^2}}$$
3. **Shooting Method Bisection**:
   Given a trial value for $x_1 \in (0, 1)$, the recurrence uniquely determines $x_2, x_3, \dots, x_{k+1}$.
   We optimize $x_1$ via high-precision bisection / shooting method so that $x_{k+1} = 1$.
4. **Execution**:
   Evaluating the optimized grid area for $N = 400$ yields $3.1486734434$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \cdot \text{iterations})$ for $N = 400$ and $50$ bisection steps. Runs in $\approx 0.01\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ gridline position array.
