# Formal Mathematical Specification: Depth-First Search (DFS)

## 1. Definitions and Notation

Let $G = (V, E)$ be a graph, where $V = \{v_1, v_2, \dots, v_n\}$ is a finite set of vertices and $E \subseteq V \times V$ is a set of edges. For a directed graph, we denote the adjacency set of a vertex $u \in V$ as $Adj(u) = \{v \in V \mid (u, v) \in E\}$.

We define the following state variables during the execution of the algorithm:
*   **Discovery Time:** A mapping $d: V \to \mathbb{N}_0$, where $d(u)$ denotes the time at which vertex $u$ is first visited.
*   **Finish Time:** A mapping $f: V \to \mathbb{N}_0$, where $f(u)$ denotes the time at which the exploration of the subtree rooted at $u$ is completed.
*   **Parent Mapping:** A partial function $\pi: V \to V \cup \{\text{null}\}$, where $\pi(v) = u$ if $v$ was discovered during the exploration of $u$.
*   **Coloring:** A function $c: V \to \{\text{white, gray, black}\}$, representing unvisited, active, and finished states, respectively.
*   **Global Timer:** A variable $t \in \mathbb{N}_0$ that increments monotonically with each discovery and finish event.

The output of the algorithm is the tuple $(d, f, \pi)$, representing the discovery times, finish times, and the predecessor subgraph $G_\pi = (V, E_\pi)$, where $E_\pi = \{(\pi(v), v) \in E \mid \pi(v) \neq \text{null}\}$.

## 2. Algebraic Characterization

The DFS algorithm can be characterized by the recursive transition of the state $c(u)$. For a source vertex $s$, the algorithm defines a traversal that satisfies the **Parenthesis Theorem**.

### The Parenthesis Theorem
For any two vertices $u, v \in V$, exactly one of the following conditions holds:
1. The intervals $[d(u), f(u)]$ and $[d(v), f(v)]$ are disjoint, and neither $u$ nor $v$ is a descendant of the other in the DFS forest.
2. The interval $[d(u), f(u)]$ is contained entirely within $[d(v), f(v)]$, and $u$ is a descendant of $v$ in the DFS forest.
3. The interval $[d(v), f(v)]$ is contained entirely within $[d(u), f(u)]$, and $v$ is a descendant of $u$ in the DFS forest.

### Recurrence Relation
The discovery and finish times are governed by the following recursive structure:
$$d(u) = \min \{t \mid \text{state of } u \text{ transitions from white to gray}\}$$
$$f(u) = \max \{t \mid \text{state of } u \text{ transitions from gray to black}\}$$

The algorithm maintains the invariant that at any time $t$, the set of gray vertices forms a path in the DFS forest from the root to the current vertex being explored. The exploration of $u$ is complete if and only if for all $v \in Adj(u)$, $v$ has been visited and $f(v)$ is defined.

## 3. Complexity Analysis

### Time Complexity
The time complexity is derived by summing the work performed at each vertex and edge.
1. **Initialization:** Setting $c(v) = \text{white}$ for all $v \in V$ takes $\Theta(|V|)$.
2. **Vertex Processing:** Each vertex $u$ is visited exactly once when its color transitions from white to gray. The work done per vertex (excluding the loop over neighbors) is $O(1)$.
3. **Edge Processing:** The loop `for v in G[u]` iterates over all $v \in Adj(u)$. Across the entire execution, each edge $(u, v) \in E$ is examined exactly once (in directed graphs) or twice (in undirected graphs).

The total time complexity $T(V, E)$ is:
$$T(V, E) = \sum_{u \in V} (1 + \text{deg}(u)) = |V| + \sum_{u \in V} \text{deg}(u)$$
By the Handshaking Lemma, $\sum_{u \in V} \text{deg}(u) = |E|$ (or $2|E|$ for undirected graphs). Thus, $T(V, E) = \Theta(|V| + |E|)$.
For an adjacency matrix representation, the inner loop iterates over all $n$ vertices for each vertex $u$, yielding $T(V) = \sum_{u \in V} O(|V|) = O(|V|^2)$.

### Space Complexity
The space complexity $S(V, E)$ is determined by the auxiliary data structures:
1. **Storage:** The arrays for $d, f, \pi$ and the set/array for $c$ require $\Theta(|V|)$ space.
2. **Recursion Stack:** In the worst case (e.g., a path graph), the depth of the recursion stack is $|V|$. Thus, the stack space is $O(|V|)$.

Total space complexity is $S(V) = \Theta(|V|)$.