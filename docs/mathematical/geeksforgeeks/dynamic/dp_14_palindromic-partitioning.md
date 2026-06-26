# Formal Mathematical Specification: Palindromic Partitioning (Boolean)

## 1. Definitions and Notation
String $S$. Determine if any valid partition exists where all substrings are palindromes (Trivially True for length 1 cuts). Here we define $C(i, j)$ as the minimum cuts required.

## 2. Algebraic Characterization (Recurrence Relation)
Let $P(i, j)$ be True if $S[i \dots j]$ is palindrome. $C(j) = \min_{i \leq j, P(i, j)} (C(i-1) + 1)$.

## 3. Complexity Analysis
- **Time Complexity:** $O(n^2)$.
- **Space Complexity:** $O(n^2)$ for $P$ table, $O(n)$ for $C$.
