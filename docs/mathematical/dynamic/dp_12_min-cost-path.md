# Formal Mathematical Specification: Min Cost Path

## 1. Definitions and Notation
Grid $C$ of size $m \times n$ with costs. Move down, right, or diagonally.

## 2. Algebraic Characterization (Recurrence Relation)
$$ M(i, j) = C[i, j] + \min(M(i-1, j), M(i, j-1), M(i-1, j-1)) $$

## 3. Complexity Analysis
- **Time Complexity:** $O(nm)$.
- **Space Complexity:** $O(n)$.
