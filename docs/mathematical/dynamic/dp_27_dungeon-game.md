# Formal Mathematical Specification: Dungeon Game

## 1. Definitions and Notation
Grid $M$. Find minimum initial health at $(1, 1)$ to reach $(m, n)$ while remaining $>0$.

## 2. Algebraic Characterization (Recurrence Relation)
Iterate backward from $(m, n)$. Let $H(i, j)$ be min health required at $(i, j)$. $$ H(i, j) = \max(1, \min(H(i+1, j), H(i, j+1)) - M[i, j]) $$

## 3. Complexity Analysis
- **Time Complexity:** $O(nm)$.
- **Space Complexity:** $O(n)$ row reduction.
