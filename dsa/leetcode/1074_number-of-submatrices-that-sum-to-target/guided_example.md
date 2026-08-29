# Guided Example: Number of Submatrices That Sum to Target

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"matrix": [[0, 1, 0], [1, 1, 1], [0, 1, 0]], "target": 0}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a `matrix` and a `target`, return the number of non-empty submatrices that sum to target.

The objective is to compute `4` from `{"matrix": [[0, 1, 0], [1, 1, 1], [0, 1, 0]], "target": 0}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Fix two row boundaries to reduce the matrix to one dimension

A submatrix is determined by top, bottom, left, and right boundaries. The solution enumerates every top and bottom row pair. Once those two boundaries are fixed, it compresses all included rows into one array of column sums.

If `col[k]` is the sum of matrix cells in column `k` between the fixed top and bottom rows, then the sum of a submatrix spanning columns `left` through `right` equals the sum of the one-dimensional subarray `col[left:right + 1]`.

The two-dimensional counting problem for one row band therefore becomes the familiar problem of counting one-dimensional subarrays with sum `target`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"matrix": [[0, 1, 0], [1, 1, 1], [0, 1, 0]], "target": 0}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count target-sum subarrays with prefix frequencies

The helper `f(nums)` begins:



`s` is the running prefix sum through the current position. `d[value]` records how many earlier prefixes had that value. `cnt` accumulates matching subarrays.

The artificial empty prefix has sum zero and occurs once. Initializing `d[0] = 1` allows a subarray starting at index zero to be counted. If the current prefix sum itself equals `target`, then `s - target` is zero and that empty prefix supplies one match.

For each value:



Suppose an earlier prefix sum was `p`. The sum after that prefix through the current index is `s - p`. This subarray equals `target` exactly when:



Every previous occurrence of `s - target` gives a different starting boundary, so the helper adds its frequency.

Only after counting does it record the current prefix. This order ensures a nonempty subarray: the current prefix cannot pair with itself.

Negative numbers cause no difficulty. Prefix sums need not be monotonic because the hash map finds exact differences rather than relying on a sliding window.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Build each compressed row band incrementally

The outer loops are:



`i` is the top row. `j` advances from that top through every possible bottom row.

For a new top row, `col` starts at zeros. When bottom `j` is included:



adds that entire row to the compressed column sums.

After the update, `col[k]` equals:



The code reuses the previous band rather than recomputing all rows from `i` through `j`. Extending the bottom boundary costs only one pass over columns.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"matrix": [[0, 1, 0], [1, 1, 1], [0, 1, 0]], "target": 0}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Choose the smaller paired dimension:** Transpose or branch so the squared dimension is `min(R, C)`. This guarantees the manifest's `O(S^2L)` time and `O(L)` space.
- **Two-dimensional prefix sums plus four boundaries:** Constant-time rectangle queries still leave `O(R^2C^2)` boundary combinations, much slower than the reduction.
- **Column-pair compression:** Fix left and right columns, compress row sums, and run the same prefix-map helper. It is symmetric and preferable when columns are fewer.
- **Target zero:** The initial zero-prefix frequency correctly counts zero-sum intervals, including those created by cancellations.
- **Negative cells:** A two-pointer window would fail because sums can decrease. Prefix differences remain correct.
- **One cell:** The single row band and single column interval contribute one exactly when the cell equals target.
- **One row:** The algorithm reduces directly to one call of the one-dimensional subarray-sum method.
- **One column:** Every row band produces one compressed value, counting all vertical submatrices with the target sum.
- **Repeated prefix sums:** Frequencies, not just set membership, are necessary because each occurrence creates a different starting boundary.
- **Empty prefix:** `d[0] = 1` counts intervals beginning at column zero; it does not represent an empty returned submatrix.
- **Nonempty submatrices:** Recording the current prefix after the lookup prevents pairing a prefix with itself.
- **Large count:** Python integers avoid overflow when many boundary combinations match.
- **Input preservation:** Compression accumulates into `col` and never modifies `matrix`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R^2C)$. Let `R` be the number of rows and `C` the number of columns.
- **Auxiliary Space Complexity:** $O(C)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
