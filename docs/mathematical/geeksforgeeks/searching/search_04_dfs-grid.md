# Formal Mathematical Specification: Depth-First Search (DFS) on a Grid

## 1. Definitions and Notation

Let the grid be represented by a matrix $G \in \{0, 1\}^{R \times C}$, where $R$ is the number of rows and $C$ is the number of columns. The set of all cells is defined as $\mathcal{V} = \{ (r, c) \mid 0 \le r < R, 0 \le c < C \}$.

We define a connectivity relation $\sim$ on $\mathcal{V}$ such that two cells $u = (r_1, c_1)$ and $v = (r_2, c_2)$ are adjacent if and only if $|r_1 - r_2| + |c_1 - c_2| = 1$. An island is defined as a connected component of the subgraph induced by the set of land cells $\mathcal{L} = \{ v \in \mathcal{V} \mid G_v = 1 \}$.

Let $\mathcal{I} = \{I_1, I_2, \dots, I_k\}$ be the partition of $\mathcal{L}$ into disjoint connected components. The objective is to compute the cardinality of the set of components, $k = |\mathcal{I}|$.

The state of the algorithm at any time $t$ is defined by the tuple $(G_t, \mathcal{V}_{visited})$, where $G_t$ is the modified grid and $\mathcal{V}_{visited} \subseteq \mathcal{V}$ is the set of cells already processed.

## 2. Algebraic Characterization

The algorithm relies on the property that the number of connected components $k$ in an undirected graph can be determined by the number of times a traversal (DFS) is initiated from an unvisited node.

Let $f: \mathcal{V} \to \{0, 1\}$ be the indicator function for land cells. We define the recursive DFS operator $\Phi$ acting on a cell $u \in \mathcal{L}$:
$$\Phi(u) = \{u\} \cup \bigcup_{v \in Adj(u), G_v=1} \Phi(v)$$
where $Adj(u) = \{v \in \mathcal{V} \mid \|u - v\|_1 = 1\}$. 

To ensure termination and avoid cycles, the algorithm enforces a state transition $G_{t+1} = G_t \setminus \{u\}$ (setting $G_u = 0$) upon visiting $u$. The total number of islands $k$ is given by the summation:
$$k = \sum_{r=0}^{R-1} \sum_{c=0}^{C-1} \mathbb{I}(G_{(r,c)}^{(initial)} = 1 \land \text{is\_start}(r, c))$$
where $\mathbb{I}$ is the indicator function and $\text{is\_start}(r, c)$ is true if the cell $(r, c)$ is reached by the main loop before being reached by any recursive call $\Phi$.

The invariant maintained throughout the execution is:
$$\text{Count} + \text{Components}(\mathcal{L} \setminus \mathcal{V}_{visited}) = k$$
where $\text{Count}$ is the number of islands identified thus far.

## 3. Complexity Analysis

### Time Complexity
The time complexity is derived from the total number of operations performed on the grid. 
1. The main loop iterates over every cell $(r, c) \in \mathcal{V}$, resulting in $R \times C$ iterations.
2. The DFS traversal $\Phi$ is invoked only when $G_{(r,c)} = 1$. 
3. Each cell $v \in \mathcal{L}$ is visited exactly once by the DFS, as it is set to $0$ immediately upon visitation. 
4. For each visited cell, we inspect its 4 neighbors.

The total work $W$ is:
$$W = \sum_{v \in \mathcal{V}} (\text{constant work}) + \sum_{v \in \mathcal{L}} (\text{degree}(v) \times \text{constant work})$$
Since $\sum_{v \in \mathcal{L}} \text{degree}(v) \le 4|\mathcal{L}| \le 4(R \times C)$, the total time complexity is:
$$T(R, C) = O(R \times C)$$

### Space Complexity
The space complexity is dominated by the recursion stack (or the explicit stack in the iterative implementation).
1. **Auxiliary Space:** In the worst-case scenario, the grid is a single connected component (e.g., a snake-like path covering all $R \times C$ cells). The depth of the recursion tree is $O(R \times C)$.
2. **Total Space:** Since we modify the grid in-place, the grid storage is $O(R \times C)$. The auxiliary stack space is $O(R \times C)$.

Thus, the total space complexity is:
$$S(R, C) = O(R \times C)$$
In the best case, where the grid contains no land, the space complexity is $O(1)$ beyond the input storage.