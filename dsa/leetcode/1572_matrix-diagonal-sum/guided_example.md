# Guided Example: Matrix Diagonal Sum

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"mat": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}`
- **Required output:** `25`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a square matrix `mat`, return the sum of the matrix diagonals.

The objective is to compute `25` from `{"mat": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Identify both diagonal coordinates from one row index

In an $N$-by-$N$ square matrix, the primary diagonal uses coordinates:

`(i, i)`.

The secondary diagonal uses:

`(i, N - i - 1)`.

The source visits each row once with `enumerate(mat)`. Variable `i` is the row index and `row` is that row's list.

It computes `j = n - i - 1`, the secondary-diagonal column for the same row.

Thus one iteration can add every diagonal contribution belonging to row `i` without scanning any off-diagonal cell.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"mat": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Always include the primary diagonal

`row[i]` is the primary-diagonal entry for the current row. It is always added.

As `i` runs from zero through `n-1`, these positions move from the top-left corner to the bottom-right corner. Every primary entry appears exactly once.

No matrix-value condition is involved; membership is determined solely by coordinates.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `row[i]` is the primary-diagonal entry for the current row.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Include the secondary entry unless it is the same cell

`row[j]` is the secondary-diagonal entry. Usually `j != i`, so the source adds it as well.

For an odd-sized matrix, both diagonals meet at the center. At the center row:

$$
i=n-i-1.
$$

That single cell belongs to both diagonal descriptions but must be counted once.

The expression `0 if j == i else row[j]` contributes zero instead of adding the secondary entry again at the intersection.

For an even-sized matrix, no integer row satisfies the equality, so every row contributes two different cells.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `25` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"mat": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `25` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Add both then subtract center:** Sum `mat[i][i:** - **Add both then subtract center:** Sum `mat[i][i]` and `mat[i][n-i-1]` for all rows, then subtract the center for odd `n`. It is equivalent.
- **Scan every cell:** Check whether `i == j` or `i+j == n-1`, but this costs $O(N^2)$.
- **Build diagonal arrays:** It adds unnecessary $O(N)$ storage.
- **Odd dimension:** Exactly one center cell lies on both diagonals.
- **Even dimension:** The diagonals share no cell.
- **One-by-one matrix:** The single value is counted once.
- **Equal values at different cells:** They are separate coordinates and must both be counted.
- **Secondary formula:** The column decreases from `n-1` to zero as the row increases.
- **Positive-value constraint:** It is not required for the indexing logic; the same method would sum negative values correctly.
- **Square guarantee:** It makes primary and secondary diagonal lengths both equal to `N`.
- **No mutation:** Matrix values and row structure remain unchanged.
- **Overlap test:** Comparing coordinates, not values, is the correct way to prevent double counting.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be matrix dimension. The loop runs exactly $N$ times and performs constant indexing and arithmetic per row. Time is $O(N)$, matching the manifest.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
