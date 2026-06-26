# Formal Mathematical Specification: Graph Representations

## 1. Definitions and Notation

Let $G = (V, E)$ be an undirected graph, where $V = \{0, 1, \dots, n-1\}$ is a finite set of $n$ vertices and $E \subseteq \{\{u, v\} : u, v \in V, u \neq v\}$ is a set of $m$ edges.

*   **Input Domain:** The input is defined by the tuple $(n, \mathcal{E})$, where $n = |V| \in \mathbb{N}$ and $\mathcal{E} = \{e_1, e_2, \dots, e_m\}$ is a sequence of edges such that $e_i = (u_i, v_i) \in V \times V$.
*   **Adjacency Matrix Representation:** A mapping $M: V \times V \to \{0, 1\}$ defined as:
    $$M_{uv} = \begin{cases} 1 & \text{if } \{u, v\} \in E \\ 0 & \text{otherwise} \end{cases}$$
*   **Adjacency List Representation:** A mapping $A: V \to \mathcal{P}(V)$, where $\mathcal{P}(V)$ denotes the power set of $V$, defined as:
    $$A(u) = \{v \in V : \{u, v\} \in E\}$$
    The representation is the collection of sets $\{A(u) : u \in V\}$.

## 2. Algebraic Characterization

The construction of the graph representation is a transformation from the edge set $\mathcal{E}$ to the structural mappings $M$ or $A$.

**Adjacency Matrix Construction:**
The matrix $M$ is initialized as the zero matrix $0_{n \times n}$. For each edge $(u, v) \in \mathcal{E}$, the state transition is:
$$M_{uv}^{(k)} = M_{vu}^{(k)} = 1$$
where $M^{(k)}$ denotes the state after processing the $k$-th edge. The final state is $M = \sum_{i=1}^m \delta_i$, where $\delta_i$ is the indicator matrix for edge $e_i$.

**Adjacency List Construction:**
The adjacency list is defined by the union of singleton sets. Let $A_0(u) = \emptyset$ for all $u \in V$. For each edge $(u, v) \in \mathcal{E}$, the update rule is:
$$A_{k}(u) = A_{k-1}(u) \cup \{v\}$$
$$A_{k}(v) = A_{k-1}(v) \cup \{u\}$$
The correctness of the representation is guaranteed by the invariant that at step $k=m$, the set $A(u)$ contains exactly the set of vertices adjacent to $u$ in $G$.

## 3. Complexity Analysis

### Time Complexity
*   **Adjacency Matrix:** The initialization requires filling $n^2$ cells, yielding $\Theta(n^2)$. Processing $m$ edges requires $O(m)$ operations. The total time complexity is $T(n, m) = \Theta(n^2 + m)$.
*   **Adjacency List:** Initialization of the hash map or array of size $n$ takes $\Theta(n)$. Inserting $m$ edges into sets (or lists) takes $O(m)$ time, assuming constant time insertion. The total time complexity is $T(n, m) = \Theta(n + m)$.

### Space Complexity
*   **Adjacency Matrix:** The space required is strictly determined by the dimensions of the matrix, $S(n) = \Theta(n^2)$.
*   **Adjacency List:** The space required is proportional to the number of vertices and the sum of the degrees of all vertices. By the Handshaking Lemma, $\sum_{v \in V} \text{deg}(v) = 2m$. Thus, the space complexity is:
    $$S(n, m) = \Theta\left(n + \sum_{v \in V} \text{deg}(v)\right) = \Theta(n + m)$$
    This demonstrates that for sparse graphs where $m \ll n^2$, the adjacency list is asymptotically superior in memory utilization.