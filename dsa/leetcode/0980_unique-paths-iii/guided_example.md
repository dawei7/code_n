# Guided Example: Unique Paths III

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` integer array `grid` where $\text{grid}[i][j]$ could be:

The objective is to compute `2` from `{"grid": [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn the grid into a search over complete walks

A walk is valid only when it satisfies all three requirements at once: it begins at the unique square containing `1`, ends at the unique square containing `2`, and visits every square other than an obstacle exactly once. Merely reaching the ending square is therefore not enough. The algorithm must remember which squares the current walk has used and how many steps it took before reaching the end.

Depth-first search with backtracking fits this requirement because every choice of the next square creates a separate possible continuation. The search follows one continuation as far as it can, counts it if it becomes a complete valid walk, and then reverses its last choice so that another continuation can reuse the square. This systematically explores possible walks without allowing one attempted walk to contaminate another.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Read the fixed information before searching

The dimensions are stored as `m` and `n`. A generator expression scans the grid to find the coordinates of the starting square:

`start = next((i, j) ... if grid[i][j] == 1)`.

The statement guarantees exactly one start, so `next` will find one coordinate and no fallback is necessary. The code also computes

`cnt = sum(row.count(0) for row in grid)`,

which is the number of ordinary empty squares. Notice that `cnt` deliberately excludes the start and end. That detail explains the less obvious condition used when the search reaches the ending square.

The visited set initially contains only `start`. Therefore, the search can never step back onto the starting square, and every coordinate subsequently added to the set represents a square already used by the current walk.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Understand exactly what the step counter means

The recursive call `dfs(i, j, k)` means that the walk is currently at `(i, j)` and has made exactly `k` moves from the starting square. The first call is `dfs(*start, 0)`, so the start itself corresponds to zero moves.

Suppose there are `cnt` empty squares. A complete walk visits, in order, the start, all `cnt` empty squares, and the end. That is `cnt + 2` visited squares. A walk through that many squares contains one fewer moves, so it reaches the end after exactly `cnt + 1` moves. Consequently,

`return int(k == cnt + 1)`

returns `1` precisely when every empty square has been included, and `0` when the end was reached too early. Converting the Boolean comparison to an integer makes the base case directly contribute either one valid walk or no valid walk to the total.

The function returns immediately whenever it sees the end. It must not treat the ending square as an ordinary intermediate square and walk away from it: the required walk ends there. If it arrived too early, that branch is invalid and cannot be repaired by leaving the end and returning later.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Bitmask dynamic programming:** Encode the visited squares in a bitmask and memoize a state such as `(position, mask)`. This can avoid recomputing equivalent states and gives a subset-state formulation, but it uses substantially more memory and is more complicated than the exact backtracking implementation shown here.
- **In-place visited marking:** Temporarily replace a grid value with an obstacle-like marker and restore it after recursion. This removes the explicit set but mutates the input during the search and requires especially careful restoration.
- **Copying the visited set:** Passing a new set to every child is conceptually simple, but copying up to `V` coordinates at every branch adds unnecessary allocation and time. Add–recurse–remove provides the same isolation efficiently.
- **Reaching the end early:** Such a branch must contribute zero even if the destination is reachable, because some required square remains unvisited. The `k == cnt + 1` check enforces this.
- **Counting only zero squares:** The move target is `cnt + 1` rather than `cnt` because the final move enters the ending square, while the starting square requires no move.
- **Obstacles:** They are never added to `vis` because the eligibility condition rejects `-1` before recursion.
- **Start and end positions:** Nothing assumes corners or a particular orientation; the preliminary scan finds the start wherever it occurs, and the base case recognizes the end by its grid value.
- **Narrow grids and dead ends:** A single row, single column, or corridor works naturally. A branch with no eligible neighbor returns its current `ans` of zero unless it already ended successfully.
- **Input preservation:** Since only `vis` changes, the caller receives the grid with exactly its original values after the method returns.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V2^V)$. Let `V` be the number of non-obstacle squares, including the start and end. Scanning the grid for the start and counting zero squares takes `O(mn)` time.
- **Auxiliary Space Complexity:** $O(V)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
