# Guided Example: Longest Increasing Path in a Matrix

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"matrix": [[9, 9, 4], [6, 6, 8], [2, 1, 1]]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an `m x n` integers `matrix`, return *the length of the longest increasing path in *`matrix`.

The objective is to compute `4` from `{"matrix": [[9, 9, 4], [6, 6, 8], [2, 1, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: View the matrix as a directed acyclic graph.

Treat every cell as a vertex. From cell $(i,j)$, draw a directed edge to each orthogonally adjacent cell $(x,y)$ whose value is strictly larger:

$$
\text{matrix}[x][y] > \text{matrix}[i][j].
$$

Then every allowed increasing path in the matrix is exactly a directed path in this implicit graph. “Implicit” means the source never constructs adjacency lists; it checks the four neighboring coordinates whenever it evaluates a cell.

This directed graph cannot contain a cycle. Along every edge, the value strictly increases. Returning to a previously visited cell would require ending with the same value with which the cycle began, contradicting a chain of strict increases. This acyclic property is why a recursive longest-path recurrence is safe without a per-call visited set.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"matrix": [[9, 9, 4], [6, 6, 8], [2, 1, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Define the recursive state.

The cached helper has the meaning

$$
\operatorname{dfs}(i,j)
=\text{length of the longest increasing path that starts at }(i,j).
$$

The path counts cells, not moves. A path containing only its starting cell has length one.

From $(i,j)$, the first move may go to any larger orthogonal neighbor $(x,y)$. Once that move is chosen, the best possible continuation is `dfs(x, y)`. Therefore the recurrence is

$$
\operatorname{dfs}(i,j)
=1+\max_{(x,y)}\operatorname{dfs}(x,y),
$$

where the maximum ranges only over in-bounds, orthogonally adjacent cells with a strictly larger value. If there is no such neighbor, the maximum over continuations is treated as zero, so the state returns one.

The source realizes this by starting `ans = 0`, maximizing it with each eligible neighbor's result, and returning `ans + 1`. The added one accounts for the current cell.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The cached helper has the meaning

$$
\operatorname{dfs}(i,j... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Generate exactly four directions.

The expression `pairwise((-1, 0, 1, 0, -1))` produces these consecutive pairs:

$$
(-1,0),\ (0,1),\ (1,0),\ (0,-1).
$$

They mean up, right, down, and left. There are no diagonal pairs. Repeating `-1` at the end closes the direction pattern so the final pair is `(0,-1)`.

For each direction `(a, b)`, the candidate neighbor is `(i + a, j + b)`. The compound condition verifies both row and column bounds before indexing the matrix. It then requires the neighbor value to be greater. Equality is rejected because the path must be strictly increasing, not merely non-decreasing.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"matrix": [[9, 9, 4], [6, 6, 8], [2, 1, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Topological layer peeling:** Compute each cell:** - **Topological layer peeling:** Compute each cell's number of outgoing edges to larger neighbors, enqueue local maxima, and remove the graph layer by layer. The number of layers equals the longest increasing path. This also runs in $O(mn)$ time and space, avoids recursion, and matches the manifest summary, but it is not the exact source.
- **- **Naive DFS from every cell:** The recurrence is:** - **Naive DFS from every cell:** The recurrence is correct without caching, but shared suffix paths are recalculated many times and can cause exponential work. Memoization is the essential optimization.
- **- **Sort cells by value:** Process coordinates in :** - **Sort cells by value:** Process coordinates in descending value order and fill a DP table from larger neighbors. This makes the dependency order explicit but adds an $O(mn\log(mn))$ sorting cost.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. Let $m$ be the number of rows and $n$ the number of columns. There are $mn$ cacheable states. Each state is computed once and checks exactly four candidate directions, so total time is $O(mn)$. Cache hits from other branches or the final outer scan take constant time.
- **Auxiliary Space Complexity:** $O(mn)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
