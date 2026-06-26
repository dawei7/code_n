# Formal Mathematical Specification: Breadth-First Search (BFS)

## 1. Definitions and Notation

Let $G = (V, E)$ be an unweighted, undirected graph, where $V = \{v_1, v_2, \dots, v_n\}$ is the set of vertices and $E \subseteq \{\{u, v\} : u, v \in V, u \neq v\}$ is the set of edges. We denote the adjacency set of a vertex $u$ as $\text{Adj}(u) = \{v \in V : \{u, v\} \in E\}$.

The algorithm operates on the following state space $\mathcal{S}$:
*   **Distance Function:** $d: V \to \mathbb{N} \cup \{\infty\}$, where $d(v)$ represents the shortest path distance from a source vertex $s \in V$ to $v$.
*   **Predecessor Function:** $\pi: V \to V \cup \{\text{null}\}$, mapping each vertex to its immediate ancestor in the BFS tree.
*   **Visited Set:** $S \subseteq V$, the set of vertices discovered by the algorithm.
*   **Queue:** $Q$, a First-In-First-Out (FIFO) sequence of vertices $Q = (q_1, q_2, \dots, q_k)$.

The input is the pair $(G, s)$, and the output is the tuple $(d, \pi, \mathcal{O})$, where $\mathcal{O}$ is the sequence of vertices in the order they were dequeued.

## 2. Algebraic Characterization

The correctness of BFS is governed by the property that it explores the graph in non-decreasing order of distance from $s$. We define the distance $d(v)$ as the length of the shortest path $\delta(s, v)$.

### The BFS Invariant
At any point during the execution, let $Q = (v_1, v_2, \dots, v_k)$. The following conditions hold:
1.  $d(v_1) \leq d(v_2) \leq \dots \leq d(v_k)$.
2.  $d(v_k) \leq d(v_1) + 1$.

### Recurrence Relation
The distance function $d(v)$ satisfies the following recurrence:
$$d(v) = \begin{cases} 0 & \text{if } v = s \\ \min_{\{u, v\} \in E} \{d(u) + 1\} & \text{if } v \neq s \text{ and } v \text{ is reachable from } s \\ \infty & \text{otherwise} \end{cases}$$

### Transition Logic
For a vertex $u$ dequeued from $Q$, the algorithm performs the following update for each neighbor $v \in \text{Adj}(u)$:
If $v \notin S$:
1.  $S \leftarrow S \cup \{v\}$
2.  $d(v) \leftarrow d(u) + 1$
3.  $\pi(v) \leftarrow u$
4.  $Q \leftarrow Q \cdot (v)$ (where $\cdot$ denotes concatenation)

This ensures that for any edge $\{u, v\} \in E$, the triangle inequality holds: $d(v) \leq d(u) + 1$.

## 3. Complexity Analysis

### Time Complexity
The time complexity is determined by the number of operations performed on vertices and edges.
*   **Vertex Processing:** Each vertex $v \in V$ is enqueued and dequeued exactly once. This contributes $O(V)$ to the complexity.
*   **Edge Processing:** In an adjacency list representation, for every vertex $u$ dequeued, we iterate over its adjacency list $\text{Adj}(u)$. Across the entire execution, each edge $\{u, v\} \in E$ is examined exactly twice (once from $u$ and once from $v$). This contributes $O(E)$ to the complexity.

Total time complexity $T(V, E)$ is given by:
$$T(V, E) = \sum_{v \in V} (1 + \text{deg}(v)) = O(V + E)$$
For an adjacency matrix representation, the algorithm must scan the entire row of length $|V|$ for each of the $|V|$ vertices, resulting in $T(V) = O(V^2)$.

### Space Complexity
The space complexity $S(V)$ is dominated by the storage of the auxiliary structures:
1.  **Distance and Predecessor arrays:** $O(V)$ to store $d(v)$ and $\pi(v)$ for all $v \in V$.
2.  **Visited set:** $O(V)$ to store the boolean status of each vertex.
3.  **Queue:** In the worst case (e.g., a star graph), the queue may contain $O(V)$ vertices.

Thus, the total auxiliary space complexity is:
$$S(V) = O(V) + O(V) + O(V) = O(V)$$