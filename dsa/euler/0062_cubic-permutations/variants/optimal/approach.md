# Cubic Permutations - Optimal Approach

## Algorithm Explanation

Find the smallest cube $C = n^3$ for which exactly $5$ permutations of its digits are also cubes.

### Key Grouping Strategy:
Instead of generating $12!$ permutations for each large number, we group calculated cubes by their **canonical sorted digit key** `"".join(sorted(str(n^3)))`:

1. Compute $C_n = n^3$ for $n = 1, 2, 3 \dots$.
2. Group cubes into hash map buckets indexed by canonical sorted digit key.
3. Batch checks by digit length $D$: when $n^3$ transitions to $D+1$ digits, inspect all buckets belonging to length $D$.
4. Return the minimum initial cube among all buckets with size equal to $5$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \cdot D \log D)$ where $N \approx 10000$ and $D \approx 12$. Runs in $< 0.02\text{s}$.
- **Space Complexity:** $\mathcal{O}(N \cdot D)$ - Hash map bucket storage.
