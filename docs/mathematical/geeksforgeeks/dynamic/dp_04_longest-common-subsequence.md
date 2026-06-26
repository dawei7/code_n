# Formal Mathematical Specification: Longest Common Subsequence

## 1. Definitions and Notation
Let $A, B \in \Sigma^*$ be sequences of lengths $n, m$. We seek the maximum length of a common non-contiguous subsequence.

## 2. Algebraic Characterization (Recurrence Relation)
Let $L(i, j)$ be the LCS of $A[1 \dots i]$ and $B[1 \dots j]$. $$ L(i, j) = \begin{cases} 0 & \text{if } i=0 \lor j=0 \\ L(i-1, j-1) + 1 & \text{if } A[i] = B[j] \\ \max(L(i-1, j), L(i, j-1)) & \text{if } A[i] \neq B[j] \end{cases} $$

## 3. Complexity Analysis
- **Time Complexity:** Evaluating $nm$ states takes $O(nm)$ time.
- **Space Complexity:** $O(nm)$, optimizable to $O(\min(n, m))$ using row reduction.
