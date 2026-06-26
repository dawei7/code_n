# Formal Mathematical Specification: Kosaraju's Algorithm (SCC)

## 1. Definitions and Notation

Let $G = (V, E)$ be a directed graph, where $V = \{v_1, v_2, \dots, v_n\}$ is the set of vertices and $E \subseteq V \times V$ is the set of directed edges. Let $|V| = n$ and $|E| = m$.

*   **Strongly Connected Component (SCC):** A subset $S \subseteq V$ is an SCC if for every pair $u, v \in S$, there exists a directed path from $u$ to $v$ and a directed path from $v$ to $u$, and $S$ is maximal with respect to this property.
*   **Transpose Graph:** The transpose of $G$, denoted $G^T = (V, E^T)$, is defined by $E^T = \{(v, u) \mid (u, v) \in E\}$.
*   **Reachability:** Let $u \rightsquigarrow v$ denote the existence of a directed path from $u$ to $v$.
*   **Finish Time:** Let $f(u)$ be the timestamp at which the depth-first search (DFS) completes the exploration of the subtree rooted at $u$.
*   **State Space:** The algorithm operates on the state space $\mathcal{S} = (V, E, E^T, \text{visited}, \text{stack}, \mathcal{C})$, where $\text{visited}: V \to \{0, 1\}$, $\text{stack}$ is an ordered sequence of $V$, and $\mathcal{C} = \{S_1, S_2, \dots, S_k\}$ is the partition of $V$ into SCCs.

## 2. Algebraic Characterization

Kosaraju's algorithm relies on the properties of the condensation graph $G^{SCC}$, which is a Directed Acyclic Graph (DAG) where each node represents an SCC of $G$.

### Pass 1: Topological Ordering
The first pass performs a DFS on $G$ to compute the finish times $f(u)$. Let $L$ be the list of vertices sorted by $f(u)$ in descending order.
**Lemma:** If there is an edge $(S_i, S_j)$ in the condensation graph $G^{SCC}$, then $\max_{u \in S_i} f(u) > \max_{v \in S_j} f(v)$.
Consequently, the first element of $L$ is guaranteed to belong to a "source" SCC in $G^{SCC}$.

### Pass 2: Transposition and Traversal
The second pass performs a DFS on $G^T$. By reversing the edges, we invert the reachability: if $S_i \to S_j$ in $G^{SCC}$, then $S_j \to S_i$ in $(G^T)^{SCC}$.
Let $u$ be the vertex with the largest $f(u)$ in the remaining unvisited set. The set of vertices reachable from $u$ in $G^T$, denoted $Reach(u, G^T)$, satisfies:
$$Reach(u, G^T) = \{v \in V \mid u \rightsquigarrow_{G^T} v\} = S_u$$
where $S_u$ is the SCC containing $u$. Because $u$ is chosen from the "sink" SCC of the current subgraph of $G^T$ (which corresponds to a "source" SCC in $G$), the DFS is restricted to $S_u$ and cannot traverse into other SCCs.

**Invariant:** After the $i$-th iteration of the second pass, the set of visited vertices $\bigcup_{j=1}^i S_j$ constitutes the union of the first $i$ SCCs identified in the topological order of $G^{SCC}$.

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of three distinct phases:
1.  **Graph Transposition:** Constructing $G^T$ requires iterating over all edges $E$. This takes $\Theta(V + E)$ time.
2.  **Pass 1 (DFS on $G$):** A standard DFS visits every vertex once and traverses every edge once. The complexity is $\Theta(V + E)$.
3.  **Pass 2 (DFS on $G^T$):** Similarly, a DFS on $G^T$ visits every vertex and edge exactly once. The complexity is $\Theta(V + E)$.

The total time complexity $T(n, m)$ is the sum of these phases:
$$T(n, m) = \Theta(V + E) + \Theta(V + E) + \Theta(V + E) = O(V + E)$$

### Space Complexity
The space complexity $S(n, m)$ is determined by the storage requirements:
1.  **Adjacency Lists:** Storing $G$ and $G^T$ requires $O(V + E)$ space.
2.  **Auxiliary Arrays:** The `visited` array and the `order` stack require $O(V)$ space.
3.  **Recursion Stack:** In the worst case (a degenerate path graph), the DFS recursion depth is $O(V)$.

Thus, the total space complexity is:
$$S(n, m) = O(V + E) + O(V) + O(V) = O(V + E)$$