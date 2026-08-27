# Guided Example: Smallest Subarray to Sort in Every Sliding Window

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 3, 2, 4, 5], "k": 3}`
- **Required output:** `[2, 2, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` and an integer `k`.

The objective is to compute `[2, 2, 0]` from `{"nums": [1, 3, 2, 4, 5], "k": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Finding the right boundary with a prefix maximum

The forward state `mx` is the greatest value seen so far while scanning from `i` toward `j`.

At position `t`:

- if `mx > nums[t]`, some earlier value is strictly greater than `nums[t]`, so `t` is the right endpoint of an inversion;
- otherwise, `nums[t]` is at least every earlier value, so it can extend the non-decreasing prefix and becomes the new `mx`.

Whenever the first case occurs, the code sets `r = t`. Since the scan proceeds left to right, the final `r` is the **rightmost** index in the window that has a greater value somewhere before it.

Why must every valid sorting segment reach at least this far? The inversion ending at `r` cannot be fixed while leaving `nums[r]` outside the sorted segment: an earlier larger value would still precede it. Therefore `r` is a necessary right boundary.

The strict comparison `mx > nums[t]` is deliberate. Equal adjacent or separated values are allowed in a non-decreasing sequence and do not form an inversion.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 3, 2, 4, 5], "k": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Finding the left boundary with a suffix minimum

At the same time, `p = j - t + i` moves in the opposite direction: when `t` runs from `i` through `j`, `p` runs from `j` down through `i`.

The reverse state `mi` is the smallest value seen so far to the right of `p`, including the current value after an update.

At position `p`:

- if `mi < nums[p]`, some later value is strictly smaller than `nums[p]`, so `p` is the left endpoint of an inversion;
- otherwise, `nums[p]` is no greater than every value already examined to its right and becomes the new `mi`.

Whenever a violation is found, the code sets `l = p`. Because `p` moves right to left, later assignments move `l` farther left. The final `l` is the **leftmost** index that has a smaller value somewhere after it.

Any sorting segment must start no later than `l`. Leaving `nums[l]` outside would preserve its inversion with that later smaller value.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | At the same time, `p = j - t + i` moves in the opposite dire... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Two directional scans in one loop

Although the helper contains one loop, it logically performs two independent scans:

- `t` advances the prefix-maximum scan;
- `p` advances the suffix-minimum scan.

This halves neither the asymptotic time nor the proof obligations; it simply combines the two linear passes. The loop variable named `k` inside the helper is local to that helper. It temporarily shadows the method parameter name, but it does not change the original window length used by the outer list comprehension.

Initial values `mx = -inf` and `mi = inf` make the first comparison in each direction safe for every allowed integer. The boundary markers `l = r = -1` mean that no inversion has yet been found.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 2, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 3, 2, 4, 5], "k": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 2, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sort a copy of every window:** Comparing each :** - **Sort a copy of every window:** Comparing each window with its sorted copy can locate changed boundaries, but it costs `O(k \log k)` time and `O(k)` space per window instead of the source’s linear scan and constant working state.
- **Find a local inversion core and expand by extrema:** The standard multi-stage method first finds adjacent disorder, computes the middle minimum and maximum, then expands boundaries. It reaches the same result, but the prefix-maximum and suffix-minimum tests encode those expansions directly in two scans.
- **Reuse state across sliding windows:** More advanced data structures might maintain order information as one value leaves and another enters. However, deriving the exact shortest unsorted segment under deletions and insertions is substantially more complex, and the current `O((n-k+1)k)` method fits `n \le 1000`.
- **Window length one:** A single value is already non-decreasing. No forward violation occurs, so the answer is zero.
- **All values equal:** Strict comparisons never treat equality as disorder, and every window correctly returns zero.
- **Strictly decreasing window:** Every position after the first is a right inversion endpoint and every position before the last is a left inversion endpoint. The final boundaries cover the entire window.
- **Disorder only in the middle:** Ordered prefix and suffix values remain outside exactly when they are compatible with every value across the middle; the boundary scans test this global condition rather than merely looking at adjacent pairs.
- **Duplicate values around a boundary:** Non-decreasing order permits equality. Using `>` and `<`, not non-strict comparisons, prevents unnecessary expansion across equal values.
- **Already sorted window:** `r == -1` is a complete certificate that no inversion exists, so returning zero is correct even though `l` also remains `-1`.
- **Overlapping windows:** They are evaluated independently. A position may belong to many windows, but the algorithm never mutates it, so one result cannot affect another.
- **Input preservation:** The phrase “must be sorted” asks for a minimum length, not for the rearranged arrays. The source intentionally computes lengths without changing `nums`.
- **Maximum window length:** When `k == n`, there is exactly one helper call covering the entire array.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(k)$. For one window of length `k`, the helper performs exactly `k` loop iterations. Each iteration does constant-time comparisons, assignments, and index arithmetic, so one call costs `O(k)` time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
