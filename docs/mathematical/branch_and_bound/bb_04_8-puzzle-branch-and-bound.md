# Formal Mathematical Specification: 8-Puzzle (Branch and Bound)

## 1. Definitions and Notation

Let the 8-puzzle be defined as a state-space graph $G = (\mathcal{S}, \mathcal{A})$, where:

*   **State Space ($\mathcal{S}$):** A set of configurations represented by a bijection $\sigma: \{1, \dots, 9\} \to \{0, 1, \dots, 8\}$, where $0$ denotes the empty tile. The cardinality of the state space is $|\mathcal{S}| = \frac{9!}{2} = 181,440$ (due to parity constraints on permutations).
*   **Actions ($\mathcal{A}$):** A set of transitions $a: \mathcal{S} \to \mathcal{S}$ defined by the movement of the empty tile into an adjacent position $(r, c) \in \{0, 1, 2\}^2$.
*   **Cost Function ($g$):** Let $g(s)$ be the path cost from the initial state $s_0$ to state $s$, defined as the number of edges in the path $P = (s_0, s_1, \dots, s_k = s)$, where $g(s) = k$.
*   **Heuristic Function ($h$):** A function $h: \mathcal{S} \to \mathbb{N}_0$ that estimates the minimum cost to reach the goal state $s_g$. For the Manhattan distance, let $pos(i, s)$ be the coordinate $(r, c)$ of tile $i$ in state $s$. Then:
    $$h(s) = \sum_{i=1}^{8} (|r_{i,s} - r_{i,g}| + |c_{i,s} - c_{i,g}|)$$
*   **Evaluation Function ($f$):** The total estimated cost $f(s) = g(s) + h(s)$.

## 2. Algebraic Characterization

The algorithm operates as a best-first search on the state-space graph. The correctness of the algorithm relies on the properties of the heuristic function $h(s)$.

### Admissibility
A heuristic $h$ is **admissible** if for all $s \in \mathcal{S}$:
$$h(s) \leq h^*(s)$$
where $h^*(s)$ is the true optimal cost from $s$ to $s_g$. Since each move changes the Manhattan distance of exactly one tile by exactly 1, and the goal state has $h(s_g) = 0$, the Manhattan distance is a lower bound on the number of moves required, satisfying the admissibility condition.

### Optimality Condition
The algorithm maintains a priority queue $Q$ of frontier states. Let $C^*$ be the cost of the optimal path. The algorithm terminates when $s_g$ is extracted from $Q$. 
Given $h$ is admissible, for any node $n$ in the frontier, $f(n) = g(n) + h(n) \leq g(n) + h^*(n) = f^*(n)$. 
Because the algorithm always expands the node with the minimum $f(n)$, it is guaranteed that when $s_g$ is selected, $g(s_g) = f(s_g) \leq f(n)$ for all $n$ in the frontier, ensuring $g(s_g) = C^*$.

### State Transitions
The transition from state $s$ to $s'$ via action $a$ is governed by:
$$g(s') = g(s) + 1$$
$$f(s') = g(s) + 1 + h(s')$$

## 3. Complexity Analysis

### Time Complexity
The time complexity is governed by the number of nodes expanded in the search tree. 
*   **Worst Case:** In the absence of an effective heuristic ($h(s) = 0$), the algorithm behaves as Dijkstra's algorithm. The number of nodes expanded is $O(b^d)$, where $b$ is the branching factor (average $b \approx 2.67$ for the 8-puzzle) and $d$ is the depth of the optimal solution.
*   **Average Case:** With an admissible heuristic, the number of expanded nodes is $O(b^{\epsilon d})$, where $\epsilon < 1$ is a factor determined by the heuristic's accuracy. The priority queue operations (insertion and extraction) contribute a logarithmic factor, resulting in $O(b^d \log(b^d))$.

### Space Complexity
The space complexity is dominated by the storage of the "closed set" (visited states) and the "open set" (priority queue).
*   **Total Space:** $O(b^d)$.
In the worst case, the algorithm must store all generated states to prevent cycles and ensure optimality. Since the state space is finite, the space complexity is bounded by $O(|\mathcal{S}|)$, but in practice, it is limited by the number of nodes generated before the goal is reached, which is $O(b^d)$.