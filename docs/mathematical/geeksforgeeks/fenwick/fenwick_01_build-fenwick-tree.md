# Formal Mathematical Specification: Build Fenwick Tree (Binary Indexed Tree)

## 1. Definitions and Notation

Let $A = (a_1, a_2, \dots, a_N)$ be a sequence of $N$ elements over a commutative group $(G, +)$. In the context of this algorithm, $G = \mathbb{Z}$ or $\mathbb{R}$.

We define the **Fenwick Tree** (or Binary Indexed Tree) as a sequence $B = (b_0, b_1, \dots, b_N)$ where $b_0$ is a dummy element (typically $0$) and $b_i$ for $i \in \{1, \dots, N\}$ is defined as the sum of a specific range of $A$:
$$b_i = \sum_{j=i - \text{lsb}(i) + 1}^{i} a_j$$
where $\text{lsb}(i)$ denotes the value of the least significant bit of $i$, defined as:
$$\text{lsb}(i) = i \& (-i) = 2^k$$
where $k$ is the largest integer such that $2^k$ divides $i$.

The state space $\mathcal{S}$ of the algorithm is the set of all possible arrays $B \in G^{N+1}$. The transformation $f: G^N \to \mathcal{S}$ maps the input array $A$ to the Fenwick representation $B$.

## 2. Algebraic Characterization

The construction of the Fenwick Tree relies on the property that each index $i$ is responsible for a range of length $\text{lsb}(i)$. To achieve $O(N)$ construction, we utilize the tree structure inherent in the BIT indices.

Let $parent(i) = i + \text{lsb}(i)$. The indices form a forest (or a tree if we consider a virtual root at $N+1$) where $i$ is a child of $parent(i)$ if $parent(i) \leq N$.

**Initialization:**
We initialize $b_i = a_i$ for all $i \in \{1, \dots, N\}$. This represents the base case where each node contains its own value.

**Propagation Invariant:**
After the initialization, we perform a single pass $i = 1, \dots, N$. The correctness of the construction is governed by the following recurrence relation:
$$b_{parent(i)} \leftarrow b_{parent(i)} + b_i, \quad \forall i \in \{1, \dots, N\} \text{ s.t. } parent(i) \leq N$$

This operation ensures that the value at $b_j$ accumulates the sums of all its direct children in the BIT structure. Since the BIT structure is a directed acyclic graph (specifically, a tree where edges are defined by $i \to i + \text{lsb}(i)$), processing indices in increasing order guarantees that when we reach index $j$, all its children $i$ (where $parent(i) = j$) have already been fully processed and their values propagated to $b_j$.

Thus, the final value of $b_j$ is:
$$b_j = a_j + \sum_{i \in \text{children}(j)} b_i$$
By induction, this satisfies the definition $b_j = \sum_{k=j-\text{lsb}(j)+1}^{j} a_k$.

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of two distinct phases:
1. **Initialization:** A linear scan to copy $N$ elements into the array $B$. This requires $\Theta(N)$ operations.
2. **Propagation:** A loop from $i = 1$ to $N$. Inside the loop, the bitwise operation $\text{lsb}(i)$ and the addition $b_{parent(i)} += b_i$ are performed in $O(1)$ time. 

The total time complexity $T(N)$ is given by:
$$T(N) = \sum_{i=1}^{N} \Theta(1) = \Theta(N)$$
Since each index $i$ is visited exactly once and contributes to at most one parent, the work is strictly linear. Thus, $T(N) \in O(N)$.

### Space Complexity
The algorithm requires an auxiliary array $B$ of size $N+1$ to store the Fenwick Tree. 
- **Auxiliary Space:** $O(1)$ (excluding the output array).
- **Total Space:** $O(N)$ to store the BIT structure.

Given that the output must be of size $N+1$, the space complexity is optimal at $\Theta(N)$.