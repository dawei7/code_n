# Guided Example: Longest Continuous Increasing Subsequence

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 3, 5, 4, 7]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an unsorted array of integers `nums`, return *the length of the longest **continuous increasing subsequence** (i.e. subarray)*. The subsequence must be **strictly** increasing.

The objective is to compute `3` from `{"nums": [1, 3, 5, 4, 7]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Continuity reduces the state to the current run

Because the requested sequence must be a contiguous subarray, the only way to extend an increasing run ending at one position is to include the immediately next element.

There is no need to compare against every earlier index as in the general longest increasing subsequence problem. One adjacent comparison tells us whether the current run continues or a new run begins.

The exact solution maintains:

- `cnt`: the length of the strictly increasing contiguous run ending at the current processed element;
- `ans`: the largest such length seen anywhere so far.

Both begin at one because the input is nonempty and any single element is an increasing subarray of length one.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 3, 5, 4, 7]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Understand the shifted enumeration

The loop is:

`for i, x in enumerate(nums[1:])`.

The slice begins with original index one. Therefore:

- loop `i = 0` has `x = nums[1]` and compares it with `nums[0]`;
- loop `i = 1` has `x = nums[2]` and compares it with `nums[1]`;
- in general, `x = nums[i + 1]` while `nums[i]` is its immediate predecessor.

This offset is easy to misread. The comparison `nums[i] < x` is exactly the adjacent original-array comparison.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Extend on a strict increase

If `nums[i] < x`, the new value is strictly greater than the previous one. Appending it preserves the current continuous increasing run, so increment `cnt`.

The new run length may be the largest seen, so update:

`ans = max(ans, cnt)`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 3, 5, 4, 7]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Index loop without slicing:** Iterate `for i in range(1, len(nums))` and compare `nums[i - 1] < nums[i]`. This retains `O(N)` time and achieves literal `O(1)` extra space.
- **Anchor-based sliding window:** Store the start index of the current increasing run and reset it after every failed comparison. Compute each length from indices.
- **Dynamic-programming array:** Store the increasing-run length ending at every index. It is correct but wastes `O(N)` space because only the previous length is needed.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N` be the array length.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
