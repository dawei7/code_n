# Guided Example: Number of Zero-Filled Subarrays

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 3, 0, 0, 2, 0, 0, 4]}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, return *the number of **subarrays** filled with *`0`.

The objective is to compute `6` from `{"nums": [1, 3, 0, 0, 2, 0, 0, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count subarrays by where they end

Every nonempty subarray has one unique ending index. Instead of generating all possible start-end pairs, the algorithm asks a smaller question at each position:

> How many zero-filled subarrays end at the current element?

If the current value is nonzero, the answer is zero. If it is zero and belongs to a consecutive run of `cnt` zeros ending here, then there are exactly `cnt` valid ending subarrays—one starting at each position in that run.

The solution maintains this run length and adds it to the total.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 3, 0, 0, 2, 0, 0, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Extend the current zero run

`cnt` starts at zero. When current `x == 0`, the code increments `cnt`.

Suppose the previous position ended a run of `r` zeros. There were `r` zero-filled subarrays ending there. Appending the new zero extends each of those `r` subarrays and also creates the single-element subarray containing only the new zero. The new ending count is therefore `r + 1`, exactly the updated `cnt`.

The method immediately adds `cnt` to `ans`, recording every zero-filled subarray whose unique final index is the current position.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Reset after a nonzero value

When `x` is nonzero, no zero-filled subarray can end at it. A contiguous subarray cannot skip this value, so any earlier zero run is separated from future zeros.

The assignment `cnt = 0` clears the ending state. The code does not add anything to `ans` in this branch.

If the next element is zero, its run begins at length one rather than incorrectly continuing across the separator.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 3, 0, 0, 2, 0, 0, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Detect complete runs and use `L(L+1)/2`:** This is equally linear but requires finalizing a run at separators and after the loop. The ending-count method avoids a special final step.
- **Enumerate all subarrays:** There are `O(n^2)` candidates, and checking their contents can add another factor. The run invariant eliminates this work.
- **Prefix sums:** A zero-sum subarray is not necessarily zero-filled when negative values exist, so numeric prefix sums solve a different condition.
- **One zero:** It contributes exactly one subarray.
- **One nonzero:** The answer remains zero.
- **All zeros:** Contributions are 1 through `n`, giving the triangular maximum.
- **No zeros:** `cnt` is repeatedly reset and `ans` stays zero.
- **Separated single zeros:** Each run contributes one; no subarray crosses a nonzero separator.
- **Several long runs:** Their triangular contributions add independently.
- **Negative nonzero values:** They reset the run just like positive values.
- **Zero after a separator:** It begins a new run with `cnt = 1`.
- **Subarray identity:** Equal value sequences at different positions are distinct subarrays and are counted at their distinct endpoints.
- **No empty subarray:** Contributions start at one only when an actual zero is processed.
- **Input preservation:** The scan does not alter `nums`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the array length. The loop visits every value exactly once and performs constant-time comparisons, increments, and assignments. Running time is `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
