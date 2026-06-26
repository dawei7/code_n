# Formal Mathematical Specification: Job Assignment (Branch and Bound)

## 1. Definitions and Notation

Let $N \in \mathbb{Z}^+$ be the number of workers and jobs. We define the set of workers as $\mathcal{W} = \{0, 1, \dots, N-1\}$ and the set of jobs as $\mathcal{J} = \{0, 1, \dots, N-1\}$. The input is a cost matrix $C \in \mathbb{R}^{N \times N}$, where $c_{i,j}$ denotes the cost of assigning worker $i$ to job $j$.

An assignment is a bijection $\sigma: \mathcal{W} \to \mathcal{J}$. The set of all possible assignments is the symmetric group $S_N$, which contains $N!$ permutations. The objective is to find an optimal assignment $\sigma^*$ such that:
$$\sigma^* = \arg \min_{\sigma \in S_N} \sum_{i=0}^{N-1} c_{i, \sigma(i)}$$

The state space $\mathcal{S}$ consists of partial assignments. A state $s$ at depth $k$ (where $0 \le k \le N$) is defined by the tuple $(A_k, U_k)$, where:
- $A_k = \{(i, \sigma(i)) \mid 0 \le i < k\}$ is the set of assignments made for the first $k$ workers.
- $U_k = \mathcal{J} \setminus \{\sigma(0), \dots, \sigma(k-1)\}$ is the set of unassigned jobs.

## 2. Algebraic Characterization

The Branch and Bound algorithm explores the state space tree where each node at depth $k$ branches into $|U_k| = N-k$ children. To prune the search, we define a lower bound function $L(s)$ for a state $s = (A_k, U_k)$.

Let $C_{curr}(s) = \sum_{(i,j) \in A_k} c_{i,j}$ be the accumulated cost of the partial assignment. The lower bound $L(s)$ is defined as:
$$L(s) = C_{curr}(s) + \sum_{i=k}^{N-1} \min_{j \in U_k} c_{i,j}$$

**Theorem (Lower Bound Validity):** For any state $s$ at depth $k$, $L(s) \le \text{cost}(\sigma)$ for any complete assignment $\sigma$ extending the partial assignment $A_k$.
*Proof:* Since $\min_{j \in U_k} c_{i,j}$ is the minimum possible cost for worker $i$ to be assigned to any remaining job $j \in U_k$, the sum $\sum_{i=k}^{N-1} \min_{j \in U_k} c_{i,j}$ provides a lower bound on the cost of any valid completion of the assignment. Because the cost of the partial assignment is fixed, the sum $L(s)$ is a valid lower bound.

**Pruning Criterion:** Let $C_{best}$ be the cost of the best complete assignment found thus far. A branch originating from state $s$ is pruned if:
$$L(s) \ge C_{best}$$

## 3. Complexity Analysis

### Time Complexity
The worst-case time complexity is $O(N!)$. 
In the absence of effective pruning (e.g., when the cost matrix is structured such that $L(s)$ is consistently small), the algorithm performs a depth-first or best-first search of the entire permutation tree. The number of nodes in the state-space tree is given by the sum of partial permutations:
$$\sum_{k=0}^{N} \frac{N!}{(N-k)!} = \lfloor N! \cdot e \rfloor$$
Each node involves calculating the lower bound, which takes $O((N-k)^2)$ time to find the minimums for remaining workers. Thus, the total work is bounded by $O(N \cdot N!)$. In practice, the pruning factor $\alpha$ reduces the effective search space to $O(\alpha^N)$, where $\alpha < N$.

### Space Complexity
The space complexity is determined by the maximum depth of the recursion stack and the storage of the priority queue (in Best-First Search) or the recursion stack (in Depth-First Search).
- **Recursion Stack:** The depth of the tree is $N$, leading to $O(N)$ space for the call stack.
- **Priority Queue:** In the worst case, the number of nodes stored in the frontier can be proportional to the number of leaves, $O(N!)$.
- **Total Space:** $O(N!)$ in the worst case, though typically $O(N)$ for depth-first implementations or $O(2^N)$ for best-first implementations depending on the pruning efficiency.