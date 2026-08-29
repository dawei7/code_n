# Guided Example: Subarray Sum Equals K

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 1, 1], "k": 2}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of integers `nums` and an integer `k`, return *the total number of subarrays whose sum equals to* `k`.

The objective is to compute `2` from `{"nums": [1, 1, 1], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

For each position, the solution counts how many earlier prefix sums would make a subarray ending here sum to `k`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 1, 1], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Let the running prefix sum `s` after reading the current element equal the sum from the array start through that element. If an earlier prefix sum was `p`, then the elements after that earlier prefix through the current position have sum:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Optimality Decision

Synthesize the final answer directly from validated sub-states.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 1, 1], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate every subarray:** Maintaining a running sum per start still takes $O(n^2)$ time.
- **Prefix array plus nested endpoints:** Sum queries become constant time, but there remain quadratic pairs.
- **Sliding window:** It is not correct when values may be negative.
- **Use a set:** It undercounts when the same prefix sum occurs at several indices.
- **Omit the empty prefix:** Subarrays starting at index zero would be missed.
- **Insert before querying:** For `k = 0`, it falsely counts an empty subarray.
- **Single element equal to `k`:** The empty prefix makes it count once.
- **Zero values:** Repeated prefix sums correctly create multiple start positions.
- **Negative `k`:** The same equation `p=s-k` applies.
- **No qualifying subarray:** Every lookup contributes zero and the result remains zero.
- **Repeated value patterns:** Index-distinct subarrays are counted separately.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. Each element performs constant arithmetic and expected-$O(1)$ Counter lookup/insertion, so expected time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
