# Guided Example: Map of Highest Peak

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"isWater": [[0, 1], [0, 0]]}`
- **Required output:** `[[1, 0], [2, 1]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer matrix `isWater` of size `m x n` that represents a map of **land** and **water** cells.

The objective is to compute `[[1, 0], [2, 1]]` from `{"isWater": [[0, 1], [0, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The greatest legal height is distance to nearest water

Every water cell must have height zero, and moving across one grid edge can change height by at most one. If a cell is $d$ steps from a water cell, its height can be at most $d$: along that path, starting from zero, height can rise by at most one per step.

The strongest such upper bound comes from the nearest water cell. Therefore every legal assignment satisfies:

$$
\text{height}[i][j]
\le
\operatorname{distanceToNearestWater}(i,j).
$$

Assigning each cell exactly that nearest-water distance is legal. Neighboring cells' distances to the same source differ by at most one, water distances are zero, and all distances are nonnegative. Because this assignment reaches the pointwise upper bound at every cell, it maximizes the highest peak.

The exact solution computes these distances with multi-source breadth-first search.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"isWater": [[0, 1], [0, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Start BFS from every water cell

`ans` is initialized to minus one in every cell. Minus one means unvisited and cannot be confused with a valid height because heights are nonnegative.

The initialization scan places every water coordinate into deque `q` and sets its answer to zero. Instead of running a separate BFS from every water cell, all sources share one queue. They form distance layer zero simultaneously.

The problem guarantees at least one water cell, so the queue is initially non-empty.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `ans` is initialized to minus one in every cell.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Generate the four side-sharing neighbors

The source uses:

`pairwise((-1, 0, 1, 0, -1))`.

Adjacent pairs of this five-value sequence are:

- `(-1, 0)` for up,
- `(0, 1)` for right,
- `(1, 0)` for down,
- `(0, -1)` for left.

For current cell `(i, j)`, adding one pair `(a, b)` produces neighbor `(i + a, j + b)`. Diagonal movement is never generated.

The boundary checks `0 <= x < m` and `0 <= y < n` reject coordinates outside the matrix.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 0], [2, 1]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"isWater": [[0, 1], [0, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 0], [2, 1]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Run BFS from each land cell:** It repeats work:** - **Run BFS from each land cell:** It repeats work and can be far slower than one multi-source traversal.
- **Two-pass dynamic programming:** Forward and backward distance passes also achieve $O(RC)$ time with an output matrix, but the BFS proof is more direct for multiple sources.
- **Priority queue:** All grid edges have equal cost, so Dijkstra's heap is unnecessary; an ordinary deque gives linear time.
- **All cells water:** Every cell starts at zero, no new cell is discovered, and the maximum height is zero.
- **Single water cell:** Heights become Manhattan distances from that source.
- **Several water cells:** The first BFS wave to reach a cell comes from a nearest source.
- **One-row grid:** The method reduces to distance along a line.
- **One-column grid:** The same line-distance behavior applies vertically.
- **Water revisited from land:** Its zero marker prevents enqueueing again.
- **Equal shortest paths:** First discovery chooses one path, but only distance matters.
- **Minus-one sentinel:** It is safe because every legal height is nonnegative.
- **Four-direction tuple:** `pairwise` over five values deliberately closes the direction cycle.
- **No diagonal adjacency:** Only side-sharing moves are generated.
- **At least one source:** The stated guarantee ensures every cell receives a finite height.
- **Input preservation:** The returned assignment is independent of the original zero/one storage.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(RC)$. Let $R=m$ and $C=n$. The initialization scans all $RC$ cells. BFS enqueues and dequeues each cell once and examines four directions per cell. Total time is $O(RC)$.
- **Auxiliary Space Complexity:** $O(RC)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
