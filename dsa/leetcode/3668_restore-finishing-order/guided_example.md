# Guided Example: Restore Finishing Order

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"order": [3, 1, 2, 5, 4], "friends": [1, 3, 4]}`
- **Required output:** `[3, 1, 4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `order` of length `n` and an integer array `friends`.

The objective is to compute `[3, 1, 4]` from `{"order": [3, 1, 2, 5, 4], "friends": [1, 3, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate race order into a position lookup

`order` lists every participant in finishing order. The index of an ID is therefore its finishing rank: a smaller index means the participant finished earlier.

The source builds

`d = {x: i for i, x in enumerate(order)}`.

For every participant ID `x`, `d[x]` is the zero-based position where that participant appears in the race result.

The permutation guarantee makes the mapping unambiguous. Every ID from one through `n` appears exactly once, so no dictionary entry is overwritten by a duplicate.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"order": [3, 1, 2, 5, 4], "friends": [1, 3, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Sort only the friends by their race positions

The input `friends` is sorted by numeric ID, but numeric ID has no relationship to finishing time. The desired output orders these same IDs by `d[x]`.

The source returns

`sorted(friends, key=lambda x: d[x])`.

The key function replaces each friend only for comparison with that friend’s race position. The returned list still contains the original IDs.

Every friend is guaranteed to appear in `order`, so all dictionary lookups succeed. No missing-ID branch is needed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the result is correct

Take any two friends `a` and `b`. If `a` finished before `b`, then `d[a] < d[b]`. Key sorting therefore places `a` before `b`.

This pairwise property holds for every pair of friends, so the complete sorted result has exactly the same relative order as their occurrences in `order`.

Every input friend appears once in the returned list because `sorted` rearranges rather than filters. No non-friend can appear because the source sorts only `friends`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 1, 4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"order": [3, 1, 2, 5, 4], "friends": [1, 3, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 1, 4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Filter `order` with a friend set:** Build a set of the at-most-eight IDs and retain finishers belonging to it. This matches the manifest’s `O(n)` time and bounded `O(1)` auxiliary space.
- **Call `order.index` for each friend:** It avoids a map but scans up to `n` elements per friend, costing `O(nf)`; with `f <= 8` it is still linear up to a constant but less scalable.
- **Sort friends by ID:** They are already ID-sorted, which does not represent finishing order.
- **Sort the complete order:** `order` already has the desired ranking; sorting it numerically would destroy that information.
- **One friend:** The returned list contains that same ID.
- **All participants are friends:** Sorting by positions reconstructs `order` exactly.
- **Friend who finished first or last:** Position keys zero and `n - 1` place them at the appropriate ends.
- **Duplicate friend IDs:** The constraints say `friends` is strictly increasing, so duplicates do not occur.
- **Missing friend ID:** The contract guarantees membership. Without it, `d[x]` would raise `KeyError`.
- **Input preservation:** `sorted` returns a new list, and dictionary construction does not mutate either input.
- **Missing import:** The stored source uses `List` without importing it. Standalone Python needs `from typing import List` unless the harness provides the name.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n + f log f)$. Let `n = len(order)` and `f = len(friends)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
