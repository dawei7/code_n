# Guided Example: Course Schedule III

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"courses": [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` different online courses numbered from `1` to `n`. You are given an array `courses` where $\text{courses}[i] = [\text{duration}_{i}, \text{lastDay}_{i}]$ indicate that the $i^{\text{th}}$ course should be taken **continuously** for $\text{duration}_{i}$ days and must be finished before or on $\text{lastDay}_{i}$.

The objective is to compute `3` from `{"courses": [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]}` while avoiding redundant calculations and unnecessary overhead.

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

**Process deadlines from earliest to latest.** The first greedy decision is `courses.sort(key=lambda x: x[1])`. If two chosen courses have deadlines `d_1 <= d_2`, placing the earlier-deadline course first is never worse: it gives the more constrained course its chance to finish early, while the later-deadline course still has at least as much allowed time. Repeated adjacent exchanges can transform any feasible chosen schedule into nondecreasing deadline order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"courses": [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Once courses are in that order, the scan only needs to decide which durations to retain.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Track a candidate set and its total duration.** `pq` contains the durations of currently selected courses. Python provides a min-heap, so the source pushes `-duration`. The most negative number represents the largest positive duration, making `heappop(pq)` remove the longest selected course.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"courses": [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Dynamic programming by time:** Sort deadlines and choose or skip each course using elapsed time as state. It is much more expensive when deadlines are large.
- **Linear search for the longest selected course:** It preserves the greedy idea but can make the scan quadratic; the heap supplies the longest duration efficiently.
- **Course longer than its own deadline:** It is pushed, immediately becomes infeasible, and is removed if no even longer selected course is a better replacement.
- **One course:** It remains only when its duration does not exceed its last day.
- **Equal deadlines:** Their relative sort order is unimportant because the heap replacement rule chooses the shortest useful collection.
- **Equal durations:** Any tied longest course may be removed; total duration and future feasibility are identical.
- **Current course removed:** This is the ordinary rejection case and restores the previous feasible set.
- **Earlier course removed:** This is a beneficial replacement that preserves count and reduces total time.
- **Input mutation:** `sort` reorders `courses`. Copy first if callers require the original order.
- **Continuous scheduling:** There is no benefit to idle time before a selected course; placing chosen courses back-to-back in deadline order minimizes every completion time.
- **Heap sign convention:** Values are negative only to simulate a max-heap. Adding a popped heap value to `s` subtracts the corresponding duration.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(C \log C)$. Let $C$ be the number of courses. Sorting by deadline costs $O(C\log C)$. Every course is pushed once, and every pushed duration is popped at most once. Each heap operation costs $O(\log C)$, so the complete scan is $O(C\log C)$.
- **Auxiliary Space Complexity:** $O(C)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
