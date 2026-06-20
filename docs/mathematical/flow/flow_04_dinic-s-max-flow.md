# Formal Mathematical Specification: Dinic's Algorithm (Max Flow)

## 1. Definitions and Notation

Let $G = (V, E)$ be a directed graph where $V$ is the set of vertices and $E \subseteq V \times V$ is the set of edges. We define a capacity function $c: E \to \mathbb{R}^+$. A flow network is a tuple $(G, c, s, t)$, where $s \in V$ is the source and $t \in V$ is the sink.

*   **Flow:** A function $f: V \times V \to \mathbb{R}$ satisfying:
    1.  **Capacity Constraint:** $\forall u, v \in V, f(u, v) \leq c(u, v)$.
    2.  **Skew Symmetry:** $\forall u, v \in V, f(u, v) = -f(v, u)$.
    3.  **Flow Conservation:** $\forall u \in V \setminus \{s, t\}, \sum_{v \in V} f(u, v) = 0$.
*   **Residual Graph:** Given a flow $f$, the residual graph $G_f = (V, E_f)$ has edges $E_f = \{ (u, v) \in V \times V : c_f(u, v) > 0 \}$, where the residual capacity is $c_f(u, v) = c(u, v) - f(u, v)$.
*   **Level Graph:** A subgraph $L_G = (V, E_L)$ where $E_L = \{ (u, v) \in E_f : \text{dist}(s, v) = \text{dist}(s, u) + 1 \}$, and $\text{dist}(s, v)$ is the shortest path distance from $s$ to $v$ in $G_f$ using BFS.
*   **Blocking Flow:** A flow $f'$ in $L_G$ such that every path from $s$ to $t$ in $L_G$ contains at least one edge $(u, v)$ where $f'(u, v) = c_f(u, v)$.

## 2. Algebraic Characterization

Dinic's algorithm iteratively constructs a sequence of flows $f_0, f_1, \dots, f_k$ until $t$ is unreachable from $s$ in $G_{f_k}$.

**The Level Graph Invariant:**
Let $d_i(v)$ denote the shortest path distance from $s$ to $v$ in the residual graph $G_{f_i}$. The algorithm maintains the property that $d_{i+1}(v) \geq d_i(v)$ for all $v \in V$. Specifically, if $t$ is reachable in $G_{f_{i+1}}$, then $d_{i+1}(t) > d_i(t)$.

**Blocking Flow Construction:**
In each phase $i$, we find a blocking flow $f'_i$ in the level graph $L_{G_i}$. The update rule for the global flow is:
$$f_{i+1}(u, v) = f_i(u, v) + f'_i(u, v)$$
The algorithm terminates when $t \notin \{v \in V : \exists \text{ path } s \to v \text{ in } G_{f_k}\}$. By the Max-Flow Min-Cut Theorem, the resulting flow $f_k$ is maximal if and only if there is no augmenting path in $G_{f_k}$.

**Next-Edge Pointer Optimization:**
Let $\text{adj}(u)$ be the set of neighbors of $u$. We define a pointer $\text{ptr}(u)$ that tracks the index of the first edge in $\text{adj}(u)$ that is not yet saturated. The DFS search space is pruned by:
$$\forall u \in V, \text{search}(u) \subseteq \{v \in \text{adj}(u) : \text{index}(v) \geq \text{ptr}(u)\}$$
This ensures that each edge is examined a constant number of times per phase.

## 3. Complexity Analysis

### Time Complexity
The complexity is derived from two components: the number of phases and the work per phase.

1.  **Number of Phases:** Since each phase (except the last) strictly increases the shortest path distance $d(s, t)$ in the residual graph, and $d(s, t) < |V|$, there are at most $|V| - 1$ phases.
2.  **Work per Phase:**
    *   **BFS:** Constructing the level graph takes $O(E)$.
    *   **DFS:** With the `ptr` optimization, each edge is traversed at most once per phase to push flow, and each vertex is visited at most $O(V)$ times to backtrack from dead ends. Thus, finding a blocking flow takes $O(V \cdot E)$.
3.  **Total Complexity:**
    $$\sum_{\text{phases}} O(V \cdot E) = O(V) \cdot O(V \cdot E) = O(V^2 E)$$

### Space Complexity
*   **Adjacency Representation:** We store the graph and residual capacities, requiring $O(V + E)$ space.
*   **Auxiliary Structures:** The `level` array, `ptr` array, and the recursion stack for DFS each require $O(V)$ space.
*   **Total Space:** $O(V + E)$, which is optimal for a graph-based flow algorithm.