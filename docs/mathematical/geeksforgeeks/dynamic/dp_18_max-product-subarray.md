# Formal Mathematical Specification: Maximum Product Subarray

## 1. Definitions and Notation
Sequence $A = (a_1 \dots a_n)$. Find contiguous subarray maximizing product.

## 2. Algebraic Characterization (Recurrence Relation)
Maintain max and min products to handle negative numbers: $$ \text{Max}(i) = \max(A[i], \text{Max}(i-1)A[i], \text{Min}(i-1)A[i]) $$ $$ \text{Min}(i) = \min(A[i], \text{Max}(i-1)A[i], \text{Min}(i-1)A[i]) $$

## 3. Complexity Analysis
- **Time Complexity:** $O(n)$.
- **Space Complexity:** $O(1)$ maintaining only the previous state.
