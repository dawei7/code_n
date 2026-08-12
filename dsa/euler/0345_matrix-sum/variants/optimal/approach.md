# Matrix Sum - Optimal Approach

## Algorithm Explanation

Find the maximum Matrix Sum (maximum sum of matrix elements such that no two selected elements share the same row or column) for the given $15 \times 15$ integer matrix.

### Maximum Weight Bipartite Matching via Bitmask Dynamic Programming:
1. **Bipartite Assignment Formulation**:
   The problem is equivalent to Maximum Weight Bipartite Matching between $N$ rows and $N$ columns for $N = 15$.
2. **Bitmask DP State**:
   Let `dp[mask]` be the maximum weight matching achievable using the first `popcount(mask)` rows paired with the set of columns represented by the bitmask `mask` ($0 \le \text{mask} < 2^N$).
   Transitions:
   $$\text{dp}[\text{mask} \mid (1 \ll c)] = \max(\text{dp}[\text{mask} \mid (1 \ll c)], \text{dp}[\text{mask}] + \text{matrix}[r][c])$$
   where $r = \text{popcount}(\text{mask})$ and $c$ is an unassigned column ($c \notin \text{mask}$).
3. **Execution**:
   Processing $2^{15} = 32768$ states yields maximum assignment sum $13938$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \cdot 2^N)$ for $N = 15$. Runs in $\approx 0.005\text{s}$.
- **Space Complexity:** $\mathcal{O}(2^N)$ DP table.
