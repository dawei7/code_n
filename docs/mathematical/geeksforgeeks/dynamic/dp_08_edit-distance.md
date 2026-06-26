# Formal Mathematical Specification: Levenshtein Edit Distance

## 1. Definitions and Notation
Strings $A, B$ of length $n, m$. Operations: insert, delete, substitute (cost 1).

## 2. Algebraic Characterization (Recurrence Relation)
Let $E(i, j)$ be distance between $A[1 \dots i], B[1 \dots j]$. $$ E(i, j) = \begin{cases} i & \text{if } j = 0 \\ j & \text{if } i = 0 \\ E(i-1, j-1) & \text{if } A[i] = B[j] \\ 1 + \min(E(i-1, j), E(i, j-1), E(i-1, j-1)) & \text{if } A[i] \neq B[j] \end{cases} $$

## 3. Complexity Analysis
- **Time Complexity:** $O(nm)$.
- **Space Complexity:** $O(\min(n, m))$ using row reduction.
