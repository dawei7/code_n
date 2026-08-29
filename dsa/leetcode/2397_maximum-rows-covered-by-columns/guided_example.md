# Guided Example: Maximum Rows Covered by Columns

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"matrix": [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 0, 1]], "numSelect": 2}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` binary matrix `matrix` and an integer `numSelect`.

The objective is to compute `3` from `{"matrix": [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 0, 1]], "numSelect": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Represent each row's required columns as bits

A row is covered when every column containing one in that row has been selected. With at most twelve columns, a single integer can represent both a row's requirements and a selected-column set.

Bit `j` corresponds to column `j`. For each row, the code generates `1 << j` only where the cell value is one and combines those bits using bitwise OR:



The initial value zero handles an all-zero row. Its resulting mask is zero, meaning it requires no selected column.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"matrix": [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 0, 1]], "numSelect": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Enumerate selected-column masks

For `n` columns, integers zero through `2^n - 1` encode every possible subset. The loop:



therefore considers every column selection once.

The problem requires exactly `numSelect` distinct columns. `mask.bit_count()` gives the number of set bits, so masks with the wrong cardinality are skipped. A bitmask cannot select the same column twice; distinctness is automatic.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Test whether one row is covered

Let row requirement mask be `x` and selected mask be `mask`. Bitwise `x & mask` retains required bits that are also selected. The row is covered exactly when:



Equality means every one bit of `x` survives, so all required columns belong to the selection. Extra selected columns do not matter.

For an all-zero row, `x = 0`. Then `0 & mask == 0` for every selection, correctly treating the row as always covered.

The expression is Boolean, and Python's `sum` counts true values as one:



`t` is therefore the number of rows covered by this exact-size selection.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"matrix": [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 0, 1]], "numSelect": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Generate only combinations:** Iterating `combinations(range(n), k)` avoids checking the other $2^n-\binom{n}{k}$ masks and aligns more closely with the manifest formula.
- **Backtracking with pruning:** Build selections one column at a time and bound remaining coverage. It can help larger domains but is unnecessary for twelve columns.
- **All-zero row:** Its zero mask is a subset of every selection and is always counted.
- **`numSelect = n`:** Only the all-bits mask qualifies, and every row is covered.
- **One selected column:** Only rows whose one bits are all in that column, plus zero rows, count.
- **Row with more than `numSelect` ones:** It can never be covered, and every subset test fails.
- **Duplicate row masks:** They are separate matrix rows and each contributes independently to `t`.
- **Extra selected zeros:** Selecting a column where a row has zero never harms coverage.
- **Bit orientation:** Only consistent mapping matters; bit `j` is used for column `j` everywhere.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O\left(mn+2^n+m\binom{n}{k}\right)$. Let $m$ be the row count, $n$ the column count, and $k$ the number selected. Building all row masks examines $mn$ cells, taking $O(mn)$ time.
- **Auxiliary Space Complexity:** $O(m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
