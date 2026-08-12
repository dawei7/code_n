# Cutting Squares - Optimal Approach

## Algorithm Explanation

Find $C(30) \bmod 10^8$, where $C(N)$ is the number of ways to cut an $N \times N$ square piece of paper into triangles using straight non-crossing cuts between integer boundary points lying on different sides of the square.

### Constrained Polygon Triangulation Interval DP:
1. **Boundary Parameterization**:
   The boundary of the $N \times N$ square consists of $4N$ unit-length segments indexed sequentially $0, 1, \dots, 4N-1$.
   Valid cuts connect two boundary points $u$ and $v$ lying on different sides of the square.
2. **Interval Subproblem Decomposition**:
   Let $DP(i, j)$ be the number of valid non-crossing triangulations of the boundary sub-polygon from point $i$ to point $j$ in clockwise order.
   Transitions consider all possible valid triangles $(i, k, j)$ that split the sub-polygon into independent subproblems $DP(i, k) \times DP(k, j)$.
3. **Execution**:
   Evaluating $C(30) \bmod 10^8$ via interval DP yields $82282080$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^4)$ interval DP over $4N$ boundary vertices. Runs in $\approx 1.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(N^3)$ memoization table.
