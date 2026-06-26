# Formal Mathematical Specification: Bipartite Matching (Max Flow)

## 1. Definitions and Notation

Let $G = (V, E)$ be a bipartite graph where the vertex set $V$ is partitioned into two disjoint sets $L$ (left, $|L| = n_L$) and $R$ (right, $|R| = n_R$), such that $E \subseteq L \times R$. A matching $M \subseteq E$ is a set of edges such that no two edges in $M$ share a common vertex. The objective is to find the cardinality of the maximum matching, $|M^*| = \max \{|M| : M \text{ is a matching}\}$.

To solve this via network flow, we define a flow network $\mathcal{N} = (V', E', c, s, t)$ where:
*   **Vertex Set:** $V' = L \cup R \cup \{s, t\}$, where $s$ is the source and $t$ is the sink.
*   **Edge Set:** $E' = \{(s, u) : u \in L\} \cup \{(u, v) : (u, v) \in E\} \cup \{(v, t) : v \in R\}$.
*   **Capacity Function:** $c: E' \to \mathbb{Z}^+$ defined as:
    *   $c(s, u) = 1, \forall u \in L$
    *   $c(u, v) = 1, \forall (u, v) \in E$
    *   $c(v, t) = 1, \forall v \in R$
*   **Flow:** A function $f: E' \to \mathbb{R}$ satisfying capacity constraints $0 \leq f(e) \leq c(e)$ and flow conservation $\sum_{u} f(u, v) = \sum_{w} f(v, w)$ for all $v \in V' \setminus \{s, t\}$.

## 2. Algebraic Characterization

The correctness of this reduction relies on the **Integrality Theorem** and the construction of the network. Since all capacities $c(e)$ are integers, there exists an integer-valued maximum flow $f^*$.

**Theorem (Equivalence):** The value of the maximum flow $|f^*| = \sum_{u \in L} f(s, u)$ is equal to the cardinality of the maximum bipartite matching $|M^*|$.

*Proof Sketch:*
1.  **Matching to Flow:** Given a matching $M$, define a flow $f$ by setting $f(s, u) = 1, f(u, v) = 1, f(v, t) = 1$ for all $(u, v) \in M$, and $0$ otherwise. The flow value is $|M|$.
2.  **Flow to Matching:** Given an integer flow $f$ in $\mathcal{N}$, the set $M = \{(u, v) \in E : f(u, v) = 1\}$ constitutes a valid matching because the capacity constraints $c(s, u) = 1$ and $c(v, t) = 1$ ensure that each $u \in L$ and $v \in R$ is incident to at most one edge in $M$.

The algorithm maintains the invariant that at each iteration, the residual graph $G_f$ contains an augmenting path $p$ from $s$ to $t$. The flow is updated via $f_{new} = f + \Delta f$, where $\Delta f$ is the flow along $p$. By the **Max-Flow Min-Cut Theorem**, the algorithm terminates when no such path exists, at which point the flow is maximal.

## 3. Complexity Analysis

### Time Complexity: $O(V \cdot E)$
The Edmonds-Karp algorithm generally runs in $O(V \cdot E^2)$. However, in a bipartite matching network, we observe the following:
1.  **Unit Capacities:** Every edge has capacity 1.
2.  **Augmenting Paths:** Each augmentation increases the flow by exactly 1 unit. Since the maximum possible flow is $\min(|L|, |R|) \leq |V|$, there are at most $O(V)$ augmentations.
3.  **BFS Cost:** Each BFS traversal of the residual graph takes $O(V + E)$.
4.  **Total Work:** The total time complexity is $O(\text{max\_flow} \times (V + E))$. Since $\text{max\_flow} \leq V$, the complexity is $O(V(V+E))$. Given that in a bipartite graph $E \geq V-1$ (for a connected graph), this simplifies to $O(V \cdot E)$.

### Space Complexity: $O(V^2)$
*   **Adjacency Matrix:** The capacity matrix $c$ requires $O(|V'|^2)$ space, where $|V'| = |L| + |R| + 2$. Since $|V'| \approx |V|$, the space complexity is $O(V^2)$.
*   **Adjacency List:** If implemented using adjacency lists to store the graph and residual capacities, the space complexity is $O(V + E)$, which is more memory-efficient for sparse bipartite graphs.