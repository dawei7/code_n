# Formal Mathematical Specification: Egg Dropping Puzzle

## 1. Definitions and Notation
$E$ eggs, $F$ floors. Find minimum trials in worst case to find critical floor.

## 2. Algebraic Characterization (Recurrence Relation)
$$ D(e, f) = \begin{cases} f & \text{if } e = 1 \\ 0 & \text{if } f = 0 \\ 1 & \text{if } f = 1 \\ 1 + \min_{1 \leq x \leq f} \max(D(e-1, x-1), D(e, f-x)) & \text{otherwise} \end{cases} $$

## 3. Complexity Analysis
- **Time Complexity:** $O(e f^2)$ (can be optimized to $O(e f \log f)$ with binary search).
- **Space Complexity:** $O(ef)$.
