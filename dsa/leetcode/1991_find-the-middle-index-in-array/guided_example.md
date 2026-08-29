# Guided Example: Find the Middle Index in Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 3, -1, 8, 4]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a **0-indexed** integer array `nums`, find the **leftmost** `middleIndex` (i.e., the smallest amongst all the possible ones).

The objective is to compute `3` from `{"nums": [2, 3, -1, 8, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Maintain sums strictly outside the current index

For index `i`, the required left sum contains positions before `i`, while the right sum contains positions after `i`. The current value belongs to neither side.

The source maintains exactly these two quantities:

- `l` is the sum strictly left of the current index;
- after one subtraction, `r` is the sum strictly right of the current index.

It initializes `l = 0` because nothing lies before index zero. It initializes `r = sum(nums)`, which initially includes every value.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 3, -1, 8, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Remove the current value before comparing

At each loop iteration, `r -= x` removes `nums[i]` from the remaining total. Before this line, `r` contains the current value and everything to its right. After it, `r` contains only elements after `i`.

`l` has not yet been updated for the current iteration, so it still contains only positions before `i`. The test `if l == r` therefore checks the middle-index definition exactly.

Only after a failed comparison does `l += x` move the current value into the left sum for the next index.

Changing this order is a common bug. Adding to `l` before comparing or subtracting from `r` after comparing would include the candidate value on one side and test the wrong equation.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Trace the first example

For `[2, 3, -1, 8, 4]`, the total is 16.

At index zero, remove two from `r`, leaving 14; `l` is zero, so the index fails. Then add two left.

At index one, remove three, leaving 11; left is two, so it fails. Add three to make left five.

At index two, removing -1 increases `r` from 11 to 12; left is five, so it fails. Adding -1 changes left to four.

At index three, remove eight, leaving right sum four. Left is also four, so index three is returned.

This trace also shows why negative values cause no problem. Subtracting a negative correctly increases the remaining right sum.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 3, -1, 8, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Prefix-sum array:** Allows direct left/right queries but uses $O(N)$ extra space that the rolling sums avoid.
- **Recompute both sides for every index:** Straightforward but takes $O(N^2)$ time and Python slicing may allocate extra memory.
- **Equation with total and left only:** Check `2 * left + nums[i] == total`; it is equivalent and also uses constant space.
- **Valid index zero:** Detected when the remaining total after removing the first value is zero.
- **Valid last index:** Detected when the accumulated left sum is zero after the last value is removed from the right.
- **Single-element array:** Both sides are empty, so index zero is returned.
- **Negative values:** Fully supported; sums need not change monotonically.
- **Several valid indices:** Increasing traversal and immediate return select the leftmost.
- **No valid index:** The final result is -1.
- **Total sum zero:** It does not automatically make every index valid; the current value and left sum still matter.
- **Update order:** Subtract current from right, compare, then add current to left.
- **Input preservation:** The method reads values without changing `nums`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the array length. `sum(nums)` takes $O(N)$ time, and the loop takes another $O(N)$ time. Total time is $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
