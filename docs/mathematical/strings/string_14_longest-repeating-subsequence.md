# Formal Mathematical Specification: Longest Repeating Subsequence

## 1. Definitions and Notation
Let $S$ be a string of length $n$.
We seek two increasing index sequences $I = (i_1, \dots, i_k)$ and $J = (j_1, \dots, j_k)$ such that $S_{i_x} = S_{j_x}$ for all $1 \leq x \leq k$, and strictly $i_x \neq j_x$. We maximize $k$.

## 2. Algebraic Characterization (Dynamic Programming)
This is equivalent to finding the Longest Common Subsequence of $S$ with itself, subject to index exclusion.
Define $L(i, j)$ as the length of the LRS up to prefixes $i$ and $j$.
$$ L(i, j) = \begin{cases} 
0 & \text{if } i = 0 \text{ or } j = 0 \\
L(i-1, j-1) + 1 & \text{if } S[i] = S[j] \land i \neq j \\
\max(L(i-1, j), L(i, j-1)) & \text{if } S[i] \neq S[j] \lor i = j
\end{cases} $$

## 3. Complexity Analysis
- **Time Complexity:** $n^2$ states, each $O(1)$ to evaluate. Time is $O(n^2)$.
- **Space Complexity:** DP matrix requires $O(n^2)$ space, optimizable to $O(n)$ by keeping only the previous row.
