# Red, Green, and Blue Tiles - Optimal Approach

## Algorithm Explanation

Find the total number of ways to tile a row of length $N = 50$ units using any mixed combination of grey tiles (length 1), red tiles (length 2), green tiles (length 3), and blue tiles (length 4).

### Multi-Tile Dynamic Programming:
Let $DP[i]$ be the number of valid tilings for a row of length $i$:

1. Base case: $DP[0] = 1$.
2. Recurrence relation for $i \in [1, N]$:
   $$DP[i] = DP[i-1] + \mathbb{I}(i \ge 2) DP[i-2] + \mathbb{I}(i \ge 3) DP[i-3] + \mathbb{I}(i \ge 4) DP[i-4]$$
3. Return $DP[50]$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ linear scan where $N = 50$. Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - 1D DP table.
