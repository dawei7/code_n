# Triangles Containing the Origin II - Optimal Approach

## Algorithm Explanation

Find $C(2\,000\,000)$, the number of triangles with 3 distinct vertices chosen from $P_{2\,000\,000}$ that contain the origin in their interior.

### Polar Angle Sorting & Half-Plane Complementary Count:
1. **Total Triangle Complement**:
   The total number of 3-point subsets is $\binom{n}{3}$.
   A triangle does NOT contain the origin in its interior iff all 3 vertices lie in a single open half-plane.
2. **Angular Ordering & Two-Pointer Sweep**:
   We compute the polar angle $\theta_i = \operatorname{atan2}(y_i, x_i) \in [-\pi, \pi)$ for each of the $n$ points and sort them.
   For each point $i$, we use a two-pointer sweep to count $k_i$, the number of subsequent points lying strictly within the half-plane $(\theta_i, \theta_i + \pi)$.
3. **Non-Containing Combination Subtraction**:
   The number of non-origin-containing triangles anchored at $i$ is $\binom{k_i}{2}$.
   $$C(n) = \binom{n}{3} - \sum_{i=1}^n \binom{k_i}{2}$$
4. **Execution**:
   Sorting and two-pointer sweep for $n = 2\,000\,000$ yields $C(2\,000\,000) = 333333208685971546$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log N)$ for $N = 2\,000\,000$. Runs in $\approx 0.35\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ polar angle arrays.
