# Formal Mathematical Specification: Fibonacci Sequence

## 1. Definitions and Notation
Let $F : \mathbb{N} \to \mathbb{N}$ denote the Fibonacci sequence.

## 2. Algebraic Characterization (Recurrence Relation)
$$ F(n) = \begin{cases} n & \text{if } n \in \{0, 1\} \\ F(n-1) + F(n-2) & \text{if } n > 1 \end{cases} $$

## 3. Complexity Analysis
- **Time Complexity:** Using dynamic programming with memoization or tabulation, the recurrence is evaluated strictly $n$ times. $O(n)$.
- **Space Complexity:** $O(n)$ for a full table, optimizable to $O(1)$ since state $F(n)$ depends only on $F(n-1)$ and $F(n-2)$.
