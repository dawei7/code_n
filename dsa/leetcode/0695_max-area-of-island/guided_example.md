# Guided Example: Max Area of Island

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[1, 1], [0, 0]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The objective is to compute `2` from `{"grid": [[1, 1], [0, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The recursive contract

`dfs(i, j)` returns:

- zero if cell `(i, j)` is water;
- otherwise, the number of land cells in the connected island portion reached from that cell before any of those cells were visited.

The caller performs boundary checks before calling a neighbor, so `dfs` itself assumes `i` and `j` are valid indices.

If `grid[i][j] == 0`, the function immediately returns zero. A zero may be original water or land that an earlier recursive call has already visited. Treating both cases identically prevents double counting.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[1, 1], [0, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Counting and marking one land cell

For a land cell, `ans = 1` counts the current cell. Then `grid[i][j] = 0` marks it visited before any neighbors are explored.

Marking before recursion is necessary. Adjacent land cells point back to one another. If the current cell remained one while exploring a neighbor, that neighbor could recursively enter it again, creating repeated counts and possibly infinite recursion.

The grid mutation replaces a separate visited structure.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For a land cell, `ans = 1` counts the current cell.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Generating four-directional neighbors

`dirs = (-1, 0, 1, 0, -1)` combined with `pairwise(dirs)` produces:

- `(-1, 0)`;
- `(0, 1)`;
- `(1, 0)`;
- `(0, -1)`.

These are exactly the four legal connectivity directions. Diagonal cells are intentionally absent.

For every offset `(a, b)`, the code computes `x = i + a` and `y = j + b`. It calls `dfs(x, y)` only when `0 <= x < m` and `0 <= y < n`. This keeps all grid accesses valid.

The returned neighbor areas are added into `ans`. Since visited cells become zero, the recursive branches cover disjoint sets of newly counted land cells even when the island contains cycles in its adjacency graph.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[1, 1], [0, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Iterative DFS:** Use a stack, mark cells when :** - **Iterative DFS:** Use a stack, mark cells when pushing them, and increment a counter when popping. This avoids recursion depth limits while retaining `O(RC)` time and space.
- **- **Breadth-first search:** A queue explores one i:** - **Breadth-first search:** A queue explores one island level by level. It computes the same component size with the same asymptotic bounds.
- **- **Separate visited set:** Preserve `grid` by tra:** - **Separate visited set:** Preserve `grid` by tracking coordinates externally. This uses explicit `O(RC)` storage but avoids input mutation.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(RC)$. Let `R` and `C` be the grid dimensions.
- **Auxiliary Space Complexity:** $O(RC)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
