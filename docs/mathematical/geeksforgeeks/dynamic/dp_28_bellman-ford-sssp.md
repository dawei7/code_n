# Formal Mathematical Specification: Bellman-Ford (Dynamic Programming Formulation)

## 1. Definitions and Notation

Let $G = (V, E)$ be a directed graph, where $V = \{v_1, v_2, \dots, v_n\}$ is the set of vertices such that $|V| = n$, and $E \subseteq V \times V$ is the set of directed edges. We define a weight function $w: E \to \mathbb{R}$, which assigns a real-valued weight to each edge $(u, v) \in E$.

We define a source vertex $s \in V$. The objective is to compute the shortest path distance $\delta(s, u)$ for all $u \in V$. 

We define the DP state space as follows:
Let $dp(k, u)$ denote the weight of the shortest path from $s$ to $u$ using at most $k$ edges, where $k \in \{0, 1, \dots, n-1\}$ and $u \in V$. 

The domain of the distance function is defined as:
$$dp: \{0, \dots, n-1\} \times V \to \mathbb{R} \cup \{\infty\}$$

## 2. Algebraic Characterization

The Bellman-Ford algorithm is governed by the principle of optimality. The shortest path to $u$ using at most $k$ edges is either the shortest path to $u$ using at most $k-1$ edges, or it is formed by extending a shortest path to some predecessor $v$ using $k-1$ edges by the edge $(v, u)$.

### Recurrence Relation
The base case for $k=0$ is:
$$dp(0, u) = \begin{cases} 0 & \text{if } u = s \\ \infty & \text{if } u \neq s \end{cases}$$

For $k \in \{1, \dots, n-1\}$, the recurrence is:
$$dp(k, u) = \min \left( dp(k-1, u), \min_{(v, u) \in E} \{ dp(k-1, v) + w(v, u) \} \right)$$

### Correctness and Convergence
A simple path in a graph with $n$ vertices contains at most $n-1$ edges. By induction on $k$, $dp(k, u)$ converges to the true shortest path distance $\delta(s, u)$ for all $u$ reachable from $s$ within $n-1$ edges. If the graph contains no negative weight cycles, then $\delta(s, u) = dp(n-1, u)$.

### Space-Optimized State
By observing that the state $dp(k, \cdot)$ depends only on $dp(k-1, \cdot)$, we can define a 1D state $dist[u]$ that represents the current best-known distance. The transition becomes an iterative relaxation:
$$dist[u] \leftarrow \min(dist[u], dist[v] + w(v, u)) \quad \forall (v, u) \in E$$
This update is performed $n-1$ times.

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of two nested loops:
1. An outer loop iterating $k$ from $1$ to $n-1$.
2. An inner loop iterating over all edges $(u, v) \in E$.

The total number of operations $T(n, |E|)$ is given by the summation:
$$T(n, |E|) = \sum_{k=1}^{n-1} \sum_{(u, v) \in E} \Theta(1)$$
Since the inner summation is performed $|E|$ times for each of the $n-1$ iterations:
$$T(n, |E|) = (n-1) \cdot |E| = \Theta(n \cdot |E|)$$
Thus, the time complexity is $O(V \cdot E)$.

### Space Complexity
The algorithm maintains a distance array $dist$ of size $|V|$. 
- **Auxiliary Space:** The space required for the distance array is $O(V)$.
- **Total Space:** Since the graph is stored as an edge list of size $|E|$ and the distance array is $O(V)$, the total space complexity is $O(V + E)$. 
- In the context of the DP formulation specifically, the space-optimized version requires $O(V)$ auxiliary space to store the current shortest path estimates.