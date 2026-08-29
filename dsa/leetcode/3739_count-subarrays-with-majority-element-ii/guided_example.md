# Guided Example: Count Subarrays With Majority Element II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 2, 3], "target": 2}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` and an integer `target`.

The objective is to compute `5` from `{"nums": [1, 2, 2, 3], "target": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Convert majority into a positive transformed sum

Replace each target occurrence conceptually with `+1` and every other value with `-1`. For a subarray with `f` target occurrences and length `L`, its transformed sum is

$$
f-(L-f)=2f-L.
$$

This is positive exactly when `2f>L`, the strict-majority condition.

Let `P[t]` be the transformed prefix sum before position `t`. The transformed sum of `nums[l:r]` is `P[r+1]-P[l]`, so it is positive exactly when

$$
P[l]<P[r+1].
$$

For every current prefix, the algorithm must count earlier prefix sums that are strictly smaller.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 2, 3], "target": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Shift prefix balances into positive Fenwick indices

Each transformed step is plus or minus one, so all prefix sums lie from `-n` through `n`. The source uses an offset: `s=n+1` represents mathematical prefix sum zero. This keeps every possible Fenwick index positive.

Before scanning elements, it inserts this empty prefix once. For each value, `s` rises by one for a target match or falls by one otherwise.

`tree.query(s-1)` returns the number of earlier shifted balances strictly below `s`. Every such prefix boundary creates one subarray ending at the current position whose transformed sum is positive. The count is added to `ans`, and then the current prefix is inserted for future endpoints.

Querying before insertion prevents a zero-length subarray from being paired with itself. Querying `s-1` rather than `s` enforces strict positivity; equal prefix sums correspond to transformed sum zero and exactly half target values.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How the Fenwick tree performs prefix counts

The tree array stores partial frequency sums. `update(x,1)` adds one to the current prefix-balance coordinate and to Fenwick ancestors by repeatedly adding the lowest set bit `x & -x`.

`query(x)` accumulates frequencies from coordinates one through `x`. It repeatedly removes the lowest set bit, visiting $O(\log n)$ tree nodes.

The tree size `2n+1` covers the shifted range. Starting at `n+1`, after at most `n` negative steps the index is at least one, and after `n` positive steps it is at most `2n+1`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 2, 3], "target": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Nested endpoint enumeration:** Incremental target counts give $O(n^2)$ time and work for the smaller version, but not for `n=10^5`.
- **Editorial unit-step counter:** Because balances move only by one, a carefully maintained count of smaller prior balances can achieve $O(n)$ time. That is not the exact source documented here.
- **Merge sort counting:** Counting ordered prefix pairs with smaller left values can also take $O(n\log n)$, but a Fenwick tree naturally respects time order online.
- **Query `s` instead of `s-1`:** This would include equal balances and count subarrays where target is exactly half, violating strict majority.
- **Insert before querying:** It would count the empty current-to-current interval.
- **Target absent:** Every step is negative and the answer is zero.
- **Every element target:** Every nonempty subarray is counted.
- **Single element:** A target match yields one; a non-match yields zero.
- **Large element values:** Only equality to `target` matters, so values do not require coordinate compression.
- **Offset boundaries:** The `n+1` shift guarantees valid positive Fenwick indices across the entire possible balance range.
- **Manifest mismatch:** Runtime claims must include the logarithmic tree operations actually present.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. There are `n` iterations. Each performs one Fenwick query and one update, both $O(\log n)$, so actual time complexity is $O(n\log n)$. Tree initialization costs $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
