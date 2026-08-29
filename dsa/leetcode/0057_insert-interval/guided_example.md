# Guided Example: Insert Interval

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"intervals": [[1, 3], [6, 9]], "newInterval": [2, 5]}`
- **Required output:** `[[1, 5], [6, 9]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of non-overlapping intervals `intervals` where $\text{intervals}[i] = [\text{start}_{i}, \text{end}_{i}]$ represent the start and the end of the $i^{\text{th}}$ interval and `intervals` is sorted in ascending order by $\text{start}_{i}$. You are also given an interval $newInterval = [start, end]$ that represents the start and end of another interval.

The objective is to compute `[[1, 5], [6, 9]]` from `{"intervals": [[1, 3], [6, 9]], "newInterval": [2, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reduce insertion to ordinary interval merging

The input intervals are already sorted and non-overlapping, so a specialized solution can insert in linear time. The selected source takes a simpler but less efficient route: append `newInterval` to the list, sort all intervals, and then run the standard merge-interval scan.

Once sorted, starts are non-decreasing. The merge helper keeps a result whose last interval represents the active overlapping chain. Each new interval either begins after that active end, creating a gap, or overlaps it and extends the active end.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"intervals": [[1, 3], [6, 9]], "newInterval": [2, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What sorting establishes

`intervals.sort()` orders each two-element list lexicographically, first by start and then by end. Even though the original input was sorted, appending an arbitrary new interval can break that order. Sorting restores it.

After sorting, when a new start is greater than the last merged end, no later interval can overlap that result interval because later starts are at least as large. This makes finalization safe.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Initialize from the first sorted interval

`ans = [intervals[0]]` starts the merged result with the first interval object. The combined list can never be empty: even if original `intervals` is empty, the public method appends `newInterval` before calling `merge`. Therefore, indexing position 0 is safe for every valid input.

This initialization stores an alias to an existing inner list rather than a copy. That has mutation consequences described below.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 5], [6, 9]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"intervals": [[1, 3], [6, 9]], "newInterval": [2, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 5], [6, 9]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Three-phase linear scan:** Append intervals strictly before `newInterval`, merge all overlaps, then append the remaining suffix. It uses the sorted/non-overlapping guarantee and achieves $O(n)$ time.
- **Binary search for insertion point:** Locate the starting neighborhood quickly, but merging and constructing the output can still require $O(n)$ time.
- **Non-mutating sort:** Use `sorted(intervals + [newInterval])` to preserve the outer input, at the cost of an explicit combined copy and the same sorting time.
- **Empty original list:** Appending first makes the merge input contain one interval, which is returned.
- **New interval before all others:** Sorting moves it to the front; it may become the aliased first output object.
- **New interval after all others:** Sorting leaves it last, and it is merged or appended according to endpoint overlap.
- **Touching endpoint:** Strict `<` treats equality as overlap, as required for closed intervals.
- **Contained new interval:** Merging may leave existing outer bounds unchanged, but the caller's outer list still contains the appended object.
- **Covers all intervals:** Repeated end extension creates one result interval spanning the entire union.
- **Input mutation:** The outer list is appended to and sorted, and the first inner interval may have its end changed through aliasing.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n \log n)$. Appending is amortized $O(1)$. Sorting $n+1$ intervals costs $O(n \log n)$. The slice `intervals[1:]` and merge scan each cost $O(n)$. Total time is therefore $O(n \log n)$, not the manifest's $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
