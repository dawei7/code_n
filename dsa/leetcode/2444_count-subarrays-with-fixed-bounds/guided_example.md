# Guided Example: Count Subarrays With Fixed Bounds

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 3, 5, 2, 7, 5], "minK": 1, "maxK": 5}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` and two integers `minK` and `maxK`.

The objective is to compute `2` from `{"nums": [1, 3, 5, 2, 7, 5], "minK": 1, "maxK": 5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count valid starts for each fixed ending position

Every subarray is uniquely identified by its start and end. Instead of generating all $O(n^2)$ pairs, the solution scans the end index `i` from left to right and counts how many starts produce a valid subarray ending exactly at `i`. Adding those counts covers every subarray once.

A fixed-bound subarray needs three facts:

- It cannot contain a value below `minK` or above `maxK`.
- It must contain at least one occurrence of `minK`.
- It must contain at least one occurrence of `maxK`.

The scan maintains the latest position relevant to each fact:

- `k` is the latest invalid position containing a value outside the allowed interval.
- `j1` is the latest occurrence of `minK`.
- `j2` is the latest occurrence of `maxK`.

All begin at -1, meaning the corresponding event has not yet appeared.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 3, 5, 2, 7, 5], "minK": 1, "maxK": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The latest invalid position sets a strict lower bound

If `nums[k]` lies outside `[minK,maxK]`, any subarray containing it has a minimum below `minK` or a maximum above `maxK`. Therefore a valid subarray ending at the current `i` must start strictly after `k`.

Only the latest invalid position matters. Starting after it automatically excludes all earlier invalid values as well. When the current value is invalid, `k=i`, and no subarray ending at that same position can be valid.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The latest bounds set an upper bound on the start

To include both required values, the start must be no later than the latest occurrence of each. Thus it must satisfy

$$
\text{start} \le \min(j1,j2).
$$

Why use the earlier of the two latest positions? If `j1 < j2`, starting after `j1` would exclude the most recent `minK`, and there is no later occurrence before the current endpoint. The same reasoning applies symmetrically.

Combining conditions, valid starts are exactly the integers satisfying

$$
k < \text{start} \le \min(j1,j2).
$$

The number of integers in that interval is `min(j1,j2) - k` when positive, and zero otherwise. That is the expression

`max(0, min(j1, j2) - k)`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 3, 5, 2, 7, 5], "minK": 1, "maxK": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate every subarray:** Maintain minimum and maximum while extending each start. This still takes $O(n^2)$ time and is too slow at $10^5$ elements.
- **Two independent window counts:** Count subarrays whose values stay in a range and use inclusion-exclusion on bounds. It can work but is less direct than tracking the latest required positions.
- **Segment tree or sparse table:** Range minimum and maximum queries become fast, yet there remain quadratically many subarrays to classify unless additional counting logic is added.
- **Invalid current value:** Setting `k=i` makes the contribution zero because no subarray ending there can exclude that endpoint.
- **One required bound not seen:** Its latest position remains -1, and the formula contributes zero.
- **Latest bound before latest invalid:** It cannot serve a subarray starting after the invalid value, so the formula correctly yields zero.
- **Repeated bounds:** Only the latest occurrence is needed because it permits the largest set of possible starts for the current endpoint.
- **Equal bounds:** Both latest positions move together, and only runs of that single value contribute.
- **Values exactly at a bound:** They are allowed and update the corresponding required position.
- **Contiguity:** The start interval counts contiguous slices ending at `i`; no elements can be skipped around an invalid position.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. The loop visits each value once and performs only constant-time comparisons, assignments, minimum/maximum operations, and arithmetic. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
