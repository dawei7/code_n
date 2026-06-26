# Formal Mathematical Specification: 0-1 Knapsack (Least Cost Branch & Bound)

## 1. Definitions and Notation

Let the 0-1 Knapsack problem be defined by a set of $n$ items, $I = \{1, 2, \dots, n\}$. Each item $i \in I$ is characterized by a weight $w_i \in \mathbb{R}^+$ and a value $v_i \in \mathbb{R}^+$. Given a total capacity $W \in \mathbb{R}^+$, we seek to find a binary vector $\mathbf{x} = (x_1, x_2, \dots, x_n) \in \{0, 1\}^n$ that maximizes the objective function:
$$f(\mathbf{x}) = \sum_{i=1}^n v_i x_i$$
subject to the constraint:
$$\sum_{i=1}^n w_i x_i \le W$$

**State Space:** The algorithm explores a binary tree $\mathcal{T}$ of depth $n$. A node $u$ at depth $k$ represents a partial solution $\mathbf{x}^{(k)} = (x_1, \dots, x_k, ?, \dots, ?)$. 
- Let $V_u = \sum_{i=1}^k v_i x_i$ be the accumulated value at node $u$.
- Let $W_u = \sum_{i=1}^k w_i x_i$ be the accumulated weight at node $u$.

**Bounding Functions:** We define two functions to prune the search space:
1. **Upper Bound ($UB$):** Let $UB(u)$ be the maximum possible value obtainable from node $u$ by allowing fractional selection of remaining items (the Fractional Knapsack relaxation). If $W_u > W$, $UB(u) = -\infty$.
2. **Lower Bound ($LB$):** Let $LB(u)$ be the value of a feasible solution found by a greedy approach from node $u$.

## 2. Algebraic Characterization

The algorithm utilizes a Priority Queue $\mathcal{Q}$ to store live nodes, ordered by their $UB$ values. The state transition is defined by the branching rule:
For a node $u$ at level $k$, we generate two children:
- **Left child (Include):** $x_{k+1} = 1$, valid if $W_u + w_{k+1} \le W$.
- **Right child (Exclude):** $x_{k+1} = 0$.

**Optimality Condition:**
Let $f^*$ be the global maximum value found so far (the current best $LB$). The algorithm maintains the invariant that for any node $u \in \mathcal{Q}$, if $UB(u) \le f^*$, then the subtree rooted at $u$ cannot contain an optimal solution. 

**Termination Criterion:**
The algorithm terminates when $\mathcal{Q} = \emptyset$ or when $\max_{u \in \mathcal{Q}} \{UB(u)\} \le f^*$. Because $UB(u)$ is an admissible heuristic (it provides an upper bound on the optimal value of the subtree), the condition $UB(u) \le f^*$ guarantees that no node in the queue can yield a value greater than the current best, ensuring global optimality.

## 3. Complexity Analysis

### Time Complexity
The worst-case time complexity is $O(2^n)$. 
- **Derivation:** In the worst case, the bounding function $UB(u)$ fails to prune any branches (e.g., when all items have identical value-to-weight ratios or the capacity is sufficiently large). The algorithm then performs a full traversal of the binary tree $\mathcal{T}$, which contains $2^{n+1}-1$ nodes.
- **Work per node:** At each node, we compute $UB$ and $LB$, which requires $O(n)$ time. However, with precomputed suffix sums, this can be reduced to $O(1)$ after an initial $O(n \log n)$ sorting phase.
- **Total:** $T(n) = O(n \log n) + \sum_{i=0}^n 2^i \cdot O(1) = O(2^n)$.

### Space Complexity
The space complexity is $O(2^n)$ in the worst case, though typically much lower.
- **Auxiliary Space:** The Priority Queue $\mathcal{Q}$ stores the frontier of the search tree. In the worst case, the number of nodes in the queue is proportional to the number of leaves, $O(2^n)$.
- **Total Space:** $S(n) = O(2^n)$. 
- **Note:** While the theoretical worst-case is exponential, the "Least Cost" heuristic significantly prunes the search tree in practice, often resulting in a space complexity closer to $O(n \cdot d)$, where $d$ is the effective depth of the search before pruning occurs.