# Guided Example: Count Islands With Total Value Divisible by K

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[3, 0, 3, 0], [0, 3, 0, 3], [3, 0, 3, 0]], "k": 3}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` matrix `grid` and a positive integer `k`. An **island** is a group of **positive** integers (representing land) that are **4-directionally** connected (horizontally or vertically).

The objective is to compute `6` from `{"grid": [[3, 0, 3, 0], [0, 3, 0, 3], [3, 0, 3, 0]], "k": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Four-directional neighbors

`dirs = (-1,0,1,0,-1)` encodes the four coordinate offsets. Consecutive pairs are:

- `(-1,0)`: up;
- `(0,1)`: right;
- `(1,0)`: down;
- `(0,-1)`: left.

The loop `for a,b in pairwise(dirs)` uses those pairs without listing four tuples separately.

Diagonal cells are never examined, matching the definition of 4-directional connectivity.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[3, 0, 3, 0], [0, 3, 0, 3], [3, 0, 3, 0]], "k": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Starting one flood fill

The outer nested loops inspect every `(i,j)`. A nonzero value means positive unvisited land because the constraints allow only zero or positive values.

Calling `dfs(i,j)` then discovers exactly the island containing that cell.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The outer nested loops inspect every `(i,j)`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Marking on discovery

At the start of `dfs`:

`s = grid[i][j]`

saves the cell value, and:

`grid[i][j] = 0`

marks it visited before exploring neighbors.

Marking before recursion is essential. If two adjacent cells recursively call each other while both still appear positive, the search would cycle forever. Once a cell is zero, all later neighbor checks ignore it.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[3, 0, 3, 0], [0, 3, 0, 3], [3, 0, 3, 0]], "k": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Iterative DFS:** Use an explicit list stack, a:** - **Iterative DFS:** Use an explicit list stack, avoiding `RecursionError` while preserving `O(mn)` time.
- **Breadth-first search:** A deque flood fill is equally correct and also avoids recursion depth.
- **Separate visited matrix:** Preserve `grid` at the cost of `O(mn)` additional Boolean storage.
- **Accumulate modulo `k`:** Replace full sums with remainders after each addition; divisibility is preserved because modular addition is compatible with ordinary addition.
- **Union-Find:** Merge adjacent land cells and accumulate per-root sums. It works but is more machinery than a one-pass flood fill.
- **All water:** No DFS starts and the answer is zero.
- **Single positive cell:** It is one island and qualifies exactly when its value is divisible by `k`.
- **Diagonal contact:** Diagonal cells remain separate islands.
- **`k = 1`:** Every integer sum is divisible by 1, so every island is counted.
- **Island sum zero:** Impossible for a nonempty island because all land values are positive.
- **Long snake island:** It is correct conceptually but can exceed Python's recursion limit in the exact source.
- **Maximum cell values:** Python integers hold the full component sum without overflow.
- **Repeated outer encounters:** Cleared cells are zero and cannot start another DFS.
- **Missing `pairwise` import:** Standalone code must import it from `itertools`.
- **Input preservation:** The exact solution does not preserve input; all visited land becomes zero.
- **Manifest mismatch:** The source sums full values rather than maintaining only modulo `k`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. Let the grid have `m` rows and `n` columns. Every cell is inspected by the outer scan. Each positive cell is entered by DFS once, zeroed once, and has four neighbor directions checked once. Total time is `O(mn)`.
- **Auxiliary Space Complexity:** $O(mn)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
