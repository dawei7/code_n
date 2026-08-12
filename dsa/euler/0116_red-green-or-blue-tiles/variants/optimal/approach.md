# Red, Green or Blue Tiles - Optimal Approach

## Algorithm Explanation

Find the total number of ways to replace grey tiles in a row measuring $N = 50$ units in length using colored tiles of a single type: **red** (length 2), **green** (length 3), or **blue** (length 4), such that at least one colored tile is used and colors are not mixed.

### Single-Color Dynamic Programming:
For a chosen tile length $L \in \{2, 3, 4\}$:
Let $DP_L[i]$ be the number of ways to fill a row of length $i$ with tiles of length $1$ (grey) or $L$:

1. Base case: $DP_L[0] = 1$.
2. Recurrence:
   $$DP_L[i] = DP_L[i-1] + (DP_L[i-L] \text{ if } i \ge L \text{ else } 0)$$
3. Subtract $1$ for the all-grey configuration (zero colored tiles).

### Combined Sum:
$$\text{Total Ways} = (DP_2[50] - 1) + (DP_3[50] - 1) + (DP_4[50] - 1)$$

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ where $N = 50$. Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - 1D DP state vector.
