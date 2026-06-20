# Formal Mathematical Specification: Knight's Tour

## 1. Definitions and Notation

To formalize the Knight's Tour problem, we model the chessboard and the legal moves of a knight using graph theory and set-theoretic formulations.

### 1.1 The Board and Coordinate Space
Let $N \in \mathbb{N}$ denote the dimension of the square chessboard. We define the coordinate space (or vertex set) $V_N$ as the Cartesian product of the coordinate intervals:
$$V_N = \{0, 1, \dots, N-1\} \times \{0, 1, \dots, N-1\}$$
The cardinality of the vertex set is $|V_N| = N^2$. An individual cell on the board is represented as a tuple $u = (r, c) \in V_N$, where $r$ denotes the row index and $c$ denotes the column index.

### 1.2 The Knight's Move Relation
The set of legal moves for a knight is defined by an algebraic relation $R \subset V_N \times V_N$. Two cells $u = (r_1, c_1)$ and $v = (r_2, c_2)$ are in relation $R$ if and only if their coordinate differences correspond to an "L-shape" jump:
$$(u, v) \in R \iff \left( |r_1 - r_2| = 1 \land |c_1 - c_2| = 2 \right) \lor \left( |r_1 - r_2| = 2 \land |c_1 - c_2| = 1 \right)$$
Since $R$ is symmetric, we can define the Knight's Graph as an undirected, unweighted graph $\mathcal{G}_N = (V_N, E_N)$, where the edge set $E_N$ is given by:
$$E_N = \left\{ \{u, v\} \subseteq V_N \mid (u, v) \in R \right\}$$

### 1.3 The Neighborhood and Degree Functions
For any vertex $v \in V_N$, the open neighborhood $N(v)$ is the set of vertices adjacent to $v$ in $\mathcal{G}_N$:
$$N(v) = \{ u \in V_N \mid \{v, u\} \in E_N \}$$
The degree of a vertex $v$ is defined as $d(v) = |N(v)|$. For any subset of vertices $U \subseteq V_N$, we define the restricted neighborhood of $v$ with respect to $U$ as:
$$N_U(v) = N(v) \cap U$$
The restricted degree is then $d_U(v) = |N_U(v)|$.

### 1.4 Mathematical Formulation of the Tour
A **Knight's Tour** is a Hamiltonian path in the Knight's Graph $\mathcal{G}_N$. Formally, it is a sequence of vertices $P = (v_0, v_1, \dots, v_{N^2-1})$ satisfying:
1. **Completeness and Uniqueness (Bijectivity):** The mapping $i \mapsto v_i$ is a bijection from $\{0, 1, \dots, N^2-1\}$ to $V_N$.
2. **Adjacency:** For all $i \in \{0, 1, \dots, N^2-2\}$, $\{v_i, v_{i+1}\} \in E_N$.
3. **Initial Condition:** $v_0 = (0, 0)$.

The output of the algorithm is represented as a matrix $M \in (\{-1\} \cup \{0, 1, \dots, N^2-1\})^{N \times N}$ defined by:
$$M[r][c] = \begin{cases} 
i & \text{if } v_i = (r, c) \text{ for some } i \in \{0, \dots, N^2-1\} \\
-1 & \text{if no such sequence } P \text{ exists}
\end{cases}$$

---

## 2. Algebraic Characterization and State-Space Search

The backtracking algorithm systematically searches the state space of simple paths in $\mathcal{G}_N$ starting at $v_0$.

### 2.1 State Space Representation
Let $\mathcal{S}$ be the set of valid partial states. A state $s \in \mathcal{S}$ at step $k$ (where $1 \le k \le N^2$) is represented by the tuple:
$$s = (P_k, U_k)$$
where:
* $P_k = (v_0, v_1, \dots, v_{k-1})$ is a sequence of $k$ distinct vertices representing the path traversed so far, with $v_0 = (0, 0)$.
* $U_k = V_N \setminus \{v_0, \dots, v_{k-1}\}$ is the set of unvisited vertices, satisfying $|U_k| = N^2 - k$.

### 2.2 State Transition and Backtracking
Let $\tau: \mathcal{S} \to \mathcal{P}(\mathcal{S})$ be the transition relation that maps a state to its potential successor states. For a state $s = (P_k, U_k)$ with $P_k = (v_0, \dots, v_{k-1})$:
$$\tau((P_k, U_k)) = \left\{ (P_{k+1}, U_{k+1}) \;\middle|\; v_{k} \in N(v_{k-1}) \cap U_k \right\}$$
where:
* $P_{k+1} = P_k \mathbin{\Vert} (v_k)$ (where $\mathbin{\Vert}$ denotes sequence concatenation).
* $U_{k+1} = U_k \setminus \{v_k\}$.

The search terminates successfully if a state is reached where $k = N^2$, meaning $U_k = \emptyset$. If $\tau((P_k, U_k)) = \emptyset$ and $k < N^2$, the algorithm backtracks by reverting the state to $s' = (P_{k-1}, U_{k-1})$ and attempting alternative transitions.

