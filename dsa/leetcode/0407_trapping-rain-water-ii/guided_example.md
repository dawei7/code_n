# Guided Example: Trapping Rain Water II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"heightMap": [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an `m x n` integer matrix `heightMap` representing the height of each unit cell in a 2D elevation map, return *the volume of water it can trap after raining*.

The objective is to compute `4` from `{"heightMap": [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Water is limited by the lowest escape boundary

In one dimension, left and right maxima are enough. In a two-dimensional grid, water can escape along many winding paths to the outside, so four independent directional maxima do not solve the problem.

The key is to flood inward from the outer boundary. Every boundary cell can leak directly out of the map and therefore cannot hold water above its own terrain. As interior cells are reached, the lowest currently known enclosing boundary determines how high water can stand there.

A min-heap always processes the lowest effective boundary cell first. This is analogous to Dijkstra’s algorithm, but the path cost is the maximum height encountered along an escape path rather than a sum of edge weights.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"heightMap": [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What a heap height means

Each heap entry is `(h, row, column)`. The value `h` is not always the cell’s original terrain height. It is the effective boundary level carried into that cell:

- if the terrain is at least the incoming boundary, `h` is the terrain height;
- if the terrain is lower, water fills it to the incoming boundary, so `h` is that water-surface height.

This effective height is what can constrain neighboring cells. A filled depression behaves like boundary at its water surface, not like a hole at its original floor.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Initialize every outer cell

The nested initialization loops push every cell in the first row, last row, first column, or last column. They also mark it visited.

Because each coordinate is encountered once by the nested loops, corners are pushed only once even though each corner satisfies two boundary conditions.

These cells begin with their terrain heights. They form the initial frontier between the known outside and the unprocessed interior. Starting anywhere else would assume a containment level before proving how that region connects to an escape edge.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"heightMap": [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Four directional maxima:** The 1D trapping-water technique does not capture winding escape paths in two dimensions. A cell can leak around a high wall through a lower route.
- **Repeated global relaxation:** One could iteratively lower tentative water levels until stable, but this revisits cells many times. The min-heap finalizes levels in the correct order.
- **Minimax Dijkstra formulation:** Define each cell’s cost as the minimum possible maximum terrain height on a path to the boundary. Standard Dijkstra relaxation uses `max(current_cost, neighbor_height)`. This is exactly the effective-height algorithm described here.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\log N)$. Let $r$ be the number of rows, $c$ the number of columns, and $N=rc$ the number of cells.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
