# Formal Mathematical Specification: Floyd-Warshall (Dynamic Programming Formulation)

## 1. Definitions and Notation

Let $G = (V, E)$ be a directed, weighted graph where $V = \{0, 1, \dots, n-1\}$ is the set of $n$ vertices. Let $w: E \to \mathbb{R}$ be a weight function assigning a real value to each edge. We define the adjacency matrix $W \in (\mathbb{R} \cup \{\infty\})^{n \times n}$ such that:

$$
W_{ij} = 
\begin{cases} 
0 & \text{if } i = j \\
w(i, j) & \text{if } (i, j) \in E \\
\infty & \text{if } i \neq j \text{ and } (i, j) \notin E 
\end{cases}
$$

We define the state space $\mathcal{S}$ as a sequence of matrices $D^{(k)} \in (\mathbb{R} \cup \{\infty\})^{n \times n}$ for $k \in \{-1, 0, \dots, n-1\}$. Each entry $D^{(k)}_{ij}$ represents the weight of the shortest path from vertex $i$ to vertex $j$ using only intermediate vertices from the set $V_k = \{0, 1, \dots, k\}$.

## 2. Algebraic Characterization

The algorithm is governed by the principle of optimality. We define the recurrence relation for the shortest path distance $D^{(k)}_{ij}$ as follows:

**Base Case ($k = -1$):**
The shortest path using no intermediate vertices is simply the direct edge weight:
$$D^{(-1)}_{ij} = W_{ij}$$

**Recursive Step ($k \geq 0$):**
For any $k \in \{0, \dots, n-1\}$, the shortest path from $i$ to $j$ using intermediate vertices in $V_k$ is the minimum of the shortest path not using vertex $k$ and the shortest path that passes through vertex $k$:
$$D^{(k)}_{ij} = \min\left( D^{(k-1)}_{ij}, D^{(k-1)}_{ik} + D^{(k-1)}_{kj} \right)$$

**Correctness Invariant:**
The algorithm maintains the invariant that after the $k$-th iteration, $D^{(k)}_{ij}$ contains the weight of the shortest path from $i$ to $j$ using only vertices in $\{0, \dots, k\}$ as intermediate nodes. By induction, for $k = n-1$, $D^{(n-1)}_{ij}$ represents the shortest path between all pairs $(i, j)$ in $G$, provided no negative-weight cycles exist. If a negative-weight cycle exists, the algorithm will yield $D^{(n-1)}_{ii} < 0$ for some $i$.

**Space Optimization:**
Since $D^{(k)}_{ij}$ depends only on values from $D^{(k-1)}$, we can perform the update in-place. Let $D$ be the matrix $D^{(k-1)}$. The update $D_{ij} \leftarrow \min(D_{ij}, D_{ik} + D_{kj})$ is valid because:
1. $D_{ik}$ and $D_{kj}$ remain unchanged during the $k$-th iteration (as $D_{ik} = D^{(k-1)}_{ik} = D^{(k)}_{ik}$ and $D_{kj} = D^{(k-1)}_{kj} = D^{(k)}_{kj}$).
2. The values $D_{ik}$ and $D_{kj}$ represent paths that do not use $k$ as an intermediate vertex, satisfying the requirement for the recurrence.

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of three nested loops, each iterating over the set of vertices $V$. The total number of operations is determined by the triple summation:
$$T(n) = \sum_{k=0}^{n-1} \sum_{i=0}^{n-1} \sum_{j=0}^{n-1} \Theta(1)$$
Evaluating this summation:
$$T(n) = \sum_{k=0}^{n-1} \sum_{i=0}^{n-1} n = \sum_{k=0}^{n-1} n^2 = n^3$$
Thus, the time complexity is $O(V^3)$.

### Space Complexity
The algorithm maintains two primary $n \times n$ matrices: the distance matrix $D$ and the predecessor matrix $nxt$. 
- The distance matrix $D$ requires $O(V^2)$ space.
- The predecessor matrix $nxt$ requires $O(V^2)$ space.
- Auxiliary variables (loop indices, temporary scalars) require $O(1)$ space.

The total space complexity is $O(V^2 + V^2) = O(V^2)$. The in-place optimization ensures that we do not require the $O(V^3)$ space that would be necessitated by storing the full 3D tensor $D^{(k)}_{ij}$.