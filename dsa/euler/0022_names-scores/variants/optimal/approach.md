# Names Scores - Optimal Approach

## Algorithm Explanation

The problem requires calculating the sum of all "name scores" in a list of over $5000$ names:

1. Parse the names list from `names.txt`.
2. Sort the names in alphabetical order ($\mathcal{O}(N \log N)$).
3. For each name at $1$-indexed position $i$:
   - Calculate alphabetical letter sum $V = \sum (\text{ord}(c) - 64)$ for letters $A \dots Z$.
   - Calculate name score $S = i \times V$.
4. Sum all name scores.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log N + N \cdot L)$ where $N \approx 5163$ names and $L \approx 6$ average length.
- **Space Complexity:** $\mathcal{O}(N \cdot L)$ - Array memory for string storage.
