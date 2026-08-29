# Guided Example: Form Array by Concatenating Subarrays of Another Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"groups": [[1, -1, -1], [3, -2, 0]], "nums": [1, -1, 0, 1, -1, -1, 3, -2, 0]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a 2D integer array `groups` of length `n`. You are also given an integer array `nums`.

The objective is to compute `true` from `{"groups": [[1, -1, -1], [3, -2, 0]], "nums": [1, -1, 0, 1, -1, -1, 3, -2, 0]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Search for groups in their required order

The groups must appear in `nums` from first to last and may not overlap. The exact solution maintains two indices:

- `i` is the next group that still needs a match.
- `j` is the earliest `nums` index where that group is allowed to begin.

Both start at zero. At each step, the code compares the entire current group `groups[i]` with the slice of `nums` beginning at `j` and having the same length.

If they match, the group is accepted and both pointers advance appropriately. If they do not, only `j` advances by one, trying the same group at the next possible start.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"groups": [[1, -1, -1], [3, -2, 0]], "nums": [1, -1, 0, 1, -1, -1, 3, -2, 0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the slice describes one candidate subarray

For current group `g`, the expression:

`nums[j : j + len(g)]`

is the contiguous segment beginning at `j` with up to `len(g)` elements. List equality requires the same length and equal values in the same order.

Near the end of `nums`, Python slicing safely returns a shorter list rather than raising an error. Such a shorter slice cannot equal `g`, whose length is positive, so the search advances until `j == m` and terminates.

Negative values and repeated values need no special logic because list equality compares integers position by position.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Advance past a successful match

When `g == nums[j : j + len(g)]`, the source executes:

`j += len(g)`

and:

`i += 1`.

Moving `j` to the first position after the matched subarray enforces disjointness. The next group can begin there or later, but can never reuse an index from the accepted group.

Increasing `i` enforces group order. Once a group is accepted, the algorithm never searches for an earlier group again or permits a later group to appear before it.

There may be unused `nums` elements between matches. On mismatches, `j` moves one step at a time until it finds the next group, so gaps are naturally allowed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"groups": [[1, -1, -1], [3, -2, 0]], "nums": [1, -1, 0, 1, -1, -1, 3, -2, 0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **KMP per group with carried position:** Prefix-function matching avoids rechecking long partial matches and can approach $O(N+S)$ total time.
- **Manual nested comparison:** Avoid Python slice allocation, but still has $O(NL)$ worst-case comparison work without a failure function.
- **Backtracking over occurrences:** It is unnecessary because the earliest valid occurrence always leaves the largest possible suffix.
- **Group longer than remaining nums:** The short slice cannot equal it, and the scan eventually returns false.
- **Unused values between groups:** Mismatch increments allow arbitrary gaps.
- **Adjacent groups:** After a match, the next search starts exactly at its endpoint.
- **Overlapping apparent matches:** Advancing by full group length prevents reuse of any accepted index.
- **Repeated group values:** Equality and ordered pointer state handle them normally.
- **Negative integers:** They are ordinary list elements and do not affect matching logic.
- **All groups matched before nums ends:** The loop exits through `i == n` and returns true; leftover values are allowed.
- **Nums exhausted first:** Remaining positive-length groups cannot be placed.
- **Non-empty groups:** Advancing `j` by `len(g)` always makes progress on a successful match.
- **Input preservation:** Slices are copies; neither `groups` nor `nums` is modified.
- **Slice cost:** Concise syntax hides both comparison time and temporary allocation, which matter to the exact complexity.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(NL)$. Let $N=\lvert\texttt{nums}\rvert$ and let $L$ be the maximum group length. Pointer `j` advances at most $N$ positions, but each attempted match constructs a slice and compares up to the current group's length. The exact worst-case time is therefore $O(NL)$, with successful matched lengths contributing within that bound.
- **Auxiliary Space Complexity:** $O(L)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
