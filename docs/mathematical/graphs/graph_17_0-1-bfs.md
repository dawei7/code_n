# Formal Mathematical Specification: 0-1 BFS (Shortest Path)

## 1. Definitions and Notation

Let $G = (V, E)$ be a weighted, undirected graph, where $V = \{v_1, v_2, \dots, v_n\}$ is the set of vertices and $E \subseteq V \times V$ is the set of edges. We define a weight function $w: E \to \{0, 1\}$ that assigns a binary cost to each edge.

*   **Input:** A graph $G = (V, E)$, a weight function $w$, and a source vertex $s \in V$.
*   **Output:** A distance mapping $\delta: V \to \mathbb{N} \cup \{\infty\}$, where $\delta(v)$ denotes the shortest path distance from $s$ to $v$.
*   **State Space:** The algorithm maintains a state represented by the tuple $(dist, Q)$, where $dist: V \to \mathbb{N} \cup \{\infty\}$ is the current estimate of the shortest path distance, and $Q$ is a double-ended queue (deque) containing a subset of $V$.
*   **Distance Metric:** The shortest path distance $d(s, v)$ is defined as:
    $$d(s, v) = \min_{P \in \mathcal{P}_{s,v}} \sum_{e \in P} w(e)$$
    where $\mathcal{P}_{s,v}$ is the set of all paths from $s$ to $v$.

## 2. Algebraic Characterization

The correctness of the 0-1 BFS algorithm relies on the maintenance of a monotonic property within the deque $Q$. Let $Q = (q_1, q_2, \dots, q_k)$ be the sequence of vertices in the deque.

**Invariant:** At any iteration, the sequence of distances in the deque is non-decreasing and takes at most two values:
$$\exists d \in \mathbb{N} \text{ s.t. } \forall q_i \in Q, dist(q_i) \in \{d, d+1\}$$
Furthermore, if $dist(q_i) = d+1$, then for all $j > i$, $dist(q_j) = d+1$.

**Relaxation Condition:** For an edge $(u, v) \in E$ with weight $w(u, v)$, the distance estimate is updated via the relaxation operation:
$$dist(v) = \min(dist(v), dist(u) + w(u, v))$$

**Transition Rules:**
When processing vertex $u$ with current distance $dist(u) = d$:
1.  If $w(u, v) = 0$ and $dist(u) + 0 < dist(v)$, we update $dist(v) \leftarrow d$ and perform $Q.\text{push\_front}(v)$.
2.  If $w(u, v) = 1$ and $dist(u) + 1 < dist(v)$, we update $dist(v) \leftarrow d + 1$ and perform $Q.\text{push\_back}(v)$.

This ensures that the deque remains sorted by distance, satisfying the property that $dist(q_i) \leq dist(q_{i+1})$ for all $i$. This is a specific instance of the **Monotonic Queue Property**, which guarantees that when a vertex $u$ is popped from the front of the deque, $dist(u)$ is the optimal shortest path distance $d(s, u)$.

## 3. Complexity Analysis

### Time Complexity
The time complexity is $O(|V| + |E|)$.

*   **Initialization:** Initializing the distance array takes $O(|V|)$.
*   **Vertex Processing:** Each vertex $v \in V$ is added to and removed from the deque at most once. This is because a vertex is only added to the deque if its distance estimate is strictly improved. Since the maximum possible distance is $|V|-1$, and each update decreases the distance, the total number of deque operations is bounded by $O(|V|)$.
*   **Edge Relaxation:** For each vertex $u$, we iterate over its adjacency list. Across the entire execution, each edge $(u, v) \in E$ is examined exactly twice (once from $u$ and once from $v$). Each relaxation check and deque operation (push/pop) is $O(1)$.
*   **Summation:** The total work $T$ is given by:
    $$T = \sum_{v \in V} O(1) + \sum_{u \in V} \text{deg}(u) \cdot O(1) = O(|V| + 2|E|) = O(|V| + |E|)$$

### Space Complexity
The space complexity is $O(|V|)$.

*   **Distance Array:** Storing $dist(v)$ for all $v \in V$ requires $O(|V|)$ space.
*   **Adjacency List:** Storing the graph requires $O(|V| + |E|)$ space. However, in the context of auxiliary space for the algorithm (excluding the input graph), we only require the deque $Q$ and the distance array.
*   **Deque:** In the worst case, the deque contains all vertices, requiring $O(|V|)$ space.
*   **Total Auxiliary Space:** $O(|V|)$.