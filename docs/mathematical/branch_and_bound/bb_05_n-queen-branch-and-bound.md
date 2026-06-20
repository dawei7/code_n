# Formal Mathematical Specification: N-Queen (Branch and Bound)

## 1. Definitions and Notation

Let $N \in \mathbb{Z}^+$ be the dimension of a square chessboard represented by the set of coordinates $\mathcal{C} = \{ (r, c) \mid 0 \le r, c < N \}$. A configuration of $N$ queens is a set of positions $\mathcal{Q} = \{ (r_0, c_0), (r_1, c_1), \dots, (r_{N-1}, c_{N-1}) \}$.

The N-Queens problem requires finding the set of all valid configurations $\mathcal{S} \subseteq \mathcal{P}(\mathcal{C})$ such that for any two distinct queens $(r_i, c_i), (r_j, c_j) \in \mathcal{Q}$:
1. **Row constraint:** $r_i \neq r_j$
2. **Column constraint:** $c_i \neq c_j$
3. **Primary diagonal constraint:** $(r_i - c_i) \neq (r_j - c_j)$
4. **Secondary diagonal constraint:** $(r_i + c_i) \neq (r_j + c_j)$

To optimize the search, we define the state space $\mathcal{S}$ using the following indicator vectors (the "Bound" arrays):
- $\mathcal{R} \in \{0, 1\}^N$, where $\mathcal{R}_r = 1$ if row $r$ is occupied.
- $\mathcal{D}_1 \in \{0, 1\}^{2N-1}$, where $\mathcal{D}_{1, k} = 1$ if the primary diagonal $r - c + (N-1) = k$ is occupied.
- $\mathcal{D}_2 \in \{0, 1\}^{2N-1}$, where $\mathcal{D}_{2, k} = 1$ if the secondary diagonal $r + c = k$ is occupied.

## 2. Algebraic Characterization

The algorithm employs a depth-first search (DFS) over the column index $j \in \{0, \dots, N-1\}$. Let $f(j)$ be the partial configuration of queens placed in columns $0$ through $j-1$. 

For a candidate position $(r, j)$, the validity predicate $\Psi(r, j)$ is defined as:
$$\Psi(r, j) \iff (\mathcal{R}_r = 0) \land (\mathcal{D}_{1, r-j+N-1} = 0) \land (\mathcal{D}_{2, r+j} = 0)$$

The state transition at column $j$ is defined by the mapping:
$$\text{Update}(\mathcal{R}, \mathcal{D}_1, \mathcal{D}_2, r, j) \to (\mathcal{R}', \mathcal{D}_1', \mathcal{D}_2')$$
where:
$$\mathcal{R}'_i = \mathcal{R}_i \lor [i=r]$$
$$\mathcal{D}'_{1, k} = \mathcal{D}_{1, k} \lor [k = r-j+N-1]$$
$$\mathcal{D}'_{2, k} = \mathcal{D}_{2, k} \lor [k = r+j]$$

The algorithm terminates when $j=N$, representing a successful placement of $N$ queens. The backtracking mechanism ensures that for every state $(j, \mathcal{R}, \mathcal{D}_1, \mathcal{D}_2)$, we explore the set of valid rows $r \in \{0, \dots, N-1\}$ such that $\Psi(r, j)$ holds.

## 3. Complexity Analysis

### Time Complexity
The search space is represented by a tree of depth $N$. At each level $j$, we iterate over $N$ possible rows. The branching factor decreases as we descend the tree due to the constraints. 

The total number of nodes visited in the worst case is bounded by the permutation space of $N$ queens, which is $N!$. In the naive backtracking approach, the `is_safe` check requires $O(N)$ time to scan the board. In this Branch and Bound formulation, the validity predicate $\Psi(r, j)$ is evaluated in $O(1)$ time via direct array indexing. 

Thus, the total time complexity is:
$$T(N) = \sum_{k=0}^{N-1} \frac{N!}{(N-k)!} \cdot O(1) = O(N!)$$
While the asymptotic complexity remains $O(N!)$, the constant factor reduction from $O(N)$ to $O(1)$ per node visit yields a significant practical performance improvement.

### Space Complexity
The space complexity is determined by the auxiliary storage required for the constraint arrays and the recursion stack:
1. **Constraint Arrays:** $\mathcal{R}$ requires $O(N)$, while $\mathcal{D}_1$ and $\mathcal{D}_2$ require $O(2N-1)$ each. Total: $O(N)$.
2. **Recursion Stack:** The depth of the DFS tree is $N$, requiring $O(N)$ stack space.

Summing these components, the total auxiliary space complexity is:
$$S(N) = O(N) + O(N) = O(N)$$