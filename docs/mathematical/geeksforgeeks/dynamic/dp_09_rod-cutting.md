# Formal Mathematical Specification: Rod Cutting

## 1. Definitions and Notation
Rod length $n$. Prices $p_1 \dots p_n$. Maximize total revenue $\sum p_i$.

## 2. Algebraic Characterization (Recurrence Relation)
Let $R(n)$ be max revenue for length $n$. $$ R(n) = \begin{cases} 0 & \text{if } n = 0 \\ \max_{1 \leq i \leq n} (p_i + R(n - i)) & \text{if } n > 0 \end{cases} $$

## 3. Complexity Analysis
- **Time Complexity:** $O(n^2)$.
- **Space Complexity:** $O(n)$.
