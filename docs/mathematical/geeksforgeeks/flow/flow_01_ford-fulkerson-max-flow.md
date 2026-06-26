# Formal Mathematical Specification: Ford-Fulkerson (Max Flow)

## 1. Definitions and Notation

Let $G = (V, E)$ be a directed graph, where $V$ is a finite set of vertices and $E \subseteq V \times V$ is a set of directed edges. We define a capacity function $c: V \times V \to \mathbb{R}_{\geq 0}$, where $c(u, v) > 0$ if $(u, v) \in E$ and $c(u, v) = 0$ otherwise. We designate a source node $s \in V$ and a sink node $t \in V$.

A **flow** is a function $f: V \times V \to \mathbb{R}$ satisfying the following three constraints:
1. **Capacity Constraint:** $\forall u, v \in V, f(u, v) \leq c(u, v)$.
2. **Skew Symmetry:** $\forall u, v \in V, f(u, v) = -f(v, u)$.
3. **Flow Conservation:** $\forall u \in V \setminus \{s, t\}, \sum_{v \in V} f(u, v) = 0$.

The **value of the flow** is defined as $|f| = \sum_{v \in V} f(s, v)$. The objective is to find a flow $f$ that maximizes $|f|$.

The **residual capacity** $c_f: V \times V \to \mathbb{R}$ is defined as $c_f(u, v) = c(u, v) - f(u, v)$. The **residual graph** $G_f = (V, E_f)$ consists of edges with $c_f(u, v) > 0$.

## 2. Algebraic Characterization

The Ford-Fulkerson method is governed by the **Max-Flow Min-Cut Theorem**, which states that the value of a maximum flow is equal to the capacity of a minimum cut. The algorithm iteratively improves the flow by finding an **augmenting path** $p$ in the residual graph $G_f$.

### Augmentation
Let $p$ be a simple path from $s$ to $t$ in $G_f$. The residual capacity of the path is:
$$c_f(p) = \min \{c_f(u, v) : (u, v) \in p\}$$

The flow $f$ is updated to $f'$ as follows:
$$f'(u, v) = \begin{cases} f(u, v) + c_f(p) & \text{if } (u, v) \in p \\ f(u, v) - c_f(p) & \text{if } (v, u) \in p \\ f(u, v) & \text{otherwise} \end{cases}$$

### Loop Invariant
At the start of each iteration, the flow $f$ is a valid flow. The algorithm terminates when there exists no path $p$ from $s$ to $t$ in $G_f$. By the Max-Flow Min-Cut theorem, if no such path exists, the current flow $f$ is a maximum flow.

## 3. Complexity Analysis

### Time Complexity
The time complexity is $O(E \cdot |f^*|)$, where $|f^*|$ is the value of the maximum flow.

**Derivation:**
1. Each iteration of the algorithm identifies an augmenting path using Depth-First Search (DFS), which takes $O(V + E)$ time. Since the graph is connected for flow purposes, this is $O(E)$.
2. In each iteration, the flow value $|f|$ increases by at least 1 (assuming integral capacities).
3. The total number of augmentations is bounded by the value of the maximum flow $|f^*|$.
4. Thus, the total time complexity is $O(E \cdot |f^*|)$. 

*Note:* If capacities are irrational, the algorithm is not guaranteed to terminate. If capacities are integers, the algorithm is guaranteed to terminate in a finite number of steps.

### Space Complexity
The space complexity is $O(V^2)$ or $O(V + E)$ depending on the implementation of the residual graph.

**Derivation:**
1. **Adjacency Matrix:** Storing the capacity $c(u, v)$ for all pairs $(u, v) \in V \times V$ requires $O(V^2)$ space.
2. **Adjacency List:** Storing the graph as an adjacency list requires $O(V + E)$ space to store the vertices and edges.
3. **Auxiliary Space:** The DFS stack and the `parent` array used to reconstruct the path require $O(V)$ space.
4. Therefore, the total space complexity is dominated by the graph representation: $O(V^2)$ for dense matrices or $O(V + E)$ for sparse adjacency lists.