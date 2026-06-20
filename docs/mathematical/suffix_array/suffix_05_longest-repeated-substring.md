# Formal Mathematical Specification: Longest Repeated Substring

## 1. Definitions and Notation

Let $\Sigma$ be a finite alphabet. Let $S$ be a string of length $n$ over $\Sigma$, represented as a sequence of characters $S = s_0s_1\dots s_{n-1}$, where $s_i \in \Sigma$. We denote the set of all substrings of $S$ as $\mathcal{Sub}(S) = \{S[i..j] \mid 0 \le i \le j < n\}$.

*   **Suffixes:** Let $Suffix_i$ denote the suffix of $S$ starting at index $i$, defined as $S[i..n-1]$. The set of all suffixes is $\mathcal{S} = \{Suffix_0, Suffix_1, \dots, S_{n-1}\}$.
*   **Suffix Array ($SA$):** The suffix array $SA$ is a permutation of the indices $\{0, 1, \dots, n-1\}$ such that the corresponding suffixes are in lexicographical order: $Suffix_{SA[0]} < Suffix_{SA[1]} < \dots < Suffix_{SA[n-1]}$.
*   **Longest Common Prefix ($LCP$):** For any two strings $A$ and $B$, $LCP(A, B)$ is the length of the longest string $P$ such that $P$ is a prefix of both $A$ and $B$.
*   **LCP Array:** The array $LCP$ of length $n$ is defined such that $LCP[i] = LCP(Suffix_{SA[i-1]}, Suffix_{SA[i]})$ for $1 \le i < n$, with $LCP[0] = 0$.
*   **Objective:** We seek a substring $T \in \mathcal{Sub}(S)$ such that there exist indices $i \neq j$ where $S[i..i+|T|-1] = S[j..j+|T|-1] = T$, and $|T|$ is maximized.

## 2. Algebraic Characterization

The correctness of the algorithm relies on the following theorem:

**Theorem:** The length of the longest repeated substring in $S$ is given by:
$$\max_{1 \le i < n} LCP[i]$$

**Proof Sketch:**
1.  **Sufficiency:** If $LCP[i] = k > 0$, then the prefix of length $k$ is common to $Suffix_{SA[i-1]}$ and $Suffix_{SA[i]}$. Since these are distinct suffixes starting at different positions in $S$, the prefix of length $k$ is a repeated substring.
2.  **Necessity:** Suppose the longest repeated substring $T$ has length $L$. Then $T$ is a prefix of two distinct suffixes $Suffix_u$ and $Suffix_v$ (where $u \neq v$). In the sorted suffix array, let $rank[u]$ and $rank[v]$ be the positions of these suffixes. Without loss of generality, assume $rank[u] < rank[v]$. By the properties of lexicographical sorting, $T$ must be a prefix of all suffixes $Suffix_{SA[k]}$ for $rank[u] \le k \le rank[v]$. Specifically, $T$ is a prefix of $Suffix_{SA[k-1]}$ and $Suffix_{SA[k]}$ for all $k$ in this range. Thus, $LCP[k] \ge |T|$ for some $k$, implying $\max(LCP) \ge L$.

**Kasai’s Algorithm Invariant:**
To compute the $LCP$ array in $O(n)$, we utilize the height property. Let $h_i$ be the $LCP$ value of the suffix starting at $i$ and its predecessor in the suffix array. The algorithm maintains the invariant:
$$h_{SA[rank[i]]} \ge h_{SA[rank[i-1]]} - 1$$
This allows the pointer $h$ to be decremented at most $n$ times and incremented at most $2n$ times, ensuring linear time complexity.

## 3. Complexity Analysis

### Time Complexity
The total time complexity is $T(n) = T_{SA}(n) + T_{LCP}(n)$.
1.  **Suffix Array Construction:** Using standard sorting algorithms (e.g., Quicksort or Mergesort) on suffixes, the comparison of two suffixes takes $O(n)$. Sorting $n$ items takes $O(n \log n)$ comparisons. Thus, $T_{SA}(n) = O(n^2 \log n)$ naively, but using prefix doubling or induced sorting, we achieve $T_{SA}(n) = O(n \log n)$.
2.  **LCP Array Construction (Kasai's):** The variable $h$ is incremented at most $n$ times and decremented at most $n$ times across the entire execution of the loop. Each character comparison is $O(1)$. Thus, $T_{LCP}(n) = O(n)$.
3.  **Total:** $T(n) = O(n \log n) + O(n) = O(n \log n)$.

### Space Complexity
The algorithm requires:
*   The string $S$: $O(n)$
*   The Suffix Array $SA$: $O(n)$
*   The Rank array: $O(n)$
*   The LCP array: $O(n)$
Total auxiliary space is $S(n) = O(n)$, which is optimal for this problem.