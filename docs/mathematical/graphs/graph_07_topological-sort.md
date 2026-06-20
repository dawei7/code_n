# Formal Mathematical Specification: Topological Sort

## 1. Definitions and Notation

Let $G = (V, E)$ be a directed graph, where $V = \{v_1, v_2, \dots, v_n\}$ is a finite set of vertices and $E \subseteq V \times V$ is a set of directed edges. We define the graph as a Directed Acyclic Graph (DAG) if there exists no sequence of vertices $(v_1, v_2, \dots, v_k)$ such that $(v_i, v_{i+1}) \in E$ for $1 \le i < k$ and $v_1 = v_k$.

*   **In-degree Function:** We define the in-degree of a vertex $v \in V$ as $\text{deg}^-(v) = |\{u \in V : (u, v) \in E\}|$.
*   **Topological Ordering:** A topological sort of $G$ is a bijection $\sigma: V \to \{1, 2, \dots, n\}$ such that for every directed edge $(u, v) \in E$, the condition $\sigma(u) < \sigma(v)$ holds.
*   **State Space:** The algorithm maintains a state $\mathcal{S} = (\text{deg}^-, Q, \mathcal{L})$, where:
    *   $\text{deg}^-: V \to \mathbb{N}_0$ is the current in-degree mapping.
    *   $Q \subseteq \{v \in V : \text{deg}^-(v) = 0\}$ is the set of vertices with zero in-degree (the "ready" set).
    *   $\mathcal{L} = (l_1, l_2, \dots, l_k)$ is the ordered sequence of vertices processed thus far.

## 2. Algebraic Characterization

The correctness of Kahn’s algorithm relies on the property that every non-empty DAG contains at least one vertex with an in-degree of zero.

**Loop Invariant:** At the start of each iteration of the `while` loop, let $V_{processed} = \{l_1, \dots, l_k\}$ be the set of vertices already appended to $\mathcal{L}$. The following conditions hold:
1.  For all $v \in V \setminus V_{processed}$, $\text{deg}^-(v)$ is equal to the number of edges $(u, v) \in E$ such that $u \notin V_{processed}$.
2.  $Q = \{v \in V \setminus V_{processed} : \text{deg}^-(v) = 0\}$.
3.  For all $(u, v) \in E$, if $u \in V_{processed}$, then $v \in V_{processed}$.

**Termination and Correctness:**
The algorithm terminates when $Q = \emptyset$. Let $n = |V|$.
*   If $|V_{processed}| = n$, then $\sigma(v_i) = i$ defines a valid topological ordering, as the invariant ensures no edge $(u, v)$ exists where $u$ is processed after $v$.
*   If $|V_{processed}| < n$, then the set $V \setminus V_{processed}$ is non-empty and contains no vertices with in-degree zero. By the contrapositive of the DAG property, $G$ must contain at least one directed cycle.

## 3. Complexity Analysis

### Time Complexity
The algorithm performs the following operations:
1.  **Initialization:** Calculating $\text{deg}^-(v)$ for all $v \in V$ requires iterating over all edges. This takes $\Theta(|V| + |E|)$.
2.  **Queue Operations:** Each vertex $v \in V$ is added to and removed from $Q$ exactly once. This contributes $\Theta(|V|)$.
3.  **Edge Relaxation:** For each vertex $u$ removed from $Q$, we iterate over its adjacency list $Adj(u)$. The total work across all iterations is $\sum_{u \in V} \text{deg}^+(u) = |E|$.

Thus, the total time complexity is:
$$T(V, E) = \Theta(|V| + |E|)$$
For an adjacency matrix representation, the inner loop iterates over all $V$ vertices for each $u$, leading to:
$$T(V) = \Theta(V^2)$$

### Space Complexity
The space complexity is determined by the storage of the graph and the auxiliary data structures:
1.  **Adjacency List:** $\Theta(|V| + |E|)$.
2.  **In-degree Array:** $\Theta(|V|)$.
3.  **Queue and Ordering List:** $\Theta(|V|)$.

The total auxiliary space complexity is $\Theta(|V|)$, while the total space complexity (including the graph representation) is $\Theta(|V| + |E|)$.