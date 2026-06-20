# Formal Mathematical Specification: Pattern Search with Suffix Array

## 1. Definitions and Notation

Let $\Sigma$ be a finite ordered alphabet. Let $T$ be a text string of length $N$ over $\Sigma$, defined as a sequence $T = t_0 t_1 \dots t_{N-1}$, where $t_i \in \Sigma$. We denote the substring of $T$ starting at index $i$ and ending at index $j$ as $T[i \dots j]$.

A **suffix** of $T$ starting at index $i$ is defined as $S_i = T[i \dots N-1]$ for $0 \le i < N$. 
The **Suffix Array** $A$ is a permutation of the set of indices $\{0, 1, \dots, N-1\}$ such that the sequence of suffixes is lexicographically ordered:
$$S_{A[0]} < S_{A[1]} < \dots < S_{A[N-1]}$$
where $<$ denotes the standard lexicographical order on strings.

Given a pattern $P$ of length $M$, where $P = p_0 p_1 \dots p_{M-1}$, we define the search problem as finding the set of indices $\mathcal{I} = \{i \mid P \text{ is a prefix of } S_i\}$. Since the suffixes are sorted in $A$, all suffixes having $P$ as a prefix form a contiguous range $[L, R]$ in $A$.

## 2. Algebraic Characterization

The correctness of the algorithm relies on the monotonicity of the lexicographical order. We define the predicate $\text{is\_prefix}(P, S)$ as:
$$\text{is\_prefix}(P, S) \iff S[0 \dots M-1] = P$$

Because $A$ is sorted, the set of indices $i$ such that $P$ is a prefix of $S_{A[i]}$ corresponds to the interval $[L, R]$ where:
1. $L = \min \{ k \in \{0, \dots, N-1\} \mid S_{A[k]} \ge P \}$
2. $R = \max \{ k \in \{0, \dots, N-1\} \mid S_{A[k]} \text{ starts with } P \}$

We utilize binary search to identify these boundaries. Let $f(k)$ be the comparison function between $P$ and $S_{A[k]}$:
$$f(k) = \begin{cases} -1 & \text{if } S_{A[k]} < P \\ 0 & \text{if } P \text{ is a prefix of } S_{A[k]} \\ 1 & \text{if } S_{A[k]} > P \text{ and } P \text{ is not a prefix} \end{cases}$$

The search space is partitioned by the binary search invariant:
- **Invariant:** At each step of the binary search on the interval $[lo, hi]$, the target boundary lies within the current range.
- **Transition:** For a midpoint $mid = \lfloor \frac{lo + hi}{2} \rfloor$:
  - If $S_{A[mid]} < P$, then $lo = mid + 1$.
  - Otherwise, $hi = mid$.

This converges to the smallest index $L$ such that $S_{A[L]} \ge P$. A symmetric binary search is performed to find the upper bound $R$ where the prefix condition fails.

## 3. Complexity Analysis

### Time Complexity
The algorithm performs two binary searches over the suffix array $A$, which has size $N$.
1. **Binary Search Steps:** Each binary search performs $\lceil \log_2 N \rceil$ iterations to narrow the search space to a single index.
2. **Comparison Cost:** In each iteration, we perform a lexicographical comparison between $P$ and a suffix $S_{A[mid]}$. The comparison $P \stackrel{?}{=} S_{A[mid]}[0 \dots M-1]$ requires at most $M$ character comparisons.
3. **Total Work:** The total time complexity $T(N, M)$ is given by:
   $$T(N, M) = \Theta(\log N \cdot M)$$
   This is derived from the summation of work over the depth of the binary search tree, where each node performs $O(M)$ work.

### Space Complexity
- **Auxiliary Space:** The algorithm maintains only a constant number of pointers ($lo, hi, mid, L, R$), resulting in $O(1)$ auxiliary space complexity.
- **Total Space:** The total space complexity is $O(N)$, dominated by the storage of the pre-computed Suffix Array $A$ of length $N$. The input string $T$ also occupies $O(N)$ space.