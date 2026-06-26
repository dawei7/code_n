# Formal Mathematical Specification: House Robber

## 1. Definitions and Notation
Wealth array $W = (w_1 \dots w_n)$. Maximize sum without selecting adjacent elements.

## 2. Algebraic Characterization (Recurrence Relation)
Let $H(i)$ be max wealth from first $i$ houses. $$ H(i) = \begin{cases} 0 & \text{if } i = 0 \\ w_1 & \text{if } i = 1 \\ \max(H(i-1), H(i-2) + w_i) & \text{if } i > 1 \end{cases} $$

## 3. Complexity Analysis
- **Time Complexity:** $O(n)$.
- **Space Complexity:** $O(1)$ maintaining only last two states.
