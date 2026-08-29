# Guided Example: Merge Intervals

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"intervals": [[1, 3], [2, 6], [8, 10], [15, 18]]}`
- **Required output:** `[[1, 6], [8, 10], [15, 18]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of `intervals` where $\text{intervals}[i] = [\text{start}_{i}, \text{end}_{i}]$, merge all overlapping intervals, and return *an array of the non-overlapping intervals that cover all the intervals in the input*.

The objective is to compute `[[1, 6], [8, 10], [15, 18]]` from `{"intervals": [[1, 3], [2, 6], [8, 10], [15, 18]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Sorting turns a global overlap problem into a neighbor decision

Before sorting, an interval may overlap another interval anywhere in the input, so it is difficult to know when a merged group is complete. `intervals.sort()` orders the pairs lexicographically: primarily by start and, for equal starts, by end.

After sorting, interval starts never decrease. Once the next start lies strictly beyond the current merged end, no later interval can reach backward and overlap the current group because every later start is at least as large. That makes it safe to finalize one merged interval and begin another.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"intervals": [[1, 3], [2, 6], [8, 10], [15, 18]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Keep one active merged interval

`st` and `ed` represent the union of the current connected chain of overlapping intervals. They are initialized from the first sorted pair. The input is guaranteed non-empty, so `intervals[0]` is valid.

For each later `[s, e]`, there are two cases:

- If `ed < s`, a genuine gap separates the active interval from the new one. The active `[st, ed]` is appended to the answer, and `[s, e]` becomes the next active interval.
- Otherwise, `s <= ed`, so the closed intervals overlap or touch. Their union begins at `st` and ends at `max(ed, e)`, so only `ed` needs updating.

The start remains `st` during a merge because sorting guarantees `s >= st`. A new interval may be completely contained inside the active one; taking the maximum keeps `ed` unchanged in that case.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why touching endpoints merge

These are closed intervals. `[1,4]` contains endpoint 4, and `[4,5]` also contains endpoint 4. Their intersection is not empty, so their union is the single interval `[1,5]`.

That is why the gap test is `ed < s`, not `ed <= s`. Equality belongs to the merge case.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 6], [8, 10], [15, 18]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"intervals": [[1, 3], [2, 6], [8, 10], [15, 18]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 6], [8, 10], [15, 18]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Append the first interval and merge into the result tail:** This removes separate `st`/`ed` state, but mutating the tail may alias input interval objects unless copies are made.
- **Sweep-line events:** Sort starts and ends as events to reconstruct covered components. It is more machinery than needed when whole intervals can be sorted directly.
- **Graph connected components:** Treat overlaps as edges and combine components. Building pairwise edges can cost $O(n^2)$ and ignores the order structure.
- **Already disjoint intervals:** Every new start creates a gap, so each interval is copied into the answer separately.
- **Nested intervals:** A contained end does not shrink `ed`; `max` preserves the outer interval.
- **Equal starts:** Lexicographic sorting places smaller ends first, but repeated merges still produce the maximum end correctly.
- **Touching endpoints:** Equality merges because intervals are closed.
- **Single interval:** The loop is empty, and the final append returns a fresh copy of that interval.
- **Empty list outside the contract:** Accessing the first interval would fail; the documented constraint guarantees at least one.
- **Caller-visible ordering:** The outer input list is sorted in place, even though its inner pairs are not modified.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n \log n)$. Sorting $n$ intervals costs $O(n \log n)$. The suffix slice and scan each cost $O(n)$, and every scan step does constant work. Overall time is $O(n \log n)$, matching the manifest.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
