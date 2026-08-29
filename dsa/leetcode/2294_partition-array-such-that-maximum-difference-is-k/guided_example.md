# Guided Example: Partition Array Such That Maximum Difference Is K

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 6, 1, 2, 5], "k": 2}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` and an integer `k`. You may partition `nums` into one or more **subsequences** such that each element in `nums` appears in **exactly** one of the subsequences.

The objective is to compute `2` from `{"nums": [3, 6, 1, 2, 5], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why sorting values does not violate subsequence rules

A subsequence must preserve the original relative order of the elements assigned to it, but the problem does not prescribe which elements belong together. Once a group of array positions has been chosen, reading those positions in original order automatically forms a valid subsequence.

Therefore, group feasibility depends only on the values assigned to each group, specifically its minimum and maximum. Sorting the values is safe for deciding membership even though the final subsequences could be reconstructed in original order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 6, 1, 2, 5], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Start a group at the smallest uncovered value

After `nums.sort()`, the first value not assigned to a previous group is the smallest remaining value. Call it `a`. Any valid group containing `a` may include only values at most `a+k`, because `a` is that group's minimum.

The greedy method includes every following sorted value `b` satisfying `b-a \le k`. Once a value has been placed within this interval, adding it cannot invalidate the group: its maximum remains no more than `a+k`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Start a new group at the first value outside the range

When `b-a>k`, `b` cannot join the current group. Since later sorted values are at least `b`, none of them can join it either.

The code increments `ans` and sets `a=b`. This makes `b` the minimum of the next group and gives that group the widest possible valid reach, through `b+k`.

The nonempty input initializes `ans=1` and `a=nums[0]`. The loop includes the first value, but its difference from itself is zero, so it does not create an extra group.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 6, 1, 2, 5], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Build groups in original order:** Greedy placement by arrival order can waste range capacity because a later small value may change a group's minimum.
- **Explicit interval covering:** The sorted problem is equivalent to covering all values with the fewest intervals of width `k`; starting each interval at the smallest uncovered value yields the same greedy method.
- **Dynamic programming:** It can model sorted prefixes but adds unnecessary state because the greedy boundary is forced.
- **Counting sort:** The bounded value range permits it, but comparison sorting is simpler and already meets the bound.
- **One element:** The initialized single group is the answer.
- **All values equal:** Every value fits in one group for any nonnegative `k`.
- **Zero** `k`: The answer is the number of distinct values.
- **Difference exactly** `k`: The condition uses `>k` to start a new group, so equality remains valid.
- **Large gaps:** Each first value beyond the active interval starts a necessary new group.
- **Duplicates across a boundary:** Equal values cannot straddle a greedy boundary because sorted equals are adjacent and have zero difference.
- **Subsequence ordering:** Membership is chosen by value, then original order within each membership set supplies a legal subsequence.
- **Input mutation:** The original ordering of `nums` is destroyed by sorting.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the number of values. Sorting takes `O(n\log n)` time and the greedy scan takes `O(n)`, for total `O(n\log n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
