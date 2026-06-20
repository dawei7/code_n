# Formal Mathematical Specification: Floyd-Warshall (All-Pairs Shortest Path)

## 1. Definitions and Notation

Let $G = (V, E)$ be a directed, weighted graph where $V = \{v_1, v_2, \dots, v_n\}$ is the set of $n$ vertices and $E \subseteq V \times V$ is the set of edges. We define a weight function $w: E \to \mathbb{R}$, which assigns a real-valued weight to each edge.

We represent the graph using an adjacency matrix $W \in (\mathbb{R} \cup \{\infty\})^{n \times n}$, where:
$$W_{ij} = \begin{cases} 0 & \text{if } i = j \\ w(v_i, v_j) & \text{if } (v_i, v_j) \in E \\ \infty & \text{if } (v_i, v_j) \notin E \text{ and } i \neq j \end{cases}$$

The objective is to compute the distance matrix $D^{(n)} \in (\mathbb{R} \cup \{\infty\})^{n \times n}$, where $D^{(n)}_{ij}$ denotes the weight of the shortest path from vertex $v_i$ to $v_j$. A path $p = \langle v_{i_0}, v_{i_1}, \dots, v_{i_k} \rangle$ has weight $w(p) = \sum_{m=1}^k w(v_{i_{m-1}}, v_{i_m})$.

## 2. Algebraic Characterization

The Floyd-Warshall algorithm is a dynamic programming approach that constructs the shortest path matrix by incrementally allowing a larger set of vertices to serve as intermediate nodes.

Let $D^{(k)}_{ij}$ be the weight of the shortest path from $v_i$ to $v_j$ such that all intermediate vertices in the path are chosen from the set $\{v_1, v_2, \dots, v_k\}$.

**Base Case:**
For $k=0$, no intermediate vertices are allowed. Thus, $D^{(0)}_{ij} = W_{ij}$.

**Recurrence Relation:**
For $k \in \{1, \dots, n\}$, the shortest path from $v_i$ to $v_j$ using only intermediate vertices in $\{v_1, \dots, v_k\}$ is either:
1. The shortest path using only vertices in $\{v_1, \dots, v_{k-1}\}$ (i.e., $D^{(k-1)}_{ij}$).
2. A path that passes through vertex $v_k$, composed of the shortest path from $v_i$ to $v_k$ and the shortest path from $v_k$ to $v_j$, both using only intermediate vertices in $\{v_1, \dots, v_{k-1}\}$.

Formally:
$$D^{(k)}_{ij} = \min(D^{(k-1)}_{ij}, D^{(k-1)}_{ik} + D^{(k-1)}_{kj})$$

**Correctness Invariant:**
After $n$ iterations, $D^{(n)}_{ij}$ represents the shortest path between $v_i$ and $v_j$ using any subset of $V$ as intermediate vertices. If $D^{(n)}_{ii} < 0$ for any $i$, the graph contains a negative cycle reachable from $v_i$.

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of three nested loops, each iterating over the set of vertices $V$. The structure is as follows:
$$T(n) = \sum_{k=1}^{n} \sum_{i=1}^{n} \sum_{j=1}^{n} \Theta(1)$$
Since each iteration of the innermost loop performs a constant number of operations (a comparison and an addition), the total number of operations is:
$$T(n) = \sum_{k=1}^{n} n^2 = n \cdot n^2 = n^3$$
Thus, the time complexity is $\Theta(n^3)$.

### Space Complexity
The algorithm maintains a distance matrix $D \in \mathbb{R}^{n \times n}$. While the recurrence is defined over $k$ stages ($D^{(0)}, \dots, D^{(n)}$), the state can be updated in-place because $D^{(k)}_{ik} = D^{(k-1)}_{ik}$ and $D^{(k)}_{kj} = D^{(k-1)}_{kj}$. Therefore, we only require $O(n^2)$ space to store the current distance matrix. If path reconstruction is required, an additional predecessor matrix $P \in V^{n \times n}$ is maintained, which also occupies $O(n^2)$ space. The total space complexity is $\Theta(n^2)$.