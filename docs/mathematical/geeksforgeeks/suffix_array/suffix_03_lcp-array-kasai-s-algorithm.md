# Formal Mathematical Specification: LCP Array (Kasai's Algorithm)

## 1. Definitions and Notation

Let $\Sigma$ be a finite alphabet. Let $S$ be a string of length $N$ over $\Sigma$, represented as a sequence of characters $S = s_0 s_1 \dots s_{N-1}$. 
We define the $i$-th suffix of $S$, denoted $S_i$, as the substring $S[i \dots N-1]$. The set of all suffixes is $\mathcal{S} = \{S_0, S_1, \dots, S_{N-1}\}$.

- **Suffix Array ($SA$):** A permutation of the indices $\{0, 1, \dots, N-1\}$ such that the corresponding suffixes are in lexicographical order: $S_{SA[0]} < S_{SA[1]} < \dots < S_{SA[N-1]}$.
- **Rank Array ($Rank$):** The inverse permutation of $SA$, defined as $Rank[SA[i]] = i$. Thus, $Rank[i]$ denotes the lexicographical rank of the suffix starting at index $i$.
- **LCP Array ($LCP$):** An array of length $N$ where $LCP[i]$ is defined as the length of the longest common prefix between the suffix at $SA[i]$ and the suffix at $SA[i-1]$ for $i > 0$, and $LCP[0] = 0$. Formally:
  $$LCP[i] = \text{lcp}(S_{SA[i]}, S_{SA[i-1]}) = \max \{ k : S[SA[i] \dots SA[i]+k-1] = S[SA[i-1] \dots SA[i-1]+k-1] \}$$

## 2. Algebraic Characterization

The correctness of Kasai's algorithm relies on the relationship between the LCP values of consecutive suffixes in the original string $S$. Let $h_i$ denote the LCP value of the suffix starting at index $i$ with its lexicographical predecessor in $SA$. That is, $h_i = LCP[Rank[i]]$.

**Theorem (Kasai's Lemma):** For any $i \in \{0, \dots, N-2\}$, if $Rank[i] > 0$, then:
$$h_{i+1} \geq h_i - 1$$

*Proof Sketch:* Let $j = SA[Rank[i]-1]$. By definition, $h_i = \text{lcp}(S_i, S_j)$. If $h_i > 0$, then $S[i] = S[j]$ and $S[i+1 \dots i+h_i-1] = S[j+1 \dots j+h_i-1]$. The suffix $S_{i+1}$ is $S_i$ with the first character removed. Its predecessor in the suffix array, $S_{j'}$, must satisfy $S_{j'} \leq S_{i+1} < S_i$. Since $S_j$ is the immediate predecessor of $S_i$, it follows that $S_j$ (or a suffix between $S_j$ and $S_i$) shares at least $h_i - 1$ characters with $S_{i+1}$.

**Recurrence Relation:**
The algorithm computes $h_i$ iteratively for $i = 0, \dots, N-1$. Let $k_i$ be the current length of the LCP being compared.
1. If $Rank[i] = 0$, $h_i = 0$.
2. If $Rank[i] > 0$, let $j = SA[Rank[i]-1]$. The algorithm initializes $k = \max(0, h_{i-1} - 1)$ and increments $k$ while $S[i+k] = S[j+k]$.
3. $LCP[Rank[i]] = k$.

## 3. Complexity Analysis

### Time Complexity
The time complexity is $\Theta(N)$. 
We analyze the total number of character comparisons performed by the variable $k$.
- In each iteration $i$, the variable $k$ is initialized to $\max(0, h_{i-1} - 1)$.
- The `while` loop increments $k$ only when a character match is found.
- Since $k$ is bounded by $N$, and in each step $i$ the value of $k$ decreases by at most 1 (due to the "Kasai Shrink"), the total number of decrements is at most $N$.
- Consequently, the total number of increments to $k$ across the entire execution cannot exceed $2N$.
- Since each iteration performs constant-time operations plus the increments of $k$, the total work is:
  $$T(N) = \sum_{i=0}^{N-1} (O(1) + \text{increments}_i) = O(N) + O(N) = O(N)$$

### Space Complexity
- **Auxiliary Space:** The algorithm requires storage for the $Rank$ array ($N$ integers) and the $LCP$ array ($N$ integers).
- **Total Space:** Given the input $SA$ (size $N$) and the string $S$ (size $N$), the total space complexity is $\Theta(N)$. The algorithm operates in-place relative to the required output structures, satisfying the $O(N)$ requirement.