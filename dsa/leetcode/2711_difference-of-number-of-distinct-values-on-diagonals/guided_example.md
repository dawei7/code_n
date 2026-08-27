# Guided Example: Difference of Number of Distinct Values on Diagonals

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[1, 2, 3], [3, 1, 5], [3, 2, 1]]}`
- **Required output:** `[[1, 1, 0], [1, 0, 1], [0, 1, 1]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a 2D `grid` of size `m x n`, you should find the matrix `answer` of size `m x n`.

The objective is to compute `[[1, 1, 0], [1, 0, 1], [0, 1, 1]]` from `{"grid": [[1, 2, 3], [3, 1, 5], [3, 2, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Compute the two diagonal sides independently

For each cell `grid[i][j]`, the solution needs two distinct-value counts:

- values reached by repeatedly moving one row up and one column left;
- values reached by repeatedly moving one row down and one column right.

The current cell must not belong to either set. The exact implementation performs two separate walks from every cell and uses a fresh set for each direction.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[1, 2, 3], [3, 1, 5], [3, 2, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Initialize the answer matrix

`ans` is an $m$ by $n$ matrix filled with zeros.

Each input cell has exactly one corresponding output cell, and the nested loops visit all row-column pairs.

The input `grid` is never overwritten, so later diagonal walks always read original values.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `ans` is an $m$ by $n$ matrix filled with zeros.

Each input... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Walk toward the top-left

Coordinates `x, y` begin at `i, j`.

Loop condition `while x and y` is true exactly while both coordinates are nonzero. Inside the loop, the code first moves:

`x, y = x - 1, y - 1`,

then adds `grid[x][y]` to set `s`.

Moving before adding excludes the current cell. The final iteration can add a boundary cell in row zero or column zero; the next condition then stops.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 1, 0], [1, 0, 1], [0, 1, 1]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[1, 2, 3], [3, 1, 5], [3, 2, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 1, 0], [1, 0, 1], [0, 1, 1]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Two sweeps per diagonal:** Store distinct pref:** - **Two sweeps per diagonal:** Store distinct prefix and suffix counts to achieve the manifest's $O(mn)$ time.
- **Frequency maps while sliding:** Can update distinct counts along a diagonal but requires careful removal bookkeeping.
- **Single cell:** Both sides are empty, so the result is zero.
- **Top row or left column:** The top-left side is empty.
- **Bottom row or right column:** The bottom-right side is empty.
- **Repeated values:** A set counts them once per side.
- **Same value on both sides:** Each side still counts it independently.
- **Rectangular matrix:** Coordinate checks handle different row and column counts.
- **Current value:** Excluded because each loop moves before insertion.
- **Input preservation:** Only `ans` and temporary sets are modified.
- **Manifest mismatch:** Linear diagonal sweeps are an alternative, not the behavior of the exact source.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mnd)$. Let $d=\min(m,n)$ be the maximum diagonal length. There are $mn$ cells, and each performs two walks of at most $d-1$ steps. Total time is $O(mnd)$, not the manifest's $O(mn)$ sweep bound.
- **Auxiliary Space Complexity:** $O(d)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
