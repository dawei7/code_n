# Guided Example: Shortest Path in Binary Matrix

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[0, 1], [1, 0]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an `n x n` binary matrix `grid`, return *the length of the shortest **clear path** in the matrix*. If there is no clear path, return `-1`.

The objective is to compute `2` from `{"grid": [[0, 1], [1, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Interpret the open cells as an unweighted graph

Every cell containing zero is a graph vertex that may be visited. Two open cells share an edge when their row and column differ by at most one and they are not the same cell. This gives horizontal, vertical, and diagonal movement, for at most eight neighbors per cell.

Every move has equal cost: entering one adjacent cell extends the path length by one visited cell. In an unweighted graph, breadth-first search is the natural shortest-path algorithm because it explores vertices in nondecreasing distance from the start.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[0, 1], [1, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reject a blocked starting point

Any clear path must include the top-left cell. If `grid[0][0]` is one, the start is blocked and no valid path exists, so the method immediately returns `-1`.

There is no separate initial test for a blocked destination. That is still correct. A blocked bottom-right cell is never enqueued because only cells equal to zero are discovered, so the queue eventually empties and the function returns `-1`. For a one-cell grid, the start and destination are the same cell, and the start test handles the blocked case.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Any clear path must include the top-left cell.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Mark a cell when it enters the queue

The open start is changed from zero to one, then coordinate `(0, 0)` is placed in the deque. In this implementation, writing one does not store the numeric distance; it is simply a visited mark. Original blocked cells and visited open cells both contain one afterward, and that is sufficient because the search only needs to distinguish undiscovered open cells from cells that must not be enqueued.

Marking happens at enqueue time, not dequeue time. This prevents two frontier cells from adding the same neighbor before either copy is processed. Consequently, every open cell enters the queue at most once, which avoids duplicate work and preserves a simple space bound.

The method intentionally mutates `grid`. Reusing the input later as the original obstacle matrix would require making a copy or maintaining a separate visited set.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[0, 1], [1, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Separate visited matrix:** Preserve `grid` and:** - **Separate visited matrix:** Preserve `grid` and store discovery state in another Boolean matrix. The time remains $O(n^2)$ and the space remains $O(n^2)$, but the caller’s input is not modified.
- **Store distance in each queue entry:** Enqueue `(row, column, distance)` and return that distance at the target. This avoids the layer-size loop but adds one integer to every queued record.
- **Write distances into the grid:** Replace each discovered zero with its distance rather than a generic one. This can make debugging clearer, though original blocked ones then overlap with the start distance unless the interpretation is handled carefully.
- **Depth-first search:** DFS can determine reachability but does not discover paths in increasing length. Finding the shortest path would require exploring many alternatives and maintaining a best value.
- **Dijkstra’s algorithm:** It is correct because all edges have nonnegative weight, but a priority queue is unnecessary when every move costs exactly one. BFS is simpler and faster.
- **A-star search:** A suitable heuristic such as Chebyshev distance can guide exploration toward the target and often visit fewer cells. Worst-case complexity remains comparable, and the implementation is more delicate.
- **Blocked start:** The immediate `-1` return is necessary because no clear path may include a cell containing one.
- **Blocked destination:** It is never enqueued, so the search exhausts reachable open cells and returns `-1`.
- **One open cell:** Start equals destination, and the returned path length is one rather than zero because length counts visited cells.
- **Diagonal-only path:** Diagonal neighbors are included, so `[[0,1],[1,0]]` correctly returns two.
- **Current cell in the nested ranges:** It is skipped by the visited mark. Removing it explicitly would be an optional micro-clarification, not a correctness requirement.
- **Negative indices:** Bounds must be checked before grid access to prevent Python from treating `-1` as the last row or column.
- **Multiple shortest paths:** A cell is kept only on its first discovery, but BFS first discovery already has minimum distance. Other equally short routes need not enqueue it again.
- **No path:** Emptying the queue means the entire reachable component of the start was explored without finding the target.
- **Input reuse:** Because open visited cells are overwritten with one, callers that need the original matrix must copy it before calling this method.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let $n$ be the side length, so the matrix contains $n^2$ cells. A cell is enqueued at most once because it changes from zero to one before entering the queue. Processing it examines exactly nine coordinate pairs, a constant amount of work. Total time is therefore $O(n^2)$.
- **Auxiliary Space Complexity:** $O(n^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
