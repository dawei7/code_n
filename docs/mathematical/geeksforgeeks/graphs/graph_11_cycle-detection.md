# Formal Mathematical Specification: Cycle Detection (Directed and Undirected)

## 1. Definitions and Notation

Let $G = (V, E)$ be a graph where $V = \{v_1, v_2, \dots, v_n\}$ is the set of vertices and $E \subseteq V \times V$ is the set of edges. Let $n = |V|$ and $m = |E|$.

*   **Undirected Graph:** $E$ is a set of unordered pairs $\{u, v\}$. The adjacency relation is symmetric: $(u, v) \in E \iff (v, u) \in E$.
*   **Directed Graph (Digraph):** $E$ is a set of ordered pairs $(u, v)$.
*   **Cycle:** A sequence of vertices $(v_1, v_2, \dots, v_k)$ such that $(v_i, v_{i+1}) \in E$ for $1 \le i < k$ and $(v_k, v_1) \in E$.
*   **State Space $\mathcal{S}$:**
    *   For undirected graphs, we define a mapping $\phi: V \to \{0, 1\}$, where $\phi(v) = 1$ if $v$ has been visited, and $0$ otherwise.
    *   For directed graphs, we define a mapping $\sigma: V \to \{0, 1, 2\}$, representing the colors: White ($0$), Gray ($1$), and Black ($2$).

## 2. Algebraic Characterization

### Undirected Graphs
A cycle exists in an undirected graph if and only if there exists an edge $(u, v) \in E$ such that $v$ is already visited and $v \neq \text{parent}(u)$, where $\text{parent}(u)$ is the vertex from which $u$ was discovered in the Depth-First Search (DFS) tree.
Formally, let $T$ be the DFS forest. A cycle exists if there exists a back-edge $(u, v) \in E \setminus T$. Since $T$ contains $n-1$ edges for each connected component, a cycle exists if:
$$|E| > |V| - c$$
where $c$ is the number of connected components. More precisely, during traversal, if we encounter an edge $(u, v)$ such that $\phi(v) = 1$ and $v \neq \text{parent}(u)$, the graph contains a cycle.

### Directed Graphs
A cycle exists in a directed graph if and only if the DFS forest contains at least one **back-edge**. A back-edge is an edge $(u, v)$ where $v$ is an ancestor of $u$ in the DFS tree.
Using the 3-color state mapping $\sigma$:
1.  $\sigma(v) = 0$ (White): $v$ is undiscovered.
2.  $\sigma(v) = 1$ (Gray): $v$ is currently in the recursion stack (an ancestor of the current node).
3.  $\sigma(v) = 2$ (Black): $v$ and all its descendants have been fully explored.

A cycle exists if and only if there exists an edge $(u, v) \in E$ such that $\sigma(u) = 1$ and $\sigma(v) = 1$. This condition implies that $v$ is an ancestor of $u$ in the current recursion path, closing a cycle.

## 3. Complexity Analysis

### Time Complexity
The algorithm performs a traversal (DFS) of the graph.
*   **Initialization:** Initializing the state/visited array takes $O(V)$.
*   **Traversal:** Each vertex $v \in V$ is visited exactly once. For each vertex, we iterate over its adjacency list $Adj(v)$. The total work is:
    $$\sum_{v \in V} \text{deg}(v)$$
    By the Handshaking Lemma, $\sum_{v \in V} \text{deg}(v) = 2|E|$ for undirected graphs and $\sum_{v \in V} \text{deg}_{out}(v) = |E|$ for directed graphs.
*   **Total Time:** $O(V + E)$. Since each edge and vertex is processed a constant number of times, the complexity is $\Theta(V + E)$.

### Space Complexity
*   **State Storage:** The `visited` array or `state` array requires $O(V)$ space to store the status of each vertex.
*   **Recursion Stack:** In the worst-case scenario (e.g., a path graph $v_1 \to v_2 \to \dots \to v_n$), the DFS recursion stack depth reaches $O(V)$.
*   **Adjacency List:** The input representation requires $O(V + E)$ space.
*   **Auxiliary Space:** Excluding the input graph storage, the auxiliary space complexity is $O(V)$.