### 2.3 Warnsdorff's Heuristic
To optimize the search, Warnsdorff's heuristic imposes a total preorder on the candidate successor vertices. For a state $s = (P_k, U_k)$ with current vertex $v_{k-1}$, the set of candidate next steps is:
$$C(s) = N_{U_k}(v_{k-1})$$
For each candidate $w \in C(s)$, we compute its onward degree within the unvisited subgraph:
$$\text{deg}_{U_k \setminus \{w\}}(w) = \left| N(w) \cap \left( U_k \setminus \{w\} \right) \right|$$
Warnsdorff's heuristic asserts that candidates should be prioritized in non-decreasing order of their onward degrees. We define the ordering relation $\le_W$ on $C(s)$ as:
$$w_1 \le_W w_2 \iff \text{deg}_{U_k \setminus \{w_1\}}(w_1) \le \text{deg}_{U_k \setminus \{w_2\}}(w_2)$$
The backtracking algorithm evaluates transitions to successor states $(P_k \mathbin{\Vert} (w), U_k \setminus \{w\})$ sequentially according to this sorted order.

### 2.4 Correctness and Invariants
The correctness of the backtracking search is established via the following loop and recursion invariants:

#### Invariant 1 (Path Validity)
At any recursion depth $k$, the sequence $P_k = (v_0, \dots, v_{k-1})$ is a simple path in $\mathcal{G}_N$.
$$\forall i, j \in \{0, \dots, k-1\}, \; i \neq j \implies v_i \neq v_j \quad \land \quad \forall i \in \{0, \dots, k-2\}, \; \{v_i, v_{i+1}\} \in E_N$$

#### Invariant 2 (State Partitioning)
At any step $k$, the set of visited vertices and unvisited vertices partition the vertex set $V_N$:
$$\{v_0, \dots, v_{k-1}\} \cup U_k = V_N \quad \text{and} \quad \{v_0, \dots, v_{k-1}\} \cap U_k = \emptyset$$

#### Theorem (Termination and Correctness)
The algorithm terminates because the state space $\mathcal{S}$ is finite (bounded by $|V_N|!$). Upon termination, it returns a non-empty path $P$ if and only if there exists a sequence satisfying the Hamiltonian path criteria on $\mathcal{G}_N$ starting at $(0,0)$.

---

## 3. Complexity Analysis

### 3.1 Time Complexity

#### Worst-Case Analysis
In the worst-case scenario, the heuristic may fail to prune dead ends early, forcing the algorithm to traverse the entire state-space tree. 

Let $T(k)$ represent the maximum number of states visited from depth $k$ to the leaf level $N^2$. At each step, the knight has at most 8 legal moves. The recurrence relation governing the worst-case search tree size is:
$$T(k) \le 8 \cdot T(k+1) + \mathcal{O}(1)$$
With base case $T(N^2) = \mathcal{O}(1)$, solving this recurrence yields:
$$T(0) \le \sum_{k=0}^{N^2-1} 8^k = \frac{8^{N^2} - 1}{7} = \mathcal{O}\left(8^{N^2}\right)$$
Thus, the worst-case time complexity is $\mathcal{O}\left(8^{N^2}\right)$.

#### Best-Case Analysis
In the best-case scenario, Warnsdorff's heuristic successfully identifies a valid Hamiltonian path without a single backtracking step. 

At each step $k \in \{1, \dots, N^2\}$, the algorithm performs the following operations:
1. Identifies adjacent unvisited vertices: $\mathcal{O}(1)$ (since $|N(v)| \le 8$).
2. Computes the onward degree for each neighbor: $\mathcal{O}(1)$ (evaluating at most 8 neighbors, each having at most 8 neighbors, requiring at most 64 checks).
3. Sorts the candidates: $\mathcal{O}(d \log d)$ where $d \le 8$, which is $\mathcal{O}(1)$.

Since the algorithm transitions directly to the correct state at each level of the recursion tree of depth $N^2$, the total work is:
$$T_{\text{best}}(N) = \sum_{k=1}^{N^2} \mathcal{O}(1) = \mathcal{O}(N^2)$$
Thus, the best-case time complexity is $\mathcal{O}(N^2)$.

### 3.2 Space Complexity

The space complexity is determined by the storage of the board state and the execution stack of the recursive helper function.

#### Auxiliary Space
1. **Recursion Stack:** The maximum depth of the recursion tree is exactly $N^2$ frames. Each stack frame stores a constant amount of information: the current coordinates $(r, c)$, the current step number, and a list of candidates of size at most 8. Thus, the stack space is:
   $$S_{\text{stack}}(N) = \mathcal{O}(N^2)$$
2. **State Tracking:** 
   * The `visited` matrix of size $N \times N$ requires $\mathcal{O}(N^2)$ bits.
   * The `path` list stores at most $N^2$ coordinate pairs, requiring $\mathcal{O}(N^2)$ space.

Combining these components, the auxiliary space complexity is:
$$\text{Space}_{\text{aux}}(N) = S_{\text{stack}}(N) + S_{\text{state}}(N) = \mathcal{O}(N^2) + \mathcal{O}(N^2) = \mathcal{O}(N^2)$$

#### Total Space Complexity
Since the output matrix $M$ is of size $N \times N$, the total space complexity (including output space) is:
$$\text{Space}_{\text{total}}(N) = \mathcal{O}(N^2)$$