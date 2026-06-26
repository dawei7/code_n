# Formal Mathematical Specification: Hamiltonian Path Existence

## 1. Definitions and Notation

Let $G = (V, E)$ be an unweighted graph, where $V = \{v_1, v_2, \dots, v_n\}$ is the set of vertices such that $|V| = n$, and $E \subseteq V \times V$ is the set of edges. For an undirected graph, $(u, v) \in E \iff (v, u) \in E$.

A **Hamiltonian Path** is defined as a sequence of vertices $P = (p_1, p_2, \dots, p_n)$ such that:
1. $\{p_1, p_2, \dots, p_n\} = V$ (The path visits every vertex).
2. $p_i \neq p_j$ for all $i \neq j$ (The path visits each vertex exactly once).
3. $(p_i, p_{i+1}) \in E$ for all $1 \le i < n$ (Consecutive vertices are adjacent).

The algorithm seeks to determine the existence of a mapping $f: \{1, \dots, n\} \to V$ such that $f$ is a bijection and $(f(i), f(i+1)) \in E$ for all $i \in \{1, \dots, n-1\}$.

## 2. Algebraic Characterization

The algorithm employs a backtracking search over the state space $\mathcal{S} \subseteq V \times \mathcal{P}(V) \times \mathbb{Z}^+$, where a state is defined by the tuple $(u, S, k)$:
- $u \in V$: The current vertex.
- $S \subseteq V$: The set of visited vertices.
- $k = |S|$: The number of vertices visited.

The existence of a Hamiltonian path is equivalent to the existence of a sequence of transitions $(u_i, S_i, i) \to (u_{i+1}, S_{i+1}, i+1)$ starting from an initial state $(v_{start}, \{v_{start}\}, 1)$ for some $v_{start} \in V$, satisfying the recurrence relation:

$$\text{Exists}(u, S, k) = 
\begin{cases} 
\text{True} & \text{if } k = n \\
\bigvee_{v \in \text{Adj}(u), v \notin S} \text{Exists}(v, S \cup \{v\}, k+1) & \text{if } k < n 
\end{cases}$$

Where $\text{Adj}(u) = \{v \in V \mid (u, v) \in E\}$. The global decision is given by:
$$\Phi(G) = \bigvee_{v \in V} \text{Exists}(v, \{v\}, 1)$$

**Invariant:** At any depth $k$ of the recursion, the set $S$ satisfies $|S| = k$, and the path constructed $P = (p_1, \dots, p_k)$ satisfies $p_i \in S$ and $(p_i, p_{i+1}) \in E$ for all $1 \le i < k$.

## 3. Complexity Analysis

### Time Complexity
The algorithm performs a depth-first search on the state space tree. In the worst case, the graph is a complete graph $K_n$. The number of possible paths of length $n$ is given by the number of permutations of $V$. 

The branching factor at depth $k$ is at most $n-k$. The total number of nodes in the search tree is bounded by:
$$T(n) = \sum_{k=0}^{n-1} \frac{n!}{(n-k)!} = O(n!)$$
Specifically, for each vertex, we explore all permutations of the remaining vertices. Since we must verify the existence of at least one valid permutation, the upper bound is $O(n \cdot n!)$, which simplifies to $O(n!)$ in asymptotic notation.

### Space Complexity
The space complexity is determined by the auxiliary structures required for the recursion:
1. **Recursion Stack:** The depth of the recursion is $n$, requiring $O(n)$ space.
2. **Visited Set:** The boolean array (or bitmask) requires $O(n)$ space.
3. **Adjacency List:** Storing the graph requires $O(V + E)$ space.

Given the algorithm operates on the graph structure, the auxiliary space complexity (excluding the input graph) is $O(n)$. Total space complexity is $O(V + E)$.