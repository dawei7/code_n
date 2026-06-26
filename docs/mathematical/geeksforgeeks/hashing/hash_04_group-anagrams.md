# Formal Mathematical Specification: Group Anagrams

## 1. Definitions and Notation

Let $\Sigma = \{'a', 'b', \dots, 'z'\}$ be the alphabet of lowercase English characters, where $|\Sigma| = 26$. Let $\Sigma^*$ denote the set of all finite strings over $\Sigma$.

*   **Input:** A finite sequence of strings $S = (s_1, s_2, \dots, s_N)$, where each $s_i \in \Sigma^*$ and $|s_i| \le K$.
*   **Anagram Equivalence Relation:** We define an equivalence relation $\sim$ on $\Sigma^*$. Two strings $s_a, s_b$ are anagrams, denoted $s_a \sim s_b$, if and only if they are permutations of each other. Formally, let $\phi: \Sigma^* \to \mathbb{N}_0^{26}$ be a frequency mapping function such that $\phi(s) = (c_a, c_b, \dots, c_z)$, where $c_j$ is the count of character $j \in \Sigma$ in string $s$. Then:
    $$s_a \sim s_b \iff \phi(s_a) = \phi(s_b)$$
*   **Output:** A partition of $S$ into equivalence classes $\{E_1, E_2, \dots, E_m\}$ such that for any $E_j$, $\forall s_x, s_y \in E_j, s_x \sim s_y$, and for any $E_i \neq E_j$, $\forall s_x \in E_i, s_y \in E_j, s_x \not\sim s_y$.
*   **State Space:** Let $\mathcal{H}$ be a hash map (associative array) mapping the domain $\mathcal{D} = \mathbb{N}_0^{26}$ to the codomain $\mathcal{R} = \mathcal{P}(\Sigma^*)$, where $\mathcal{P}$ denotes the power set.

## 2. Algebraic Characterization

The algorithm relies on the existence of a canonical representative for each equivalence class under $\sim$. 

**The Invariant:**
Let $H_i$ be the state of the hash map after processing the first $i$ strings. The invariant is:
$$\forall \text{ key } \kappa \in \text{dom}(H_i), H_i(\kappa) = \{s \in \{s_1, \dots, s_i\} \mid \phi(s) = \kappa\}$$

**Correctness via Fundamental Theorem of Arithmetic (Variant):**
While the frequency vector $\phi(s)$ is the standard canonical key, one may define a mapping $\psi: \Sigma^* \to \mathbb{Z}^+$ using the first 26 prime numbers $P = \{p_1, p_2, \dots, p_{26}\}$:
$$\psi(s) = \prod_{j=1}^{26} p_j^{c_j}$$
By the Fundamental Theorem of Arithmetic, the prime factorization of $\psi(s)$ is unique. Thus, $\psi(s_a) = \psi(s_b) \iff \phi(s_a) = \phi(s_b)$. This confirms that the grouping is mathematically sound, provided the product does not exceed the machine's word size (overflow).

**Transition:**
For each $s_{i+1}$, the update rule is:
$$H_{i+1} = H_i \cup \{ (\phi(s_{i+1}), H_i(\phi(s_{i+1})) \cup \{s_{i+1}\}) \}$$
where the union is defined as an insertion or update operation in the hash map.

## 3. Complexity Analysis

### Time Complexity
The algorithm processes $N$ strings. For each string $s_i$ of length $k_i \le K$:
1.  **Frequency Mapping:** Computing $\phi(s_i)$ requires a single pass over the string, yielding $O(k_i)$ operations.
2.  **Hash Map Access:** Inserting or updating the map involves computing a hash of the 26-tuple. Since the tuple size is constant ($|\Sigma| = 26$), the hash computation and map insertion are $O(1)$ on average.

The total time complexity $T(N, K)$ is given by the summation:
$$T(N, K) = \sum_{i=1}^{N} O(k_i) + O(N) \approx O\left(\sum_{i=1}^{N} K\right) = O(N \cdot K)$$
Thus, the algorithm is linear with respect to the total number of characters in the input.

### Space Complexity
The space complexity $S(N, K)$ is determined by the storage of the strings and the hash map:
1.  **Hash Map Storage:** We store each of the $N$ strings exactly once in the hash map. The total number of characters stored is $\sum_{i=1}^N k_i \le N \cdot K$.
2.  **Auxiliary Space:** The hash map keys (tuples of size 26) occupy $O(N \cdot 26) = O(N)$ space.

Summing these components:
$$S(N, K) = O(N \cdot K + N) = O(N \cdot K)$$
The space complexity is $O(N \cdot K)$, which is optimal as it is proportional to the size of the input data.