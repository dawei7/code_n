# Guided Example: Maximum Points Activated with One Addition

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"points": [[1, 1], [1, 2], [2, 2]]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a 2D integer array `points`, where $\text{points}[i] = [x_{i}, y_{i}]$ represents the coordinates of the $i^{\text{th}}$ point. All coordinates in `points` are **distinct**.

The objective is to compute `4` from `{"points": [[1, 1], [1, 2], [2, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Represent coordinates as a bipartite graph

Create one kind of node for every x-coordinate and another kind of node for every y-coordinate. An existing point `(x,y)` becomes an edge between x-node `x` and y-node `y`.

Two points sharing an x-coordinate correspond to two edges incident to the same x-node. Two points sharing a y-coordinate correspond to edges incident to the same y-node. Following repeated activation steps is therefore the same as walking through connected edges in this bipartite graph.

An activation component of points is exactly one connected component of edge-bearing coordinate nodes. Starting from any point in that component eventually activates every point-edge in it and cannot reach an edge in another component.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"points": [[1, 1], [1, 2], [2, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Keep x and y namespaces separate

The numerical coordinate `5` used as an x-coordinate is not the same graph node as numerical coordinate `5` used as a y-coordinate. They represent different axes and should connect only when an actual point supplies an edge between them.

The source chooses `m = int(3e9)` and represents y-coordinate `y` as `y+m`. Original x-coordinates lie in `[-10^9,10^9]`, while shifted y-coordinates lie in `[2\cdot10^9,4\cdot10^9]`. These ranges are disjoint, so an x-node can never collide with a y-node.

For every point, `uf.union(x, y + m)` inserts its two coordinate nodes if needed and connects them. Path compression in `find` and union by component size make the sequence of operations almost linear.

The union-find `size` field counts coordinate nodes, not points. A component can have differing numbers of unique coordinates and point edges, so those sizes are not the desired activation counts.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count point edges per component

After all unions are complete, the source scans every point once. It finds the root of the point's x-node and increments `cnt[root]`.

The x-node and shifted y-node of that point were unioned, so either endpoint has the same final root. Counting through x is simply convenient. Each input point contributes exactly once, so `cnt[root]` is the number of existing points in that activation component.

It is important that counting occurs after all unions. Roots may change while later edges merge coordinate components; a counter built too early would need to be merged alongside union-find state.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"points": [[1, 1], [1, 2], [2, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Build a point-to-point graph:** Connect every pair sharing x or y, then find components. A coordinate with many points creates quadratically many explicit edges; coordinate-node union avoids that explosion.
- **Breadth-first activation for every possible new point:** The coordinate domain is infinite and repeated graph traversal is too expensive. Component compression reduces every choice to selecting at most two sizes.
- **Use raw numeric coordinates for both axes:** This falsely merges x-value `v` with y-value `v` even without a point connecting them. Separate types or a safe offset are mandatory.
- **Use union-find node sizes as point counts:** Coordinate-node count is not edge count. The separate `Counter` correctly counts actual points.
- **Sort component sizes:** Sorting works in `O(C\log C)` for `C` components, but only the largest two are needed and can be found linearly.
- **One existing component:** The result is `N+1`; the second-largest size remains zero.
- **One existing point:** Add a distinct point sharing either coordinate, activating both, so the answer is two.
- **Two components with chosen coordinate pair already occupied:** Impossible; such an existing edge would already unite the components.
- **New coordinates on both axes:** The added point activates only itself, which is never better when at least one existing point is available.
- **Duplicate maximum component sizes:** The streaming top-two logic keeps both equal values.
- **Distinct point guarantee:** It ensures each input edge is unique. Multiple points may still share one coordinate and are correctly joined.
- **Negative coordinates:** The offset keeps shifted y nodes disjoint even at the extreme negative bound.
- **Added point count:** The final plus one is essential because the return includes the newly inserted and initially activated point.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\alpha(N)$. Let `N` be the number of points. There are at most `2N` distinct coordinate nodes and exactly `N` point edges. The union phase performs `N` unions, and the counting phase performs `N` finds. With path compression and union by size, time is `O(N\alpha(N))`, where `\alpha` is the inverse Ackermann function.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
