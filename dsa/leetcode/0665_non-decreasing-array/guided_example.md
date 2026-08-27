# Guided Example: Non-decreasing Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [4, 2, 3]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array `nums` with `n` integers, your task is to check if it could become non-decreasing by modifying **at most one element**.

The objective is to compute `true` from `{"nums": [4, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Find the first place where order fails

An array is non-decreasing when every adjacent pair satisfies `nums[i] <= nums[i + 1]`. The outer loop scans from left to right until it finds the first inversion:

`a = nums[i] > nums[i + 1] = b`.

If no inversion exists, the array is already valid and using zero modifications satisfies “at most one,” so the method returns `true`.

Once the first inversion is found, any successful one-element repair must change one of its two elements. Changing any unrelated position would leave `a > b` untouched. The exact solution therefore tests the two meaningful repair directions and then returns immediately.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [4, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The helper verifies the entire array

`is_sorted(nums)` uses `pairwise` to generate every adjacent pair and `all` to verify `a <= b` for all of them.

The helper short-circuits at the first failed comparison. It allocates no list of pairs; `pairwise` and the generator expression produce values lazily.

Checking the entire array after a candidate modification is simple and robust. It automatically catches:

- a new inversion created with the element before the changed position;
- a new inversion created with the element after it;
- a separate original inversion farther to the right.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `is_sorted(nums)` uses `pairwise` to generate every adjacent... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: First candidate: lower the left value

For inversion `a > b`, changing the left element requires its new value to be at most `b`. The code chooses the canonical value `b`:

`nums[i] = b`.

Why is testing exactly `b` enough? It is the largest value that fixes the current pair. A larger choice would not fix `a > b`. A smaller choice would only make it harder to remain at least as large as the previous neighbor. Therefore:

- if setting the left element to `b` preserves global order, a valid repair exists;
- if it violates the previous boundary, no still-smaller value could repair that boundary.

The helper checks the complete array. If sorted, return `true` immediately.

For `[4, 2, 3]`, lowering four to two gives `[2, 2, 3]`, which is non-decreasing.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [4, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Single-pass greedy repair:** At the first inve:** - **Single-pass greedy repair:** At the first inversion, inspect the previous neighbor to decide immediately whether to lower the left value or raise the right, then continue scanning for a second inversion. This avoids full rescans while retaining `O(N)` time and `O(1)` space.
- **- **Try modifications on a copy:** Preserves the c:** - **Try modifications on a copy:** Preserves the caller's input but uses `O(N)` additional space.
- **- **Count inversions only:** This is insufficient :** - **Count inversions only:** This is insufficient because repairing one inversion can create another with an adjacent element, as in `[3, 4, 2, 3]`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N` be the array length.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
