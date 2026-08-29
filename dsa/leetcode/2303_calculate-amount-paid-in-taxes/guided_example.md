# Guided Example: Calculate Amount Paid in Taxes

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"brackets": [[3, 50], [7, 10], [12, 25]], "income": 10}`
- **Required output:** `2.65`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** 2D integer array `brackets` where $\text{brackets}[i] = [\text{upper}_{i}, \text{percent}_{i}]$ means that the $i^{\text{th}}$ tax bracket has an upper bound of $\text{upper}_{i}$ and is taxed at a rate of $\text{percent}_{i}$. The brackets are **sorted** by upper bound (i.e. $\text{upper}_{i}-1 < \text{upper}_{i}$ for `0 < i < brackets.length`).

The objective is to compute `2.65` from `{"brackets": [[3, 50], [7, 10], [12, 25]], "income": 10}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Tax only the slice belonging to each bracket

Tax brackets are progressive. The rate for one bracket applies only to income above the preceding upper bound and at or below the current upper bound.

`prev` stores the previous bracket's upper bound, beginning at zero. For current `upper`, the nominal bracket width is `upper-prev`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"brackets": [[3, 50], [7, 10], [12, 25]], "income": 10}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Cap the taxable endpoint at income

`min(income,upper)` is the highest earned dollar boundary that lies in this bracket or below. Subtracting `prev` gives the amount of income inside the current interval when income has reached it.

If income is already below `prev`, the subtraction is negative. `max(0,...)` clamps it to zero. The exact taxable width is therefore

`max(0,min(income,upper)-prev)`.

This one expression handles full, partial, and untouched brackets.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Accumulate percentage numerators

The code multiplies taxable dollars by the integer `percent` and adds the product to `ans`. At this stage, `ans` is measured in dollar-percent units, one hundred times the monetary tax.

Only after every bracket does the method return `ans/100`, converting the accumulated percentage numerator into the requested monetary value.

Delaying division avoids repeated floating operations inside the loop.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2.65` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"brackets": [[3, 50], [7, 10], [12, 25]], "income": 10}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2.65` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Break after reaching income:** Once `upper>=income`, later brackets contribute zero; an early return can reduce practical work.
- **Divide per bracket:** It is mathematically equivalent but introduces more floating-point operations.
- **Apply one marginal rate to all income:** That is not progressive taxation and overtaxes lower slices.
- **Zero income:** Every taxable width is zero.
- **Zero-percent bracket:** Its slice is processed but contributes zero.
- **Income exactly at an upper bound:** That bracket is fully taxed and the next has zero width.
- **Income inside a bracket:** `min` includes only the partial slice.
- **Income beyond several brackets:** Earlier bracket widths are fully included.
- **Last bracket guarantee:** It ensures all income is covered by the schedule.
- **Strictly increasing bounds:** They make every nominal width positive and prevent overlap.
- **Rates up to 100:** Multiplication remains direct; 100 percent taxes the full slice amount.
- **Input preservation:** Bracket rows are read in their supplied sorted order.
- **First bracket:** `prev=0` makes its taxable width begin at the first earned dollar boundary without a special case.
- **Later zero contributions:** Updating `prev` even after income is exhausted is harmless because `max(0,...)` continues to return zero.
- **Integer numerator:** Before the final division, `ans` is exact integer arithmetic, so no rounding accumulates between brackets.
- **Accepted tolerance:** Returning a float after one division satisfies the problem's numerical-output contract.
- **Income equals zero:** The loop may still visit every bracket, but it never creates a positive taxable slice.
- **Partial first bracket:** `min(income,upper)` taxes only the earned amount rather than the entire first upper bound.
- **No deductions or credits:** The source model contains only progressive slices; no other adjustment belongs in the computation.
- **Unsorted extension:** The formula assumes the guaranteed increasing bounds; arbitrary order could make `prev` invalid.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(b)$. Let `b` be the number of brackets. The exact method visits all `b` rows and performs constant arithmetic for each, so time is `O(b)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
