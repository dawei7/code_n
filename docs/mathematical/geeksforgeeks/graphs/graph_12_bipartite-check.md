# Formal Mathematical Specification: Bipartite Graph Check

## 1. Definitions and Notation

Let $G = (V, E)$ be an undirected graph, where $V = \{v_1, v_2, \dots, v_n\}$ is the set of vertices and $E \subseteq \{\{u, v\} : u, v \in V, u \neq v\}$ is the set of edges. Let $n = |V|$ and $m = |E|$. The graph is represented by an adjacency list $Adj: V \to \mathcal{P}(V)$, where $Adj(u) = \{v \in V : \{u, v\} \in E\}$.

A graph $G$ is **bipartite** if there exists a partition of $V$ into two disjoint sets $U$ and $W$ such that $V = U \cup W$, $U \cap W = \emptyset$, and for every edge $\{u, v\} \in E$, either ($u \in U$ and $v \in W$) or ($u \in W$ and $v \in U$).

We define a coloring function $c: V \to \{0, 1, \perp\}$, where $\perp$ denotes an uncolored state. The algorithm seeks to determine if there exists a function $c$ such that for all $\{u, v\} \in E$:
1. $c(u) \neq \perp$ and $c(v) \neq \perp$
2. $c(u) \neq c(v)$

## 2. Algebraic Characterization

The correctness of the algorithm relies on the following theorem: *A graph $G$ is bipartite if and only if it contains no cycles of odd length.*

### Loop Invariant
Let $Q$ be the queue used in the Breadth-First Search (BFS) and $c_k$ be the coloring state after $k$ iterations. For any vertex $v$ such that $c(v) \in \{0, 1\}$, the following invariant holds:
$$\forall u \in Adj(v), \text{ if } c(u) \neq \perp \implies c(u) = 1 - c(v)$$
If at any step $k$, there exists an edge $\{u, v\} \in E$ such that $c(u) = c(v) \neq \perp$, the algorithm terminates and returns $\text{False}$. This condition implies the existence of an odd cycle, as the path from the root of the BFS tree to $u$ and $v$ combined with the edge $\{u, v\}$ forms a cycle of length $d(root, u) + d(root, v) + 1$. Since $c(u) = c(v)$, the distances $d(root, u)$ and $d(root, v)$ must have the same parity, making the cycle length $2k + 1$, which is odd.

### State Transition
The algorithm performs a traversal where for a current vertex $u$ and neighbor $v$:
$$c(v) = \begin{cases} 1 - c(u) & \text{if } c(v) = \perp \\ c(v) & \text{if } c(v) \neq \perp \end{cases}$$
The algorithm returns $\text{False}$ if $\exists \{u, v\} \in E$ such that $c(u) = c(v)$. Otherwise, it returns $\text{True}$.

## 3. Complexity Analysis

### Time Complexity
The algorithm visits each vertex $v \in V$ exactly once and traverses each edge $\{u, v\} \in E$ exactly twice (once from $u$ and once from $v$). 
The total work $T(n, m)$ can be expressed as:
$$T(n, m) = \sum_{v \in V} \Theta(1) + \sum_{v \in V} \sum_{u \in Adj(v)} \Theta(1)$$
Since $\sum_{v \in V} |Adj(v)| = 2m$, the complexity is:
$$T(n, m) = \Theta(n + 2m) = O(V + E)$$
This is optimal as the algorithm must inspect every vertex and edge at least once to verify the bipartite property.

### Space Complexity
The space complexity $S(n)$ is dominated by the auxiliary structures required for the traversal:
1. The `colors` array: $O(V)$ to store the state of each vertex.
2. The `queue` for BFS: In the worst case (a star graph), the queue stores $O(V)$ vertices.
3. The adjacency list: $O(V + E)$ to represent the graph.

Excluding the input graph storage, the auxiliary space complexity is:
$$S(n) = O(V)$$
This is optimal for a graph traversal algorithm requiring state tracking for each vertex.