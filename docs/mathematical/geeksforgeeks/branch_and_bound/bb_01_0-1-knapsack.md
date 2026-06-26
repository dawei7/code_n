# Formal Mathematical Specification: 0-1 Knapsack (Branch and Bound)

## 1. Definitions and Notation

Let $I = \{1, 2, \dots, n\}$ be a set of $n$ items. Each item $i \in I$ is characterized by a pair $(v_i, w_i) \in \mathbb{R}^+ \times \mathbb{R}^+$, representing its value and weight, respectively. Let $W \in \mathbb{R}^+$ denote the total capacity of the knapsack.

We define the decision vector $\mathbf{x} = (x_1, x_2, \dots, x_n) \in \{0, 1\}^n$, where $x_i = 1$ if item $i$ is included in the knapsack, and $x_i = 0$ otherwise. The 0-1 Knapsack problem is defined as the following Integer Linear Program (ILP):

$$\text{Maximize } Z = \sum_{i=1}^n v_i x_i$$
$$\text{subject to } \sum_{i=1}^n w_i x_i \leq W, \quad x_i \in \{0, 1\}$$

The state space $\mathcal{S}$ is represented as a binary tree of depth $n$. A node $u \in \mathcal{S}$ at level $k$ is defined by the tuple $(k, \text{profit}_u, \text{weight}_u)$, where:
- $\text{profit}_u = \sum_{i=1}^k v_i x_i$
- $\text{weight}_u = \sum_{i=1}^k w_i x_i$

## 2. Algebraic Characterization

To prune the search space, we define an upper bound function $U(u)$ for any node $u$. We relax the integrality constraint $x_i \in \{0, 1\}$ to $x_i \in [0, 1]$ for the remaining items $i > k$.

### The Fractional Relaxation
Let the items be sorted such that $\frac{v_1}{w_1} \geq \frac{v_2}{w_2} \geq \dots \geq \frac{v_n}{w_n}$. For a node $u$ at level $k$, the upper bound $U(u)$ is calculated by filling the remaining capacity $W - \text{weight}_u$ greedily:

1. Let $j$ be the first index such that $j > k$ and $\sum_{i=k+1}^j w_i > W - \text{weight}_u$.
2. The bound is:
   $$U(u) = \text{profit}_u + \sum_{i=k+1}^{j-1} v_i + \left( \frac{W - \text{weight}_u - \sum_{i=k+1}^{j-1} w_i}{w_j} \right) v_j$$

### Pruning Condition
Let $Z^*$ be the global maximum value found thus far (the incumbent). A node $u$ is pruned if and only if:
$$U(u) \leq Z^*$$
This is valid because $U(u)$ represents the optimal solution to the Linear Programming (LP) relaxation of the subproblem at node $u$. Since the feasible region of the ILP is a subset of the feasible region of the LP relaxation, $U(u)$ provides a rigorous upper bound on the objective value obtainable from any descendant of $u$.

## 3. Complexity Analysis

### Time Complexity
The worst-case time complexity is $O(2^n)$. 
- **Derivation:** In the worst case, the pruning condition $U(u) \leq Z^*$ is never satisfied until the leaf nodes are reached. The algorithm then performs an exhaustive search of the binary tree of height $n$. The number of nodes in a complete binary tree of height $n$ is $\sum_{i=0}^n 2^i = 2^{n+1} - 1$.
- **Average Case:** By sorting items by density $\rho_i = v_i/w_i$, the algorithm finds a high-value incumbent $Z^*$ early. The number of nodes visited is reduced to $O(2^n \cdot \alpha)$, where $\alpha \ll 1$ is the pruning factor determined by the tightness of the fractional bound.

### Space Complexity
The space complexity is $O(2^n)$ in the worst case.
- **Derivation:** The algorithm utilizes a queue (or stack) to store the frontier of the search tree. In a Breadth-First Search (BFS) implementation, the maximum number of nodes stored in the queue at any time occurs at the deepest level of the tree, which is $O(2^n)$. 
- **Auxiliary Space:** The sorting step requires $O(n)$ space, and the recursion stack (if implemented via Depth-First Search) requires $O(n)$ space. However, the total space is dominated by the storage of the frontier nodes in the state space tree.