# Guided Example: Magic Squares In Grid

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A `3 x 3` **magic square** is a `3 x 3` grid filled with distinct numbers **from **1** to **9 such that each row, column, and both diagonals all have the same sum.

The objective is to compute `1` from `{"grid": [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat every cell as a possible top-left corner

A candidate magic square always has exactly three rows and three columns. The outer expression calls `check(i,j)` for every grid coordinate, interpreting it as a possible top-left corner.

The first check rejects positions where `i+3 > m` or `j+3 > n`. Those candidates would extend below or to the right of the grid.

Calling `check` even near boundaries keeps the outer iteration simple. Out-of-bounds candidates return zero before any cell access.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Validate the allowed values and distinctness

Inside a valid 3-by-3 window, the nested loops inspect all nine cells.

If a value is below 1 or above 9, the candidate immediately fails. Otherwise, it is inserted into set `s`.

After scanning, `len(s) == 9` means all nine values are distinct. Combined with every value lying in the nine-element domain `1..9`, this proves the window contains each number from 1 through 9 exactly once.

The code does not need a separate sorted comparison against `[1,2,\ldots,9]`. Nine distinct selections from a domain containing exactly nine possibilities must be the complete domain.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Accumulate every required line sum

Arrays `row` and `col` contain three zeroes each. For grid cell `(x,y)`:

- `row[x-i]` receives its value;
- `col[y-j]` receives its value.

Subtracting the window's top-left coordinate converts global grid indices into local indices 0, 1, and 2.

Variable `a` sums the main diagonal, where local row equals local column. Variable `b` sums the other diagonal, where local row equals `2 - local column`.

The center cell belongs to both diagonals, as it should.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate only valid top-left ranges:** Loop through `range(r-2)` and `range(c-2)`. This avoids boundary calls but has the same complexity.
- **Exploit special Lo Shu properties:** Every 3-by-3 normal magic square has center 5 and other structural constraints. Those checks can reject faster, but explicit definition validation is easier to prove.
- **Check only line sums:** Equal lines are not enough; values must also be distinct and in 1 through 9.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(rc)$. Let the grid have `r` rows and `c` columns. The outer iteration calls `check` `rc` times. Each call performs either a constant-time boundary rejection or examines exactly nine cells and fixed-size arrays. Nine is constant, so total time is `O(rc)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
