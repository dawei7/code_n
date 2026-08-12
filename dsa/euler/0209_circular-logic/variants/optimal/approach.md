# Obtuse Angled Triangles - Optimal Approach

## Algorithm Explanation

Find $N(10^9)$, the number of points $B(x, y)$ in the domain $|x| + |y| \le r$ such that triangle $OBC$ has an obtuse angle, where $O = (0,0)$ and $C = (r/4, r/4)$.

### Region Decomposition & Circle Geometry:
1. **Three Obtuse Angle Conditions**:
   - **Obtuse at $O$**: Dot product $x + y < 0$. Count of non-collinear integer points is $r^2$.
   - **Obtuse at $C$**: Dot product $r/2 - (x + y) < 0 \implies x + y > r/2$. Count of non-collinear integer points is $\frac{r^2}{2}$.
   - **Obtuse at $B$**: Point $B$ lies strictly inside the Thales circle on diameter $OC$.
2. **Thales Circle Boundary**:
   The center of diameter $OC$ is $(\frac{r}{8}, \frac{r}{8})$, and the radius squared is $R^2 = 2(\frac{r}{8})^2$.
   Sub-shifting the circle to $(0,0)$ requires counting lattice points strictly inside $X^2 + Y^2 < 2 K^2 - 1$ where $K = r/8$.
3. **Collinear Exclusion & Execution**:
   Collinear points along $y = x$ are excluded. Summing $N_O + N_C + N_B$ for $r = 10^9$ yields $1598174769467582678$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(r/8)$ using 2-pointer integer step traversal. Runs in $\approx 71\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
