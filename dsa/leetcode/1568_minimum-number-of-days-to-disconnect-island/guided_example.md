# Guided Example: Minimum Number of Days to Disconnect Island

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` binary grid `grid` where `1` represents land and `0` represents water. An **island** is a maximal **4-directionally** (horizontal or vertical) connected group of `1`'s.

The objective is to compute `2` from `{"grid": [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate the only three possible answers

The result is always zero, one, or two.

- Zero days are needed when the grid already has zero islands or at least two islands.
- One day is enough when removing some single land cell makes the island count different from one.
- If neither condition holds, the grid-specific bound guarantees two removals suffice.

The exact stored solution tests these cases directly with repeated island counting. It does not implement the editorial's articulation-point algorithm.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count islands by destructive flood fill

Helper `count(grid)` scans every cell. When it finds a land value one, it starts `dfs` and increments `cnt`.

The recursive flood fill changes every reached land cell from one to two. It explores the four horizontal and vertical directions and continues only to in-bounds cells still equal to one.

Marking with two prevents revisiting cells without allocating a separate visited matrix. Once the full scan has counted all components, a second pair of loops changes every two back to one.

Therefore `count` restores all land cells it used as traversal marks before returning.

Diagonal contacts do not connect islands because DFS never uses diagonal directions.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Helper `count(grid)` scans every cell.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Check whether the grid is already disconnected

`minDays` first calls `count(grid)`.

If the result is not exactly one, the definition already calls the grid disconnected. This includes both all-water grids with zero islands and grids with multiple separate islands.

The method returns zero immediately in that case. Because `count` restores its temporary twos, this initial test does not leave traversal marks behind.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Tarjan articulation points:** Count initial is:** - **Tarjan articulation points:** Count initial islands and find a removable articulation land cell in one DFS, achieving $O(RC)$ time.
- **Explicit-stack flood fill:** It preserves brute-force logic while avoiding recursive depth limits.
- **Pair enumeration:** It is unnecessary because the two-day theorem lets the source return two directly.
- **Already all water:** Island count zero produces answer zero.
- **Several initial islands:** The grid is already disconnected and returns zero.
- **Single land cell:** Removing it produces zero islands and answer one.
- **Two adjacent land cells:** Either single removal leaves one island, so answer is two.
- **Articulation cell:** Its trial removal produces multiple islands and answer one.
- **Solid block:** It commonly has no single articulation cell and needs two removals.
- **Diagonal land cells:** They are separate islands because only four directions count.
- **Failed trial:** The removed cell is restored before continuing.
- **Successful trial mutation:** The exact source returns before restoring that cell.
- **Temporary marker two:** `count` converts all such markers back to one before returning.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V^2)$. Let $V=RC$ be cell count. One `count` call scans the grid, flood-fills each land cell at most once, and performs a restoration scan, costing $O(V)$ time.
- **Auxiliary Space Complexity:** $O(V)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
