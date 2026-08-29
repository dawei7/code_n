# Guided Example: As Far from Land as Possible

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[1, 0, 1], [0, 0, 0], [1, 0, 1]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an `n x n` `grid` containing only values `0` and `1`, where `0` represents water and `1` represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return `-1`.

The objective is to compute `2` from `{"grid": [[1, 0, 1], [0, 0, 0], [1, 0, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reverse the viewpoint: expand from every land cell

For each water cell, the desired value is its distance to the nearest land cell. Running a separate breadth-first search from every water cell would repeat most of the same exploration.

Instead, place all land cells into one queue before the search begins. This is multi-source breadth-first search. It behaves as if a new virtual source were connected to every land cell with zero-cost edges. The first search wave reaches all water cells at distance one, the next reaches distance two, and so on.

Because the final wave contains the water cells with the greatest nearest-land distance, the number of completed waves gives the answer.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[1, 0, 1], [0, 0, 0], [1, 0, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Initialize every distance-zero source

The deque comprehension scans all `n^2` coordinates and inserts `(i, j)` whenever `grid[i][j]` is one. These are exactly the land cells, and each has distance zero from the nearest land because it is land itself.

The early condition handles the two invalid result cases:

- an empty queue means there is no land, so no water cell has a finite distance to land;
- a queue of size `n * n` means every cell is land, so there is no water cell to choose.

Both return the initial `ans = -1` as required.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Process one distance layer at a time

At the beginning of a `while q` iteration, the queue contains all cells at one BFS distance layer. `range(len(q))` captures that layer's size before any new cells are appended.

Every current cell explores its four orthogonal neighbors. The compact direction tuple

`(-1, 0, 1, 0, -1)`

combined with `pairwise` produces the offsets up `(-1, 0)`, right `(0, 1)`, down `(1, 0)`, and left `(0, -1)`. These are exactly the moves whose shortest-path length equals Manhattan distance.

A neighbor is accepted only when it lies inside the grid and its current value is zero. The solution immediately changes it to one and appends it.

Changing the grid at discovery time is the visited marker. Immediate marking is important: if two cells in the current frontier can both reach the same water cell, the first one marks it before the second examines it, so the cell enters the queue only once.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[1, 0, 1], [0, 0, 0], [1, 0, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **BFS from every water cell:** This repeats searches and can take `O(n^4)` time on an `n` by `n` grid.
- **Dynamic programming in directional passes:** Distances can be propagated with forward and backward scans in `O(n^2)` time. Multi-source BFS more directly matches unweighted Manhattan layers.
- **Use a separate visited set:** It preserves the input but adds another `O(n^2)` structure. The exact solution intentionally marks the grid.
- **Mark cells when dequeued:** Several parents could enqueue the same water cell before its first dequeue. Marking at discovery prevents duplicates.
- **No land:** The initial queue is empty and the answer is `-1` because nearest-land distance is undefined.
- **No water:** Every cell is already in the source queue and the answer is `-1` because there is no candidate water cell.
- **One land cell:** BFS radiates from that source, and the farthest grid position determines the result.
- **Several land cells:** Their waves run simultaneously; the first wave to reach a water cell automatically represents its nearest source.
- **One-cell grid:** It is either all land or all water, so the early condition returns `-1`.
- **Input mutation:** Every visited water cell becomes one. A caller needing the original grid would have to pass a copy, adding `O(n^2)` space.
- **Only orthogonal movement:** Diagonal steps are not explored because Manhattan distance counts horizontal and vertical moves only.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. There are `n^2` cells. Initial source collection scans all of them once. Each water cell is marked and enqueued at most once, and each dequeued cell examines exactly four neighbors. Total time is `O(n^2)`.
- **Auxiliary Space Complexity:** $O(n^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
