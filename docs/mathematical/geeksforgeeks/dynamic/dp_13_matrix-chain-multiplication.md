# Formal Mathematical Specification: Matrix Chain Multiplication

## 1. Definitions and Notation
Matrices $A_1 \dots A_n$ with dimensions $p_0 \dots p_n$. Minimize scalar multiplications.

## 2. Algebraic Characterization (Recurrence Relation)
Let $M(i, j)$ be min cost to multiply $A_i \dots A_j$. $$ M(i, j) = \begin{cases} 0 & \text{if } i = j \\ \min_{i \leq k < j} (M(i, k) + M(k+1, j) + p_{i-1}p_k p_j) & \text{if } i < j \end{cases} $$

## 3. Complexity Analysis
- **Time Complexity:** $O(n^3)$ due to interval length iteration and pivot point selection.
- **Space Complexity:** $O(n^2)$.
