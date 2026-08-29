# Guided Example: Check if Grid can be Cut into Sections

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 5, "rectangles": [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n` representing the dimensions of an `n x n`<!-- notionvc: fa9fe4ed-dff8-4410-8196-346f2d430795 --> grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates `rectangles`, where $\text{rectangles}[i]$ is in the form `[start_x, start_y, end_x, end_y]`, representing a rectangle on the grid. Each rectangle is defined as follows:

The objective is to compute `true` from `{"n": 5, "rectangles": [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]}` while avoiding redundant calculations and unnecessary overhead.

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

**A cut depends only on rectangle projections.** Horizontal cuts care about each rectangle's y-interval `[y1,y2]`. A cut is valid when no projection spans across it. Vertical cuts use x-intervals in the same way.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 5, "rectangles": [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The source builds start/end events for both axes. Marker one is a start and marker zero is an end.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Sweep how many projections overlap.** `overlap` increments at a start and decrements at an end. Whenever it becomes zero, one connected group of projected intervals has finished.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 5, "rectangles": [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort intervals by start and merge:** It yields the same group count and is the editorial's formulation.
- **Try coordinate cuts directly:** Coordinates may reach $10^9$, so dense scanning is impossible.
- **Exactly three groups:** Two cuts separate them directly.
- **More than three groups:** Choose cuts so all three sections remain nonempty; extra groups can share a section.
- **Several rectangles per group:** They may overlap in projection and remain in one section.
- **Only two groups:** One gap cannot create three nonempty sections.
- **Touching endpoints:** End-before-start treats the shared boundary as cuttable.
- **Overlapping projections:** They remain one group until all active intervals end.
- **Nested interval:** Its end does not close the group while an outer projection remains active.
- **Horizontal success:** X grouping becomes irrelevant because OR short-circuits conceptually.
- **Vertical success:** Y may fail while x succeeds.
- **Non-overlapping 2D rectangles:** Their projections can still overlap on one axis.
- **Large grid size:** It does not affect event count or runtime.
- **Helper name:** `countLineIntersections` actually counts completed projection groups.
- **Unused `n`:** It is part of the contract but unnecessary to the algorithm.
- **Input preservation:** Only new event tuples are sorted.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r)$. For $r$ rectangles, each axis list contains $2r$ events. Sorting both costs $O(r\log r)$ time, and both sweeps cost $O(r)$. Total time is $O(r\log r)$.
- **Auxiliary Space Complexity:** $O(r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
