# Guided Example: Valid Subarrays With Exactly One Peak

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 3, 2], "k": 1}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of length `n` and an integer `k`.

The objective is to compute `4` from `{"nums": [1, 3, 2], "k": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Peak status belongs to the original array

An index is a peak only when it is internal to the complete `nums` array and its value is strictly greater than both original neighbors. The status is not recomputed relative to a selected subarray.

This means a one-element subarray `[i,i]` can contain one peak when `i` is a peak of `nums`, even though that subarray itself has no internal neighbors. The algorithm must first identify global peak indices and then reason only about which of those indices lie inside each interval.

The source scans indices one through `N-2` and appends every strict peak to `peaks`. Because the scan is left to right, this list is sorted by index.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 3, 2], "k": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Attribute every valid subarray to its unique peak

A valid interval contains exactly one peak. Therefore it can be counted under that peak and under no other.

Fix peak `p=peaks[j]`. A left endpoint `l` must satisfy:

- `l\le p` so the interval contains the peak;
- `p-l\le k`, equivalently `l\ge p-k`;
- `l\ge0`; and
- if a previous peak exists, `l>peaks[j-1]` so that peak is excluded.

Combining the lower bounds gives

$$
leftMin=
\max(p-k,0,peaks[j-1]+1),
$$

omitting the previous-peak term when `j=0`.

The source computes this in two steps with `max`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | A valid interval contains exactly one peak.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why only the nearest previous peak matters

All earlier peaks lie at or before `peaks[j-1]`. If `l` is greater than the nearest previous peak, it is automatically greater than every earlier one, so none can lie in `[l,p]`.

Conversely, if `l\le peaks[j-1]`, the nearest previous peak lies inside the interval because the right endpoint must be at least `p`. The interval would then contain at least two peaks. The nearest previous peak is therefore the exact exclusion boundary.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 3, 2], "k": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate every subarray:** Check its containe:** - **Enumerate every subarray:** Check its contained peaks and distances directly in `O(N^2)` intervals. Peak boundaries allow counting whole rectangles of endpoint choices at once.
- **Prefix sum of peak indicators:** It can test whether an interval contains exactly one peak in constant time, but enumerating all intervals remains quadratic unless combined with additional boundary logic.
- **Two pointers:** A window can maintain peak count, but the separate distance bound around the unique peak complicates direct counting. Neighbor-peak formulas are simpler.
- **Recompute peaks inside each subarray:** Incorrect. Peak status is defined using neighbors in the original array.
- **Length-one subarray containing a peak:** It is valid because the global peak is contained and both distances are zero.
- **No peaks:** The result is zero.
- **One peak:** Only array and distance bounds restrict endpoints; both neighboring-peak terms are absent.
- **Several peaks:** The nearest peak on each side is sufficient to exclude all others.
- **Strict comparisons:** Equal neighboring values do not form a peak because the definition requires greater than both.
- **Endpoint indices zero and `N-1`:** They can never be peaks but may be subarray endpoints around an internal peak.
- **Large `k`:** Array bounds and neighboring peaks still cap choices; `k` does not force an interval to extend fully.
- **Peaks two positions apart:** Both are valid global peaks with a valley between. The previous-plus-one and next-minus-one boundaries still leave legal intervals centered on either peak without overlap in contained peak sets.
- **Independent multiplication:** Once boundaries are fixed, choosing a left endpoint does not constrain a legal right endpoint beyond both containing `p`, so the product is exact.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. The first pass checks each possible peak index once, taking `O(N)` time. The second pass processes each of `P` peaks with constant work, taking `O(P)`, where `P\le N`. Total time is `O(N)`.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
