# Formal Mathematical Specification: Edmonds-Karp (Max Flow)

## 1. Definitions and Notation

Let $G = (V, E)$ be a finite directed graph, where $V$ is the set of vertices such that $|V| = n$, and $E \subseteq V \times V$ is the set of directed edges such that $|E| = m$. We define a capacity function $c: V \times V \to \mathbb{R}_{\ge 0}$, where $c(u, v) > 0$ if $(u, v) \in E$, and $c(u, v) = 0$ otherwise.

A **flow network** is a tuple $(G, c, s, t)$, where $s \in V$ is the source and $t \in V$ is the sink. A flow is a function $f: V \times V \to \mathbb{R}$ satisfying:
1. **Capacity Constraint:** $\forall u, v \in V, f(u, v) \le c(u, v)$.
2. **Skew Symmetry:** $\forall u, v \in V, f(u, v) = -f(v, u)$.
3. **Flow Conservation:** $\forall u \in V \setminus \{s, t\}, \sum_{v \in V} f(u, v) = 0$.

The **residual capacity** $c_f(u, v)$ is defined as $c_f(u, v) = c(u, v) - f(u, v)$. The residual graph $G_f = (V, E_f)$ consists of edges with $c_f(u, v) > 0$.

## 2. Algebraic Characterization

The Edmonds-Karp algorithm is an implementation of the Ford-Fulkerson method that selects the augmenting path $p$ in $G_f$ that minimizes the number of edges (the shortest path in terms of hop count).

**Augmentation Step:**
Let $p$ be a simple path from $s$ to $t$ in $G_f$. The bottleneck capacity is defined as:
$$c_f(p) = \min \{c_f(u, v) : (u, v) \in p\}$$
The flow update rule is:
$$f_{new}(u, v) = f(u, v) + c_f(p) \cdot \mathbb{I}((u, v) \in p) - c_f(p) \cdot \mathbb{I}((v, u) \in p)$$
where $\mathbb{I}(\cdot)$ is the indicator function.

**Monotonicity Invariant:**
Let $\delta_f(s, v)$ be the shortest path distance (number of edges) from $s$ to $v$ in $G_f$. For every vertex $v \in V \setminus \{s, t\}$, the distance $\delta_f(s, v)$ increases monotonically with each augmentation. Specifically, if $f$ is updated to $f'$, then $\delta_{f'}(s, v) \ge \delta_f(s, v)$.

**Critical Edge Lemma:**
An edge $(u, v)$ is *critical* on an augmenting path $p$ if $c_f(u, v) = c_f(p)$. When $(u, v)$ is critical, it disappears from the residual graph $G_f$. For it to reappear, flow must be pushed along $(v, u)$, which requires $\delta_f(s, v) = \delta_f(s, u) + 1$. After the push, the new distance satisfies $\delta_{f'}(s, u) = \delta_{f'}(s, v) + 1 \ge \delta_f(s, v) + 1 = \delta_f(s, u) + 2$. Thus, the distance to $u$ increases by at least 2 each time $(u, v)$ becomes critical.

## 3. Complexity Analysis

### Time Complexity
The total time complexity is $O(V E^2)$.

1. **Number of Augmentations:** Each edge $(u, v)$ can become critical at most $O(V)$ times because its distance from the source increases by at least 2 each time it becomes critical, and the maximum distance is $|V|-1$. Since there are $O(E)$ edges, the total number of augmentations is $O(V E)$.
2. **Work per Augmentation:** Each augmentation requires a Breadth-First Search (BFS) to find the shortest path. A BFS on a graph with $V$ vertices and $E$ edges takes $O(E)$ time.
3. **Total Work:** Multiplying the number of augmentations by the cost per augmentation yields:
$$T(V, E) = O(V E) \cdot O(E) = O(V E^2)$$

### Space Complexity
The space complexity is $O(V^2)$ when using an adjacency matrix to represent capacities, or $O(V + E)$ when using an adjacency list.

1. **Auxiliary Space:** The algorithm maintains a `parent` array of size $O(V)$, a `visited` array of size $O(V)$, and a queue for BFS of size $O(V)$.
2. **Total Space:** The primary storage is the residual capacity structure. Using an adjacency matrix, we store $n^2$ values, resulting in $O(V^2)$ space. Using an adjacency list, we store $O(V + E)$ entries. Given that $E \le V^2$, the matrix representation is often preferred for dense graphs, while the list representation is optimal for sparse graphs.