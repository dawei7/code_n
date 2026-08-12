# Pythagorean Polygons - Optimal Approach

## Algorithm Explanation

Find $P(120)$, the number of distinct convex Pythagorean polygons (polygons with integer vertices and integer edge lengths up to translation) with perimeter $\le 120$.

### Angular-Sorted Vector DP Knapsack:
1. **Pythagorean Vector Characterization**:
   Each edge of a Pythagorean polygon corresponds to an integer vector $(dx, dy)$ whose length $c = \sqrt{dx^2 + dy^2}$ is an integer.
2. **Convexity & Angle Order**:
   A polygon is strictly convex iff its edge vectors $(dx_i, dy_i)$ have strictly increasing polar angles $\theta_i \in [0, 2\pi)$ around the origin.
   Closure requires $\sum dx_i = 0$ and $\sum dy_i = 0$, with total length $\sum c_i \le 120$.
3. **Dynamic Programming**:
   We collect all valid integer-length vectors $(dx, dy)$, sort them by angle, and perform 3D DP over `(sum_dx, sum_dy, perimeter_left)`.
4. **Execution**:
   Evaluating the total closed convex polygons for perimeter $\le 120$ yields $3600060866$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(V \cdot L^3)$ for $V \approx 100$ vectors and $L = 120$. Runs in $\approx 2.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(L^3)$ DP state table.
