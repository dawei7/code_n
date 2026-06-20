# Formal Mathematical Specification: Coin Change (Minimum Coins)

## 1. Definitions and Notation
Let $C = \{c_1 \dots c_k\}$ be denominations. Target sum $S$. We seek $\min \sum x_i$ such that $\sum x_i c_i = S, x_i \in \mathbb{N}$.

## 2. Algebraic Characterization (Recurrence Relation)
Let $M(s)$ be the minimum coins for sum $s$. $$ M(s) = \begin{cases} 0 & \text{if } s = 0 \\ \min_{c \in C, c \leq s} M(s - c) + 1 & \text{if } s > 0 \end{cases} $$

## 3. Complexity Analysis
- **Time Complexity:** $O(S \cdot k)$ where $k = |C|$.
- **Space Complexity:** $O(S)$.
