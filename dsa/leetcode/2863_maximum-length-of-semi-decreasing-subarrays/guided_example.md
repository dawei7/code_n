# Guided Example: Maximum Length of Semi-Decreasing Subarrays

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [7, 6, 5, 4, 3, 2, 1, 6, 10, 11]}`
- **Required output:** `8`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `8` from `{"nums": [7, 6, 5, 4, 3, 2, 1, 6, 10, 11]}` while avoiding redundant calculations and unnecessary overhead.

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

**Only the endpoints determine validity.** A subarray from index $i$ through index $j$ is semi-decreasing when `nums[i] > nums[j]`. Values between those endpoints may rise, fall, or repeat; they do not affect whether the subarray qualifies. Its length is `j - i + 1`. The goal is therefore to find a value at a late index and some strictly larger value at the earliest possible earlier index.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [7, 6, 5, 4, 3, 2, 1, 6, 10, 11]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The exact solution reorganizes indices by value. The first loop builds `d` so that `d[x]` is the increasing list of every index containing value `x`. Because indices are appended during a left-to-right scan:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The exact solution reorganizes indices by value.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

- `d[x][0]` is the earliest occurrence of `x`;
- `d[x][-1]` is the latest occurrence of `x`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `8` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [7, 6, 5, 4, 3, 2, 1, 6, 10, 11]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `8` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Monotonic prefix candidates:** Store indices t:** - **Monotonic prefix candidates:** Store indices that set a new prefix maximum, then scan right endpoints from right to left and pop candidates once their values are strictly greater. This obtains the intended $O(n)$ time and $O(n)$ space.
- **Sorting index-value pairs:** Sorting all elements by value can express the same idea but still costs $O(n\log n)$ and needs careful equal-value batching to preserve strictness.
- **All equal values:** No first value can be strictly greater than a last value; equal values are deliberately never added to `k` until after their own candidate, so the answer stays `0`.
- **Strict inequality:** Processing current value only after querying prevents equal endpoint values from being accepted.
- **Negative values:** Dictionary ordering and numerical comparisons work unchanged; the algorithm does not assume values are positive.
- **Single element:** No two ordered endpoints exist, and the sentinel-based candidate leaves the answer at `0`.
- **Sentinel arithmetic:** Python permits finite integers minus `inf`, producing negative infinity. A language without such a numeric sentinel should explicitly skip the first key.
- **Worst-case distinct values:** Sorting dominates at $O(n\log n)$; describing this exact source as $O(n)$ would be inaccurate.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+u\log u)$. Let $n$ be the array length and $u$ the number of distinct values. Building the dictionary of index lists takes expected $O(n)$ time. Sorting its $u$ keys takes $O(u\log u)$ time. The descending scan does $O(1)$ work per key, so exact total time is $O(n+u\log u)$, which becomes $O(n\log n)$ when $u=n$.
- **Auxiliary Space Complexity:** $O(n+u)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
