# Guided Example: Set Matrix Zeroes

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"matrix": [[1, 1, 1], [1, 0, 1], [1, 1, 1]]}`
- **Required output:** `[[1, 0, 1], [0, 0, 0], [1, 0, 1]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.

The objective is to compute `[[1, 0, 1], [0, 0, 0], [1, 0, 1]]` from `{"matrix": [[1, 1, 1], [1, 0, 1], [1, 1, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Record causes before changing any cells

The required zeroes are determined by cells that were zero in the original matrix. This word “original” is the central difficulty. If the algorithm finds a zero and immediately clears its row and column, those newly written zeroes are indistinguishable from original zeroes during the rest of the scan. They can trigger additional rows and columns and incorrectly spread zeroes through the matrix.

The source prevents that cascade by separating discovery from mutation. The first complete pass only records which row indices and column indices contain an original zero. The second complete pass uses those frozen records to write the final values. Because no matrix cell changes during discovery, every cause recorded by the first pass is genuine.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"matrix": [[1, 1, 1], [1, 0, 1], [1, 1, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use one Boolean marker per row and column

`row[i]` means that original row `i` contained at least one zero and must be cleared. `col[j]` means the same for original column `j`. Both arrays begin entirely false because no original cell has yet been inspected.

When the first pass finds `matrix[i][j] == 0`, the chained assignment `row[i] = col[j] = true` marks both affected dimensions. Python evaluates this as assigning the same Boolean value to each target. It does not connect the two array entries; they remain ordinary independent Boolean slots.

One original zero can mark a row and a column that were already marked by another zero. Reassigning `true` is harmless. This idempotence is useful because the algorithm needs only existence information, not the number of zeroes in each dimension.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `row[i]` means that original row `i` contained at least one ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Interpret the first-pass invariant

After the first pass has inspected some prefix of cells in row-major order, `row[i]` is true exactly when an inspected original zero belongs to row `i`, and `col[j]` is true exactly when an inspected original zero belongs to column `j`.

The invariant is initially true because the inspected set is empty and all markers are false. Inspecting a nonzero cell changes nothing, so the statement remains true. Inspecting a zero sets exactly its row and column markers, adding precisely the two facts caused by that cell. After all cells are inspected, the arrays exactly describe every row and column that the specification says to clear.

For the matrix `[[1,1,1],[1,0,1],[1,1,1]]`, discovery produces `row = [false, true, false]` and `col = [false, true, false]`. The marker arrays contain the complete effect of the central zero without altering any neighboring value yet.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 0, 1], [0, 0, 0], [1, 0, 1]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"matrix": [[1, 1, 1], [1, 0, 1], [1, 1, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 0, 1], [0, 0, 0], [1, 0, 1]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **First row and first column as markers:** Store:** - **First row and first column as markers:** Store dimension flags inside the matrix and keep separate Booleans for whether the original first row and column contained zeroes. This achieves $O(1)$ auxiliary space.
- **Sets of affected indices:** Record only rows and columns actually seen with zeroes. It still uses up to $O(m+n)$ space and has hashing overhead, but can be convenient in sparse cases.
- **Full copied matrix:** Read from an untouched copy while writing the original. It is straightforward but uses $O(mn)$ extra space.
- **Immediate zeroing:** Clearing a row and column during discovery is incorrect because written zeroes can trigger unrelated dimensions later.
- **No original zeroes:** Every marker remains false, so the matrix is unchanged.
- **All zeroes:** Every marker becomes true and the second pass keeps every cell zero.
- **One row:** The row marker clears the entire row if any element is zero; otherwise only marked columns would matter, with the same final outcome.
- **One column:** The column marker clears it if any element is zero.
- **Zero at a corner:** Its full row and full column are both marked like any interior zero.
- **Several zeroes in one row:** The row is marked once, while every corresponding column is marked independently.
- **Negative and large values:** Only equality with integer zero matters; other values are preserved unless their row or column is affected.
- **Rectangular shape:** Separate `m` and `n` marker lengths support non-square matrices.
- **Return behavior:** Mutation is the result, and the implicit return value is `null`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. Let $m$ be the number of rows and $n$ the number of columns. Each of the two nested passes visits all $mn$ cells and performs constant work per cell, so total time is $O(mn)$, matching the manifest's time declaration.
- **Auxiliary Space Complexity:** $O(m+n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
