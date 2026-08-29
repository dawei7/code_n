# Guided Example: Number of Distinct Islands

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The objective is to compute `1` from `{"grid": [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Discovering islands and marking cells

The outer loops scan the grid row by row and left to right. When they encounter a `1`, that cell has not belonged to any earlier traversal, so it begins a new island.

Inside `dfs`, the statement `grid[i][j] = 0` marks the current land cell visited by turning it into water. This prevents the four-directional traversal from returning to the same cell and prevents the outer scan from starting the island again.

The method intentionally mutates `grid` instead of allocating a separate visited matrix.

The sequence `dirs = (-1, 0, 1, 0, -1)` encodes four neighbor offsets in a cycle. For `h` from `1` through `4`, the pair

`(dirs[h - 1], dirs[h])`

is respectively:

- `(-1, 0)`: up;
- `(0, 1)`: right;
- `(1, 0)`: down;
- `(0, -1)`: left.

This fixed order is essential: congruent translated islands must be explored in the same relative order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Encoding how DFS enters a cell

The parameter `k` records the direction used to enter the current cell. A root call uses `0`. Recursive calls use `h` from `1` to `4`.

As soon as a cell is visited, `path.append(str(k))` records its entry direction. If two islands are translations of one another, their row-major first cells occupy the same relative position in the shape, and the deterministic neighbor order makes DFS take the same entry-direction sequence.

Entry directions alone are not sufficient, however. Different branching shapes can produce the same preorder directions if the signature does not say when one branch ends.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why exit markers are necessary

After all reachable neighbors of a cell have been explored, the code appends `str(-k)`. This records that DFS is leaving the cell and backtracking over the same conceptual traversal edge.

For example, entering in direction `2` contributes `"2"`, and leaving that call contributes `"-2"`. The root contributes `"0"` on both entry and exit because negative zero is still zero when converted to a string.

These exit tokens preserve the nesting structure of the DFS tree. A direction explored as a child of the current cell can be distinguished from the same direction explored after returning to an ancestor.

Without exit markers, two different island shapes can share an entry preorder. With paired entry and exit events, the signature describes the entire ordered traversal structure.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Relative-coordinate sets:** Record `(row - origin_row, col - origin_col)` for each island and insert a `frozenset` of those offsets into the shape set. This is often easier to prove and has the same asymptotic bounds.
- **Sorted coordinate tuples:** Collect relative coordinates, sort them, and use the tuple as a hashable key. Sorting can add logarithmic work within islands.
- **Entry directions without exits:** This is insufficient because different branching structures can share the same preorder direction sequence. Backtracking markers are material, not decorative.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(RC)$. Let `R` be the number of rows and `C` the number of columns.
- **Auxiliary Space Complexity:** $O(RC)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
