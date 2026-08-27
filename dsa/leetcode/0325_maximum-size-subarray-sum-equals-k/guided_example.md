# Guided Example: Maximum Size Subarray Sum Equals k

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, -1, 5, -2, 3], "k": 3}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums` and an integer `k`, return *the maximum length of a **subarray** that sums to* `k`. If there is not one, return `0` instead.

The objective is to compute `4` from `{"nums": [1, -1, 5, -2, 3], "k": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use contiguity to replace each subarray sum with a prefix difference.

A subarray must contain consecutive positions. That makes prefix sums useful because subtracting two cumulative totals cancels everything before the subarray.

Let $P_i$ be the sum of `nums[0]` through `nums[i]`, and define $P_{-1}=0$ for the empty prefix before the array. The sum of a subarray from index $a$ through index $i$ is

$$
P_i - P_{a-1}.
$$

To make that sum equal `k`, the prefix immediately before the subarray must satisfy

$$
P_i - P_{a-1} = k,
$$

or, after rearranging,

$$
P_{a-1} = P_i-k.
$$

This equation turns the problem around. When the scan reaches ending index `i` and its running prefix sum is `s`, there is no need to test every possible start. It only needs to know whether the specific earlier prefix sum `s - k` has occurred. A hash map provides that lookup in expected constant time.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, -1, 5, -2, 3], "k": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What the map stores and why it stores the earliest index.

The dictionary `d` maps each prefix-sum value to the earliest index where that sum occurred. If `s - k` was first seen at index `p`, then the elements from `p + 1` through `i` sum to `k`, and their length is

$$
i-p.
$$

For a fixed ending index `i`, making `p` as small as possible makes this length as large as possible. That is why the source inserts a prefix sum only if it is not already present:

`if s not in d: d[s] = i`.

Overwriting an earlier occurrence with a later one could only shorten every future subarray that uses that prefix value. The actual numeric sum is identical, so the later occurrence provides no advantage for this maximum-length objective.

Repeated prefix sums are common when the array contains positive and negative values. For example, the running sums of `[1,-1,1,3]` are `1,0,1,4`. The sum `1` appears at indices `0` and `2`. If a later end needs a preceding sum of `1`, index `0` always creates a longer subarray than index `2`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The dictionary `d` maps each prefix-sum value to the earlies... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the map begins with `{0: -1}`.

A valid subarray may start at index zero. If the running sum at index `i` equals `k`, then the desired earlier prefix is `s-k=0`. Conceptually, that zero belongs to the empty prefix ending immediately before index zero, at index `-1`.

Storing `0: -1` unifies this boundary with every other lookup. Its computed length is

$$
i-(-1)=i+1,
$$

which is exactly the number of elements from index `0` through `i`. No separate `if s == k` branch is required.

This initialization is also important when `k = 0`. A zero-sum prefix ending at `i` can use the earliest zero at `-1`, giving the full prefix length rather than starting after a later occurrence of the same cumulative sum.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, -1, 5, -2, 3], "k": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate all starts and ends:** There are $n(:** - **Enumerate all starts and ends:** There are $n(n+1)/2$ subarrays. Prefix sums can make each sum query $O(1)$, but enumerating all pairs still takes $O(n^2)$ time, which is too large for $n$ up to $2\cdot10^5$.
- **- **Sliding window:** A two-pointer window works w:** - **Sliding window:** A two-pointer window works when all numbers are nonnegative because expanding cannot decrease the sum and shrinking cannot increase it. Here negative values break that monotonic behavior, so a window can skip valid answers. Prefix differences impose no positivity requirement.
- **- **Store the latest prefix index:** This is appro:** - **Store the latest prefix index:** This is appropriate for some minimum-length objectives, but it is wrong here. The earliest matching prefix always yields the longest subarray for a fixed end.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `len(nums)`. The method scans the array once. Each iteration performs a constant number of dictionary lookups or insertions, which are expected $O(1)$ in Python. The expected time complexity is therefore $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
