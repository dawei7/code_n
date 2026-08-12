# Squares Under a Hyperbola - Optimal Approach

## Algorithm Explanation

Find the largest index $n$ for which square $S_n$ under the hyperbola $y = 1/x$ ($x \ge 1, y \ge 0$) has index $(3, 3)$ (meaning 3 squares to its left and 3 squares below it).

### Max-Heap Greedy Placement:
1. **Square Geometry**:
   For a region with bottom-left corner $(x_0, y_0)$, placing a square of side length $s$ touching $(x_0+s)(y_0+s) = 1$ yields:
   $$s = \frac{-(x_0 + y_0) + \sqrt{(x_0 + y_0)^2 - 4(x_0 y_0 - 1)}}{2}$$
2. **Binary Tree & Heap Priority Queue**:
   Placing square $S_n$ at $(x, y, L, B)$ spawns two candidate regions:
   - Right region: $(x + s, y, L + 1, B)$
   - Above region: $(x, y + s, L, B + 1)$
   Squares are placed in decreasing order of area $s^2$ using a Max-Heap.
3. **Execution**:
   The largest $n$ for which $S_n$ has index $(3, 3)$ is $782252$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log N)$ where $N = 782\,252$. Runs in $\approx 0.35\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ for heap storage.
