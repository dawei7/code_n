# Guided Example: Count Sub Islands

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid1": [[1]], "grid2": [[1]]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two `m x n` binary matrices `grid1` and `grid2` containing only `0`'s (representing water) and `1`'s (representing land). An **island** is a group of `1`'s connected **4-directionally** (horizontal or vertical). Any cells outside of the grid are considered water cells.

The objective is to compute `1` from `{"grid1": [[1]], "grid2": [[1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Judge each complete island in `grid2`.** A sub-island condition applies to an entire four-connected component, not to isolated cells. The algorithm launches DFS from every still-land cell in `grid2`. That search consumes the whole island and returns one only if every one of its cells overlaps land in `grid1`. Summing these return values counts qualifying islands.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid1": [[1]], "grid2": [[1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Use `grid2` itself as the visited structure.** On entering `dfs(i, j)`, the source saves `ok = grid1[i][j]`, then writes `grid2[i][j] = 0`. Changing the current land cell to water marks it visited before exploring neighbors. Any later path reaching the same coordinate sees zero and does not recurse, preventing cycles and duplicate work.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

This mutation is intentional and observable: after the method returns, all land cells of `grid2` have been cleared. No separate visited matrix is allocated.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid1": [[1]], "grid2": [[1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Iterative DFS or BFS:** An explicit stack or queue avoids Python recursion limits while keeping $O(mn)$ time and worst-case space. It can still clear `grid2` in place.
- **Separate visited matrix:** Preserves `grid2` but allocates $O(mn)$ additional memory. The exact source chooses destructive marking.
- **Erase invalid land first:** Remove every `grid2` cell lying over `grid1` water, then count remaining islands. Care is needed because removing one cell can split an original invalid island into pieces that must not be counted.
- **Grid2 island over multiple Grid1 islands:** If every corresponding cell is land and cells are four-connected, they cannot actually belong to different `grid1` islands; their same adjacencies connect them there too.
- **Single-cell island:** It contributes one exactly when the corresponding `grid1` cell is land.
- **Diagonal contact:** Diagonally touching land belongs to separate islands because only four directions are generated.
- **Invalid cell found early:** DFS must continue clearing the component. The source preserves exploration even after `ok` becomes zero.
- **Input mutation:** All visited `grid2` land is changed to water. Pass a copy if the caller must retain the original grid.
- **Large solid island:** Correct asymptotic work is linear, but recursive depth may exceed Python's default limit; iterative traversal is safer.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. Let the grids have $m$ rows and $n$ columns. The outer generator examines all $mn$ coordinates. Every original `grid2` land cell enters DFS once and checks four neighbors. Total time is $O(mn)$.
- **Auxiliary Space Complexity:** $O(mn)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
