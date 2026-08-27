# Guided Example: Where Will the Ball Fall

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[-1]]}`
- **Required output:** `[-1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have a 2-D `grid` of size `m x n` representing a box, and you have `n` balls. The box is open on the top and bottom sides.

The objective is to compute `[-1]` from `{"grid": [[-1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Simulate one row of movement at a time

A ball entering cell `(i, j)` sees either `1` or `-1`. A `1` board directs it toward column `j + 1`; a `-1` board directs it toward `j - 1`. If the move is valid, the ball then enters the next row at that adjacent column.

The nested `dfs(i, j)` function returns the eventual exit column for a ball currently entering row `i` at column `j`, or `-1` if it becomes stuck. Although the name says DFS, there is no branching search: every cell determines at most one next state. Recursion is used to express a deterministic path.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[-1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Recognize successful exit before reading another row

The first condition is `if i == m: return j`. Reaching row index `m` means the ball has passed all rows because valid grid rows are zero through `m - 1`. Its current column `j` is exactly the bottom exit column.

This base case comes before all grid accesses, preventing an attempt to read `grid[m]` after a successful fall.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The first condition is `if i == m: return j`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Stop boards that point into a wall

At the left boundary, a `-1` board would send the ball to column minus one. The source detects `j == 0 and grid[i][j] == -1` and returns `-1`.

At the right boundary, a `1` board would send the ball to column `n`. The condition `j == n - 1 and grid[i][j] == 1` returns `-1`.

These checks occur before inspecting either adjacent cell. That order is important in Python: it guarantees the later `j + 1` or `j - 1` access is within bounds whenever evaluated.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[-1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[-1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[-1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Iterative simulation:** Loop through rows for :** - **Iterative simulation:** Loop through rows for each starting column. It keeps the same $O(mn)$ time while reducing per-ball auxiliary space to $O(1)$.
- **Bottom-up dynamic programming:** Store the eventual result for every cell, reusing the next row. It can avoid repeated suffix paths but uses $O(mn)$ storage unless rows are compressed.
- **Memoized recursion:** Cache `dfs(i,j)` so merged paths are solved once. It uses up to $O(mn)$ cache space and does not improve the worst-case cell count below $O(mn)$.
- **Single column:** Every `1` points into the right wall and every `-1` into the left wall, so every ball is stuck.
- **Left-wall trap:** A negative-one board in column zero returns `-1` before accessing column minus one.
- **Right-wall trap:** A one board in column `n-1` returns `-1` before accessing column `n`.
- **V shape `1,-1`:** A ball entering either side becomes stuck between the opposing boards.
- **Matching pair:** Adjacent `1,1` permits rightward passage, while `-1,-1` permits leftward passage.
- **Stuck early:** Recursion returns immediately and does not inspect lower rows for that ball.
- **Exit after last row:** The returned column is the column after completing all row transitions, not the last cell's original column.
- **Input preservation:** The grid is read-only; no board values are changed.
- **Independent balls:** Balls do not interact, so simulating one does not alter another's path.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. Let $m$ be the number of rows and $n$ the number of columns. Each of the $n$ balls visits at most one cell per row, so there are at most $mn$ recursive calls. Each call does constant work, giving $O(mn)$ time.
- **Auxiliary Space Complexity:** $O(m+n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
