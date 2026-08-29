# Guided Example: Remove Interval

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"intervals": [[0, 2], [3, 4], [5, 7]], "toBeRemoved": [1, 6]}`
- **Required output:** `[[0, 1], [6, 7]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A set of real numbers can be represented as the union of several disjoint intervals, where each interval is in the form `[a, b)`. A real number `x` is in the set if one of its intervals `[a, b)` contains `x` (i.e. $a \le x < b$).

The objective is to compute `[[0, 1], [6, 7]]` from `{"intervals": [[0, 2], [3, 4], [5, 7]], "toBeRemoved": [1, 6]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Subtract the removal interval from each disjoint input interval

The input intervals are already sorted and mutually disjoint, so there is no need to merge or reorder them. The algorithm processes each interval `[a, b)` independently against the removal interval `[x, y)` and appends whatever portion remains.

Half-open boundaries matter. Two half-open intervals overlap only when `a < y` and `b > x`. Equivalently, they do not overlap when `a >= y` or `b <= x`. The exact source uses that non-overlap test.

If `a >= y`, the input begins at or after the removal interval's excluded right endpoint. If `b <= x`, it ends at or before the removal interval's included left endpoint. In either case the sets share no real number, so `[a, b)` is appended unchanged.

Equality belongs in the non-overlap condition. For example, `[0, 2)` and `[2, 5)` merely touch at two. The first excludes two while the second includes it, so their intersection is empty.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"intervals": [[0, 2], [3, 4], [5, 7]], "toBeRemoved": [1, 6]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: An overlapping interval leaves at most two pieces

When overlap exists, removing one contiguous interval can leave a portion to its left, a portion to its right, both portions, or nothing.

If `a < x`, values from `a` up to but excluding `x` remain, so the code appends `[a, x)`. The strict inequality guarantees this piece is nonempty.

If `b > y`, values from `y` up to but excluding `b` remain, so the code appends `[y, b)`. Again, strict inequality prevents an empty interval.

Both tests can succeed when the removal interval lies strictly inside the input interval. For `[0, 5)` minus `[2, 3)`, the output is `[0, 2)` followed by `[3, 5)`. If removal covers the entire input interval, neither condition succeeds and that interval contributes nothing.

For the first example, `[0, 2)` overlaps `[1, 6)` and leaves `[0, 1)`. Interval `[3, 4)` lies completely inside the removal range and disappears. Interval `[5, 7)` leaves `[6, 7)`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why output order and disjointness are preserved

Input intervals are visited from left to right. Any surviving left piece begins at the original `a`, and any right piece begins at `y` within that same original interval. The left piece is appended before the right piece. Therefore pieces from one interval are ordered, and all pieces from an earlier input interval remain before pieces from a later one.

Subtraction can only remove points; it cannot create an overlap between originally disjoint intervals. The two pieces from one split are separated by the removed interval. Consequently the output remains sorted and disjoint without a final sort or merge.

For correctness, consider any real value in an appended piece. It was inside the original interval, and the endpoint tests place it outside `[x, y)`, so it belongs in the required set difference. Conversely, any original value not in the removal interval lies either in a completely non-overlapping input interval, to the left of `x` in an overlapping interval, or at or to the right of `y` in that interval. One of the append rules retains it. Thus the result contains every and only required value.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[0, 1], [6, 7]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"intervals": [[0, 2], [3, 4], [5, 7]], "toBeRemoved": [1, 6]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[0, 1], [6, 7]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Four explicit overlap cases:** Fully covered, left overlap, right overlap, and internal removal can be handled separately. The two surviving-piece tests express all cases more compactly.
- **General sweep-line events:** Sorting all endpoints works but is unnecessary because input intervals are already sorted and only one interval is removed.
- **Removal completely outside:** Every interval passes the non-overlap test and is copied unchanged.
- **Removal covers an interval:** Neither residual condition succeeds, so the interval disappears.
- **Removal strictly inside one interval:** Both residual pieces are emitted in left-to-right order.
- **Touching endpoints:** `b == x` or `a == y` means no intersection for half-open intervals, so the original interval remains intact.
- **Removal shares a left endpoint:** There is no empty left piece because `a < x` is false.
- **Removal shares a right endpoint:** There is no empty right piece because `b > y` is false.
- **Negative coordinates:** Only ordering matters, so signs have no effect.
- **Do not use closed-interval logic:** Treating touching endpoints as overlap can create unnecessary or empty fragments.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of input intervals and $r$ the number of returned intervals. The loop examines each input once and performs constant work, so time is $O(n)$. This is optimal because the output may contain information from every input interval.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
