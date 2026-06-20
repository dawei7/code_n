# Formal Mathematical Specification: Climbing Stairs

## 1. Definitions and Notation
Let $C(n)$ be the number of distinct ways to climb $n$ stairs, taking steps $s \in \{1, 2\}$.

## 2. Algebraic Characterization (Recurrence Relation)
$$ C(n) = \begin{cases} 1 & \text{if } n \in \{0, 1\} \\ C(n-1) + C(n-2) & \text{if } n > 1 \end{cases} $$

## 3. Complexity Analysis
- **Time Complexity:** $O(n)$, identical to the Fibonacci sequence computation.
- **Space Complexity:** $O(1)$ space using state reduction.
