# Formal Mathematical Specification: Count Distinct Substrings

## 1. Definitions and Notation

Let $\Sigma$ be a finite alphabet. Let $S$ be a string of length $N$ over $\Sigma$, represented as a sequence of characters $S = s_0s_1\dots s_{N-1}$, where $s_i \in \Sigma$.

*   **Substring:** A substring $S[i..j]$ is a contiguous sequence of characters $s_i s_{i+1} \dots s_j$ where $0 \le i \le j < N$. The set of all substrings of $S$ is denoted by $\mathcal{Sub}(S)$.
*   **Suffix:** A suffix $S_i$ is the substring $S[i..N-1]$ for $0 \le i < N$. The set of all suffixes is $\mathcal{Suf}(S) = \{S_0, S_1, \dots, S_{N-1}\}$.
*   **Suffix Array ($SA$):** A permutation of the indices $\{0, 1, \dots, N-1\}$ such that the suffixes are sorted lexicographically: $S_{SA[0]} < S_{SA[1]} < \dots < S_{SA[N-1]}$.
*   **LCP Array:** A sequence $LCP$ of length $N$, where $LCP[i]$ is the length of the longest common prefix between the suffix $S_{SA[i]}$ and its predecessor $S_{SA[i-1]}$ in the sorted suffix array, for $i > 0$, and $LCP[0] = 0$. Formally:
    $$LCP[i] = \max \{ k : S[SA[i]..SA[i]+k-1] = S[SA[i-1]..SA[i-1]+k-1] \}$$

## 2. Algebraic Characterization

The total number of substrings in $S$ is given by the sum of the lengths of all suffixes, as each suffix $S_i$ contributes $N-i$ substrings (its prefixes). Thus:
$$|\mathcal{Sub}(S)|_{total} = \sum_{i=0}^{N-1} (N - i) = \frac{N(N+1)}{2}$$

To find the number of *distinct* substrings, we observe that the sorted suffix array $SA$ groups identical prefixes together. For any suffix $S_{SA[i]}$, the prefixes of length $1, 2, \dots, LCP[i]$ have already been counted as prefixes of the lexicographically preceding suffix $S_{SA[i-1]}$. 

The number of unique substrings contributed by the suffix $S_{SA[i]}$ is the length of the suffix minus the length of the longest prefix it shares with its predecessor:
$$\text{Unique}(S_{SA[i]}) = |S_{SA[i]}| - LCP[i] = (N - SA[i]) - LCP[i]$$

Summing over all suffixes, the total number of distinct substrings $\mathcal{D}(S)$ is:
$$\mathcal{D}(S) = \sum_{i=0}^{N-1} (N - SA[i] - LCP[i])$$

By substituting the total substring count, we derive the identity:
$$\mathcal{D}(S) = \frac{N(N+1)}{2} - \sum_{i=0}^{N-1} LCP[i]$$

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of three primary phases:
1.  **Suffix Array Construction:** Using an optimal construction algorithm (e.g., SA-IS or prefix doubling with radix sort), the suffix array $SA$ is constructed in $T_{SA} = O(N \log N)$ or $O(N)$.
2.  **LCP Array Construction:** Using Kasai’s algorithm, we compute $LCP$ in $T_{LCP} = O(N)$. Kasai's algorithm relies on the observation that the LCP value decreases by at most 1 when moving from suffix $S_i$ to $S_{i+1}$, ensuring the pointer $h$ is incremented at most $2N$ times.
3.  **Summation:** The final summation is a linear scan of the $LCP$ array, taking $T_{sum} = O(N)$.

The total time complexity is dominated by the suffix array construction:
$$T(N) = T_{SA} + T_{LCP} + T_{sum} = O(N \log N) + O(N) + O(N) = O(N \log N)$$

### Space Complexity
The algorithm requires storage for:
*   The input string $S$: $O(N)$.
*   The Suffix Array $SA$: $O(N)$.
*   The Rank array (inverse of $SA$): $O(N)$.
*   The LCP array: $O(N)$.

The total auxiliary space complexity is:
$$S(N) = O(N) + O(N) + O(N) + O(N) = O(N)$$