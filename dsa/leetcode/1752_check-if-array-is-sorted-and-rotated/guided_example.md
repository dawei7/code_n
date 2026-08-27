# Guided Example: Check if Array Is Sorted and Rotated

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 4, 5, 1, 2]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array `nums`, return `true`* if the array was originally sorted in non-decreasing order, then rotated **some** number of positions (including zero)*. Otherwise, return `false`.

The objective is to compute `true` from `{"nums": [3, 4, 5, 1, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Look at the array as a circle

Rotating an array changes where the linear representation begins, but it does not change the cyclic order of its elements. If a non-decreasing array is placed around a circle, almost every adjacent pair satisfies “previous value is less than or equal to next value.” There can be only one place where a larger value is followed by a smaller value: the wrap from the sorted array's end back to its beginning.

The exact solution counts these strict decreases around the entire cycle and returns true when there is at most one.

Its whole condition is:

`sum(nums[i - 1] > x for i, x in enumerate(nums)) <= 1`.

Although compact, this line contains the complete circular check.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 4, 5, 1, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Understand the generator's adjacent pairs

`enumerate(nums)` produces each current index `i` and value `x = nums[i]`. The expression `nums[i - 1]` accesses the preceding value.

For ordinary indices `i > 0`, this compares `nums[i - 1]` with `nums[i]`. At `i = 0`, Python index minus one refers to the last element, so the comparison is `nums[n - 1] > nums[0]`. That special first iteration supplies the circular pair connecting the end back to the beginning.

Each comparison returns a Boolean. In Python arithmetic, `true` contributes one and `false` contributes zero. Applying `sum` therefore counts how many cyclic adjacent pairs are strict decreases.

No array slice, rotated copy, or explicit counter variable is needed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `enumerate(nums)` produces each current index `i` and value ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the comparison is strict

The original array is sorted in non-decreasing order, not strictly increasing order. Equal adjacent values are valid. Consequently, a break occurs only when the preceding value is greater than the current value.

Using `>=` would incorrectly count equal neighbors as breaks and reject arrays containing duplicates. The strict `>` exactly captures a violation of non-decreasing order.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 4, 5, 1, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Try every rotation:** Construct or inspect all:** - **Try every rotation:** Construct or inspect all $n$ rotations and test each for sorting, which can take $O(n^2)$ time.
- **Compare with a sorted copy:** Sorting costs $O(n\log n)$ and checking rotations can still be quadratic without a string-matching technique.
- **Find a minimum value and scan:** Duplicated minimum values make choosing the correct starting occurrence less direct than counting decreases.
- **Explicit loop counter:** It is equivalent and can return early after a second decrease; the generator version always completes the sum.
- **One element:** Its predecessor through index minus one is itself, so the count is zero.
- **All equal values:** Strict comparison reports no decreases, correctly accepting duplicates.
- **Already sorted array:** The only possible decrease is the circular last-to-first pair, so zero rotation is accepted.
- **Rotation at a duplicate boundary:** Equal values do not create an extra decrease.
- **Two decreases:** No single rotation boundary can eliminate both, so the array is rejected.
- **Strict versus non-decreasing:** The `>` operator is essential; `>=` would be wrong for duplicates.
- **Circular pair:** Omitting `nums[-1] > nums[0]` would accept some invalid arrays with an internal decrease plus a bad wrap.
- **Boolean summation:** Python treats true as one and false as zero, so `sum` is a count.
- **Input preservation:** The method derives a property of the current order without changing `nums`.
- **Value bounds:** The algorithm uses comparisons only, so numeric magnitude does not affect it.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. `enumerate` visits every element once. Each iteration performs one indexed lookup, comparison, and Boolean addition, all constant-time operations. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
