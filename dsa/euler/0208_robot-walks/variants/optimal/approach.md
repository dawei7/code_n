# Robot Walks - Optimal Approach

## Algorithm Explanation

Find the number of closed journeys of $70$ circular arcs ($72^\circ$ each) starting facing North that return to the starting position facing North.

### Direction Vector Equipartition & Dynamic Programming:
1. **Geometric Invariant**:
   The $5$ arc direction vectors $v_0, v_1, v_2, v_3, v_4$ form a regular pentagon in the complex plane with $\sum_{k=0}^4 v_k = 0$.
   For a path of $N = 70$ arcs to sum to $0$, each direction $v_k$ must be traversed **exactly $N/5 = 14$ times**.
2. **State Space**:
   A state is defined by $(c_0, c_1, c_2, c_3, c_4, o)$ where $c_k$ is the usage count of direction $k$ ($0 \le c_k \le 14$) and $o \in \{0, 1, 2, 3, 4\}$ is the current orientation angle.
3. **Transitions**:
   - Clockwise (CW): uses direction $o$, moves to orientation $(o - 1) \bmod 5$.
   - Counter-Clockwise (CCW): uses direction $(o + 1) \bmod 5$, moves to orientation $(o + 1) \bmod 5$.
4. **Execution**:
   Memoized DP yields $331951449665644800$ in $\approx 0.27\text{s}$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}\left(5 \cdot (N/5)^5\right)$ for $N = 70$. Runs in $\approx 0.27\text{s}$.
- **Space Complexity:** $\mathcal{O}\left(5 \cdot (N/5)^5\right)$ memoization table.
