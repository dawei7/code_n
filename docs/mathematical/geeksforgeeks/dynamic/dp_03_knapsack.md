# Formal Mathematical Specification: 0/1 Knapsack Problem

## 1. Definitions and Notation
Let $\mathcal{I} = \{1, \dots, n\}$ be a set of items where item $i$ has weight $w_i > 0$ and value $v_i > 0$. Let $W$ be the capacity constraint.

## 2. Algebraic Characterization (Recurrence Relation)
Let $K(i, w)$ be the maximum value attainable using a subset of $\{1 \dots i\}$ with total weight $\leq w$. $$ K(i, w) = \begin{cases} 0 & \text{if } i = 0 \lor w = 0 \\ K(i-1, w) & \text{if } w_i > w \\ \max(K(i-1, w), K(i-1, w - w_i) + v_i) & \text{if } w_i \leq w \end{cases} $$

## 3. Complexity Analysis
- **Time Complexity:** The matrix has $n \times W$ states. Each transition is $O(1)$. Total time is $O(nW)$.
- **Space Complexity:** $O(nW)$ which can be reduced to $O(W)$ since computing row $i$ only requires row $i-1$.
