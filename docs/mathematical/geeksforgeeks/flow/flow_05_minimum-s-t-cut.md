# Formal Mathematical Specification: Minimum S-T Cut

## 1. Definitions and Notation

Let $G = (V, E)$ be a directed graph, where $V$ is a finite set of vertices and $E \subseteq V \times V$ is a set of directed edges. We define a capacity function $c: E \to \mathbb{R}_{\geq 0}$, which assigns a non-negative capacity to each edge. Given a source $s \in V$ and a sink $t \in V$, a **flow network** is the triple $(G, c, s, t)$.

A **flow** is a function $f: E \to \mathbb{R}_{\geq 0}$ satisfying:
1. **Capacity Constraint:** $\forall (u, v) \in E, 0 \leq f(u, v) \leq c(u, v)$.
2. **Flow Conservation:** $\forall v \in V \setminus \{s, t\}, \sum_{u:(u, v) \in E} f(u, v) = \sum_{w:(v, w) \in E} f(v, w)$.

An **$s-t$ cut** is a partition of $V$ into two disjoint sets $S$ and $T$ such that $s \in S$ and $t \in T$, where $T = V \setminus S$. The capacity of the cut $(S, T)$, denoted $c(S, T)$, is defined as:
$$c(S, T) = \sum_{u \in S, v \in T, (u, v) \in E} c(u, v)$$

The **Minimum $s-t$ Cut** problem seeks to find a partition $(S, T)$ that minimizes $c(S, T)$.

## 2. Algebraic Characterization

The correctness of the algorithm relies on the **Max-Flow Min-Cut Theorem**, which states that the value of the maximum flow $|f|$ is equal to the capacity of the minimum $s-t$ cut.

### Residual Graph
Given a flow $f$, the residual capacity $c_f(u, v)$ for any pair $(u, v) \in V \times V$ is defined as:
$$c_f(u, v) = \begin{cases} c(u, v) - f(u, v) & \text{if } (u, v) \in E \\ f(v, u) & \text{if } (v, u) \in E \\ 0 & \text{otherwise} \end{cases}$$
The residual graph $G_f = (V, E_f)$ consists of edges with $c_f(u, v) > 0$.

### Reachability and Cut Identification
Let $f^*$ be a maximum flow. Let $S \subseteq V$ be the set of vertices reachable from $s$ in the residual graph $G_{f^*}$ using paths with strictly positive residual capacity:
$$S = \{v \in V \mid \exists \text{ a path from } s \text{ to } v \text{ in } G_{f^*}\}$$
By definition, $s \in S$. Since $f^*$ is a maximum flow, there is no augmenting path from $s$ to $t$ in $G_{f^*}$, implying $t \notin S$. Thus, $(S, V \setminus S)$ constitutes an $s-t$ cut.

For any edge $(u, v) \in E$ where $u \in S$ and $v \notin S$:
1. $f^*(u, v) = c(u, v)$ (The edge is saturated).
2. $f^*(v, u) = 0$ (If $f^*(v, u) > 0$, then $u$ would be reachable from $v$ in $G_{f^*}$, contradicting $v \notin S$).

Consequently, the capacity of the cut is:
$$c(S, V \setminus S) = \sum_{u \in S, v \notin S} f^*(u, v) = |f^*|$$
This confirms that the set of edges $E_{cut} = \{(u, v) \in E \mid u \in S, v \notin S\}$ is a minimum $s-t$ cut.

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of two phases:
1. **Max-Flow Computation:** Let $T_{maxflow}(V, E)$ be the time complexity of the chosen max-flow algorithm. For Edmonds-Karp, $T_{maxflow} = O(VE^2)$.
2. **Reachability Analysis:** Constructing the set $S$ via Breadth-First Search (BFS) or Depth-First Search (DFS) on the residual graph $G_{f^*}$ requires visiting each vertex and edge at most once, resulting in $O(V + E)$ time.
3. **Cut Identification:** Iterating over the edge set $E$ to identify edges $(u, v)$ where $u \in S$ and $v \notin S$ takes $O(E)$ time.

The total time complexity is:
$$T(V, E) = O(T_{maxflow}(V, E) + V + E) = O(T_{maxflow}(V, E))$$

### Space Complexity
1. **Residual Graph:** Storing the capacity matrix requires $O(V^2)$ space.
2. **Auxiliary Structures:** The `parent` array, `visited` array, and `reachable` set each require $O(V)$ space.
3. **Total Space:** The space complexity is dominated by the capacity matrix, yielding $O(V^2)$.