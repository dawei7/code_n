# Formal Mathematical Specification: Regular Expression Matching

## 1. Definitions and Notation
String $S$, Pattern $P$ with `.` and `*`.

## 2. Algebraic Characterization (Recurrence Relation)
Let $M(i, j)$ be True if $S[1 \dots i]$ matches $P[1 \dots j]$. For `*` at $P[j]$, $M(i, j) = M(i, j-2) \lor (M(i-1, j) \land (S[i] == P[j-1] \lor P[j-1] == '.'))$.

## 3. Complexity Analysis
- **Time Complexity:** $O(nm)$.
- **Space Complexity:** $O(nm)$.
