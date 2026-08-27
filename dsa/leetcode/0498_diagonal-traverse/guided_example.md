# Guided Example: Diagonal Traverse

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"mat": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}`
- **Required output:** `[1, 2, 4, 7, 5, 3, 6, 8, 9]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an `m x n` matrix `mat`, return *an array of all the elements of the array in a diagonal order*.

The objective is to compute `[1, 2, 4, 7, 5, 3, 6, 8, 9]` from `{"mat": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}` while avoiding redundant calculations and unnecessary overhead.

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

Cells belong to the same top-right-to-bottom-left diagonal when their row and column indices have the same sum. Moving one row down and one column left changes `i + j` by `+1 - 1 = 0`, so the sum remains constant. The solution names that constant `k` and processes diagonals in order from `k = 0` through `k = m + n - 2`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"mat": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

There are `m + n - 1` diagonals in an `m` by `n` matrix. The smallest index sum is zero at `(0, 0)`. The largest is `(m - 1) + (n - 1) = m + n - 2`. Python's `range(m + n - 1)` includes exactly those values.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | There are `m + n - 1` diagonals in an `m` by `n` matrix.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Find the topmost valid cell for one diagonal.** The traversal inside every diagonal moves down-left with `i += 1` and `j -= 1`. It therefore needs to begin at the diagonal's topmost or rightmost endpoint.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2, 4, 7, 5, 3, 6, 8, 9]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"mat": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2, 4, 7, 5, 3, 6, 8, 9]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Direct zigzag simulation:** Track one cell at :** - **Direct zigzag simulation:** Track one cell at a time, move up-right or down-left, and handle boundary bounces. It can use $O(1)$ auxiliary space but has more corner-specific state transitions.
- **Group by `i + j` in a dictionary:** Append every cell to its diagonal bucket, then reverse alternating buckets. It is easy to derive but stores the full matrix again.
- **One row:** Every diagonal has one value, so the output stays in left-to-right order despite alternating reversal calls.
- **One column:** Each diagonal also has one value, producing top-to-bottom order.
- **Wide matrix:** Early diagonals start along the first row; only after `k >= n` do starts move down the last column.
- **Tall matrix:** The same formulas remain valid, and the down-left loop stops at the bottom before the column becomes negative where appropriate.
- **Parity convention:** Diagonals are zero-indexed. Even `k` is reversed; describing them as human-numbered first, third, fifth diagonals refers to the same set.
- **Nonempty guarantee:** The implementation immediately reads `mat[0]` and relies on the stated positive dimensions.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. Every matrix value is appended to one temporary diagonal and then extended into `ans` exactly once. Reversing even diagonals processes those values one additional time, but the total across all diagonals remains $O(mn)$. Therefore time is $O(mn)$.
- **Auxiliary Space Complexity:** $O(\min(m,n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
