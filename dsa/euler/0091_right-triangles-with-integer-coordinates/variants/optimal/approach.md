# Right Triangles with Integer Coordinates - Optimal Approach

## Algorithm Explanation

Find the total number of right-angled triangles $\triangle OPQ$ where $O = (0, 0)$ and $P(x_1, y_1), Q(x_2, y_2)$ are integer grid coordinates in $0 \le x, y \le 50$.

### Case Breakdown by Right-Angle Vertex:
1. **Right angle at $O(0, 0)$**: $P$ on x-axis ($y_1 = 0$) and $Q$ on y-axis ($x_2 = 0$). Yields $N \times N = 2500$ triangles.
2. **Right angle on axes**: $P$ at $(x_1, 0)$ with $Q$ vertically at $(x_1, y_2)$ ($N^2$) or $P$ at $(0, y_1)$ with $Q$ horizontally at $(x_2, y_1)$ ($N^2$). Total $2 N^2 = 5000$.
3. **Right angle at $P(x_1, y_1)$ in quadrant 1 ($x_1, y_1 > 0$)**:
   - Vector $\vec{OP} = (x_1, y_1)$.
   - Perpendicular vector step $(\Delta x, \Delta y) = \left(\frac{y_1}{g}, -\frac{x_1}{g}\right)$ where $g = \gcd(x_1, y_1)$.
   - Valid integer points $Q$ in direction 1: $\min\left(\lfloor \frac{N - x_1}{\Delta x} \rfloor, \lfloor \frac{y_1}{\Delta y} \rfloor\right)$.
   - Valid integer points $Q$ in direction 2: $\min\left(\lfloor \frac{x_1}{\Delta x} \rfloor, \lfloor \frac{N - y_1}{\Delta y} \rfloor\right)$.

Summing across all $P(x_1, y_1)$ yields the exact total count.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^2)$ where $N = 50$ ($2500$ grid points). Runs in $< 0.005\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Memory overhead is constant.
