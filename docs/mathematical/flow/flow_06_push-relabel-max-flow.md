# Formal Mathematical Specification: Push-Relabel (Max Flow)

## 1. Definitions and Notation

Let $G = (V, E)$ be a directed graph where $V$ is the set of vertices and $E \subseteq V \times V$ is the set of edges. We define a capacity function $c: V \times V \to \mathbb{R}_{\geq 0}$, where $c(u, v) = 0$ if $(u, v) \notin E$. We designate a source $s \in V$ and a sink $t \in V$.

The algorithm maintains a **preflow** $f: V \times V \to \mathbb{R}$, which satisfies the following constraints:
1. **Capacity Constraint:** $\forall u, v \in V, f(u, v) \leq c(u, v)$.
2. **Skew Symmetry:** $\forall u, v \in V, f(u, v) = -f(v, u)$.
3. **Non-negativity of Excess:** For all $v \in V \setminus \{s\}$, the excess flow $e(v)$ is defined as:
   $$e(v) = \sum_{u \in V} f(u, v) \geq 0$$
   A vertex $v$ is **active** if $v \in V \setminus \{s, t\}$ and $e(v) > 0$.

We define a **height function** $h: V \to \mathbb{N}$ and the **residual capacity** $c_f(u, v) = c(u, v) - f(u, v)$. A residual edge $(u, v)$ exists if $c_f(u, v) > 0$.

## 2. Algebraic Characterization

The algorithm maintains the **height invariant**:
1. $h(s) = |V|$ and $h(t) = 0$.
2. For any residual edge $(u, v) \in E_f$, $h(u) \leq h(v) + 1$.

### The Push Operation
For an active vertex $u$ and a neighbor $v$ such that $c_f(u, v) > 0$ and $h(u) = h(v) + 1$, the push operation updates the flow:
$$\delta = \min(e(u), c_f(u, v))$$
$$f(u, v) \leftarrow f(u, v) + \delta, \quad f(v, u) \leftarrow f(v, u) - \delta$$
$$e(u) \leftarrow e(u) - \delta, \quad e(v) \leftarrow e(v) + \delta$$

### The Relabel Operation
For an active vertex $u$ where $\forall v \in V$ such that $c_f(u, v) > 0$, $h(u) \leq h(v)$, the relabel operation updates the height:
$$h(u) \leftarrow 1 + \min \{h(v) : (u, v) \in E_f\}$$

### Correctness Invariant
The algorithm terminates when no active vertices remain. At termination, the height function ensures that no path exists from $s$ to $t$ in the residual graph $G_f$. By the Max-Flow Min-Cut Theorem, the resulting flow $f$ is a maximum flow, and the value is given by $\sum_{v \in V} f(v, t)$.

## 3. Complexity Analysis

### Time Complexity
The complexity is derived from the total number of operations:
1. **Relabel operations:** Each vertex $u$ can be relabeled at most $2|V|-1$ times. Total relabels: $O(V^2)$.
2. **Saturating pushes:** A push is saturating if $c_f(u, v)$ becomes 0. Between two saturating pushes on edge $(u, v)$, $u$ and $v$ must be relabeled. Total saturating pushes: $O(VE)$.
3. **Non-saturating pushes:** Using the "Highest-Label" selection rule, the number of non-saturating pushes is bounded by $O(V^2 E)$ in general, but specifically $O(V^3)$ for the highest-label variant.

Summing these, the total time complexity is $O(V^3)$. The work per iteration is dominated by the search for an admissible edge, which is amortized over the relabeling process.

### Space Complexity
The algorithm requires:
1. **Residual Capacity Matrix:** $O(V^2)$ to store $c_f(u, v)$ for all pairs.
2. **Auxiliary Arrays:** $O(V)$ to store $h(v)$ and $e(v)$.
3. **Active Set:** $O(V)$ to maintain the set of active vertices.

Total space complexity is $O(V^2)$, which is optimal for dense graphs represented by adjacency matrices.