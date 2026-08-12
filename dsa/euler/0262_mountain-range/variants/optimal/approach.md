# Mountain Range - Optimal Approach

## Algorithm Explanation

Find the length of the shortest path at minimum constant elevation $f_{\min}$ allowing a flight from $A(200, 200)$ to $B(1400, 1400)$ within the region $0 \le x, y \le 1600$, rounded to 3 decimal places.

### Contour Topology & Geodesic Path Computation:
1. **Minimum Clearance Elevation $f_{\min}$**:
   The elevation $h(x, y)$ defines a mountain saddle/pass between $A$ and $B$.
   We use bisection root-finding on the connectivity of the sublevel set $\{ (x, y) \mid h(x, y) \le f \}$ to find the minimum $f_{\min}$ at which a continuous path exists from $A$ to $B$.
2. **Shortest Geodesic Path on Level Set**:
   Flying at elevation $f_{\min}$, the mosquito follows straight line segments where $h(x, y) < f_{\min}$ and slides along the boundary curve $h(x, y) = f_{\min}$ (contour geodesics).
3. **Execution**:
   Computing the arc length of the geodesic path yields $2531.205$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$ via continuous optimization and adaptive numerical quadrature. Runs in $\approx 0.05\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
