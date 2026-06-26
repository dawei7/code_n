# Formal Mathematical Specification: Range Minimum Query

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be an array of elements drawn from a totally ordered set $(\mathcal{X}, \le)$, where $\mathcal{X} \subseteq \mathbb{R} \cup \{\infty\}$. 

A **Segment Tree** $\mathcal{T}$ is a rooted binary tree where each node $u$ corresponds to a closed interval $[lo, hi] \subseteq [0, n-1]$. The tree is defined recursively:
- **Leaf Nodes:** For each $i \in [0, n-1]$, there exists a leaf node representing $[i, i]$ such that its value $v(u) = a_i$.
- **Internal Nodes:** For a node $u$ covering $[lo, hi]$ where $lo < hi$, let $mid = \lfloor \frac{lo + hi}{2} \rfloor$. Node $u$ has two children: $u_{left}$ covering $[lo, mid]$ and $u_{right}$ covering $[mid+1, hi]$. The value of the node is defined by the associative binary operation $\min: \mathcal{X} \times \mathcal{X} \to \mathcal{X}$:
  $$v(u) = \min(v(u_{left}), v(u_{right}))$$

The **Range Minimum Query (RMQ)** is a function $f: [0, n-1] \times [0, n-1] \to \mathcal{X}$ defined as:
$$f(l, r) = \min_{i \in [l, r]} a_i$$
where $0 \le l \le r \le n-1$. If $l > r$, we define $f(l, r) = \infty$, where $\infty$ is the identity element for the $\min$ operation such that $\forall x \in \mathcal{X}, \min(x, \infty) = x$.

## 2. Algebraic Characterization

The correctness of the RMQ algorithm relies on the decomposition of the query interval $[l, r]$ into a set of canonical nodes in $\mathcal{T}$. Let $Q(u, l, r)$ be the recursive query function for a node $u$ covering $[lo, hi]$:

$$Q(u, l, r) = 
\begin{cases} 
\infty & \text{if } [lo, hi] \cap [l, r] = \emptyset \\
v(u) & \text{if } [lo, hi] \subseteq [l, r] \\
\min(Q(u_{left}, l, r), Q(u_{right}, l, r)) & \text{otherwise}
\end{cases}$$

**Invariant:** For any node $u$ covering $[lo, hi]$, the value $v(u)$ satisfies the invariant $v(u) = \min_{i \in [lo, hi]} a_i$. By the associativity and commutativity of the $\min$ operator, the recursive decomposition correctly partitions the interval $[l, r]$ into at most $O(\log n)$ disjoint canonical sub-intervals whose union is exactly $[l, r]$.

## 3. Complexity Analysis

### Time Complexity
The time complexity $T(n)$ is governed by the number of nodes visited during the traversal. 
At any depth $d$ of the tree, the query range $[l, r]$ intersects at most 4 nodes. Specifically, for any level, the query range can partially overlap with at most two nodes (the ones containing $l$ and $r$), while all nodes strictly between these are either fully contained or fully disjoint.

Since the height of the tree is $H = \lceil \log_2 n \rceil$, and we visit a constant number of nodes $c \le 4$ per level:
$$T(n) = \sum_{d=0}^{\lceil \log_2 n \rceil} c = O(\log n)$$
Thus, the query operation is strictly $O(\log n)$.

### Space Complexity
- **Total Space:** The segment tree is a full binary tree with $n$ leaves. The number of internal nodes is $n-1$, resulting in $2n-1$ total nodes. In a heap-indexed array representation, we allocate $4n$ space to accommodate the tree structure, yielding $O(n)$ space complexity.
- **Auxiliary Space:** The recursion depth of the `query` function is bounded by the height of the tree $H = \lceil \log_2 n \rceil$. Therefore, the auxiliary space complexity required for the call stack is $O(\log n)$.