# Guided Example: Maximum Number of Fish in a Grid

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]}`
- **Required output:** `7`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** 2D matrix `grid` of size `m x n`, where `(r, c)` represents:

The objective is to compute `7` from `{"grid": [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Every water component can be harvested completely

A fisher can move only between horizontally or vertically adjacent positive cells. Therefore, starting in one water cell permits reaching exactly its connected component of positive cells.

Every cell in that component can be visited and all its fish caught. No land cell can be crossed, so fish in a different component are unreachable from the same start.

The problem reduces to:

> Find the sum of each positive connected component and return the largest sum.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use zero as both land and visited marker

The input already uses zero to mean land. When DFS visits a positive cell, it stores its fish count locally and writes:

`grid[i][j] = 0`.

That cell now behaves like land for future searches, preventing revisits and cycles.

This removes the need for a separate visited matrix but intentionally mutates the input grid.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Generate the four directions compactly

The sequence:

`(-1, 0, 1, 0, -1)`

passed through `pairwise` yields:

$$
(-1,0),\ (0,1),\ (1,0),\ (0,-1).
$$

These are up, right, down, and left.

For each offset $(a,b)$, neighbor coordinates are $(i+a,j+b)$. Bounds checks ensure the cell exists, and `grid[x][y]` truthiness ensures it still contains positive fish.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `7` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `7` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Breadth-first search:** Uses an explicit queue and has the same $O(mn)$ bounds.
- **Separate visited matrix:** Preserves the grid at the cost of $O(mn)$ additional storage.
- **Union-find:** Can merge adjacent water cells and track component sums, but is heavier than a grid traversal.
- **All land:** No component starts and answer remains zero.
- **Single water cell:** Its fish value is one complete component total.
- **Diagonal water cells:** They are not connected because only four directions count.
- **Cycles within water:** Zeroing on entry prevents infinite recursion and double counting.
- **Several equal maximum components:** Only the maximum sum is returned, so identity does not matter.
- **Input mutation:** Every visited water cell becomes zero.
- **Small dimensions:** Recursion depth is bounded by at most 100 cells under the contract.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. Every cell is scanned by the outer loops, and every positive cell is entered by DFS exactly once. Each entry checks four neighbors. Total time is $O(mn)$.
- **Auxiliary Space Complexity:** $O(mn)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
