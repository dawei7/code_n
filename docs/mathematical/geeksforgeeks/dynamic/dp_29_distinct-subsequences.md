# Formal Mathematical Specification: Distinct Subsequences

## 1. Definitions and Notation

Let $\Sigma$ be a finite alphabet. We are given two strings $s \in \Sigma^M$ and $t \in \Sigma^N$, where $M = |s|$ and $N = |t|$. We denote the $i$-th character of $s$ as $s_i$ (for $1 \le i \le M$) and the $j$-th character of $t$ as $t_j$ (for $1 \le j \le N$).

We define the state space $\mathcal{S}$ as the set of all pairs of indices $(i, j)$ such that $0 \le i \le M$ and $0 \le j \le N$. Let $f(i, j)$ be a function $f: \mathcal{S} \to \mathbb{N}_0$ representing the number of distinct subsequences of the prefix $s[1 \dots i]$ that are equal to the prefix $t[1 \dots j]$.

The objective is to compute $f(M, N)$.

## 2. Algebraic Characterization

The function $f(i, j)$ is defined by the following recurrence relation, derived from the principle of inclusion-exclusion on the choice of including or excluding the character $s_i$:

**Base Cases:**
1. $f(i, 0) = 1$ for all $0 \le i \le M$: An empty target string $t[1 \dots 0]$ is a subsequence of any prefix of $s$ exactly once (by deleting all characters).
2. $f(0, j) = 0$ for all $1 \le j \le N$: A non-empty target string cannot be formed from an empty source string.

**Recursive Step:**
For $i \ge 1$ and $j \ge 1$:
$$f(i, j) = \begin{cases} f(i-1, j) + f(i-1, j-1) & \text{if } s_i = t_j \\ f(i-1, j) & \text{if } s_i \neq t_j \end{cases}$$

**Space-Optimized Formulation:**
Let $dp_j^{(i)}$ denote the value of $f(i, j)$. Since $dp_j^{(i)}$ depends only on values from the previous iteration $i-1$, we can reduce the state to a 1D array $dp[j]$. To maintain correctness when updating in-place, we iterate $j$ in descending order ($N$ down to $1$):
$$dp[j] \leftarrow \begin{cases} dp[j] + dp[j-1] & \text{if } s_i = t_j \\ dp[j] & \text{if } s_i \neq t_j \end{cases}$$
The invariant maintained at the start of each iteration $i$ is that $dp[j] = f(i-1, j)$. After the update, $dp[j] = f(i, j)$.

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of a nested loop structure. The outer loop iterates over the source string $s$ of length $M$, and the inner loop iterates over the target string $t$ of length $N$. 

The total number of operations $T(M, N)$ is given by the summation:
$$T(M, N) = \sum_{i=1}^{M} \sum_{j=1}^{N} \Theta(1) = \Theta(M \cdot N)$$
Given that each iteration performs a constant number of comparisons and additions, the time complexity is $O(M \cdot N)$.

### Space Complexity
The algorithm utilizes a 1D array $dp$ of size $N+1$ to store the counts of subsequences. 

1. **Auxiliary Space:** The space required for the DP table is $O(N)$.
2. **Total Space:** Including the input strings $s$ and $t$, the space complexity is $O(M + N)$. However, in the context of dynamic programming auxiliary space, the complexity is strictly $O(N)$.

The space optimization is valid because the update $dp[j] = dp[j] + dp[j-1]$ requires the value of $dp[j-1]$ from the *previous* iteration ($i-1$). By iterating $j$ from $N$ down to $1$, we ensure that $dp[j-1]$ has not yet been updated for the current $i$, effectively preserving the state $f(i-1, j-1)$.