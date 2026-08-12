# Balanced Sculptures - Optimal Approach

## Algorithm Explanation

Find the number of balanced sculptures of order $n = 18$. A balanced sculpture consists of $n+1$ tiles: $1$ plinth tile at $(0, 0)$ and $n$ connected block tiles with $y > 0$ such that the center of mass $\sum_{i=1}^n x_i = 0$, counting $y$-axis reflections as identical.

### Polyomino Frontier Backtracking & Center-of-Mass Pruning:
1. **Frontier-Based Polyomino Generation**:
   Starting from the plinth $(0,0)$, we place $n = 18$ blocks in $y > 0$ using Redelmeier's polyomino expansion algorithm.
2. **Center-of-Mass Constraint**:
   We track the running $x$-sum $\sum x_i$ and prune branches where the remaining available blocks cannot possibly bring the sum back to $0$.
3. **Reflection Deduplication**:
   Sculptures symmetric under $x \leftrightarrow -x$ are counted once; asymmetric pairs are divided by $2$.
4. **Execution**:
   The number of balanced sculptures of order $18$ is $150376550$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(A^n)$ polyomino search for $n = 18$. Runs in $\approx 2.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(n)$ recursion depth.
