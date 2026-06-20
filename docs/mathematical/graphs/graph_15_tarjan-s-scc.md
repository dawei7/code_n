# Formal Mathematical Specification: Strongly Connected Components (Tarjan's)

## 1. Definitions and Notation

Let $G = (V, E)$ be a directed graph, where $V = \{v_1, v_2, \dots, v_n\}$ is the set of vertices and $E \subseteq V \times V$ is the set of directed edges. Let $n = |V|$ and $m = |E|$.

*   **Strongly Connected Component (SCC):** A subset $S \subseteq V$ is an SCC if for every pair $u, v \in S$, there exists a directed path from $u$ to $v$ and a directed path from $v$ to $u$, and $S$ is maximal with respect to this property.
*   **Discovery Time ($\text{tin}: V \to \mathbb{N}$):** A mapping assigning each vertex $v$ the time at which it was first visited during a Depth-First Search (DFS) traversal.
*   **Low-link Value ($\text{low}: V \to \mathbb{N}$):** A mapping defined as:
    $$\text{low}(u) = \min \left( \{\text{tin}(u)\} \cup \{\text{low}(v) \mid (u, v) \in E, v \text{ is in the current DFS subtree}\} \cup \{\text{tin}(v) \mid (u, v) \in E, v \in \text{Stack}\} \right)$$
*   **State Space ($\mathcal{S}$):** The algorithm maintains a state tuple $(\text{tin}, \text{low}, \text{Stack}, \text{on\_stack}, \text{SCCs})$, where $\text{Stack}$ is an ordered sequence of vertices, and $\text{on\_stack}: V \to \{0, 1\}$ is an indicator function.

## 2. Algebraic Characterization

The correctness of Tarjan's algorithm relies on the properties of the DFS tree and the maintenance of the stack.

### The Root Condition
A vertex $u$ is the root of an SCC if and only if:
$$\text{low}(u) = \text{tin}(u)$$
This condition implies that no vertex in the subtree rooted at $u$ has a back-edge to any ancestor of $u$ in the DFS tree. Consequently, the vertices in the subtree of $u$ that have not yet been assigned to an SCC form a complete SCC.

### Stack Invariant
Let $\mathcal{S}_t$ be the set of vertices currently on the stack at time $t$. For any vertex $u$, if $v \in \mathcal{S}_t$ and there exists a path from $u$ to $v$, then $v$ must be an ancestor of $u$ in the DFS tree or $v$ must be in the same SCC as $u$. The stack maintains the property that vertices are popped if and only if they form a maximal strongly connected subgraph.

### Transition Logic
For an edge $(u, v) \in E$:
1.  **Tree Edge:** If $v$ is unvisited, $\text{low}(u) \leftarrow \min(\text{low}(u), \text{low}(v))$.
2.  **Back Edge:** If $v$ is visited and $\text{on\_stack}(v) = 1$, $\text{low}(u) \leftarrow \min(\text{low}(u), \text{tin}(v))$.
3.  **Cross Edge:** If $v$ is visited and $\text{on\_stack}(v) = 0$, the edge is ignored, as $v$ belongs to a previously identified SCC.

## 3. Complexity Analysis

### Time Complexity
The algorithm performs a single DFS traversal. 
*   Each vertex $v \in V$ is visited exactly once, resulting in $O(V)$ operations for initialization and stack management.
*   Each edge $(u, v) \in E$ is examined exactly once during the adjacency list traversal.
*   The stack operations (push and pop) occur at most once per vertex.
*   The total time complexity is given by the sum of vertex visits and edge relaxations:
    $$T(V, E) = \sum_{v \in V} O(1) + \sum_{u \in V} \text{deg}_{out}(u) = O(V + E)$$
Thus, the algorithm is linear with respect to the size of the graph.

### Space Complexity
The space complexity is determined by the auxiliary data structures:
*   $\text{tin}$ and $\text{low}$ arrays: $O(V)$.
*   $\text{on\_stack}$ boolean array: $O(V)$.
*   $\text{Stack}$ and recursion depth (DFS stack): $O(V)$.
*   Adjacency list storage: $O(V + E)$.
Since the output (the SCCs) partitions $V$, storing the result requires $O(V)$ space.
Total auxiliary space complexity is $O(V)$, while total space including the input graph is $O(V + E)$.