# Formal Mathematical Specification: Bellman-Ford Algorithm

## 1. Definitions and Notation

Let $G = (V, E)$ be a directed, weighted graph, where $V = \{v_1, v_2, \dots, v_n\}$ is the set of vertices such that $|V| = n$, and $E \subseteq V \times V$ is the set of directed edges. Each edge $e = (u, v) \in E$ is associated with a weight function $w: E \to \mathbb{R}$.

We define the following:
*   **Source Vertex:** A designated vertex $s \in V$.
*   **Distance Function:** A mapping $d: V \to \mathbb{R} \cup \{\infty\}$, where $d(v)$ represents the current estimate of the shortest path distance from $s$ to $v$.
*   **Path Weight:** For a path $P = (v_0, v_1, \dots, v_k)$, the weight is defined as $W(P) = \sum_{i=1}^{k} w(v_{i-1}, v_i)$.
*   **Shortest Path:** The distance $\delta(s, v) = \inf \{ W(P) : P \text{ is a path from } s \text{ to } v \}$. If no path exists, $\delta(s, v) = \infty$. If $v$ is reachable from a negative weight cycle, $\delta(s, v) = -\infty$.

## 2. Algebraic Characterization

The Bellman-Ford algorithm is an application of dynamic programming based on the principle of relaxation. We define $d^{(k)}(v)$ as the weight of the shortest path from $s$ to $v$ using at most $k$ edges.

### Recurrence Relation
The optimal substructure is defined by the following recurrence:
1.  **Base Case:** 
    $d^{(0)}(s) = 0$ and $d^{(0)}(v) = \infty$ for all $v \in V \setminus \{s\}$.
2.  **Recursive Step:** For $k = 1, 2, \dots, n-1$:
    $d^{(k)}(v) = \min \left( d^{(k-1)}(v), \min_{(u, v) \in E} \{ d^{(k-1)}(u) + w(u, v) \} \right)$

### Loop Invariant
At the start of each iteration $k$ of the outer loop (where $k$ ranges from $1$ to $n-1$), the following invariant holds:
For every vertex $v \in V$, $d(v)$ is the weight of the shortest path from $s$ to $v$ using at most $k-1$ edges.

### Negative Cycle Detection
A graph contains a negative weight cycle reachable from $s$ if and only if there exists an edge $(u, v) \in E$ such that:
$$\delta(s, v) > \delta(s, u) + w(u, v)$$
After $n-1$ iterations, the algorithm performs a final check. If for any $(u, v) \in E$, $d(u) + w(u, v) < d(v)$, then the graph contains a negative cycle, as the shortest path would require at least $n$ edges, implying a cycle exists by the Pigeonhole Principle.

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of an outer loop that executes $n-1$ times. Inside this loop, the algorithm iterates over the set of edges $E$. 

The total number of operations $T(n, m)$ (where $m = |E|$) is given by:
$$T(n, m) = \sum_{k=1}^{n-1} \sum_{(u, v) \in E} \Theta(1) = \Theta((n-1) \cdot m) = \Theta(n \cdot m)$$
In the worst case, where the graph is dense ($m = \Theta(n^2)$), the complexity is $O(n^3)$. In a sparse graph ($m = \Theta(n)$), the complexity is $O(n^2)$. The "early exit" optimization (terminating if no relaxation occurs in an iteration) provides a best-case time complexity of $\Omega(m)$, occurring when the shortest path tree is discovered in the first iteration.

### Space Complexity
The algorithm maintains a distance array $d$ of size $|V|$ to store the current shortest path estimates. 
*   **Auxiliary Space:** $O(n)$ to store the distance estimates.
*   **Total Space:** $O(n + m)$ to store the graph representation (the edge list) and the distance array.
Since the algorithm operates directly on the edge list, the auxiliary space complexity is strictly $O(n)$, satisfying the requirement for $O(V)$ space.