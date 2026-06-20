# Formal Mathematical Specification: Articulation Points (Cut Vertices)

## 1. Definitions and Notation

Let $G = (V, E)$ be an undirected, connected graph where $V = \{v_1, v_2, \dots, v_n\}$ is the set of vertices and $E \subseteq \{\{u, v\} : u, v \in V, u \neq v\}$ is the set of edges. Let $n = |V|$ and $m = |E|$.

An **Articulation Point** is a vertex $v \in V$ such that the subgraph $G' = (V \setminus \{v\}, E')$ has more connected components than $G$, where $E' = \{e \in E : v \notin e\}$.

We define the following mappings and sets generated during a Depth-First Search (DFS) traversal starting at an arbitrary root $r \in V$:
*   $T = (V, E_T)$: The DFS spanning tree, where $E_T \subset E$ is the set of tree edges.
*   $E_B = E \setminus E_T$: The set of back-edges.
*   $tin(u) \in \mathbb{N}_0$: The discovery time of vertex $u$, representing the order in which $u$ is first visited.
*   $low(u) \in \mathbb{N}_0$: The lowest discovery time reachable from $u$ in $T$ by traversing zero or more tree edges in the subtree rooted at $u$, followed by at most one back-edge.
*   $parent(u)$: The predecessor of $u$ in $T$.
*   $children(u) = \{v \in V : (u, v) \in E_T\}$: The set of children of $u$ in $T$.

## 2. Algebraic Characterization

The values of $low(u)$ are defined by the following recurrence relation:
$$low(u) = \min \left( \{tin(u)\} \cup \{low(v) : v \in children(u)\} \cup \{tin(v) : (u, v) \in E_B\} \right)$$

A vertex $u \in V$ is an articulation point if and only if it satisfies one of the following two conditions:

1.  **Root Case:** If $u = r$, then $u$ is an articulation point if and only if $|children(r)| > 1$.
2.  **Non-Root Case:** If $u \neq r$, then $u$ is an articulation point if and only if there exists at least one child $v \in children(u)$ such that:
    $$low(v) \geq tin(u)$$

**Proof Sketch:**
If $low(v) \geq tin(u)$, there exists no path from the subtree rooted at $v$ to any ancestor of $u$ that does not pass through $u$. Thus, removing $u$ disconnects the subtree $T_v$ from the remainder of the graph $G \setminus T_v$. Conversely, if $u$ is not the root and has no such child, every subtree $T_v$ has a back-edge to an ancestor of $u$, ensuring connectivity remains upon the removal of $u$.

## 3. Complexity Analysis

### Time Complexity: $O(V + E)$
The algorithm performs a single DFS traversal. 
*   Each vertex $v \in V$ is visited exactly once, contributing $O(1)$ to the discovery time assignment.
*   Each edge $e \in E$ is examined exactly twice (once from each endpoint).
*   The update operations for $low(u)$ and the conditional checks for articulation points are $O(1)$ per edge traversal.
*   The total time complexity is given by the summation of work over all vertices and edges:
    $$T(n, m) = \sum_{v \in V} O(deg(v)) = O(2m) = O(V + E)$$

### Space Complexity: $O(V)$
The auxiliary space required is dominated by the storage of the graph and the state arrays:
*   **Adjacency List:** $O(V + E)$ to store the graph structure.
*   **State Arrays:** The arrays $tin$, $low$, and $parent$ each require $O(V)$ space.
*   **Recursion Stack:** In the worst case (a path graph), the DFS recursion depth is $O(V)$.
*   **Total Space:** Excluding the input graph, the auxiliary space is $O(V)$. Including the input representation, the space complexity is $O(V + E)$. Given the problem constraints, the auxiliary space is strictly $O(V)$.