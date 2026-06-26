# Formal Mathematical Specification: Longest Increasing Subsequence

## 1. Definitions and Notation
Sequence $A = (a_1 \dots a_n)$. Find longest subsequence $A_{i_1} < A_{i_2} \dots < A_{i_k}$.

## 2. Algebraic Characterization (Recurrence Relation)
Let $L(i)$ be the LIS ending precisely at index $i$. $$ L(i) = 1 + \max_{1 \leq j < i, A[j] < A[i]} L(j) $$ Result is $\max_{i} L(i)$.

## 3. Complexity Analysis
- **Time Complexity:** $O(n^2)$ using the standard DP recurrence. (Optimizable to $O(n \log n)$ via Patience Sorting).
- **Space Complexity:** $O(n)$.
