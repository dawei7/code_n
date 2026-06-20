# Formal Mathematical Specification: Palindromic Partitioning (Min Cuts)

## 1. Definitions and Notation

Let $\Sigma$ be a finite alphabet. Let $s = s_0 s_1 \dots s_{n-1}$ be a string of length $n$ where $s_i \in \Sigma$. 
A substring $s[i..j]$ is defined as the sequence of characters $s_i s_{i+1} \dots s_j$ for $0 \le i \le j < n$.

**Definition 1 (Palindrome):** A string $P$ is a palindrome if $P = P^R$, where $P^R$ denotes the reversal of $P$. Formally, $s[i..j]$ is a palindrome if and only if $s_{i+k} = s_{j-k}$ for all $0 \le k \le j-i$.

**Definition 2 (Partition):** A partition of $s$ is a sequence of substrings $(p_1, p_2, \dots, p_k)$ such that their concatenation yields $s$. We define the set of all valid palindromic partitions as:
$$\mathcal{P}(s) = \{ (p_1, \dots, p_k) \mid \forall m \in \{1, \dots, k\}, p_m \text{ is a palindrome and } \bigoplus_{m=1}^k p_m = s \}$$

**Definition 3 (Objective):** We seek to minimize the number of cuts, which is equivalent to minimizing $(k-1)$, where $k$ is the number of palindromic substrings in the partition. Let $f(i)$ be the minimum number of cuts required to partition the suffix $s[i..n-1]$. The goal is to compute $f(0)$.

## 2. Algebraic Characterization

The algorithm relies on two distinct recurrence relations.

### Stage 1: Palindrome Precomputation
Let $P(i, j)$ be a boolean indicator function such that $P(i, j) = 1$ if $s[i..j]$ is a palindrome, and $P(i, j) = 0$ otherwise. The recurrence is defined as:
$$P(i, j) = \begin{cases} 1 & \text{if } i \ge j \\ (s_i = s_j) \land P(i+1, j-1) & \text{if } i < j \end{cases}$$
This defines a dynamic programming table of size $n \times n$.

### Stage 2: Min-Cut Optimization
Let $dp[i]$ denote the minimum number of cuts required for the suffix $s[i..n-1]$. The base case is $dp[n] = -1$ (representing the empty suffix requiring no further cuts, adjusted for the final summation). The recurrence is:
$$dp[i] = \min \{ 1 + dp[j+1] \mid i \le j < n, P(i, j) = 1 \}$$
where the final answer is $dp[0]$. Note that if $P(i, n-1) = 1$, the cost is $0$ (no cuts needed for the entire suffix).

**Invariants:**
1. At the completion of Stage 1, for all $0 \le i \le j < n$, $P(i, j)$ correctly identifies palindromic substrings.
2. At the completion of Stage 2, $dp[i]$ represents $\min_{k} \{ (\text{number of cuts for } s[i..n-1]) \}$.

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of two stages:
1. **Stage 1:** The computation of $P(i, j)$ involves filling an $n \times n$ table. Each entry $(i, j)$ is computed in $O(1)$ time given the results of $(i+1, j-1)$. The total time is:
   $$\sum_{i=0}^{n-1} \sum_{j=i}^{n-1} O(1) = \frac{n(n+1)}{2} = O(n^2)$$
2. **Stage 2:** The computation of $dp[i]$ involves iterating over $j$ from $i$ to $n-1$. The total time is:
   $$\sum_{i=0}^{n-1} \sum_{j=i}^{n-1} O(1) = O(n^2)$$
Thus, the total time complexity is $O(n^2) + O(n^2) = O(n^2)$.

### Space Complexity
1. **Auxiliary Space:** The table $P$ requires $O(n^2)$ space to store boolean values. The array $dp$ requires $O(n)$ space.
2. **Total Space:** The dominant term is the $n \times n$ matrix, resulting in $O(n^2)$ space complexity. 

*Note:* While the space can be reduced to $O(n)$ by computing palindromic status on-the-fly using the "expand-around-center" technique, the standard dynamic programming approach specified here maintains $O(n^2)$ space.