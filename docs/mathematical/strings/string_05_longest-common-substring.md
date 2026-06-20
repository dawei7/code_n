# Formal Mathematical Specification: Longest Common Substring

## 1. Definitions and Notation
Let $S_1, S_2 \in \Sigma^*$ be two strings of lengths $n$ and $m$ respectively.
We seek $i, j, k \in \mathbb{N}$ such that $S_1[i \dots i+k-1] = S_2[j \dots j+k-1]$ and $k$ is maximized.

## 2. Algebraic Characterization (Dynamic Programming)
Define $L(i, j)$ as the length of the longest common suffix of prefixes $S_1[1 \dots i]$ and $S_2[1 \dots j]$.
Recurrence relation:
$$ L(i, j) = \begin{cases} 
0 & \text{if } i = 0 \text{ or } j = 0 \\
L(i-1, j-1) + 1 & \text{if } S_1[i] = S_2[j] \\
0 & \text{if } S_1[i] \neq S_2[j]
\end{cases} $$

The length of the longest common substring is $\max_{i, j} L(i, j)$.

## 3. Complexity Analysis
- **Time Complexity:** The recurrence $L(i, j)$ is evaluated for all $1 \leq i \leq n$ and $1 \leq j \leq m$. Each evaluation takes $O(1)$ time. Time complexity is $O(nm)$.
- **Space Complexity:** Evaluated strictly using a 2D array, space is $O(nm)$. Because $L(i, j)$ only depends on $L(i-1, j-1)$, memory can be optimized to $O(\min(n, m))$ by keeping only the previous row.
