# Guided Example: Number of Islands

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [["1", "1", "0"], ["1", "0", "0"], ["0", "0", "1"]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.

The objective is to compute `2` from `{"grid": [["1", "1", "0"], ["1", "0", "0"], ["0", "0", "1"]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: View the grid as an implicit graph

Every land cell is a graph vertex. An edge connects two land vertices when
their cells share a horizontal or vertical side. Under this interpretation, an
island is exactly one connected component of land vertices.

The algorithm scans every coordinate. Whenever it finds land that has not been
visited, that cell belongs to a new component. A depth-first traversal erases
the entire component, and the island count increases once.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [["1", "1", "0"], ["1", "0", "0"], ["0", "0", "1"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Encode the four allowed directions compactly

`dirs = (-1, 0, 1, 0, -1)` contains a circular sequence of coordinate offsets.
Applying `pairwise(dirs)` yields:

`(-1, 0), (0, 1), (1, 0), (0, -1)`

These are up, right, down, and left. Diagonal offsets never appear, matching
the Reference's four-direction connectivity rule. The repeated final `-1`
closes the pattern so four adjacent pairs encode all directions.

This concise construction requires `itertools.pairwise`, available in modern
Python versions. A literal tuple of four coordinate pairs would be more
portable to older Python runtimes.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `dirs = (-1, 0, 1, 0, -1)` contains a circular sequence of c... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Erase a component with recursive DFS

`dfs(i, j)` begins on a known land cell and immediately assigns
`grid[i][j] = '0'`. Changing land to water serves as the visited mark, so no
separate boolean matrix is required.

For each direction, it computes neighbor `(x, y)`, checks both row and column
bounds, and recurses only when the neighbor still contains `'1'`. Marking the
current cell before exploring neighbors is essential. Adjacent land cells can
point back to one another; early marking prevents that cycle from causing
unbounded recursive calls.

The traversal continues until every horizontally or vertically reachable land
cell has been changed to `'0'`. Water and out-of-bounds positions terminate a
direction without recursion.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [["1", "1", "0"], ["1", "0", "0"], ["0", "0", "1"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit DFS stack:** Push discovered coordina:** - **Explicit DFS stack:** Push discovered coordinates and mark on push; preserves $O(mn)$ worst-case space while avoiding `RecursionError`.
- **Breadth-first queue:** Equivalent component marking with different frontier order.
- **Union-find:** Join adjacent land cells and count remaining components; useful when connectivity is built incrementally but needs $O(mn)$ storage.
- **Separate visited set:** Preserves the input grid at the cost of additional memory.
- **All water:** No DFS starts and the answer remains zero.
- **All land:** One traversal erases every cell and returns one, but recursive depth can be unsafe.
- **Diagonal contact:** Does not connect islands because no diagonal direction is generated.
- **One cell:** Returns one for land and zero for water.
- **Rectangular guarantee:** Allows one shared column count `n`; ragged rows would break bounds assumptions.
- **Missing imports:** `List` and `pairwise` must be available in the execution environment.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. Let the grid have $m$ rows and $n$ columns. The outer scan examines $mn$ cells.
- **Auxiliary Space Complexity:** $O(mn)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
