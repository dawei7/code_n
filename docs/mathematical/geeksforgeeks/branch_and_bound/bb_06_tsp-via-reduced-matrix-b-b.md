# Formal Mathematical Specification: TSP via Reduced Matrix (Branch and Bound)

## 1. Definitions and Notation

Let $G = (V, E)$ be a complete directed graph where $V = \{0, 1, \dots, n-1\}$ is the set of $n$ cities. Let $C \in (\mathbb{R}_{\ge 0} \cup \{\infty\})^{n \times n}$ be the adjacency matrix, where $c_{ij}$ denotes the cost of the edge $(i, j) \in E$. If no edge exists, $c_{ij} = \infty$.

A **tour** is a Hamiltonian cycle in $G$, represented as a permutation $\sigma$ of $V$ such that the total cost is $L(\sigma) = \sum_{i=0}^{n-1} c_{\sigma(i), \sigma(i+1)}$, with $\sigma(n) = \sigma(0)$. The objective is to find $\sigma^* = \arg \min_{\sigma \in S_n} L(\sigma)$.

- **State Space $\mathcal{S}$**: A node in the search tree is defined by a tuple $(P, M, \text{cost\_so\_far})$, where $P = (v_0, v_1, \dots, v_k)$ is the current path, $M$ is the reduced cost matrix for the remaining subproblem, and $\text{cost\_so\_far}$ is the sum of edge weights in $P$.
- **Reduction Operator $\mathcal{R}(M)$**: A function that transforms $M$ into $M'$ such that $\min_{j} m'_{ij} = 0$ for all $i$ and $\min_{i} m'_{ij} = 0$ for all $j$. The reduction cost $\rho(M)$ is the total value subtracted from $M$ to achieve this state.

## 2. Algebraic Characterization

The algorithm relies on the **Lower Bound Property**. For any matrix $M$, the cost of any Hamiltonian cycle contained within $M$ is bounded below by the sum of the current path cost and the reduction cost of the matrix.

### Matrix Reduction
Given a matrix $M$, the reduction cost $\rho(M)$ is defined as:
$$\rho(M) = \sum_{i=0}^{n-1} \min_{j} m_{ij} + \sum_{j=0}^{n-1} \min_{i} m_{ij}$$
where the minimum is taken over finite elements. The reduced matrix $M'$ is given by:
$$m'_{ij} = m_{ij} - \min_{k} m_{ik} - \min_{k} m_{kj}$$

### Branching and Bound
When transitioning from a state with matrix $M$ to a child state by selecting edge $(i, j)$, we define the new matrix $M_{ij}$ by:
1. Setting row $i$ and column $j$ to $\infty$.
2. Setting $M_{ji} = \infty$ to prevent sub-tours.
3. Applying $\mathcal{R}(M_{ij})$ to obtain $M'_{ij}$ and its associated reduction cost $\rho(M_{ij})$.

The **Lower Bound** $LB$ for a node is defined recursively:
$$LB(\text{child}) = LB(\text{parent}) + c_{ij} + (\rho(M_{ij}) - \rho(M_{\text{parent}}))$$
where $c_{ij}$ is the cost in the parent's reduced matrix. The algorithm maintains the invariant that for any node in the priority queue, $LB$ is a non-decreasing estimate of the optimal tour cost passing through the partial path $P$.

## 3. Complexity Analysis

### Time Complexity
The worst-case time complexity is $O(n! \cdot n^2)$.
- **Branching Factor:** At each level $k$ of the search tree, there are at most $(n-k)$ choices. The total number of nodes in the state-space tree is $\sum_{k=0}^{n} \frac{n!}{k!} = O(n!)$.
- **Work per Node:** At each node, the `reduce` function iterates over the $n \times n$ matrix, performing row and column scans, resulting in $O(n^2)$ operations.
- **Total:** The product of the number of nodes and the work per node yields $O(n! \cdot n^2)$. In practice, the pruning condition $LB \ge \text{best}$ significantly reduces the effective search space, often approaching polynomial time for specific instances.

### Space Complexity
The space complexity is $O(n! \cdot n^2)$ in the absolute worst case, as the priority queue may store a significant fraction of the state-space tree nodes.
- **Auxiliary Space:** Each node stores an $n \times n$ matrix, requiring $O(n^2)$ space.
- **Total Space:** Given the priority queue can contain $O(n!)$ nodes, the total space is $O(n! \cdot n^2)$. However, because the algorithm uses a Best-First Search strategy, the memory footprint is dominated by the width of the search tree at the current depth, which is typically much smaller than $n!$ for well-behaved cost matrices.