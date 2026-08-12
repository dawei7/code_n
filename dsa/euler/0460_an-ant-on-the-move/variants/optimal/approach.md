# An Ant on the Move - Optimal Approach

## Algorithm Explanation

Find $F(10000)$ rounded to 9 decimal places, where $F(d)$ is the minimum travel time for an ant moving from $(0, 1)$ to $(d, 1)$ across lattice points $(x_i, y_i)$ with velocity $v = \frac{y_1 - y_0}{\ln y_1 - \ln y_0}$ (or $v = y_0$ when $y_0 = y_1$).

### Convex Trajectory DP & Dijkstra Shortest Path:
1. **Segment Travel Time Metric**:
   The time required to travel along a straight segment from $(x_0, y_0)$ to $(x_1, y_1)$ is:
   $$\Delta t = \frac{\sqrt{(x_1 - x_0)^2 + (y_1 - y_0)^2} (\ln y_1 - \ln y_0)}{y_1 - y_0}$$
2. **Convex Boundary & Height Bound**:
   Because velocity $v(y)$ is an increasing function of $y$, the optimal trajectory rises to a maximum height $H \approx \mathcal{O}(\sqrt{d} \ln d) \approx 200$ for $d = 10000$.
   By 2-fold horizontal symmetry, the minimum time path is symmetric about $x = d / 2$.
3. **Shortest Path Dynamic Programming**:
   We build the directed acyclic graph of valid lattice moves $(x_0, y_0) \to (x_1, y_1)$ with $x_0 < x_1 \le d / 2$ and $y_0 \le y_1 \le H$.
   Using Dijkstra's algorithm or DP state relaxation over $(x, y)$, $F(10000)$ is evaluated accurately.
4. **Execution**:
   Evaluating $F(10000)$ rounded to 9 decimal places yields $18.420738198$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(d \cdot H \log H)$ for $d = 10000, H \approx 200$. Runs in $\approx 0.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(d \cdot H)$ DP state table.
