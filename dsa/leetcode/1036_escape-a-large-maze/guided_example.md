# Guided Example: Escape a Large Maze

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"blocked": [[0, 1], [1, 0]], "source": [0, 0], "target": [0, 2]}`
- **Required output:** `false`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a 1 million by 1 million grid on an XY-plane, and the coordinates of each grid square are `(x, y)`.

The objective is to compute `false` from `{"blocked": [[0, 1], [1, 0]], "source": [0, 0], "target": [0, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why searching the whole grid is impossible

The grid has `10^6 \times 10^6` cells, so an ordinary search from source to target could examine up to a trillion positions. The key constraint is not grid size but the number of blocked cells: at most 200.

Such a small set of obstacles cannot form an enormous closed wall. It can only trap an endpoint inside a bounded region whose area is quadratic in the number of blockers. Once a search visits more cells than any possible enclosed region, it has proved that its start is not trapped. It does not need to continue all the way across the grid.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"blocked": [[0, 1], [1, 0]], "source": [0, 0], "target": [0, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The enclosure limit

Let `B = len(blocked)`. Arranging blockers diagonally against a grid boundary is the most efficient way to surround many open cells with few blocked cells. The resulting triangular region has on the order of

$$
\frac{B(B-1)}{2}
$$

reachable cells. A fully interior enclosure cannot beat the same quadratic scale because it needs blocked cells around all sides.

The code uses the conservative threshold

`m = B^2 // 2`.

This is at least as large as the standard maximum finite enclosure bound. Therefore, if a search visits more than `m` distinct cells, those cells cannot all lie inside a region sealed by the available blockers. The starting endpoint has escaped any possible blockade.

The threshold is a proof cutoff, not an estimate of the source-to-target distance. The endpoints may be hundreds of thousands of coordinates apart, yet exploring only about 20,001 cells is enough when `B = 200`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Blocked and visited sets

`s = {(x, y) for x, y in blocked}` converts blocked coordinates to tuples in a hash set. Membership checks then take expected constant time.

Each bounded DFS receives its own `vis` set. A coordinate is added as soon as its call begins. This prevents cycles and makes `len(vis)` the number of distinct open cells reached from that endpoint.

Source and target searches use separate visited sets because each must independently prove that its own endpoint is not enclosed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `false` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"blocked": [[0, 1], [1, 0]], "source": [0, 0], "target": [0, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `false` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Full-grid BFS or DFS:** It is logically correct but computationally impossible on up to `10^{12}` cells. The blocker-derived cutoff is essential.
- **Bounded breadth-first search:** A queue can perform the same two directional checks and stop after more than `m` discoveries. It avoids recursion-depth risk and has the same `O(B^2)` bounds.
- **Coordinate compression:** Compress rows and columns around obstacles and endpoints, preserving gaps between significant coordinates. This can solve the problem but requires careful treatment of large empty intervals and adjacency.
- **Search only from source:** This misses a target enclosed in a small region while the source is outside. Both directions are necessary.
- **Zero blockers:** Threshold zero makes both checks succeed immediately, which is correct for an open grid.
- **One blocker:** A single cell cannot enclose either endpoint, so the threshold also permits immediate escape proof.
- **Corner enclosure:** Grid boundaries act like free walls, allowing very few blocked cells to trap a corner. The DFS bounds checks and finite-region exhaustion detect it.
- **Target reached before cutoff:** The helper returns true immediately because a concrete path is stronger evidence than the enclosure argument.
- **Source and target far apart:** Distance does not increase the bounded search once both endpoints are known to be outside small enclosures.
- **Blocked coordinates as tuples:** Hash-set membership requires immutable tuple keys; visited coordinates use the same representation.
- **Separate visited sets:** Reusing the source set for the reverse check would not prove independent escape and could skip necessary exploration.
- **Grid outer boundary:** Coordinates equal to `-1` or `10^6` are rejected, so searches never leave the legal board.
- **Recursive implementation:** The mathematical cutoff can still exceed Python's default recursion depth. An iterative queue or stack preserves the algorithm when runtime stack limits are a concern.
- **Conservative threshold:** `B^2 // 2` may allow slightly more exploration than the tight triangular bound, but exceeding it still safely proves non-enclosure.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(B^2)$. Let `B` be the number of blocked cells. The threshold is `O(B^2)`. Each directional DFS visits at most the finite enclosed region or stops as soon as its visited count becomes `m + 1`. Each visited cell checks four neighbors, so both searches together take `O(B^2)` time.
- **Auxiliary Space Complexity:** $O(B^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
