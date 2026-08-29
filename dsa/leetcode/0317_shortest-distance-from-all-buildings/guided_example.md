# Guided Example: Shortest Distance from All Buildings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]}`
- **Required output:** `7`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` grid `grid` of values `0`, `1`, or `2`, where:

The objective is to compute `7` from `{"grid": [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why searching from buildings is equivalent

Legal movement between empty cells is undirected. If an empty cell can reach a building along a path of passable empty cells ending beside that building, the same path can be followed in reverse from the building to the empty cell.

Therefore, instead of starting one search from every candidate land cell, the algorithm can start from each building and distribute that building's distance to all reachable candidates. Summing those contributions later gives the same total distance for each land cell.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The two accumulation matrices

`cnt[r][c]` is the number of processed building searches that reached empty cell `(r, c)`.

`dist[r][c]` is the sum of the shortest distances from those buildings to that cell.

These meanings must be kept separate. A small distance sum is irrelevant if only some buildings can reach the cell. The count matrix proves universal reachability; the distance matrix provides the objective value once reachability is established.

Both matrices start at zero. Buildings and obstacles never need meaningful entries because the final house candidate must have original grid value zero.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Starting one building BFS

When the outer grid scan finds `grid[i][j] == 1`, it increments `total`, places `(i, j)` in the queue, resets level distance `d = 0`, and creates a fresh visited set `vis`.

The visited set is local to one building. An empty cell should be counted once for each different building, so visitation information must not carry across searches. Within one search, however, a cell may be reachable by several paths and must be accumulated only once at its shortest distance.

The queue object is created before the outer scan but is empty after every completed BFS. Each building appends its start only after the previous search has drained the queue, so searches remain independent.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `7` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `7` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Grid-marker pruning between building searches:** After each BFS, mutate reachable zeros to the next marker and let the next building traverse only cells reached by all prior buildings. This can prune impossible regions and avoid a fresh visited matrix, but the exact source uses independent sets.
- **BFS from every empty land:** Sum distances to buildings from each candidate. It is correct but can be much slower when empty cells greatly outnumber buildings.
- **Manhattan distance:** It ignores obstacles and impassable buildings, so it can underestimate or claim a route where none exists.
- **Multi-source BFS from all buildings at once:** It finds distance to the nearest building, not the sum of separate shortest distances to every building.
- **DFS:** It can discover reachability but does not naturally guarantee shortest paths in an unweighted graph without additional distance relaxation.
- **Reuse one visited set across buildings:** This would prevent later buildings from contributing to cells already visited by earlier searches.
- **Mark at dequeue time:** The same cell may enter the queue multiple times from one level, corrupting counts and sums.
- **Allow traversal through a building:** The rules make buildings impassable, so another building cannot serve as a corridor.
- **One building and adjacent land:** That land receives count one and distance one, yielding answer one if no closer legal cell exists.
- **Only a building:** There is no empty candidate; infinity remains and the answer is `-1`.
- **Unreachable region:** Its cells have reach count below `total` and are excluded regardless of their partial distance sum.
- **Several equal optima:** The problem asks only for the minimum distance, so no coordinate tie handling is needed.
- **Obstacles enclosing a building:** If that prevents every empty cell from reaching all buildings, no count reaches `total` and the method returns `-1`.
- **Boundary cells:** Explicit range tests prevent grid wrapping and out-of-bounds access.
- **At least one building:** `total` is positive, so a never-reached empty cell with count zero cannot accidentally qualify.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(bmn)$. Let $m$ be the row count, $n$ the column count, and $b$ the number of buildings.
- **Auxiliary Space Complexity:** $O(mn)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
