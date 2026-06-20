# Formal Mathematical Specification: Longest Palindromic Subsequence

## 1. Definitions and Notation

Let $\Sigma$ be a finite alphabet. Let $s = s_0s_1\dots s_{n-1}$ be a string of length $n$ over $\Sigma$, where $s_i \in \Sigma$. 
A subsequence of $s$ is a string $z$ obtained by deleting zero or more characters from $s$. Formally, $z$ is a subsequence if there exists a strictly increasing sequence of indices $0 \le i_1 < i_2 < \dots < i_k < n$ such that $z_j = s_{i_j}$ for all $1 \le j \le k$.

A string $z$ is a palindrome if $z = z^R$, where $z^R$ denotes the reversal of $z$. 
We define the set $\mathcal{P}(s)$ as the set of all palindromic subsequences of $s$. The objective is to find the length of the longest such subsequence:
$$LPS(s) = \max_{z \in \mathcal{P}(s)} |z|$$

We define the state space $\mathcal{S}$ as a two-dimensional matrix $D \in \mathbb{Z}^{n \times n}$, where each entry $D_{i,j}$ represents the length of the longest palindromic subsequence of the substring $s[i \dots j]$, defined for $0 \le i, j < n$.

## 2. Algebraic Characterization

The problem exhibits optimal substructure and overlapping subproblems, allowing for a recursive formulation. For any substring $s[i \dots j]$ where $i \le j$:

**Base Cases:**
1. If $i = j$, the substring is a single character, which is a palindrome of length 1:
   $$D_{i,i} = 1$$
2. If $i > j$, the substring is empty, yielding a length of 0:
   $$D_{i,j} = 0$$

**Recursive Step:**
For $i < j$, the value $D_{i,j}$ is determined by the relationship between the boundary characters $s_i$ and $s_j$:
1. If $s_i = s_j$, the characters $s_i$ and $s_j$ can be included in the palindrome, extending the longest palindromic subsequence of the inner substring $s[i+1 \dots j-1]$ by 2:
   $$D_{i,j} = D_{i+1, j-1} + 2$$
2. If $s_i \neq s_j$, the longest palindromic subsequence must be contained within either $s[i+1 \dots j]$ or $s[i \dots j-1]$:
   $$D_{i,j} = \max(D_{i+1, j}, D_{i, j-1})$$

The final solution is given by $D_{0, n-1}$.

## 3. Complexity Analysis

### Time Complexity
The algorithm computes the entries of the $n \times n$ matrix $D$. The computation proceeds by increasing the length of the substring $L = j - i + 1$, where $L$ ranges from $2$ to $n$. 

For each length $L$, the number of possible starting positions $i$ is $n - L + 1$. The total number of states computed is:
$$\sum_{L=2}^{n} (n - L + 1) = \sum_{k=1}^{n-1} k = \frac{n(n-1)}{2}$$
Since each state $D_{i,j}$ is computed in $O(1)$ time using the recurrence relation, the total time complexity is:
$$T(n) = \sum_{L=2}^{n} O(n - L + 1) = O(n^2)$$

### Space Complexity
The algorithm requires a two-dimensional array $D$ of size $n \times n$ to store the results of subproblems. 
- **Auxiliary Space:** The space required for the DP table is $n^2$ integers. Thus, the space complexity is $O(n^2)$.
- **Total Space:** The total space complexity is $O(n^2)$, as the input string occupies $O(n)$ and the DP table occupies $O(n^2)$. 

*Note:* While space can be optimized to $O(n)$ by observing that the computation of length $L$ only requires values from lengths $L-1$ and $L-2$, the standard implementation provided utilizes $O(n^2)$ for clarity and ease of reconstruction.