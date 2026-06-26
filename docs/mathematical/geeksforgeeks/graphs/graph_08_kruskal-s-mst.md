# Formal Mathematical Specification: Kruskal's Algorithm (Minimum Spanning Tree)

## 1. Definitions and Notation

Let $G = (V, E, w)$ be a connected, undirected, weighted graph, where:
*   $V = \{v_1, v_2, \dots, v_n\}$ is the set of vertices, with $|V| = n$.
*   $E \subseteq \{\{u, v\} : u, v \in V, u \neq v\}$ is the set of edges, with $|E| = m$.
*   $w: E \to \mathbb{R}^+$ is a weight function assigning a positive real value to each edge.

A **Spanning Tree** $T = (V, E_T)$ is a subgraph of $G$ such that $E_T \subseteq E$, $|E_T| = n - 1$, and $T$ is acyclic. The weight of the spanning tree is defined as $W(T) = \sum_{e \in E_T} w(e)$. A **Minimum Spanning Tree (MST)** is a spanning tree $T^*$ such that $W(T^*) \leq W(T)$ for all spanning trees $T$ of $G$.

The algorithm utilizes a **Disjoint Set Union (DSU)** data structure, defined as a partition $\mathcal{P} = \{S_1, S_2, \dots, S_k\}$ of $V$. The DSU supports two operations:
*   $\text{find}(v)$: Returns the representative element of the set $S_i$ containing $v$.
*   $\text{union}(u, v)$: Merges the sets containing $u$ and $v$ if they are distinct, maintaining the partition property.

## 2. Algebraic Characterization

Kruskal's algorithm is a greedy strategy based on the **Cut Property** of MSTs. For any cut $(S, V \setminus S)$ of $G$, if an edge $e$ is the minimum weight edge crossing the cut, then $e$ belongs to some MST of $G$.

Let $E' = \{e_1, e_2, \dots, e_m\}$ be the set of edges sorted such that $w(e_1) \leq w(e_2) \leq \dots \leq w(e_m)$. The algorithm constructs a sequence of forests $F_i = (V, E_i)$, where $E_0 = \emptyset$ and $E_i$ is defined by the recurrence:

$$E_i = \begin{cases} E_{i-1} \cup \{e_i\} & \text{if } e_i = \{u, v\} \text{ and } \text{find}(u) \neq \text{find}(v) \\ E_{i-1} & \text{otherwise} \end{cases}$$

**Loop Invariant:** At each step $i$, the forest $F_i$ is a subset of some MST of $G$. 
*   **Initialization:** $F_0$ is a forest of $n$ isolated vertices, which is trivially a subset of any MST.
*   **Maintenance:** By the Cut Property, if $e_i$ connects two components $C_u$ and $C_v$ and has the minimum weight among all edges connecting $C_u$ to $V \setminus C_u$, then $e_i$ is safe to add. Since we process edges in non-decreasing order, $e_i$ is guaranteed to be the minimum weight edge crossing the cut defined by the partition of $V$ into the current connected components.
*   **Termination:** The algorithm terminates when $|E_i| = n - 1$, resulting in a spanning tree $T^* = (V, E_{n-1})$.

## 3. Complexity Analysis

### Time Complexity
The total time complexity $T(n, m)$ is the sum of the sorting phase and the DSU operations:

1.  **Sorting:** Sorting $m$ edges takes $O(m \log m)$. Since $m \leq n^2$, $\log m \leq \log n^2 = 2 \log n$, thus $O(m \log m) = O(m \log n)$.
2.  **DSU Operations:** We perform $m$ `find` operations and at most $n-1$ `union` operations. Using path compression and union-by-rank, the amortized time complexity per operation is $O(\alpha(n))$, where $\alpha$ is the inverse Ackermann function.

The total time is:
$$T(n, m) = O(m \log m + m \cdot \alpha(n))$$
Given that $\alpha(n)$ grows extremely slowly and is effectively constant for all practical $n$, the sorting term dominates:
$$T(n, m) = O(m \log m) \equiv O(m \log n)$$

### Space Complexity
The space complexity $S(n, m)$ is determined by the storage requirements:
1.  **Graph Storage:** $O(m)$ to store the edge list.
2.  **DSU Structure:** $O(n)$ to store the `parent` and `rank` arrays.
3.  **Output:** $O(n)$ to store the edges of the MST.

Thus, the total space complexity is:
$$S(n, m) = O(n + m)$$
In a sparse graph where $m = O(n)$, this simplifies to $O(n)$.