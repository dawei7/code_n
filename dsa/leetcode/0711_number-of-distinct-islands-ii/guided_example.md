# Guided Example: Number of Distinct Islands II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 1]]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The objective is to compute `1` from `{"grid": [[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Collecting one island

The outer loops scan every grid cell. When a cell still contains `1`, a new `shape` list is created and `dfs` explores its entire four-directional component.

Each visited coordinate `[i, j]` is appended to `shape`, then `grid[i][j] = 0` marks it visited.

The four offsets `[1,0]`, `[-1,0]`, `[0,1]`, and `[0,-1]` include exactly vertical and horizontal neighbors. Boundary and land checks guard recursive calls.

Mutating land to water ensures every cell belongs to one DFS and every island is processed once.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why eight transformed shapes are sufficient

The symmetries of a square grid that preserve distances and adjacency consist of four rotations and four reflected rotations. For a coordinate `(i,j)`, the code generates:

- `(i,j)`;
- `(i,-j)`;
- `(-i,j)`;
- `(-i,-j)`;
- `(j,i)`;
- `(j,-i)`;
- `(-j,i)`;
- `(-j,-i)`.

These sign changes and coordinate swaps enumerate the full eight-element dihedral symmetry group. Some variants may coincide for a symmetric shape, which is harmless.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Removing absolute translation

After transformation, coordinates still contain the island's original location. Each variant list `e` is sorted lexicographically. Its first coordinate is the top-left-most point under that transformed orientation.

Every point then subtracts `e[0]`:

$$
(x,y)\mapsto(x-e_0.x,\ y-e_0.y).
$$

This moves the anchor to `(0,0)` and expresses every other cell relative to it. Translating the original island changes all coordinates by the same offset, which disappears under subtraction.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Traversal signatures for each symmetry:** Transform coordinates or traversal directions and choose a canonical signature. Coordinate sets are usually easier to reason about.
- **Only translation normalization:** That solves Distinct Islands I but would incorrectly separate rotated or reflected copies here.
- **Single-cell islands:** All eight variants normalize to `((0,0),)`, so every isolated cell shares one class.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L\log L)$. Let `L = RC` be the number of grid cells, and let island sizes be `a_1,a_2,\ldots` with total land at most `L`.
- **Auxiliary Space Complexity:** $O(RC)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
