# Guided Example: Number of Increasing Paths in a Grid

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[1, 1], [3, 4]]}`
- **Required output:** `8`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` integer matrix `grid`, where you can move from a cell to any adjacent cell in all `4` directions.

The objective is to compute `8` from `{"grid": [[1, 1], [3, 4]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count paths by their first cell

The memoized function `dfs(i, j)` counts all strictly increasing paths that start at cell `(i, j)`. Such a path has two possible forms:

- it stops immediately, using only the starting cell;
- it moves first to one of the four adjacent cells with a strictly larger value, then follows any increasing path starting there.

This gives a direct recurrence. Start `ans` at one for the single-cell path, and for every larger neighbor add that neighbor's `dfs` count.

The outer expression calls `dfs` for every cell and sums the results. Every increasing path has exactly one starting coordinate, so it belongs to exactly one of those counts.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[1, 1], [3, 4]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Generate the four directions from one compact sequence

`pairwise((-1, 0, 1, 0, -1))` produces the consecutive pairs

`(-1,0), (0,1), (1,0), (0,-1)`.

They represent up, right, down, and left. For each direction `(a, b)`, the candidate neighbor is `(i + a, j + b)`.

The bounds checks ensure the candidate stays inside the `m x n` matrix. The final comparison

`grid[i][j] < grid[x][y]`

permits movement only to a strictly larger value. Equal neighbors are deliberately excluded because the path must be strictly, not merely non-decreasingly, increasing.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Strict increase turns the grid into a directed acyclic graph

Imagine a directed edge from each cell to every larger adjacent cell. Along an edge, the grid value strictly rises. Following a directed cycle would require returning to the starting cell with a value greater than itself, which is impossible. The implicit graph is therefore a directed acyclic graph.

`dfs(i, j)` counts paths beginning at one vertex of this DAG. Its recursive calls always move forward to a larger value, so recursion must eventually reach a cell with no larger neighbor. At that sink, the count is one: the path containing the sink alone.

The acyclic property is also why no separate “currently visiting” marker is needed. There can be no recursive cycle.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `8` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[1, 1], [3, 4]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `8` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Kahn topological propagation:** Compute indegrees in the increasing-edge DAG, start from local minima, and propagate path counts toward larger cells. This is iterative `O(mn)` time and space and avoids recursion depth.
- **Sort all cells by value:** Process from largest to smallest for starting-path counts or smallest to largest for ending-path counts. This is straightforward but costs `O(mn \log(mn))` time.
- **DFS toward smaller neighbors:** Define the state as paths ending at the current cell instead. This is equally valid if the outer sum and comparison direction remain consistent.
- **Plain DFS without cache:** Overlapping suffix subproblems would be recomputed many times and can cause exponential work.
- **Allow equal-valued moves:** That violates strict increase and can also introduce directed cycles between equal neighbors, invalidating the simple recursion.
- **One cell:** `dfs` returns its single-cell path, and the total is one.
- **All values equal:** No edge passes the strict comparison, so the answer is the number of cells.
- **Several cells with the same value:** They are distinct possible single-cell paths but cannot move directly between equal values.
- **Multiple paths with identical value sequences:** They are still different when their coordinate sequences differ, and separate neighbor branches count them separately.
- **Local maximum:** It has no larger neighbor, so its only starting path is itself.
- **Local minimum:** It may begin many paths through different larger neighbors; their disjoint second steps make addition correct.
- **Very long increasing path:** The mathematical count is correct, but recursive depth can exceed the Python interpreter limit.
- **Modulo during recursion:** Reducing each addition preserves the final answer and prevents exponential-size cached integers.
- **Availability of helpers:** The exact source relies on `cache` and `pairwise` being provided by the Python environment, conventionally from `functools` and `itertools`.
- **Input preservation:** No cell is marked or reordered; all traversal state lives in the function cache.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N = mn` be the number of cells. Memoization fully evaluates each cell once, and each evaluation checks exactly four directions. Cache hits are constant-time expected dictionary operations. Total running time is `O(N) = O(mn)`.
- **Auxiliary Space Complexity:** $O(mn)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
