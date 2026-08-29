# Guided Example: Modify the Matrix

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"matrix": [[1, 2, -1], [4, -1, 6], [7, 8, 9]]}`
- **Required output:** `[[1, 2, 9], [4, 8, 6], [7, 8, 9]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a **0-indexed** `m x n` integer matrix `matrix`, create a new **0-indexed** matrix called `answer`. Make `answer` equal to `matrix`, then replace each element with the value `-1` with the **maximum** element in its respective column.

The objective is to compute `[[1, 2, 9], [4, 8, 6], [7, 8, 9]]` from `{"matrix": [[1, 2, -1], [4, -1, 6], [7, 8, 9]]}` while avoiding redundant calculations and unnecessary overhead.

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

**Process one column at a time.** Every cell containing $-1$ must be replaced by the maximum value from its own column. Columns are independent: a replacement in column $j$ never affects the maximum or output of another column. The exact source therefore loops over column index `j`, determines that column's maximum, and then performs all replacements in the same column.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"matrix": [[1, 2, -1], [4, -1, 6], [7, 8, 9]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 4

visits every row and returns the maximum original value in that column. The reference guarantees that each column contains at least one non-negative integer. Since every other value is at least $-1$, the maximum is non-negative and cannot be the sentinel $-1$.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Optimality Decision

Synthesize the final answer directly from validated sub-states.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 2, 9], [4, 8, 6], [7, 8, 9]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"matrix": [[1, 2, -1], [4, -1, 6], [7, 8, 9]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 2, 9], [4, 8, 6], [7, 8, 9]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Copy the matrix first:** A deep row-by-row copy would preserve the input and use $O(MN)$ extra space, matching the manifest summary. The protected source instead chooses in-place mutation.
- **Precompute all column maxima:** Store an $N$-element maxima array, then scan the matrix once for replacement. This also takes $O(MN)$ time but uses $O(N)$ extra space; computing one column at a time avoids it.
- **Row-wise processing:** A row maximum is irrelevant because replacements depend on columns. Any row-oriented approach must still maintain separate information for every column.
- **Replace while searching:** A sentinel encountered before the true maximum cannot be filled correctly yet. The exact two-pass-per-column structure avoids that ordering problem.
- **Several $-1$ values in one column:** They all receive the same precomputed column maximum.
- **No $-1$ in a column:** The maximum is still computed, but the replacement pass changes nothing.
- **Maximum equals zero:** Zero is non-negative and valid; every sentinel in that column becomes zero.
- **Other negative values:** The contract permits only $-1$ below zero, so there is no ambiguity between a real negative intensity and the sentinel.
- **All but one cell are $-1$:** The one non-negative entry is the maximum and is copied into every sentinel position in that column.
- **Input mutation:** Any outside reference to `matrix` observes the replacements, and `result is matrix` would be true in Python.
- **Column independence:** Changes already made in earlier columns cannot affect the maximum in the current column.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(MN)$. Let the matrix have $M$ rows and $N$ columns. Each column is traversed once to find its maximum and once to replace sentinels, for $2MN$ cell visits. Total time is $O(MN)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
