# Formal Mathematical Specification: Range Minimum Query with Lazy Updates

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be an array of elements where $a_i \in \mathbb{R}$. We define a Segment Tree $\mathcal{T}$ as a rooted binary tree where each node $u$ corresponds to a closed interval $[L_u, R_u] \subseteq [0, n-1]$.

- **State Space:** Each node $u$ maintains two values:
    - $T_u$: The minimum value in the range $[L_u, R_u]$, defined as $T_u = \min_{i \in [L_u, R_u]} a_i$.
    - $\Lambda_u$: A lazy propagation value representing a pending additive update. $\Lambda_u \in \mathbb{R} \cup \{0\}$ (where $0$ denotes the identity element for addition).
- **Operations:**
    - $\text{Update}(l, r, \delta)$: For all $i \in [l, r]$, $a_i \leftarrow a_i + \delta$.
    - $\text{Query}(l, r)$: Returns $\min_{i \in [l, r]} a_i$.
- **Domain:** The set of indices is $\mathcal{I} = \{0, 1, \dots, n-1\}$. The tree structure is defined such that for any internal node $u$ with children $v_{left}$ and $v_{right}$, $[L_u, R_u] = [L_{v_{left}}, R_{v_{left}}] \cup [L_{v_{right}}, R_{v_{right}}]$.

## 2. Algebraic Characterization

The correctness of the algorithm relies on the distributive property of the minimum operator over addition.

### The Update Invariant
For any range $[L_u, R_u]$, if we apply an additive update $\delta$, the new minimum $T_u'$ is:
$$T_u' = \min_{i \in [L_u, R_u]} (a_i + \delta) = \left( \min_{i \in [L_u, R_u]} a_i \right) + \delta = T_u + \delta$$
This confirms that the minimum value is shifted by the exact magnitude of the update, independent of the segment length.

### Lazy Propagation Recurrence
Let $\text{push}(u)$ be the operation that propagates $\Lambda_u$ to its children $v \in \{v_{left}, v_{right}\}$. The state transitions are:
1. $T_v \leftarrow T_v + \Lambda_u$
2. $\Lambda_v \leftarrow \Lambda_v + \Lambda_u$
3. $\Lambda_u \leftarrow 0$

This satisfies the invariant that at any time, the value $T_u$ stored in the node correctly reflects all updates applied to the range $[L_u, R_u]$ that have been "pushed" to $u$, but potentially not yet to its descendants.

### Query Recurrence
The query function $Q(u, l, r)$ is defined recursively:
$$Q(u, l, r) = 
\begin{cases} 
\infty & \text{if } [L_u, R_u] \cap [l, r] = \emptyset \\
T_u & \text{if } [L_u, R_u] \subseteq [l, r] \\
\min(Q(v_{left}, l, r), Q(v_{right}, l, r)) & \text{otherwise}
\end{cases}$$
Before evaluating the recursive step, $\text{push}(u)$ is invoked to ensure the children nodes $v_{left}, v_{right}$ contain the most current values.

## 3. Complexity Analysis

### Time Complexity
The algorithm performs operations on a balanced binary tree of height $H = \lceil \log_2 n \rceil$.

- **Update/Query:** In both operations, we visit nodes in the tree. A range $[l, r]$ is decomposed into at most $O(\log n)$ canonical nodes. Because each node is visited at most a constant number of times per operation (due to the lazy propagation mechanism), the work performed is proportional to the height of the tree.
- **Recurrence:** Let $W(n)$ be the work for an operation on a range of size $n$.
$$W(n) = 2W(n/2) + O(1) \implies W(n) = O(\log n)$$
Thus, both `update_range` and `query_min` operate in $O(\log n)$ time.

### Space Complexity
- **Tree Storage:** The segment tree is a complete binary tree. For an array of size $n$, the number of nodes in the tree is bounded by $4n$.
- **Auxiliary Space:** We maintain two arrays, `tree` and `lazy`, each of size $4n$.
- **Total Space:** The total space complexity is $O(n)$, which is optimal for storing the state of the segment tree.