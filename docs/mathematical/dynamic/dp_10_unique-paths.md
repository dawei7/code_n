# Formal Mathematical Specification: Unique Paths

## 1. Definitions and Notation
Grid $m \times n$. Path goes down or right. Find total paths from $(1, 1)$ to $(m, n)$.

## 2. Algebraic Characterization (Recurrence Relation)
Let $U(i, j)$ be paths to reach $(i, j)$. $$ U(i, j) = \begin{cases} 1 & \text{if } i = 1 \lor j = 1 \\ U(i-1, j) + U(i, j-1) & \text{otherwise} \end{cases} $$

## 3. Complexity Analysis
- **Time Complexity:** $O(nm)$. (Alternatively, combinatorics computes $\binom{m+n-2}{m-1}$ in $O(m)$ time).
- **Space Complexity:** $O(n)$ space via row optimization.
