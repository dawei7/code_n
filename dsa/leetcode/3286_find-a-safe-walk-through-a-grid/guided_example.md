# Guided Example: Find a Safe Walk Through a Grid

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]], "health": 1}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` binary matrix `grid` and an integer `health`.

The objective is to compute `true` from `{"grid": [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]], "health": 1}` while avoiding redundant calculations and unnecessary overhead.

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

Entering an unsafe cell costs one health; entering a safe cell costs zero. The starting cell's value also reduces health, which is why `dist[0][0] = grid[0][0]`. The problem becomes finding the minimum total cell cost along any path from the upper-left to lower-right.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]], "health": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

`dist[x][y]` stores the best cost discovered for a cell. It begins at infinity except at the start. The deque initially contains the start.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

For each popped cell, the source tries four directions produced by consecutive pairs of `(-1,0,1,0,-1)`. A neighbor is relaxed when the current distance plus its binary cell value is smaller than the recorded distance. The new cell is appended to the deque.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]], "health": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **true 0-1 BFS:** Use `appendleft` for a neighbor with value zero and `append` for value one. This provides the advertised linear bound.
- **Dijkstra:** A min-heap gives $O(mn\log(mn))$ worst-case time and straightforward shortest-path guarantees.
- **Ordinary BFS with visited cells:** It minimizes steps, not unsafe-cell count, and can reject a longer but healthier path.
- **DFS over all paths:** Cycles and exponentially many routes make direct enumeration unsuitable.
- **Cost equal to health:** Remaining health is zero, so the answer is false.
- **Unsafe destination:** Its one cost must be included before checking positivity.
- **Safe zero-cost cycles:** Strict improvement prevents endless equal-distance enqueueing.
- **One row or column:** The algorithm follows the only corridor and sums its unsafe cells.
- **Several optimal paths:** Only their shared minimum cost matters.
- **Start unsafe:** `dist[0][0]` correctly begins at one.
- **Missing `pairwise` import:** Standalone execution requires the itertools import if absent from the harness.
- **No early exit:** FIFO order does not guarantee the first destination pop is final, so computing until the deque empties is appropriate.
- **Why step count is irrelevant:** Safe cells can make a longer route cost less health than a short route. The distance metric is accumulated cell values, not number of moves.
- **Relaxing back toward the start:** Cyclic movement can propose the start again, but its existing minimal cost cannot be improved by adding nonnegative cell costs, so it is not re-enqueued.
- **Destination unreachable geometrically:** A rectangular grid with four-direction movement and no blocked cells is always connected; failure comes only from insufficient health.
- **Health pruning opportunity:** A relaxation with cost at least health cannot belong to a successful path because later costs are nonnegative. The source does not use this optional optimization.
- **Zero-weight ordering defect:** Appending a zero-cost neighbor at the back may delay it behind higher-cost work and cause later reprocessing. `appendleft` is the precise change that restores 0-1 BFS ordering.
- **Distance versus remaining health:** Minimizing cost maximizes final health because initial health is constant. This equivalence justifies solving a shortest-path problem.
- **Starting-cell convention:** The source charges `grid[0][0]` before any move. This matches examples and the notion that occupying an unsafe start reduces health.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V+E)$. Let $V=mn$ and $E=O(mn)$ grid edges. The distance table and deque use $O(mn)$ space.
- **Auxiliary Space Complexity:** $O(mn)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
