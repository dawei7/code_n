# Guided Example: Check if the Rectangle Corner Is Reachable

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"xCorner": 3, "yCorner": 4, "circles": [[2, 1, 1]]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two positive integers `xCorner` and `yCorner`, and a 2D array `circles`, where $\text{circles}[i] = [x_{i}, y_{i}, r_{i}]$ denotes a circle with center at $(x_{i}, y_{i})$ and radius $r_{i}$.

The objective is to compute `true` from `{"xCorner": 3, "yCorner": 4, "circles": [[2, 1, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

The forbidden regions are closed disks: the path may neither enter nor touch any circle. Trying to construct a curve explicitly is difficult because there are infinitely many possible paths. The solution instead asks when the union of the disks forms a continuous barrier across the rectangle. This turns geometry into connectivity among circles and rectangle sides.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"xCorner": 3, "yCorner": 4, "circles": [[2, 1, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Name the start corner bottom-left and the destination top-right. Group the left and top sides together, and group the right and bottom sides together. A connected forbidden component that touches at least one side in the first group and at least one side in the second group separates the two corners. The possible contacts include left-to-right, top-to-bottom, left-to-bottom, and top-to-right barriers. Conversely, if neither corner is covered and no relevant disk component connects those opposing boundary groups, there remains a route through the rectangle's free region.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Reject a covered endpoint first.** The helper `in_circle` compares the squared center-to-point distance with `r ** 2`. It is called for both `(0, 0)` and `(xCorner, yCorner)`. The comparison uses `<=` because touching a circle is forbidden. If either endpoint lies on or inside any disk, no legal path can even begin or end, so the method immediately returns `false`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"xCorner": 3, "yCorner": 4, "circles": [[2, 1, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Disjoint-set union:** Create two conceptual boundary nodes and union every relevant overlapping circle pair plus each circle's boundary contacts. Testing whether the boundary nodes become connected gives the same $O(n^2)$ time and $O(n)$ space, avoids recursion depth, and often makes the connectivity interpretation explicit.
- **Explicit adjacency lists:** Precomputing all relevant edges and then running BFS or DFS is straightforward, but it can store $O(n^2)$ edges. The source recomputes pair relations while scanning and needs only `vis`.
- **Union every intersecting pair in the plane:** This simpler test is unsafe. An overlap outside the rectangle must not connect two obstacles for a path constrained to the rectangle; the weighted coordinate filter prevents that false connection.
- **Grid search:** Rasterizing the rectangle loses exactness and is impossible when coordinates reach $10^9$. Narrow passages can also disappear or appear depending on grid resolution.
- **Attempt a straight segment only:** A blocked diagonal does not imply that every curved path is blocked. Reachability depends on topological separation by obstacle components, not on visibility along one line.
- **A circle touching the start or destination:** The immediate `in_circle` checks return false reachability, including exact tangency, because the path is forbidden from touching a disk.
- **Tangent circles:** The disk-overlap comparison uses `<=`, so externally tangent disks are connected. There is no positive-width gap between closed forbidden regions, and a path may not pass through their touching point.
- **A circle entirely outside the rectangle:** It has no relevant boundary contact and normally no accepted interior connection, so it does not affect the result. Example four is of this form.
- **One disk touches only left and top:** Both contacts belong to the same boundary group, so they do not alone prove separation. A connection to right or bottom is still required.
- **One disk touches left and bottom:** Those sides belong to opposite groups, so DFS begins from its left contact and immediately succeeds through its bottom contact. The component traps the starting corner's side of the rectangle even if the corner itself is outside the disk.
- **Strict weighted upper-bound tests:** The source uses `<` rather than `<=` for the weighted point's right/top coordinates. This is part of its definition of an overlap relevant to the rectangle interior; changing the comparisons without a fresh geometric proof can alter boundary-only configurations.
- **Long chains of circles:** Connectivity is transitive. No single circle needs to touch both boundary groups; DFS correctly detects a chain in which neighboring disks overlap and only the two end disks touch the respective sides.
- **Deep recursion:** With up to one thousand vertices, an iterative DFS or DSU is operationally safer in Python. The recursive source may encounter a `RecursionError` on a sufficiently deep overlap chain even though its geometric reasoning and asymptotic bounds are otherwise sound.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let $n$ be the number of circles. A visited circle scans all $n$ circles in its DFS loop. Each circle is visited at most once, so there are at most $n^2$ pair examinations. The outer endpoint and boundary checks add only $O(n)$ work. Every geometric test uses a constant number of integer operations, giving $O(n^2)$ time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
