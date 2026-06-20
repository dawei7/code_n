# Formal Mathematical Specification: Shortest Common Supersequence

## 1. Definitions and Notation

Let $\Sigma$ be a finite alphabet. Let $X = \langle x_1, x_2, \dots, x_M \rangle$ and $Y = \langle y_1, y_2, \dots, y_N \rangle$ be two strings (sequences) over $\Sigma$, where $M, N \in \mathbb{N}_0$.

*   **Subsequence:** A string $Z$ is a subsequence of $X$ if there exists a strictly increasing sequence of indices $\langle i_1, i_2, \dots, i_k \rangle$ such that $1 \le i_1 < i_2 < \dots < i_k \le M$ and $Z = \langle x_{i_1}, x_{i_2}, \dots, x_{i_k} \rangle$.
*   **Supersequence:** A string $S$ is a supersequence of $X$ if $X$ is a subsequence of $S$.
*   **Shortest Common Supersequence (SCS):** A string $S^*$ is an SCS of $X$ and $Y$ if $S^*$ is a supersequence of both $X$ and $Y$, and for any other common supersequence $S'$, $|S^*| \le |S'|$.
*   **State Space:** We define a DP table $D \in \mathbb{N}_0^{(M+1) \times (N+1)}$, where $D_{i,j}$ represents the length of the SCS of the prefixes $X_{1..i}$ and $Y_{1..j}$.

## 2. Algebraic Characterization

The problem is governed by the relationship between the SCS and the Longest Common Subsequence (LCS). Let $L_{i,j}$ denote the length of the LCS of prefixes $X_{1..i}$ and $Y_{1..j}$. The recurrence for $L_{i,j}$ is defined as:

$$
L_{i,j} = 
\begin{cases} 
0 & \text{if } i=0 \text{ or } j=0 \\
1 + L_{i-1, j-1} & \text{if } x_i = y_j \\
\max(L_{i-1, j}, L_{i, j-1}) & \text{if } x_i \neq y_j 
\end{cases}
$$

The length of the SCS, $|S^*|$, is given by the identity:
$$|S^*| = M + N - L_{M,N}$$

To construct $S^*$, we define a path $\mathcal{P}$ in the grid from $(M, N)$ to $(0, 0)$. Let $S^{(k)}$ be the sequence of characters appended during the traceback. The transition function $\delta(i, j)$ for the traceback is:

$$
\text{Step}(i, j) = 
\begin{cases} 
(i-1, j-1), \text{ append } x_i & \text{if } x_i = y_j \\
(i-1, j), \text{ append } x_i & \text{if } x_i \neq y_j \text{ and } L_{i-1, j} \ge L_{i, j-1} \\
(i, j-1), \text{ append } y_j & \text{if } x_i \neq y_j \text{ and } L_{i-1, j} < L_{i, j-1}
\end{cases}
$$

The base cases for the traceback occur when $i=0$ or $j=0$, where we append the remaining suffix of the non-empty string.

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of two distinct phases:
1.  **Table Construction:** The DP table $D$ (or $L$) is filled using a nested loop structure. The outer loop runs $M$ times and the inner loop runs $N$ times. Each cell computation is $O(1)$. The total time is:
    $$\sum_{i=1}^{M} \sum_{j=1}^{N} \Theta(1) = \Theta(MN)$$
2.  **Traceback:** The traceback traverses the grid from $(M, N)$ to $(0, 0)$. In each step, either $i$ or $j$ (or both) is decremented. The maximum number of steps is $M+N$. Thus, the traceback is $O(M+N)$.

The total time complexity is $O(MN) + O(M+N) = O(MN)$.

### Space Complexity
The algorithm requires the storage of the DP table $L$ of dimensions $(M+1) \times (N+1)$ to facilitate the reconstruction of the string $S^*$. 
*   **Auxiliary Space:** The matrix $L$ occupies $(M+1)(N+1)$ memory cells.
*   **Total Space:** Since the traceback requires random access to the values of $L_{i,j}$ to determine the optimal path, the space complexity is strictly $\Theta(MN)$. Unlike the length-only calculation, which can be optimized to $O(\min(M, N))$ using two rows, the reconstruction phase necessitates the full matrix to maintain the decision history.