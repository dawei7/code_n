# Formal Mathematical Specification: Optimal Binary Search Tree

## 1. Definitions and Notation

Let $K = \{k_1, k_2, \dots, k_n\}$ be a set of $n$ keys sorted such that $k_1 < k_2 < \dots < k_n$.
Let $F = \{f_1, f_2, \dots, f_n\}$ be a set of associated frequencies, where $f_i \in \mathbb{R}^+$ represents the search frequency of key $k_i$.

A Binary Search Tree (BST) $T$ is defined as a rooted tree where for any node $u$ with key $k_i$, all nodes in the left subtree have keys $k_j < k_i$ and all nodes in the right subtree have keys $k_m > k_i$.

The **search cost** of a node $u$ at depth $d(u)$ (where the root is at depth 1) is defined as $f_u \cdot d(u)$. The total cost of a tree $T$ is:
$$C(T) = \sum_{i=1}^n f_i \cdot d(k_i)$$

We define the weight of a subtree containing keys $k_i$ through $k_j$ as the sum of their frequencies:
$$w(i, j) = \sum_{m=i}^j f_m$$

The objective is to find a tree $T^*$ such that $C(T^*) = \min_{T \in \mathcal{T}} C(T)$, where $\mathcal{T}$ is the set of all valid BSTs for the given keys.

## 2. Algebraic Characterization

We define the state $dp[i][j]$ as the minimum search cost of a BST constructed from the keys $\{k_i, \dots, k_j\}$, where $1 \le i \le j \le n$. 

For a sub-problem defined by the interval $[i, j]$, we choose a root $k_r$ where $i \le r \le j$. By the properties of a BST, the left subtree must contain keys $\{k_i, \dots, k_{r-1}\}$ and the right subtree must contain keys $\{k_{r+1}, \dots, k_j\}$.

When these subtrees are attached to the root $k_r$, every node in the subtrees increases its depth by 1. Consequently, the total cost increases by the sum of the frequencies of all nodes in the subtrees plus the frequency of the root itself, which is exactly $w(i, j)$.

The recurrence relation is given by:
$$dp[i][j] = \min_{i \le r \le j} \left( dp[i][r-1] + dp[r+1][j] \right) + w(i, j)$$

**Base Cases:**
1. If $i > j$, the tree is empty: $dp[i][j] = 0$.
2. If $i = j$, the tree consists of a single node: $dp[i][i] = f_i$.

The final solution is $dp[1][n]$.

## 3. Complexity Analysis

### Time Complexity
The algorithm employs a dynamic programming approach with three nested loops.
1. The outer loop iterates over the length of the interval $L = j - i + 1$, where $1 \le L \le n$.
2. The middle loop iterates over the starting index $i$, where $1 \le i \le n - L + 1$.
3. The inner loop iterates over the possible roots $r$, where $i \le r \le j$.

The total number of operations is proportional to:
$$T(n) = \sum_{L=1}^n \sum_{i=1}^{n-L+1} L = \sum_{L=1}^n (n - L + 1) \cdot L$$
Using the identity for the sum of squares and arithmetic series, this evaluates to:
$$T(n) = (n+1)\sum L - \sum L^2 = (n+1)\frac{n(n+1)}{2} - \frac{n(n+1)(2n+1)}{6} = \frac{n(n+1)(n+2)}{6}$$
Thus, $T(n) = \Theta(n^3)$.

### Space Complexity
The algorithm maintains a DP table of size $n \times n$ to store the results of sub-problems $dp[i][j]$. Additionally, a prefix sum array of size $n+1$ is used to compute $w(i, j)$ in $O(1)$ time.
The total space complexity is:
$$S(n) = O(n^2) + O(n) = O(n^2)$$
This is optimal for the standard DP formulation, as we must store the results of the $O(n^2)$ possible sub-intervals.