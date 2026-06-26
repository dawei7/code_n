# Formal Mathematical Specification: Longest Substring Without Repeating Characters

## 1. Definitions and Notation

Let $\Sigma$ be a finite alphabet (e.g., ASCII or Unicode). A string $s$ of length $n$ is defined as a sequence of characters $s = (s_0, s_1, \dots, s_{n-1})$, where $s_i \in \Sigma$.

*   **Substring:** A substring $s[i..j]$ is a contiguous subsequence of $s$ starting at index $i$ and ending at index $j$, where $0 \le i \le j < n$. The length of the substring is $L = j - i + 1$.
*   **Distinctness Property:** A substring $s[i..j]$ is defined as *distinct* if and only if the mapping $f: \{i, i+1, \dots, j\} \to \Sigma$ defined by $f(k) = s_k$ is injective. That is, $\forall p, q \in \{i, \dots, j\}, p \neq q \implies s_p \neq s_q$.
*   **Objective:** We seek the value $\mathcal{L} = \max \{ j - i + 1 \mid 0 \le i \le j < n \text{ and } s[i..j] \text{ is distinct} \}$.
*   **State Space:** Let $\mathcal{M}: \Sigma \to \mathbb{Z} \cup \{-\infty\}$ be a hash map (or partial function) where $\mathcal{M}(c)$ stores the most recent index $k$ such that $s_k = c$. Let $L \in \{0, \dots, n-1\}$ denote the left boundary of the sliding window.

## 2. Algebraic Characterization

The algorithm maintains a sliding window $[L, R]$ such that the substring $s[L..R]$ is always distinct. We define the state transition at each step $R \in \{0, \dots, n-1\}$ as follows:

1.  **Update Rule for $L$:**
    When considering character $s_R$, if $s_R$ has appeared previously at index $k = \mathcal{M}(s_R)$, the window must be contracted to maintain the distinctness property. The new left boundary $L_{R}$ is defined by:
    $$L_R = \max(L_{R-1}, \mathcal{M}(s_R) + 1)$$
    where $L_{-1} = 0$. If $s_R \notin \text{domain}(\mathcal{M})$, we treat $\mathcal{M}(s_R) = -1$.

2.  **Update Rule for $\mathcal{M}$:**
    After processing $s_R$, the map is updated:
    $$\mathcal{M}_{R}(c) = \begin{cases} R & \text{if } c = s_R \\ \mathcal{M}_{R-1}(c) & \text{otherwise} \end{cases}$$

3.  **Loop Invariant:**
    At the end of each iteration $R$, the following invariant holds:
    $$\forall x, y \in \{L_R, \dots, R\}, x \neq y \implies s_x \neq s_y$$
    The maximum length $\mathcal{L}$ is updated as:
    $$\mathcal{L}_R = \max(\mathcal{L}_{R-1}, R - L_R + 1)$$

## 3. Complexity Analysis

### Time Complexity
The algorithm iterates through the string $s$ exactly once, where $R$ ranges from $0$ to $n-1$. 
*   In each iteration, the operations performed are:
    1.  A hash map lookup: $\mathcal{M}(s_R)$, which is $O(1)$ on average.
    2.  A comparison and assignment: $O(1)$.
    3.  A map update: $\mathcal{M}[s_R] \leftarrow R$, which is $O(1)$ on average.
*   The total time complexity is the summation of work over $n$ steps:
    $$T(n) = \sum_{R=0}^{n-1} O(1) = O(n)$$
Thus, the algorithm is linear with respect to the input length $n$.

### Space Complexity
The space complexity is determined by the storage requirements of the hash map $\mathcal{M}$.
*   The map $\mathcal{M}$ stores at most one entry for each unique character present in the string $s$.
*   Let $\sigma = |\Sigma|$ be the size of the alphabet. The number of entries in $\mathcal{M}$ is bounded by $\min(n, \sigma)$.
*   Therefore, the auxiliary space complexity is $O(\min(n, \sigma))$. In the context of fixed alphabets (e.g., ASCII where $\sigma = 128$), this is effectively $O(1)$. In the general case, it is $O(\sigma)$.