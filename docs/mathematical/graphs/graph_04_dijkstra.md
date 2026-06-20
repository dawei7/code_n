# Formal Mathematical Specification: Dijkstra's Algorithm

## 1. Definitions and Notation

Let $G = (V, E, w)$ be a weighted directed graph, where:
*   $V = \{v_1, v_2, \dots, v_n\}$ is the set of $n$ vertices.
*   $E \subseteq V \times V$ is the set of edges.
*   $w: E \to \mathbb{R}_{\ge 0}$ is a weight function assigning a non-negative real value to each edge.

We define the following state variables:
*   $s \in V$: The source vertex.
*   $d: V \to \mathbb{R}_{\ge 0} \cup \{\infty\}$: A distance function where $d(v)$ denotes the current shortest path estimate from $s$ to $v$.
*   $S \subseteq V$: The set of "finalized" vertices for which the shortest path distance from $s$ is known.
*   $Q = V \setminus S$: The set of "unvisited" vertices.

The objective is to compute the function $\delta(s, v)$, defined as the weight of the shortest path from $s$ to $v$ in $G$.

## 2. Algebraic Characterization

Dijkstra's algorithm is an iterative greedy procedure that maintains the following **Loop Invariant**:
For every vertex $u \in S$, $d(u) = \delta(s, u)$. Furthermore, for all $v \in V$, $d(v)$ is the weight of the shortest path from $s$ to $v$ using only vertices in $S$ as intermediate nodes.

### Relaxation
The core transition is the relaxation of an edge $(u, v) \in E$. If $d(u) + w(u, v) < d(v)$, we update:
$$d(v) \leftarrow d(u) + w(u, v)$$

### Greedy Choice Property
At each iteration, we select $u \in Q$ such that:
$$u = \text{argmin}_{v \in Q} \{d(v)\}$$
The correctness of the algorithm relies on the fact that since $w(e) \ge 0$ for all $e \in E$, once $u$ is added to $S$, no path discovered later can yield a distance smaller than $d(u)$. Formally, if $u$ is the vertex with the minimum $d$ value in $Q$, then $d(u) = \delta(s, u)$.

### Termination
The algorithm terminates when $Q = \emptyset$ or when the target vertex $t$ is moved to $S$. The final state satisfies:
$$\forall v \in V, d(v) = \min_{p \in \mathcal{P}_{s,v}} \sum_{e \in p} w(e)$$
where $\mathcal{P}_{s,v}$ is the set of all paths from $s$ to $v$.

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of an initialization phase and a main loop that executes $n$ times.

1.  **Initialization:** Setting $d(s) = 0$ and $d(v) = \infty$ for $v \neq s$ takes $O(n)$ time.
2.  **Main Loop:**
    *   **Selection:** Finding $u = \text{argmin}_{v \in Q} d(v)$ requires a linear scan over the set $Q$. In the $k$-th iteration, $|Q| = n - k + 1$. The total time for selection is $\sum_{k=1}^{n} (n - k + 1) = \sum_{i=1}^{n} i = \frac{n(n+1)}{2} = O(n^2)$.
    *   **Relaxation:** Each edge $(u, v)$ is relaxed exactly once when its source $u$ is extracted from $Q$. Across the entire execution, we perform at most $|E| = m$ relaxations.
    *   **Total Time:** The complexity is dominated by the selection process:
        $$T(n, m) = O(n^2 + m) = O(n^2)$$
    Since $m \le n^2$ in a simple graph, the $O(n^2)$ term bounds the total work.

### Space Complexity
The algorithm requires storage for:
*   The distance array $d$: $O(n)$.
*   The visited set $S$ (or boolean array): $O(n)$.
*   The graph representation $G$ (adjacency list): $O(n + m)$.

Thus, the auxiliary space complexity is $O(n)$, and the total space complexity, including the graph storage, is $O(n + m)$.