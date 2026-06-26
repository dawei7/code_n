# Formal Mathematical Specification: BFS Grid

## 1. Definitions and Notation

Let the grid be represented as a finite set of cells $G = \{ (r, c) \in \mathbb{Z}^2 \mid 0 \le r < H, 0 \le c < W \}$. 
We define a characteristic function $\chi: G \to \{0, 1\}$, where $\chi(r, c) = 0$ denotes a **passable** cell and $\chi(r, c) = 1$ denotes a **blocked** cell.

The grid induces an undirected graph $\mathcal{G} = (V, E)$ where:
*   **Vertices:** $V = \{ v \in G \mid \chi(v) = 0 \}$.
*   **Edges:** $E = \{ \{u, v\} \subseteq V \mid \|u - v\|_1 = 1 \}$, where $\|\cdot\|_1$ is the Manhattan distance. This defines the 4-connectivity of the grid.

**Input:** A tuple $(G, \chi, s, t)$ where $s, t \in V$.
**Output:** A value $d \in \mathbb{N}_0 \cup \{-1\}$, representing the shortest path length $\delta(s, t)$ in $\mathcal{G}$, or $-1$ if $t$ is unreachable from $s$.

## 2. Algebraic Characterization

The algorithm computes the shortest path distance $\delta(s, t)$ using the property that BFS explores the graph in layers. Let $L_k$ be the set of vertices at distance $k$ from the source $s$:
*   $L_0 = \{s\}$
*   $L_{k+1} = \{ v \in V \setminus \bigcup_{i=0}^k L_i \mid \exists u \in L_k, \{u, v\} \in E \}$

The distance function $\delta(s, v)$ is defined as the smallest $k$ such that $v \in L_k$. The algorithm maintains a queue $Q$ and a set of visited vertices $M \subseteq V$. 

**Loop Invariant:** At the start of each iteration of the `while` loop, for every vertex $v$ that has been dequeued:
1.  If $v$ was reached, $\delta(s, v)$ is correctly recorded.
2.  The set $M$ contains exactly the vertices $v$ for which $\delta(s, v) \le k$, where $k$ is the current distance layer being processed.

The transition function for the state $(u, d)$ is defined by the neighborhood operator $N(u) = \{ v \in V \mid \{u, v\} \in E \}$. The algorithm explores the state space by applying the operator:
$$ \text{Next}(u, d) = \{ (v, d+1) \mid v \in N(u) \land v \notin M \} $$
The algorithm terminates at the smallest $d$ such that $t \in L_d$, satisfying the optimality condition:
$$ \delta(s, t) = \min \{ k \mid t \in L_k \} $$

## 3. Complexity Analysis

### Time Complexity
The time complexity is $O(|V| + |E|)$. 
*   Each vertex $v \in V$ is added to the queue at most once and removed at most once.
*   For each vertex $v$, we examine its neighbors $N(v)$. Since the grid is 4-connected, $|N(v)| \le 4$.
*   The total work is proportional to $\sum_{v \in V} \text{deg}(v) = 2|E|$.
*   Given $|V| = W \times H$ and $|E| \le 4|V|$, the complexity is $O(W \cdot H)$. In the context of an $n \times n$ grid, this is $O(n^2)$.

### Space Complexity
The space complexity is $O(|V|)$.
*   **Visited Set:** The set $M$ stores at most $|V|$ vertices, requiring $O(W \cdot H)$ space.
*   **Queue:** In the worst case (e.g., a grid with no walls), the queue $Q$ may contain a frontier proportional to the perimeter of the search, which is $O(\sqrt{|V|})$ for a grid, but in the worst-case graph topology, it is bounded by $O(|V|)$.
*   **Total:** The auxiliary space is $O(W \cdot H)$, which is $O(n^2)$ for an $n \times n$ grid.