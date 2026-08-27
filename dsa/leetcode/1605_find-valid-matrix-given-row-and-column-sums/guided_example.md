# Guided Example: Find Valid Matrix Given Row and Column Sums

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"rowSum": [3, 8], "colSum": [4, 7]}`
- **Required output:** `[[3, 0], [1, 7]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two arrays `rowSum` and `colSum` of non-negative integers where $\text{rowSum}[i]$ is the sum of the elements in the $$i^{\text{th}}$$ row and $\text{colSum}[j]$ is the sum of the elements of the $$j^{\text{th}}$$ column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

The objective is to compute `[[3, 0], [1, 7]]` from `{"rowSum": [3, 8], "colSum": [4, 7]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat the inputs as remaining sums

The source constructs an $M\times N$ zero matrix `ans`. During filling, `rowSum[i]` and `colSum[j]` no longer represent untouched original requirements; they represent how much total still needs to be placed in that row and column.

At cell `(i,j)`, the largest non-negative value that does not exceed either remaining requirement is:

`x = min(rowSum[i], colSum[j])`.

The code stores `x` in the cell, then subtracts it from both remaining sums.

This is the northwest-corner greedy rule for a transportation table. The source visits every matrix coordinate in row-major order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"rowSum": [3, 8], "colSum": [4, 7]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why taking the minimum is always safe

Any cell value must be no larger than the row’s remaining sum and no larger than the column’s remaining sum. Choosing their minimum satisfies both constraints and makes at least one of them zero:

- if the row remainder is smaller, the current row is completed;
- if the column remainder is smaller, the current column is completed;
- if they are equal, both are completed.

All input sums and all remainders are non-negative, so every assigned `x` is non-negative.

The algorithm does not need to reserve capacity through lookahead. Total row demand equals total column demand. If a row consumes the available amount in one column, that amount had to be assigned somewhere in that column; if a column is exhausted, later rows simply place zero there and use remaining columns.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Any cell value must be no larger than the row’s remaining su... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How the nested loops behave

The outer loop fixes a row `i`, and the inner loop visits every column `j`.

If a prior cell exhausts the current row, `rowSum[i]` becomes zero. Every later cell in that row receives `min(0, colSum[j]) = 0`.

If earlier rows exhaust a column, `colSum[j]` is zero. Later rows place zero in that column.

The source does not skip these completed rows or columns, so it performs all $MN$ cell iterations. A pointer-optimized variant could jump after one side reaches zero, but the returned matrix initialization itself is already $O(MN)$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[3, 0], [1, 7]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"rowSum": [3, 8], "colSum": [4, 7]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[3, 0], [1, 7]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Pointer-optimized northwest-corner traversal:*:** - **Pointer-optimized northwest-corner traversal:** Advance the row when its remainder reaches zero, otherwise advance the column. It fills only $O(M+N)$ potentially nonzero positions, though allocating the dense output still costs $O(MN)$.
- **Separate current row and column totals:** This avoids mutating inputs but adds $O(M+N)$ auxiliary arrays.
- **Network flow:** The problem can be modeled as transportation flow, but equal totals and unrestricted non-negative cells make the greedy construction sufficient.
- **Try to reconstruct a unique original matrix:** No unique original is promised or required; any valid margins are accepted.
- **Zero-sum row:** Every cell in it becomes zero.
- **Zero-sum column:** Every row places zero in that column.
- **One row:** Each cell receives the remaining column sum, and the equal-total guarantee completes the row.
- **One column:** Each row’s required sum is placed in its only cell.
- **Equal row and column remainder:** The chosen value exhausts both simultaneously.
- **Large sums:** Python integers handle values through $10^8$ and their totals without overflow.
- **Non-negativity:** Taking the minimum of non-negative remainders and never overspending keeps every cell and remainder non-negative.
- **Input mutation:** Both requirement lists are consumed to zeros; pass copies when preservation matters.
- **Guaranteed equal totals:** The proof relies on `sum(rowSum) == sum(colSum)`. Without it, no valid completion may exist.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(MN)$. Let $M$ be the number of rows and $N$ the number of columns.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
