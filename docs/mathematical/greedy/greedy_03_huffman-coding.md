# Formal Mathematical Specification: Huffman Coding

## 1. Definitions and Notation

Let $\Sigma = \{c_1, c_2, \dots, c_n\}$ be a finite alphabet of $n$ unique symbols. Each symbol $c_i \in \Sigma$ is associated with a probability or frequency $f_i \in \mathbb{R}^+$. We define the input as a set of pairs $S = \{(c_1, f_1), (c_2, f_2), \dots, (c_n, f_n)\}$.

A **binary code** is a function $C: \Sigma \to \{0, 1\}^*$, where $\{0, 1\}^*$ is the set of all finite-length binary strings. The length of the codeword for symbol $c_i$ is denoted by $\ell_i = |C(c_i)|$.

The objective is to construct a **prefix-free code** (or instantaneous code), which satisfies the Kraft's inequality and the condition that for any $c_i, c_j \in \Sigma$ where $i \neq j$, $C(c_i)$ is not a prefix of $C(c_j)$. This is represented by a binary tree $T$ where:
- Each leaf node corresponds to exactly one $c_i \in \Sigma$.
- The path from the root to the leaf $c_i$ defines the codeword $C(c_i)$, where a left branch corresponds to '0' and a right branch to '1'.

The **expected code length** $L(T)$ is defined as:
$$L(T) = \sum_{i=1}^{n} f_i \cdot \ell_i$$
The goal is to find a tree $T^*$ such that $L(T^*) = \min_{T \in \mathcal{T}} L(T)$, where $\mathcal{T}$ is the set of all possible binary trees with $n$ leaves.

## 2. Algebraic Characterization

The Huffman algorithm constructs $T$ bottom-up using a greedy strategy based on the following recurrence. Let $\mathcal{F}$ be a forest of trees. Initially, $\mathcal{F} = \{T_1, \dots, T_n\}$ where each $T_i$ is a single node with weight $w(T_i) = f_i$.

**Greedy Choice Property:**
At each step, we select two trees $T_a, T_b \in \mathcal{F}$ such that their weights are minimal:
$$w(T_a) = \min_{T \in \mathcal{F}} w(T), \quad w(T_b) = \min_{T \in \mathcal{F} \setminus \{T_a\}} w(T)$$
We form a new tree $T_{new}$ with children $T_a$ and $T_b$, and weight:
$$w(T_{new}) = w(T_a) + w(T_b)$$
The update rule for the forest is $\mathcal{F} \leftarrow (\mathcal{F} \setminus \{T_a, T_b\}) \cup \{T_{new}\}$. This process repeats until $|\mathcal{F}| = 1$.

**Optimality Invariant:**
The Huffman algorithm maintains the invariant that at any step $k$, the forest $\mathcal{F}_k$ consists of optimal prefix-free trees for the current set of weights. By the **Huffman-Shannon-Fano theorem**, the greedy choice of merging the two least-frequent nodes is optimal because it minimizes the weighted path length of the resulting tree, satisfying the recurrence:
$$L(T_{new}) = L(T_a) + L(T_b) + w(T_a) + w(T_b)$$
where the additional cost $w(T_a) + w(T_b)$ represents the increment in path length for all leaves contained within the merged subtrees.

## 3. Complexity Analysis

### Time Complexity
The algorithm's execution is dominated by the priority queue operations.
1. **Initialization:** Building the initial min-heap from $n$ elements takes $O(n)$ time using Floyd's heap construction algorithm.
2. **Iteration:** The algorithm performs $n-1$ iterations. In each iteration:
   - Two `extract-min` operations are performed: $2 \cdot O(\log n) = O(\log n)$.
   - One `insert` operation is performed: $O(\log n)$.
   - Total work per iteration is $O(\log n)$.
3. **Total Time:** The total time complexity $T(n)$ is given by:
   $$T(n) = O(n) + \sum_{k=1}^{n-1} O(\log(n-k+1)) = O(n) + O(n \log n) = O(n \log n)$$

### Space Complexity
1. **Heap Space:** The priority queue stores at most $n$ nodes at any time, requiring $O(n)$ space.
2. **Tree Structure:** The resulting Huffman tree contains $n$ leaf nodes and $n-1$ internal nodes, totaling $2n-1$ nodes. Each node stores a constant amount of data (frequency, pointers), requiring $O(n)$ space.
3. **Output Dictionary:** Storing the mapping of $n$ characters to their respective binary strings requires $O(n \cdot \bar{\ell})$ space, where $\bar{\ell}$ is the average codeword length. Since $\bar{\ell} \leq n$, the space is bounded by $O(n^2)$ in the worst case (a degenerate tree), but typically $O(n \log n)$ for balanced trees. Given the standard implementation, the auxiliary space is $O(n)$.