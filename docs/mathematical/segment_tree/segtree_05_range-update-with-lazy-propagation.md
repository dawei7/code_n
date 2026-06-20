# Formal Mathematical Specification: Range Update with Lazy Propagation (Sum)

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be an array of $n$ elements where $a_i \in \mathbb{R}$. We define a Segment Tree as a rooted binary tree $\mathcal{T}$ where each node $v$ represents a contiguous interval $[lo_v, hi_v] \subseteq [0, n-1]$.

- **State Space:** Each node $v$ maintains two values:
    - $S_v$: The sum of elements in the range $[lo_v, hi_v]$, defined as $S_v = \sum_{i=lo_v}^{hi_v} a_i$.
    - $L_v$: A lazy propagation value representing a pending additive update to be applied to all elements in the range $[lo_v, hi_v]$.
- **Domain:** The set of all possible states is $\mathcal{S} = \{ (S_v, L_v) \mid v \in \mathcal{T} \}$.
- **Update Operation:** A range update $U(l, r, \delta)$ modifies the array such that $a_i \leftarrow a_i + \delta$ for all $i \in [l, r] \cap [0, n-1]$.
- **Query Operation:** A range sum query $Q(l, r)$ returns $\sum_{i=l}^r a_i$.

## 2. Algebraic Characterization

The correctness of the algorithm relies on the distributive property of the sum operator over the additive update.

### The Apply Operator
For a node $v$ covering interval $[lo_v, hi_v]$, applying a lazy value $\delta$ updates the state as follows:
1. $S_v \leftarrow S_v + \delta \cdot (hi_v - lo_v + 1)$
2. $L_v \leftarrow L_v + \delta$

### Recurrence Relations
The sum $S_v$ is maintained by the invariant:
$$S_v = \begin{cases} a_{lo_v} & \text{if } lo_v = hi_v \\ S_{left(v)} + S_{right(v)} & \text{if } lo_v < hi_v \end{cases}$$

When an update $U(l, r, \delta)$ is applied to node $v$:
1. **Total Overlap ($[lo_v, hi_v] \subseteq [l, r]$):** Apply the update to $S_v$ and $L_v$ and terminate.
2. **Partial Overlap ($[lo_v, hi_v] \cap [l, r] \neq \emptyset$):**
   - Perform a "Push" operation: If $L_v \neq 0$, apply $L_v$ to children $left(v)$ and $right(v)$, then set $L_v = 0$.
   - Recurse: $update(left(v), \dots) + update(right(v), \dots)$.
   - Recompute: $S_v = S_{left(v)} + S_{right(v)}$.

### Invariant
For any node $v$, the true sum $S_v$ is always consistent with the sum of its children plus the effect of its own pending lazy value $L_v$ applied to its range length $len_v = hi_v - lo_v + 1$:
$$S_v = \left( \sum_{i \in \text{leaves}(v)} a_i \right) + L_v \cdot len_v$$

## 3. Complexity Analysis

### Time Complexity
The time complexity is governed by the number of nodes visited during an update or query.
- **Recurrence:** Let $T(n)$ be the time to process a range of size $n$.
- In the worst case, the algorithm visits nodes that partially overlap with $[l, r]$. At each level of the tree, there are at most 4 nodes that partially overlap the query range boundaries.
- Since the height of the tree is $H = \lceil \log_2 n \rceil$, and we perform a constant amount of work at each visited node (the `push` and `apply` operations are $O(1)$):
$$T(n) = O(H) = O(\log n)$$
Thus, both `update` and `query` operations are strictly $O(\log n)$.

### Space Complexity
- **Tree Storage:** The segment tree is a complete binary tree (or a heap-indexed array). For $n$ leaves, the number of nodes in the tree is at most $4n$.
- **Auxiliary Space:** We maintain two arrays, `tree` and `lazy`, each of size $4n$.
- **Total Space:** The total space complexity is $O(n)$, which is optimal for storing the state of the segment tree.