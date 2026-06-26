# Formal Mathematical Specification: Travelling Salesperson (Held-Karp DP)

## 1. Definitions and Notation

Let $G = (V, E)$ be a complete undirected graph where $V = \{0, 1, \dots, n-1\}$ is the set of vertices, and $n = |V|$. Let $w: V \times V \to \mathbb{R}^+$ be a weight function represented by an adjacency matrix $W$, where $w_{ij}$ denotes the cost of the edge $(i, j)$.

A Hamiltonian cycle is a permutation $\sigma$ of $V$ such that the total cost is $\sum_{i=0}^{n-1} w_{\sigma(i), \sigma(i+1 \pmod n)}$. The objective is to find:
$$\min_{\sigma \in S_n} \sum_{i=0}^{n-1} w_{\sigma(i), \sigma(i+1 \pmod n)}$$

We define the state space $\mathcal{S}$ using a power set representation. Let $S \subseteq V$ be a subset of vertices, represented by a bitmask $m \in \{0, 1, \dots, 2^n - 1\}$, where the $i$-th bit is set if $i \in S$.
The DP state is defined as:
$C(S, i)$: The minimum cost of a path that visits exactly the set of vertices $S \subseteq V$, starting at vertex $0$ and ending at vertex $i \in S$, where $0 \in S$.

## 2. Algebraic Characterization

The Held-Karp algorithm relies on the principle of optimality, decomposing the problem into subproblems of increasing subset size.

### Base Case
For a path starting at vertex $0$ and ending at $0$ with only vertex $0$ visited:
$$C(\{0\}, 0) = 0$$
For all $i \in V \setminus \{0\}$:
$$C(\{0, i\}, i) = w_{0, i}$$

### Recurrence Relation
For any subset $S \subseteq V$ such that $|S| > 2$ and $0 \in S$, and for any $i \in S \setminus \{0\}$:
$$C(S, i) = \min_{j \in S \setminus \{i\}, j \neq 0} \{ C(S \setminus \{i\}, j) + w_{j, i} \}$$

### Optimal Solution
The optimal cost of the Travelling Salesperson tour is the minimum cost to visit all vertices and return to the origin:
$$\text{TSP}_{opt} = \min_{i \in V \setminus \{0\}} \{ C(V, i) + w_{i, 0} \}$$

## 3. Complexity Analysis

### Time Complexity
The algorithm iterates through all possible subsets $S \subseteq V$ and all possible ending vertices $i \in S$.
1. **State Space Size:** There are $2^n$ possible subsets $S$. For each subset, there are $n$ possible ending vertices $i$. Thus, the number of states is $O(n \cdot 2^n)$.
2. **Transition Cost:** For each state $(S, i)$, the recurrence relation requires iterating over all possible previous vertices $j \in S \setminus \{i\}$. This takes $O(n)$ time.

The total time complexity $T(n)$ is given by the summation over the number of states multiplied by the transition work:
$$T(n) = \sum_{k=2}^{n} \binom{n}{k} \cdot k \cdot (k-1) \approx O(n^2 \cdot 2^n)$$
Formally, since there are $2^n$ subsets and for each subset we perform $O(n^2)$ operations (or $O(n)$ per state), the complexity is $O(n^2 2^n)$.

### Space Complexity
The algorithm requires a memoization table (or DP table) to store the results of $C(S, i)$.
1. **Table Dimensions:** The table requires $2^n$ rows (for each mask) and $n$ columns (for each ending vertex).
2. **Memory Requirement:** Each entry stores a scalar cost value.
$$S(n) = \Theta(n \cdot 2^n)$$
This space complexity is necessary to store the optimal substructure results, ensuring that each subproblem is computed exactly once, thereby avoiding the $O(n!)$ complexity of exhaustive search.