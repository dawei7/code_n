# Guided Example: Largest Magic Square

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[7, 1, 4, 5, 6], [2, 5, 1, 6, 4], [1, 5, 4, 3, 2], [1, 2, 7, 3, 4]]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A `k x k` **magic square** is a `k x k` grid filled with integers such that every row sum, every column sum, and both diagonal sums are **all equal**. The integers in the magic square **do not have to be distinct**. Every `1 x 1` grid is trivially a **magic square**.

The objective is to compute `3` from `{"grid": [[7, 1, 4, 5, 6], [2, 5, 1, 6, 4], [1, 5, 4, 3, 2], [1, 2, 7, 3, 4]]}` while avoiding redundant calculations and unnecessary overhead.

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

**Search sizes from largest to smallest.** A candidate square is determined by its side length and top-left corner. The outer loop tries `k = min(m, n)` down through two. As soon as any square of a size passes, that size is returned; no smaller size can improve the answer. If none passes, the method returns one because every single cell is trivially a magic square.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[7, 1, 4, 5, 6], [2, 5, 1, 6, 4], [1, 5, 4, 3, 2], [1, 2, 7, 3, 4]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Precompute row and column prefix sums.** `rowsum[i][j]` uses one-based storage and equals the sum of grid row `i - 1` across the first `j` columns. Its recurrence extends leftward prefix `rowsum[i][j - 1]`. Similarly, `colsum[i][j]` equals the sum of grid column `j - 1` across the first `i` rows and extends `colsum[i - 1][j]`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Both arrays have `(m + 1)` rows and `(n + 1)` columns filled initially with zero. Padding lets a segment beginning at grid index zero subtract a valid zero prefix rather than requiring a boundary branch.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[7, 1, 4, 5, 6], [2, 5, 1, 6, 4], [1, 5, 4, 3, 2], [1, 2, 7, 3, 4]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Diagonal prefix sums:** Two additional diagonal-prefix tables can make each diagonal sum $O(1)$, but checking all $k$ rows and columns still costs $O(k)$ per candidate, so the overall asymptotic bound remains unchanged.
- **Brute-force all cells per candidate:** Recomputing each line from scratch costs $O(k^2)$ per square and raises the total bound substantially.
- **Check only total row and column sums:** Equal totals across the whole square do not prove each individual row and column is equal. Every line must be tested.
- **Single row or column grid:** No side length above one is enumerated, and the method returns one.
- **One-by-one squares:** They are not passed to `check` because they are always magic; the final return handles them.
- **Repeated values:** Allowed by the definition. The algorithm compares sums only and never imposes uniqueness.
- **Rectangular grid:** Candidate side is bounded by `min(m, n)`, and placement loops independently respect both dimensions.
- **Early mismatch:** The helper returns as soon as a row, column, or diagonal differs. This is safe because one failed required equality disproves the candidate.
- **Prefix off-by-one:** Stored coordinates are shifted by one, while helper corners are zero-based and inclusive. The `+1` endpoints and unshifted subtraction boundaries are essential.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(MNS^2)$. Let $S=\min(m,n)$. Prefix construction costs $O(mn)$ time and space. For side length $k$, there are at most $O(mn)$ placements, and checking one placement takes $O(k)$ time in the worst case for rows, columns, and diagonals. Summing over all sizes gives
- **Auxiliary Space Complexity:** $O(mn)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
