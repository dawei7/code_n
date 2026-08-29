# Guided Example: Find the Degree of Each Vertex

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"matrix": [[0, 1, 1], [1, 0, 1], [1, 1, 0]]}`
- **Required output:** `[2, 2, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a 2D integer array `matrix` of size `n x n` representing the adjacency matrix of an undirected graph with `n` vertices labeled from 0 to $n - 1$.

The objective is to compute `[2, 2, 2]` from `{"matrix": [[0, 1, 1], [1, 0, 1], [1, 1, 0]]}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Why one matrix row corresponds to one vertex

The first index is the vertex whose neighbors are being described. For a fixed $i$, moving across columns $j=0,1,\ldots,N-1$ asks whether vertex $i$ connects to each possible endpoint $j$.

The degree of $i$ is

$$
\deg(i)=\sum_{j=0}^{N-1}\texttt{matrix}[i][j].
$$

There is no need to interpret a 1 as anything more complicated than one incident edge. A zero adds nothing.

The diagonal guarantee `matrix[i][i] = 0` means no row includes a self-loop. This matters because conventions for self-loops can count two toward an undirected degree, while a plain row sum would count a diagonal 1 only once. The simple-graph contract removes that ambiguity.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"matrix": [[0, 1, 1], [1, 0, 1], [1, 1, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: How the nested loops realize the formula

The source first creates `ans` with one zero for every row:



During `for i, row in enumerate(matrix)`, `i` is both the row index and the vertex label. The inner loop visits each binary entry `x` in that row and performs



After the first $t$ entries of row $i$ have been processed, `ans[i]` equals their sum. Processing the next entry adds one exactly when the next neighbor exists. At the end of the row, all $N$ potential neighbors have been considered, so `ans[i]` equals $\deg(i)$.

Each row has its own accumulator position. Finishing one row does not affect any other answer entry.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why matrix symmetry does not cause an error

For an undirected edge $\{i,j\}$, the symmetric matrix contains

$$
\texttt{matrix}[i][j]=1
\quad\text{and}\quad
\texttt{matrix}[j][i]=1.
$$

The algorithm visits both entries. That does not double-count the degree of one vertex. The first entry contributes one to `ans[i]`, while the symmetric entry contributes one to `ans[j]`. An undirected edge is incident to both endpoints, so both degrees must increase.

Double-counting would be a concern if the task asked for the total number of edges. In that different task, summing the entire matrix would count each undirected edge twice. Here the output deliberately asks for a separate incident-edge count at every endpoint.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 2, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"matrix": [[0, 1, 1], [1, 0, 1], [1, 1, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 2, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Built-in row sums:** Returning `[sum(row) for row in matrix]` expresses the same algorithm more compactly, with the same $O(N^2)$ time and $O(N)$ output space.
- **Upper-triangle scan:** Visit only entries with $i<j$ and increment both endpoint degrees for every one. This uses symmetry explicitly but does not improve the asymptotic time for dense matrix storage.
- **Adjacency-list input:** If the graph were stored by neighbors, degrees could be obtained in $O(N+E)$ time. Converting this matrix first would still require reading $N^2$ entries.
- **Single vertex:** The sole diagonal entry is zero, so the answer is `[0]`.
- **Isolated vertex:** An all-zero row leaves its accumulator at zero.
- **Complete simple graph:** Every row has $N-1$ ones and one diagonal zero, so every returned degree is $N-1$.
- **Symmetric duplicate entries:** They belong to different vertex accumulators and correctly account for the edge at both endpoints.
- **Zero diagonal requirement:** The row-sum method relies on the promise of no self-loops; a different self-loop degree convention would need explicit handling.
- **Binary-entry requirement:** Summation works because 1 means one edge and 0 means none. Weighted adjacency values would produce weighted sums rather than ordinary degrees.
- **Input preservation:** The method does not sort or alter any row, so the supplied matrix remains unchanged.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$. Let $N$ be the number of vertices. An adjacency matrix has exactly $N^2$ entries. The nested loops inspect every entry once and perform constant work for it, so the running time is
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
