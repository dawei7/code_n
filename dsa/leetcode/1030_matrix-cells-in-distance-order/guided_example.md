# Guided Example: Matrix Cells in Distance Order

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"rows": 1, "cols": 2, "rCenter": 0, "cCenter": 0}`
- **Required output:** `[[0, 0], [0, 1]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given four integers `row`, `cols`, `rCenter`, and `cCenter`. There is a `rows x cols` matrix and you are on the cell with the coordinates `(rCenter, cCenter)`.

The objective is to compute `[[0, 0], [0, 1]]` from `{"rows": 1, "cols": 2, "rCenter": 0, "cCenter": 0}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Manhattan distance is shortest-path distance in this grid

Treat every matrix cell as a vertex. Connect two vertices when their cells share an edge. Every move changes the row by one or the column by one, so each edge has unit cost.

To travel from `(rCenter, cCenter)` to `(r, c)`, any path must make at least `|r - rCenter|` vertical moves and `|c - cCenter|` horizontal moves. A path that makes exactly those moves exists inside the rectangular matrix: move toward the target row, then toward the target column. Its length is

$$
\lvert r-rCenter\rvert+\lvert c-cCenter\rvert.
$$

Therefore, the required Manhattan distance is exactly the unweighted graph distance from the center. Breadth-first search visits an unweighted graph in nondecreasing shortest-path distance, so its visitation order is already a valid answer order. No comparison sort is needed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"rows": 1, "cols": 2, "rCenter": 0, "cCenter": 0}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Initialize distance zero

The queue begins with `[rCenter, cCenter]`. The center is the unique cell at distance zero, so it must appear first.

The Boolean matrix `vis` records whether a cell has already been discovered. The center is marked immediately. Marking on enqueue, rather than waiting until dequeue, ensures that two neighboring cells cannot add the same coordinate twice.

The answer starts empty. A coordinate is appended when removed from the front of the queue, which is when BFS processes it in distance order.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The queue begins with `[rCenter, cCenter]`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the outer loop is divided into layers

At the start of each `while q` iteration, all cells currently in the queue belong to one distance layer. The expression `range(len(q))` snapshots how many such cells exist.

New neighbors discovered during that loop are appended to the back of the queue. They are one move farther away and are not included in the already-created `range`, so they wait until the next outer iteration.

Consequently, the algorithm appends all distance-zero cells, then all distance-one cells, then all distance-two cells, and so forth. The problem permits any order among cells with equal distance, so the precise order within a layer is irrelevant.

A standard FIFO BFS would preserve the same order even without the explicit layer loop. The loop makes the distance grouping visible and prevents any doubt that newly discovered cells are processed only after the current layer.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[0, 0], [0, 1]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"rows": 1, "cols": 2, "rCenter": 0, "cCenter": 0}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[0, 0], [0, 1]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Generate all cells and comparison-sort:** Comp:** - **Generate all cells and comparison-sort:** Compute each Manhattan distance and sort coordinates by it. This is simple but costs `O(M \log M)` time instead of exploiting bounded integer distance layers.
- **Bucket by distance:** The maximum possible distance is at most `rows + cols - 2`. Append every cell to its distance bucket and concatenate buckets. This also runs in `O(M + rows + cols)` time but requires explicit buckets.
- **Direct diamond-ring generation:** Enumerate coordinates at distance zero, one, two, and so on around the center. It can use little visited state, but handling clipped diamonds at matrix borders without duplicates is more error-prone.
- **Priority queue:** Push cells keyed by distance. It produces sorted order but adds `O(\log M)` overhead to each extraction even though BFS already supplies the correct layers.
- **One cell:** The queue contains only the center, which is appended and returned.
- **One row:** BFS expands left and right along a line, still producing nondecreasing absolute column distance.
- **One column:** The same reasoning applies vertically.
- **Center on a corner:** Every cell lies in directions inward from the corner; invalid outward neighbors are rejected by bounds checks.
- **Center in the interior:** Several cells share each distance. Any of their relative orders is accepted.
- **Duplicate discovery paths:** Marking at enqueue time prevents a coordinate from entering the queue more than once.
- **Tie ordering:** The up, right, down, left direction order determines one valid order among equal-distance cells, but correctness does not depend on that choice.
- **No obstacles:** Manhattan distance equals graph distance because every monotone row-and-column path stays within the rectangle. With obstacles, BFS distance could be larger and the problem would be different.
- **Imports supplied by the environment:** The exact solution uses `deque` and `pairwise`. They must be available from the solution environment, but they do not change the algorithmic reasoning.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M)$. Let `M = rows \cdot cols` be the number of cells. Every cell is enqueued once, dequeued once, appended once, and checks four neighbors. The constant factor of four does not change the bound, so time complexity is `O(M)`, matching the manifest.
- **Auxiliary Space Complexity:** $O(M)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
