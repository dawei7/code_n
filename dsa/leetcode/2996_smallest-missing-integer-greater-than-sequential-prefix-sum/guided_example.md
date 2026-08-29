# Guided Example: Smallest Missing Integer Greater Than Sequential Prefix Sum

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 2, 5]}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** array of integers `nums`.

The objective is to compute `6` from `{"nums": [1, 2, 3, 2, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The task has two independent phases

First find the sum of the longest sequential prefix. Then, starting from that sum, find the first integer absent from the entire array. Mixing these ideas can cause a common mistake: the sequential condition applies only while discovering the prefix, whereas the missing-value condition checks all positions in `nums`.

The prefix always contains `nums[0]`, even when the second value fails immediately. The code therefore initializes `s = nums[0]` and `j = 1`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 2, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Extend the prefix only while the exact rule holds

The loop condition is:

`nums[j] == nums[j - 1] + 1`.

This requires consecutive values increasing by exactly one. Merely being increasing is not enough, and a repeated or smaller value also ends the prefix.

Whenever the condition holds, `nums[j]` is added to `s` and `j` advances. The first failure ends the longest sequential prefix permanently. Even if a later part of the array becomes sequential again, it cannot belong to a prefix because a prefix must start at index zero and contain every preceding position.

For `[3,4,5,1,12,14,13]`, the loop includes three, four, and five, making `s = 12`. It stops at one because one is not six. Values after that point do not affect the prefix sum.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Build a membership set for the whole array

The code creates `vis = set(nums)`. Duplicates are irrelevant to the next question: an integer is either present at least once or missing. A set gives expected constant-time membership tests.

Notice that `vis` includes elements after the sequential prefix. In the example, 12, 13, and 14 all appear outside the prefix and must be skipped even though the prefix sum is 12.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 2, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Linear membership scans:** Testing each candidate with `x in nums` can repeat an $O(N)$ scan and become quadratic when many consecutive candidates are present.
- **Sort a copy:** It can find the missing value after prefix computation but costs $O(N\log N)$ time and $O(N)$ copy space.
- **Continue after a prefix break:** This would form a subsequence or later run, not the longest prefix required by the definition.
- **One-element array:** Its sole value is the sequential-prefix sum; return it if absent is impossible because it is present, so the search advances to the next missing integer.
- **Duplicate values:** They occupy one set entry and do not change presence.
- **Prefix sum already missing:** It is returned immediately.
- **Values after the prefix:** They still matter to missingness and are included in `vis`.
- **Infinite iterator safety:** Finiteness of `vis` guarantees termination even though `count` itself has no endpoint.
- **Input preservation:** Neither the scan nor set construction modifies `nums`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the array length and $U$ the number of distinct values. The prefix scan visits at most $N$ positions. Building `vis` visits all $N$ elements.
- **Auxiliary Space Complexity:** $O(U)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
