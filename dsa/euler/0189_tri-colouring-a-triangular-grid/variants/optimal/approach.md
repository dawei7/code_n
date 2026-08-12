# Tri-colouring a Triangular Grid - Optimal Approach

## Algorithm Explanation

Count the number of valid $3$-colorings (red, green, blue) of $64$ small triangles in a size $8$ triangular grid such that no two adjacent triangles sharing an edge have the same color.

### Row-by-Row Transfer DP:
1. **Grid Geometry**:
   Row $r$ ($1$-indexed) contains $r$ upward-pointing triangles $U = (u_1, \dots, u_r)$.
   Between row $r$ and row $r+1$, there are $r$ downward-pointing triangles $D = (d_1, \dots, d_r)$.
   Downward triangle $d_i$ shares edges with $u_i$, $v_i$, and $v_{i+1}$ (where $V$ is row $r+1$ upward triangles).
2. **DP State**:
   `dp[r]` stores a dictionary mapping upward-color tuple $U \in \{0, 1, 2\}^r$ to the count of valid colorings for the top $r$ rows.
3. **Transition**:
   For a fixed top row $U$ of length $r$ and next row $V$ of length $r+1$:
   The number of valid choices for downward triangle $d_i$ is $3 - |\{u_i, v_i, v_{i+1}\}|$.
   The product of choices $\prod_{i=1}^r \text{choices}_i$ gives the transition weight.
   Updating `next_dp[V] += dp[U] * weight` for each row $r=1 \dots 7$ computes the total count.
4. **Final Answer**:
   Summing `dp.values()` at row $8$ gives $10,834,893,628,237,824$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n \cdot 3^{2n+1})$ where $n=8$. States at row $8$ are $3^8 = 6561$. Runs in $\approx 10.6\text{s}$.
- **Space Complexity:** $\mathcal{O}(3^n)$ - Space for DP dictionary storing at most $3^8 = 6561$ tuples.
