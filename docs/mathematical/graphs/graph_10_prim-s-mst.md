# Formal Mathematical Specification: Prim's Algorithm (Minimum Spanning Tree)

## 1. Definitions and Notation

Let $G = (V, E, w)$ be a connected, undirected, weighted graph, where:
*   $V = \{v_1, v_2, \dots, v_n\}$ is the set of vertices, with $|V| = n$.
*   $E \subseteq \{\{u, v\} : u, v \in V, u \neq v\}$ is the set of edges, with $|E| = m$.
*   $w: E \to \mathbb{R}^+$ is a weight function assigning a positive real value to each edge.

A **Spanning Tree** $T = (V, E_T)$ is a subgraph of $G$ such that $E_T \subseteq E$, $|E_T| = n - 1$, and $T$ is acyclic. The objective is to find a tree $T^*$ that minimizes the total weight:
$$W(T^*) = \sum_{e \in E_T^*} w(e) = \min_{T \in \mathcal{T}} \sum_{e \in E_T} w(e)$$
where $\mathcal{T}$ is the set of all spanning trees of $G$.

The algorithm maintains the following state:
*   $S \subset V$: The set of vertices already included in the growing tree.
*   $Q$: A priority queue containing edges $e = \{u, v\}$ such that $u \in S$ and $v \in V \setminus S$, ordered by $w(e)$.
*   $E_T$: The set of edges selected for the MST.

## 2. Algebraic Characterization

Prim's algorithm is governed by the **Cut Property** of MSTs. For any cut $(S, V \setminus S)$ of a graph $G$, if an edge $e = \{u, v\}$ with $u \in S$ and $v \in V \setminus S$ has the minimum weight among all edges crossing the cut, then this edge belongs to some MST of $G$.

### Loop Invariant
At the start of each iteration of the main loop, the following conditions hold:
1.  $S$ is the set of vertices connected by the edges in $E_T$.
2.  $E_T$ forms a spanning tree for the subgraph induced by $S$.
3.  $Q$ contains all edges $\{u, v\}$ such that $u \in S$ and $v \in V \setminus S$.
4.  For every $v \in V \setminus S$, the priority queue $Q$ stores the minimum weight edge connecting $v$ to any vertex in $S$.

### Transition
Let $e_{min} = \{u, v\} = \arg \min \{w(e) : e = \{x, y\}, x \in S, y \in V \setminus S\}$.
The state transitions as:
$$S_{i+1} = S_i \cup \{v\}$$
$$E_{T, i+1} = E_{T, i} \cup \{e_{min}\}$$
The algorithm terminates when $S = V$, at which point $|E_T| = n - 1$.

## 3. Complexity Analysis

### Time Complexity
The algorithm performs the following operations:
1.  **Initialization:** Building the adjacency list takes $O(m)$.
2.  **Priority Queue Operations:**
    *   Each vertex $v \in V$ is added to $S$ exactly once. When $v$ is added, we iterate over its adjacency list $\text{adj}(v)$.
    *   Each edge $\{u, v\} \in E$ is inserted into the priority queue at most twice (once for each endpoint). Thus, there are at most $2m$ `push` operations.
    *   Each `pop` operation removes an edge from the priority queue. There are at most $2m$ `pop` operations.
    *   Since the priority queue contains at most $m$ elements, each `push` and `pop` operation takes $O(\log m)$ time.

Given $m \leq n^2$, we have $\log m \leq \log n^2 = 2 \log n$, thus $O(\log m) = O(\log n)$. The total time complexity is:
$$T(n, m) = O(m \log m) = O(m \log n)$$

### Space Complexity
1.  **Adjacency List:** Storing the graph requires $O(n + m)$ space.
2.  **Visited Set:** Storing the membership of $S$ requires $O(n)$ space.
3.  **Priority Queue:** In the worst case, the priority queue stores all edges, requiring $O(m)$ space.

Total auxiliary space complexity is $O(n + m)$. In a standard implementation where the graph is provided, the space complexity is dominated by the storage of the graph and the priority queue, yielding $O(V + E)$.