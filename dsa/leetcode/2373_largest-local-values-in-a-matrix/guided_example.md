# Guided Example: Largest Local Values in a Matrix

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]}`
- **Required output:** `[[9, 9], [8, 6]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `n x n` integer matrix `grid`.

The objective is to compute `[[9, 9], [8, 6]]` from `{"grid": [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Map every output position to one fixed window

The output has size $(n-2)\times(n-2)$. An output coordinate `(i, j)` corresponds to the contiguous $3\times3$ input window whose top-left corner is `(i, j)`. Equivalently, that window is centered at input coordinate `(i+1, j+1)`.

Its rows are:



and its columns are:



The largest of those nine cells is exactly `ans[i][j]`. Once this coordinate mapping is clear, the solution is a direct simulation of the definition.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why there are exactly `n - 2` starting positions

A $3\times3$ window starting at row `i` needs index `i + 2` to remain inside the matrix, so `i <= n - 3`. The valid zero-based starts are `0` through `n - 3`, which is `n - 2` choices. The same reasoning applies to columns.

Therefore, both outer loops use `range(n - 2)`, and the result matrix is allocated with `n - 2` rows and columns. No padding or boundary checks are needed inside a valid window.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | A $3\times3$ window starting at row `i` needs index `i + 2` ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Inspect the nine cells with a generator

For one output coordinate, the exact assignment is:



The first generator loop chooses each of the three rows. For each selected row, the second chooses each of the three columns. Their Cartesian product yields all nine coordinates in the window exactly once.

`max` consumes these values and returns their greatest value. The generator is lazy: it does not allocate a separate nine-element list. It produces one cell value at a time for `max`.

All input values are positive, but the implementation does not depend on choosing zero as an initial maximum. Python's `max` initializes from actual generated values. This would remain correct even if negative grid values were allowed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[9, 9], [8, 6]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[9, 9], [8, 6]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Two-pass sliding maxima:** Compute width-three:** - **Two-pass sliding maxima:** Compute width-three row maxima and then height-three column maxima with deques. This is useful for variable or very large windows, but fixed $3\times3$ scanning is simpler and already $O(n^2)$.
- **Helper function per window:** Moving the nine-cell scan into a named function may improve readability but performs the same work.
- **Materialize each window:** Building a list of nine values before calling `max` is correct but creates unnecessary temporary objects; the generator avoids them.
- **Minimum size `n = 3`:** There is exactly one valid window, so the result is a $1\times1$ matrix containing the maximum of the entire input.
- **All values equal:** Every local maximum equals that common value.
- **Maximum on a window boundary:** The generator includes all three rows and columns, so corners and edges are treated the same as the center.
- **One large value shared by windows:** Every overlapping window that contains it independently reports it.
- **Input preservation:** A separate `ans` matrix ensures later windows never see altered values.
- **Off-by-one boundary:** `range(n - 2)` ends at `n - 3`, the last start whose `+2` index is `n - 1`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. There are $(n-2)^2$ output cells. For each, the generator yields exactly nine input values. The number of cell inspections is:
- **Auxiliary Space Complexity:** $O(n^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
