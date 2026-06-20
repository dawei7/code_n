# Formal Mathematical Specification: Build Suffix Array

## 1. Definitions and Notation

Let $\Sigma$ be a finite ordered alphabet. Let $S = s_0s_1\dots s_{n-1}$ be a string of length $n$ over $\Sigma$, where $s_i \in \Sigma$. We denote the empty string as $\epsilon$.

*   **Suffix:** For any $0 \le i < n$, the suffix $S_i$ is the substring $S[i \dots n-1] = s_i s_{i+1} \dots s_{n-1}$.
*   **Suffix Array:** The suffix array $SA$ is a permutation of the set of indices $\{0, 1, \dots, n-1\}$ such that the corresponding suffixes are lexicographically ordered: $S_{SA[0]} < S_{SA[1]} < \dots < S_{SA[n-1]}$.
*   **Lexicographical Order:** For two strings $A$ and $B$, $A < B$ if there exists some index $j$ such that $A[k] = B[k]$ for all $k < j$ and either ($j = |A| < |B|$) or ($j < |A|, j < |B|$ and $A[j] < B[j]$).
*   **Rank Array:** Let $R_k[i]$ denote the lexicographical rank of the prefix of length $k$ starting at index $i$. Specifically, $R_k[i] = \text{rank}(S[i \dots \min(i+k-1, n-1)])$.

## 2. Algebraic Characterization

The construction relies on the principle of prefix doubling. We define the rank of a suffix of length $2^m$ based on the ranks of two overlapping prefixes of length $2^{m-1}$.

**Base Case ($m=0$):**
For length $k=1$, the rank $R_1[i]$ is simply the ordinal value of the character $s_i$ in $\Sigma$:
$$R_1[i] = \text{ord}(s_i)$$

**Recursive Step ($m > 0$):**
To compute the rank for length $2^m$, we define a tuple $T_m[i]$ for each index $i$:
$$T_m[i] = \left( R_{2^{m-1}}[i], \quad R_{2^{m-1}}[i + 2^{m-1}] \right)$$
where we define $R_{2^{m-1}}[j] = -1$ for all $j \ge n$ (padding for suffixes shorter than $2^{m-1}$).

The rank $R_{2^m}[i]$ is the index of $T_m[i]$ in the sorted sequence of all tuples $\{T_m[0], T_m[1], \dots, T_m[n-1]\}$. Formally:
$$R_{2^m}[i] = \text{rank}(T_m[i] \mid \{T_m[0], \dots, T_m[n-1]\} \text{ sorted lexicographically})$$

**Invariant:**
After $m$ iterations, the array $R_{2^m}$ provides a total ordering of all prefixes of length $2^m$. The algorithm terminates at $m = \lceil \log_2 n \rceil$, where $R_{2^m}[i]$ induces a unique total ordering of all suffixes $S_i$, such that $R_{2^m}[SA[j]] = j$.

## 3. Complexity Analysis

### Time Complexity
The algorithm proceeds in $k = \lceil \log_2 n \rceil$ iterations. 
In each iteration $m \in \{1, \dots, k\}$:
1.  **Tuple Construction:** We construct $n$ tuples, each taking $O(1)$ time. Total: $O(n)$.
2.  **Sorting:** We sort $n$ tuples. Using a comparison-based sort, this takes $O(n \log n)$ time.
3.  **Rank Assignment:** We iterate through the sorted tuples to assign ranks, taking $O(n)$ time.

The total time complexity $T(n)$ is given by the summation:
$$T(n) = \sum_{m=1}^{\lceil \log_2 n \rceil} O(n \log n) = O(n \log n \cdot \log n) = O(n \log^2 n)$$
*Note: If Radix Sort is employed for the tuple sorting, the inner step reduces to $O(n)$, yielding a total complexity of $O(n \log n)$.*

### Space Complexity
The algorithm maintains:
1.  The input string $S$ of size $O(n)$.
2.  The rank array $R$ of size $O(n)$.
3.  The tuple array $T$ of size $O(n)$.
4.  The suffix array $SA$ of size $O(n)$.

Since all auxiliary structures are linear with respect to the input length $n$, the total space complexity is:
$$S(n) = O(n)$$