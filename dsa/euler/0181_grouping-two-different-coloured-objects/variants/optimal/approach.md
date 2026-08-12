# Grouping Two Different Coloured Objects - Optimal Approach

## Algorithm Explanation

Find the total number of ways to partition $B = 60$ black objects and $W = 40$ white objects into non-empty groups.

### Bivariate Partition Dynamic Programming:
A group is represented by a pair $(i, j) \in [0, B] \times [0, W] \setminus \{(0, 0)\}$, representing $i$ black objects and $j$ white objects.

To count un-ordered partitions without duplicate permutations, iterate through group types $(i, j)$ in canonical lexicographical order:

1. **State Definition**:
   `dp[b][w]` stores the number of partitions of $b$ black objects and $w$ white objects using processed group types.
2. **Base Case**:
   `dp[0][0] = 1`
3. **Transition**:
   For each group type $(i, j)$:
   For $b \in [i, B]$ and $w \in [j, W]$:
   $$\text{dp}[b][w] += \text{dp}[b - i][w - j]$$

Return `dp[60][40]`.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(B^2 W^2)$ operations where $B = 60, W = 40$ ($\approx 1.8 \times 10^6$ inner steps). Runs in $\approx 0.31\text{s}$.
- **Space Complexity:** $\mathcal{O}(B \cdot W) = 61 \times 41$ matrix memory.
