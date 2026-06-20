# Formal Mathematical Specification: Count Distinct Elements in Every Window

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{N-1}]$ be a sequence of elements where $a_i \in \mathcal{U}$ for some universe $\mathcal{U}$. Let $K \in \mathbb{Z}^+$ be the fixed window size such that $1 \le K \le N$.

A sliding window of size $K$ starting at index $i$ is defined as the subsequence $W_i = [a_i, a_{i+1}, \dots, a_{i+K-1}]$ for $0 \le i \le N-K$.

We define the following:
*   **Frequency Map:** A function $f_i: \mathcal{U} \to \mathbb{N}_0$ representing the count of each element in the window $W_i$, defined as:
    $$f_i(x) = \sum_{j=i}^{i+K-1} \mathbb{I}(a_j = x)$$
    where $\mathbb{I}(\cdot)$ is the indicator function.
*   **Support Set:** The set of distinct elements in window $W_i$ is the support of $f_i$:
    $$\text{supp}(f_i) = \{x \in \mathcal{U} \mid f_i(x) > 0\}$$
*   **Target Output:** The sequence $D = [d_0, d_1, \dots, d_{N-K}]$, where $d_i = |\text{supp}(f_i)|$.

## 2. Algebraic Characterization

The algorithm relies on the incremental update of the frequency map $f_i$ to $f_{i+1}$. Given $f_i$, the transition to $f_{i+1}$ involves the removal of $a_i$ and the addition of $a_{i+K}$:

$$f_{i+1}(x) = f_i(x) - \mathbb{I}(x = a_i) + \mathbb{I}(x = a_{i+K})$$

The distinct count $d_{i+1}$ is derived from $d_i$ based on the state of the frequency map:

1.  **Update for $a_{i+K}$:** If $f_i(a_{i+K}) = 0$, then $d_{i+1} = d_i + 1$. Otherwise, $d_{i+1} = d_i$.
2.  **Update for $a_i$:** If $f_{i+1}(a_i) = 0$, then $d_{i+1} = d_{i+1} - 1$. Otherwise, $d_{i+1}$ remains unchanged.

**Loop Invariant:**
At the start of each iteration $i \in \{0, \dots, N-K\}$, the map $M$ satisfies:
$$\forall x \in \mathcal{U}, M(x) = f_i(x) \quad \text{and} \quad |M| = d_i$$
where $|M|$ denotes the number of keys in the map with a non-zero value. The deletion operation `del map[old]` ensures that the invariant $|M| = \sum_{x \in \mathcal{U}} \mathbb{I}(M(x) > 0)$ is maintained.

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of two phases:
1.  **Initialization:** Constructing $f_0$ requires $K$ insertions into the hash map. Assuming a uniform hash distribution, each insertion is $O(1)$ on average. Total: $O(K)$.
2.  **Sliding Phase:** The loop runs for $N-K$ iterations. In each iteration $i$:
    *   One insertion and one deletion/update occur in the map.
    *   The size of the map is queried.
    *   Each operation is $O(1)$ amortized.

The total time complexity $T(N)$ is:
$$T(N) = O(K) + \sum_{i=0}^{N-K-1} O(1) = O(K + (N-K)) = O(N)$$
Thus, the algorithm is linear with respect to the input size $N$.

### Space Complexity
The space complexity $S(N)$ is dominated by the storage of the frequency map $M$.
*   The map stores at most $K$ distinct elements at any time, as the window size is fixed at $K$.
*   The auxiliary space required is $O(K)$.
*   The output array requires $O(N-K+1)$ space.

Excluding the output, the auxiliary space complexity is $O(K)$. If the universe $\mathcal{U}$ is large, the hash map effectively maps the active elements to a space proportional to the window size, satisfying the $O(K)$ requirement.