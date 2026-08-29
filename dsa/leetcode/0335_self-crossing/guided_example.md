# Guided Example: Self Crossing

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"distance": [2, 1, 1, 2]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of integers `distance`.

The objective is to compute `true` from `{"distance": [2, 1, 1, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use the geometry forced by ninety-degree turns.

Every segment is horizontal or vertical, and directions repeat north, west, south, east. Segment `i` is perpendicular to segments `i - 1`, `i - 3`, and `i - 5`, while it is parallel to segments `i - 2` and `i - 4`. The path's rigid turning pattern severely limits how the first self-intersection can occur.

Adjacent segments always share their ordinary endpoint; that required connection is not the self-crossing being tested. Segment `i - 2` is parallel to the current segment and separated by the positive-length intervening move, so it cannot be the first new intersection. For the first self-crossing, only three local configurations remain:

1. the current segment crosses or touches segment `i - 3`;
2. the current segment overlaps or touches segment `i - 4` after the path folds exactly onto the same line;
3. the current segment crosses or touches segment `i - 5` during the transition from an outward spiral to an inward spiral.

The source checks exactly these three cases for every `i` starting at `3`. No crossing is possible with fewer than four segments.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"distance": [2, 1, 1, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Normalize the current direction.

The inequalities are easier to understand if the picture is rotated so that the current segment `i` points north. Rotation does not change whether segments intersect. In that orientation, the recent directions are:

- segment `i`: north;
- segment `i - 1`: east;
- segment `i - 2`: south;
- segment `i - 3`: west;
- segment `i - 4`: north;
- segment `i - 5`: east.

Write $d_t=\text{distance}[t]$. All lengths are positive, so the orientation and relative placement are unambiguous.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Case one: cross the segment three moves back.

Place the start of segment `i - 3` at coordinate $(0,0)$. After moving west by $d_{i-3}$, south by $d_{i-2}$, and east by $d_{i-1}$, the current northward segment begins at

$$
(-d_{i-3}+d_{i-1},-d_{i-2}).
$$

Segment `i - 3` lies horizontally at height zero from $x=-d_{i-3}$ through $x=0$. The current vertical segment's $x$ coordinate lies on that horizontal range exactly when

$$
d_{i-1}\le d_{i-3}.
$$

The current segment begins $d_{i-2}$ below the horizontal line, so it reaches that line exactly when

$$
d_i\ge d_{i-2}.
$$

These are the source's first two-part condition:

`d[i] >= d[i - 2] and d[i - 1] <= d[i - 3]`.

Equality is intentional. It includes touching at an endpoint, which counts as the path crossing itself. For `[2,1,1,2]` at `i = 3`, `2 >= 1` and `1 <= 2`, so the eastward fourth segment reaches the first northward segment.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"distance": [2, 1, 1, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Construct every segment and compare with all earlier segments:** General axis-aligned intersection checks are straightforward, but comparing each new segment against the whole prefix takes $O(n^2)$ time. The turning pattern makes only three local configurations necessary.
- **Store every visited lattice point:** Distances can be as large as `100000`, so expanding moves into unit steps can require enormous time and memory. Crossings can also occur along segment interiors, which geometric inequalities handle directly.
- **Track full coordinates with a sweep-line structure:** This solves a more general segment-intersection problem in roughly $O(n\log n)$ time, but is unnecessary for the fixed counter-clockwise direction cycle.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of distances. The loop visits indices `3` through `n - 1` once. Each iteration performs a fixed number of arithmetic comparisons involving at most the previous five lengths. Total time complexity is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
