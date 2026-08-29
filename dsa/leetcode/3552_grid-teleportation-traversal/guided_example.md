# Guided Example: Grid Teleportation Traversal

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"matrix": ["A..", ".A.", "..."]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a 2D character grid `matrix` of size `m x n`, represented as an array of strings, where $\text{matrix}[i][j]$ represents the cell at the intersection of the $i^{\text{th}}$ row and $j^{\text{th}}$ column. Each cell is one of the following:

The objective is to compute `2` from `{"matrix": ["A..", ".A.", "..."]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Modeling the grid as a graph

Treat every traversable cell as a graph vertex. Up, down, left, and right moves create weight-one edges when the destination is inside the grid and is not `'#'`. If several cells contain the same letter, any one of them can teleport to any other at weight zero while that letter is available.

The answer is the shortest-path distance from vertex `(0, 0)` to vertex `(m - 1, n - 1)`. This graph interpretation is valuable because “minimum number of moves” becomes a standard shortest-path question, while free teleports explain why edge weights are not uniform.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"matrix": ["A..", ".A.", "..."]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Collecting portal groups before the search

The dictionary `g` maps each uppercase letter to the coordinates carrying that letter. The initial double loop visits every grid cell once and appends portal coordinates to their group. Empty cells and obstacles are not added.

This preprocessing allows the search to find all zero-cost destinations of a portal immediately. Without it, reaching a letter would require rescanning the entire grid to locate matching cells, potentially repeating that expensive scan many times.

The check `c.isalpha()` identifies the portal cells under the stated input alphabet. The constraints promise uppercase English letters, dots, or hash marks, so alphabetic cells are precisely portals.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How 0-1 BFS orders work

The matrix `dist` starts at infinity everywhere except `dist[0][0] = 0`. The deque `q` initially contains only the start.

When a transition improves a distance, its destination is scheduled according to its edge cost:

- a zero-cost teleport is inserted with `appendleft`, at the front;
- a one-cost grid move is inserted with `append`, at the back.

This maintains the key 0-1 BFS ordering: work reachable at the current distance is handled before work that costs one more move. It plays the same role as Dijkstra’s minimum-priority extraction, but a deque is enough because there are only two possible increments.

When `(i, j)` is popped, the source reads `d = dist[i][j]`. It does not store an old distance inside the deque entry. If a coordinate was scheduled and later improved before being processed, the pop therefore uses its newest, smaller distance. Relaxation still occurs only for a strict improvement, so equal-distance discoveries do not cause pointless reinsertions.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"matrix": ["A..", ".A.", "..."]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Dijkstra’s algorithm:** A binary-heap shortest-path search correctly handles zero- and one-cost edges and is easier to generalize to larger weights, but it costs `O(mn \log(mn))` here. 0-1 BFS exploits the restricted weights to obtain linear time.
- **Ordinary BFS:** Treating teleports and grid steps identically would charge the wrong cost, while processing free portal destinations without deque priority can finalize cells in the wrong order. Plain BFS is suitable only when every edge costs the same amount.
- **Explicit portal-clique edges:** Connecting every pair of equal-letter cells makes the graph conceptually direct, but a group of `k` portals would create `O(k^2)` edges. Storing each group once and expanding it once represents the same useful reachability in linear total work.
- **State including a used-letter mask:** Such a state is unnecessary and could multiply the search space by `2^{26}`. Any repeated use of one letter can be compressed into a single free jump between the first and final same-letter cells.
- **One-time group deletion:** Removing `g[c]` is safe only because the first expansion occurs at the minimum reachable distance and reaches the entire same-letter group at zero cost. This shortest-path argument is the reason the optimization is correct.
- **A portal appearing once:** Its group expansion checks only that same cell and creates no useful transition. Deleting the group still prevents repeated work.
- **Starting on a portal:** The source may teleport before making any ordinary move, because the start is processed at distance zero.
- **Starting at the destination:** In a `1 x 1` grid, the first popped coordinate is already the bottom-right cell, so the method returns zero even if that cell contains a portal.
- **Obstacle destination:** Obstacles are never enqueued as ordinary-move destinations. If the bottom-right cell is an obstacle in an input beyond the stated practical assumptions, it is unreachable unless it is also the start, which cannot simultaneously be `'#'` because the start is guaranteed non-obstacle.
- **Unreachable open regions:** The deque eventually empties after exploring the start’s entire reachable component, and `-1` is returned.
- **Multiple shortest routes:** Strict improvement checks avoid rescheduling a cell for an equal distance. Keeping one shortest distance is sufficient; the problem asks only for the minimum count, not for the number or reconstruction of shortest routes.
- **Large portal groups:** Every coordinate in the group is scanned together only once, which is essential for grids as large as `10^3 x 10^3`.
- **Portal-letter semantics:** The proof relies on every occurrence of a letter being mutually reachable by one free teleport. If portals instead formed directed pairs or charged different costs, the group-expansion model would need to change.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. Let `N = mn` be the number of grid cells. Building portal groups scans all `N` cells once, taking `O(N)` time.
- **Auxiliary Space Complexity:** $O(mn)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
