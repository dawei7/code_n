# Guided Example: Remove Covered Intervals

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"intervals": [[1, 4], [3, 6], [2, 8]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array `intervals` where $\text{intervals}[i] = [l_{i}, r_{i}]$ represent the interval $[l_{i}, r_{i})$, remove all intervals that are covered by another interval in the list.

The objective is to compute `2` from `{"intervals": [[1, 4], [3, 6], [2, 8]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Sort so a possible covering interval always comes first

An interval `[a,b)` is covered when an earlier candidate has a start no greater than $a$ and an end no smaller than $b$. Sorting by ascending start establishes the first condition automatically: while scanning, every earlier interval begins at or before the current one.

Intervals with the same start need special handling. The longer interval must appear first, because it covers every shorter interval sharing that start. The key `(x[0], -x[1])` sorts starts upward and ends downward for ties.

Without the negative end tie-breaker, `[1,4)` could be seen before `[1,8)`. The shorter interval might be counted as uncovered even though the later longer interval covers it. Putting `[1,8)` first prevents that mistake.

The source calls `intervals.sort`, so it mutates the caller's list order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"intervals": [[1, 4], [3, 6], [2, 8]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Track the farthest end reached so far

Variable `pre` stores the largest right endpoint among intervals already counted as not covered. It begins at negative infinity, ensuring the first sorted interval has `cur > pre` and is counted.

For each interval, the start is ignored in the loop because sorting has already incorporated it. If current end `cur <= pre`, some earlier interval starts no later and ends at least as late. That earlier interval covers the current one, so the count and `pre` remain unchanged.

If `cur > pre`, no earlier interval reaches the current end. Therefore none can cover it, the interval remains, `ans` increases, and `pre` becomes `cur`.

It is sufficient to remember only the maximum end rather than a particular full interval. Any earlier interval responsible for that maximum also has a start no greater than the current start due to sorting. Those two facts are exactly the coverage conditions.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why `pre` never decreases

When an interval is covered, replacing `pre` with its smaller or equal end would forget a stronger covering interval and could make a later covered interval appear new. The code deliberately updates `pre` only on a strict increase. It is therefore a monotone summary of the farthest right boundary reached by any earlier surviving interval. This is the central scan invariant: before processing each interval, `pre` is the maximum end among all earlier intervals. The skip and update branches both preserve it.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"intervals": [[1, 4], [3, 6], [2, 8]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Quadratic pair checks:** Compare every interval with every other interval. It is straightforward but costs $O(n^2)$ time.
- **Sort only by start:** This fails when equal-start intervals appear shortest first; the descending-end tie-break is essential.
- **Track the immediately previous end only:** The maximum end is needed because a much earlier interval may cover the current one even when the immediately previous interval does not.
- **No covered intervals:** Ends strictly increase through the sorted scan, so every interval is counted.
- **All covered by one interval:** The first longest interval sets `pre`, and all remaining ends are no greater.
- **Equal right endpoints:** The later-start interval is covered because `cur == pre` does not pass the strict increase test.
- **Nested intervals:** Descending reachable ends cause all inner intervals to be skipped.
- **Disjoint intervals:** Their ends increase with starts, so they all remain.
- **Unique interval guarantee:** Exact duplicate pairs do not occur, though the same logic would count only one duplicate.
- **Input mutation:** Copy the list before sorting if caller-visible order must remain unchanged.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the number of intervals. Python sorting takes $O(n\log n)$ comparisons, and the scan takes $O(n)$ time. Total time is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
