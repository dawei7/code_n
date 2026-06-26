# Formal Mathematical Specification: M-Coloring Problem

## 1. Definitions and Notation

Let $G = (V, E)$ be an undirected graph, where $V = \{0, 1, \dots, n-1\}$ is the set of vertices and $E \subseteq \{\{u, v\} : u, v \in V, u \neq v\}$ is the set of edges. Let $M \in \mathbb{Z}^+$ be the number of available colors.

*   **Coloring Function:** A mapping $f: V \to \{1, 2, \dots, M\}$.
*   **Valid Coloring:** A coloring function $f$ is valid if and only if for every edge $\{u, v\} \in E$, $f(u) \neq f(v)$.
*   **State Space:** The state space $\mathcal{S}$ is the set of all partial mappings $f_k: \{0, \dots, k-1\} \to \{1, \dots, M\}$ for $0 \leq k \leq n$.
*   **Goal:** Determine if there exists a total mapping $f_n: V \to \{1, \dots, M\}$ such that $f_n$ is a valid coloring.

## 2. Algebraic Characterization

The problem is defined as a search for a valid assignment in the configuration space $\mathcal{C} = \{1, \dots, M\}^n$. The validity of a partial assignment $f_k$ is governed by the constraint predicate $P(f_k)$:

$$P(f_k) = \bigwedge_{\{u, v\} \in E, u, v < k} [f_k(u) \neq f_k(v)]$$

The algorithm employs a backtracking search defined by the recursive function $H(k, f_k)$, which returns true if there exists an extension of the partial coloring $f_k$ to a valid total coloring $f_n$. The transition is defined as:

$$H(k, f_k) = \begin{cases} 
\text{True} & \text{if } k = n \\
\bigvee_{c=1}^M \left( \text{is\_safe}(k, c, f_k) \land H(k+1, f_k \cup \{k \mapsto c\}) \right) & \text{if } k < n 
\end{cases}$$

where the predicate $\text{is\_safe}(k, c, f_k)$ is defined as:
$$\text{is\_safe}(k, c, f_k) = \forall u \in \text{Adj}(k) \text{ s.t. } u < k : f_k(u) \neq c$$

The algorithm terminates successfully if $H(0, \emptyset) = \text{True}$.

## 3. Complexity Analysis

### Time Complexity
The algorithm explores a state-space tree of depth $n$. At each level $k$ of the recursion, the algorithm iterates through $M$ possible color assignments. 

1.  **Branching Factor:** The branching factor of the search tree is at most $M$.
2.  **Tree Depth:** The depth of the recursion is $n = |V|$.
3.  **Work per Node:** At each node in the recursion tree, the `is_safe` function iterates over the adjacency list of the current vertex. In the worst case, this takes $O(\text{deg}(v)) = O(n)$ time.

The total number of nodes in the search tree is bounded by $\sum_{i=0}^{n} M^i = \frac{M^{n+1}-1}{M-1} = O(M^n)$. 
Including the cost of the safety check at each node, the total time complexity $T(n)$ is:
$$T(n) = O\left( \sum_{i=0}^{n-1} M^i \cdot n \right) = O(n \cdot M^n)$$
Thus, the time complexity is $O(V \cdot M^V)$.

### Space Complexity
The space complexity is determined by two factors:
1.  **Recursion Stack:** The depth of the recursion is $n$, requiring $O(n)$ space on the call stack.
2.  **Color Array:** The `color` array stores the current assignment for each vertex, requiring $O(n)$ space.
3.  **Adjacency List:** The graph representation requires $O(V + E)$ space.

Excluding the input storage, the auxiliary space complexity is $O(V)$. Including the input, the total space complexity is $O(V + E)$.