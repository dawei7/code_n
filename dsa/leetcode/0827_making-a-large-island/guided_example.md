# Guided Example: Making A Large Island

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[1, 0], [0, 1]]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `n x n` binary matrix `grid`. You are allowed to change **at most one** `0` to be `1`.

The objective is to compute `3` from `{"grid": [[1, 0], [0, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why trying a flood fill separately for every zero is too slow

Changing one water cell to land can connect as many as four neighboring islands. A direct idea is to flip each zero temporarily and run a complete flood fill to measure the resulting island. An `n \times n` grid contains `O(n^2)` candidate zeroes, and one flood fill can inspect `O(n^2)` cells, leading to `O(n^4)` work.

The optimal solution separates the work into two passes:

1. discover every existing island once, give it an identifier, and record its size;
2. for each zero, add the sizes of the distinct islands touching it, plus one for the flipped cell.

Once island sizes are known, evaluating one zero needs only its four neighbors.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[1, 0], [0, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Keep labels separate from the input grid

The matrix `p` has the same dimensions as `grid` and begins filled with zeroes. For a land cell:

- `p[i][j] == 0` means the cell has not been assigned to an island yet;
- a positive value means the cell belongs to the island with that identifier.

The solution does not overwrite `grid`. It uses `p` as a parallel label matrix, which keeps the original distinction between water and land available during the second pass.

The `Counter` named `cnt` maps each positive island identifier to its number of cells. Identifier zero is reserved for “no island.” Because a `Counter` returns zero for a missing key, `cnt[0]` is harmless when a water neighbor's label is later encountered.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The four directions encoded compactly

`dirs = (-1, 0, 1, 0, -1)` and `pairwise(dirs)` produce:

- `(-1, 0)` for up;
- `(0, 1)` for right;
- `(1, 0)` for down;
- `(0, -1)` for left.

These are exactly the four directions allowed by the island definition. Diagonal cells are deliberately excluded.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[1, 0], [0, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Flood fill after every possible flip:** It repeats almost the same island discovery for each zero and can require `O(n^4)` time.
- **Disjoint set union:** Union adjacent land cells, store component sizes at roots, and combine distinct neighboring roots for each zero. It has the same near-linear-in-cells behavior but requires parent and size machinery.
- **Overwrite `grid` with island identifiers:** This can save the separate label matrix, provided identifiers do not conflict with 0 and 1. The exact solution preserves the input and stores labels in `p`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. The grid contains `n^2` cells. The labeling scan visits every position, and DFS labels every land cell once. Each labeled cell checks four neighbors, so the first phase takes `O(n^2)` time.
- **Auxiliary Space Complexity:** $O(n^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
