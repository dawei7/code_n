# Guided Example: Minimum Adjacent Swaps to Make a Valid Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 4, 5, 5, 3, 1]}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums`.

The objective is to compute `6` from `{"nums": [3, 4, 5, 5, 3, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Choose the occurrences that are already closest to their required ends

Only one occurrence of the global minimum must reach index zero, and only one occurrence of the global maximum must reach index `n - 1`. When a value occurs several times, the best minimum candidate is its leftmost occurrence because it needs the fewest leftward adjacent swaps. The best maximum candidate is its rightmost occurrence because it needs the fewest rightward swaps.

The scan stores these indices as `i` and `j`:

- `i` becomes the index of the leftmost minimum;
- `j` becomes the index of the rightmost maximum.

Both start at zero, then every element is compared with the value at the currently selected index.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 4, 5, 5, 3, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the minimum comparison keeps the leftmost copy

When `v < nums[i]`, the scan has found a genuinely smaller value and updates `i = k`. When values are equal, the code contains the additional condition `k < i`.

Because `k` advances from left to right, a later equal occurrence normally cannot have `k < i`, so the first occurrence of the current minimum remains selected. The explicit tie condition states the intended rule even though the traversal order already enforces it.

Moving this selected minimum to index zero costs exactly `i` adjacent swaps: it must cross each of the `i` elements before it once.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the maximum comparison keeps the rightmost copy

The condition `v >= nums[j]` updates `j` for both a larger value and an equal maximum. Consequently, every later occurrence of the current maximum replaces the earlier one. The extra equal-and-later clause is redundant after `>=`, but it reinforces the rightmost intention.

Moving the selected maximum from index `j` to the final index costs `n - 1 - j` swaps before accounting for interaction with the minimum move.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 4, 5, 5, 3, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Use built-in minimum and maximum plus index searches:** Find the minimum and maximum values, then locate the first minimum and last maximum. This is correct but makes several linear passes instead of one.
- **Simulate adjacent swaps:** Moving the chosen elements step by step takes `O(n)` operations and mutates data merely to obtain a count that endpoint distances already provide.
- **Choose the rightmost minimum:** It requires at least as many swaps to reach the left edge and can be strictly worse.
- **Choose the leftmost maximum:** It requires at least as many swaps to reach the right edge and can be strictly worse.
- **Forget the crossing correction:** When `i > j`, one swap advances both selected elements toward their endpoints, so the raw sum overcounts by one.
- **Subtract for `i < j`:** Their routes do not cross in that order, so subtracting would undercount.
- **One element:** It is simultaneously smallest, largest, leftmost, and rightmost; zero swaps are needed.
- **All values equal:** The first and last elements already provide valid endpoint occurrences, so the result is zero.
- **Minimum already first:** Its distance contribution is zero.
- **Maximum already last:** Its distance contribution is zero.
- **Maximum immediately before minimum:** Their single mutual swap is exactly the shared crossing represented by the subtraction.
- **Multiple minima and maxima:** The scan's tie behavior selects the endpoint-nearest copies.
- **Minimum equals maximum:** This means all values are equal, handled naturally.
- **Input preservation:** The method only reads `nums` and returns a count.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the array length. The single loop examines each element once and performs constant-time comparisons and assignments, so running time is `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
