# Guided Example: Number of Subarrays with Bounded Maximum

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 1, 4, 3], "left": 2, "right": 3}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums` and two integers `left` and `right`, return *the number of contiguous non-empty **subarrays** such that the value of the maximum array element in that subarray is in the range *`[left, right]`.

The objective is to compute `3` from `{"nums": [2, 1, 4, 3], "left": 2, "right": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Replace a two-sided maximum condition with two prefix conditions

A subarray is valid when:

$$
left \le \max(\text{subarray}) \le right.
$$

Directly maintaining the maximum of every possible subarray would be expensive. Instead, define `f(x)` as the number of nonempty contiguous subarrays whose every element is at most `x`. Equivalently, it counts subarrays whose maximum is at most `x`.

Then:

- `f(right)` counts subarrays with maximum no greater than `right`;
- `f(left - 1)` counts the subset whose maximum is strictly below `left`, because array values are integers.

Subtracting removes exactly the too-small maxima:

$$
\text{answer}=f(right)-f(left-1).
$$

Any subarray containing a value above `right` appears in neither count. Any maximum inside the inclusive interval appears only in the first. Any maximum below `left` appears in both and cancels.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 1, 4, 3], "left": 2, "right": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count subarrays with maximum at most one threshold

For a fixed threshold `x`, a subarray qualifies if and only if all its elements are at most `x`. Values greater than `x` act as barriers: no qualifying subarray may cross one.

Variable `t` stores the length of the current consecutive suffix consisting entirely of values at most `x`.

For each value `v`:

- if `v > x`, set `t = 0` because the current position breaks every qualifying suffix;
- otherwise increment `t`, extending every previous qualifying suffix and creating the one-element suffix `[v]`.

The exact assignment is:

`t = 0 if v > x else t + 1`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For a fixed threshold `x`, a subarray qualifies if and only ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why `t` is also the number of valid subarrays ending here

Suppose the last `t` positions all contain values at most `x`. A subarray ending at the current position may start at any of those `t` positions, and every such choice stays entirely within the valid suffix.

Starting earlier would cross either the array boundary or the most recent value greater than `x`, so no additional valid ending subarray exists.

Therefore exactly `t` qualifying subarrays end at the current index. Adding `t` to `cnt` counts them.

Every nonempty subarray has exactly one ending index, so summing these per-index contributions counts each qualifying subarray once.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 1, 4, 3], "left": 2, "right": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Single-pass last-valid-index method:** Track t:** - **Single-pass last-valid-index method:** Track the most recent element above `right` and the most recent element inside the allowed range. It also reaches $O(n)$ time but has a less immediately reusable counting proof.
- **- **Monotonic deque for every ending index:** It c:** - **Monotonic deque for every ending index:** It can maintain window maxima, but here no fixed window length exists and threshold subtraction is simpler.
- **- **Enumerate all subarrays:** Updating a running :** - **Enumerate all subarrays:** Updating a running maximum for each start still costs $O(n^2)$ time.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(2n)$. Let $n$ be the length of `nums`. Helper `f` scans the array once in $O(n)$ time. It is called twice, so total time is $O(2n)=O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
