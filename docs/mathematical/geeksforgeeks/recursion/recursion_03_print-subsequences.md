# Formal Mathematical Specification: Print All Subsequences

## 1. Definitions and Notation

Let $S = \{s_0, s_1, \dots, s_{n-1}\}$ be a set of $n$ unique elements represented as an ordered sequence (array) of length $n$. 

*   **Power Set:** The objective is to construct the power set $\mathcal{P}(S)$, defined as the set of all subsets of $S$, where $|\mathcal{P}(S)| = 2^n$.
*   **State Space:** A state is defined by the tuple $(i, \sigma)$, where $i \in \{0, 1, \dots, n\}$ denotes the current index in $S$ being considered, and $\sigma \in \mathcal{P}(S_i)$ is the partial subsequence constructed from the prefix $S_i = \{s_0, \dots, s_{i-1}\}$.
*   **Decision Space:** At each index $i$, we define a decision variable $d_i \in \{0, 1\}$, where $d_i = 1$ denotes the inclusion of $s_i$ in the subsequence, and $d_i = 0$ denotes exclusion.
*   **Output:** The algorithm produces a collection $\mathcal{R} = \{ \sigma_1, \sigma_2, \dots, \sigma_{2^n} \}$, where each $\sigma_j$ corresponds to a unique vector $(d_0, d_1, \dots, d_{n-1}) \in \{0, 1\}^n$.

## 2. Algebraic Characterization

The algorithm is governed by a recursive function $f(i, \sigma)$, which explores the binary tree of decisions. The correctness is established by the following recurrence relation:

Let $f(i, \sigma)$ be the set of all subsequences obtainable from index $i$ given the current prefix $\sigma$:

$$
f(i, \sigma) = 
\begin{cases} 
\{\sigma\} & \text{if } i = n \\
f(i+1, \sigma) \cup f(i+1, \sigma \cup \{s_i\}) & \text{if } 0 \le i < n 
\end{cases}
$$

**Invariants:**
1. **Completeness:** For any subset $A \subseteq S$, there exists a unique path in the recursion tree such that the sequence of decisions $(d_0, \dots, d_{n-1})$ satisfies $d_j = 1 \iff s_j \in A$.
2. **Termination:** Since the index $i$ strictly increases by 1 at each recursive step, the depth of the recursion tree is exactly $n$. The base case $i=n$ is guaranteed to be reached in finite time.

The total set of subsequences is given by the union of all leaf nodes in the recursion tree:
$$\mathcal{R} = \bigcup_{\text{paths } \pi} \text{leaf}(\pi) = \mathcal{P}(S)$$

## 3. Complexity Analysis

### Time Complexity
The recursion tree is a complete binary tree of depth $n$. The number of nodes in a complete binary tree of depth $n$ is $2^{n+1} - 1$. 

At each leaf node (where $i=n$), the algorithm performs a copy operation of the current path $\sigma$. In the worst case, $|\sigma| = n$. The number of leaf nodes is exactly $2^n$. 

The total time complexity $T(n)$ is the sum of the work at each node:
$$T(n) = \sum_{k=0}^{n-1} 2^k \cdot O(1) + 2^n \cdot O(n)$$
The first term represents the internal nodes (constant work), and the second term represents the leaf nodes (copying the subsequence).
$$T(n) = O(2^n) + O(n \cdot 2^n) = O(n \cdot 2^n)$$
Thus, the time complexity is $O(n \cdot 2^n)$.

### Space Complexity
The space complexity is determined by two components:
1. **Recursion Stack:** The maximum depth of the recursion is $n$. Thus, the call stack requires $O(n)$ space.
2. **Auxiliary Space:** The `current_path` array stores at most $n$ elements, requiring $O(n)$ space.

The total auxiliary space complexity is $O(n)$. 

*Note: If the output $\mathcal{R}$ is considered part of the space requirement, the total space complexity is $O(n \cdot 2^n)$, as there are $2^n$ subsets, each of average length $n/2$.*