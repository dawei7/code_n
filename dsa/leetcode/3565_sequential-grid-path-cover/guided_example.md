# Guided Example: Sequential Grid Path Cover

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[0, 0, 0], [0, 1, 2]], "k": 2}`
- **Required output:** `[[0, 0], [1, 0], [1, 1], [1, 2], [0, 2], [0, 1]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a 2D array `grid` of size `m x n`, and an integer `k`. There are `k` cells in `grid` containing the values from 1 to `k` **exactly once**, and the rest of the cells have a value 0.

The objective is to compute `[[0, 0], [1, 0], [1, 1], [1, 2], [0, 2], [0, 1]]` from `{"grid": [[0, 0, 0], [0, 1, 2]], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Representing visited cells with one bitmask

For a grid with `m` rows and `n` columns, helper `f(i,j) = i*n+j` maps each coordinate to a unique integer from zero through `mn-1`.

Bit `f(i,j)` in `st` records whether cell `(i,j)` is on the current path. To test a candidate:

`st & (1 << f(x,y))`

is nonzero exactly when that cell has already been used.

When entering a cell, the source sets its bit with OR. When backtracking, it toggles that bit off with XOR. XOR is safe here because the DFS enters only unvisited cells, so the bit is known to be one at removal time and no other active path occurrence uses the same cell.

A single Python integer replaces a Boolean matrix and can represent all 25 grid cells comfortably.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[0, 0, 0], [0, 1, 2]], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What v means

The parameter `v` is the next numbered checkpoint that may be visited.

Every root search begins with `v = 1`. After appending the current cell, if `grid[i][j] == v`, that required checkpoint has just been visited and `v` increments. Zeros do not change it.

When considering a neighbor, the condition

`grid[x][y] in (0, v)`

permits:

- any ordinary zero cell;
- the one checkpoint whose value is currently expected.

It rejects every future checkpoint value greater than `v`. A past checkpoint value smaller than `v` cannot be revisited because each number occurs once and its cell’s visited bit is still set while on the active path.

Thus every explored path respects checkpoint order automatically.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why only zero or checkpoint one can be a start

A valid path may begin on an unnumbered zero cell, visiting checkpoint one later. It may also begin directly on checkpoint one.

It cannot begin on checkpoint two or any larger number, because that would visit a later checkpoint before checkpoint one. The outer loops therefore call DFS only for cells whose value is `0` or `1`. Every possible valid starting position is included, and every impossible numbered start is skipped.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[0, 0], [1, 0], [1, 1], [1, 2], [0, 2], [0, 1]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[0, 0, 0], [0, 1, 2]], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[0, 0], [1, 0], [1, 1], [1, 2], [0, 2], [0, 1]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Subset dynamic programming:** A state such as `(visited_mask,last_cell,next_checkpoint)` can avoid revisiting equivalent subproblems but may require `O(V2^V)` or more memory, which is large at `V=25`. Backtracking uses much less memory.
- **Memoize failed states:** Caching `(st,i,j,v)` can reduce repeated work but may consume exponential space. The source performs no such caching.
- **Connectivity pruning:** After each move, one could reject states where unvisited cells become disconnected. This can greatly accelerate difficult cases but requires additional checks not present in the exact implementation.
- **Forced-degree pruning:** Unvisited cells with too few available neighbors can reveal impossibility early. Again, this is a valid enhancement rather than current source behavior.
- **One-cell grid:** The only cell is checkpoint one because `k \ge 1` and all checkpoints exist; it is an allowed start, path length immediately reaches one, and that coordinate is returned.
- **Start on zero:** Checkpoint state remains one until cell one is reached.
- **Start on checkpoint one:** The first recursive expansion increments the expected value to two.
- **Future checkpoint adjacent too early:** The move is skipped, but the search may reach that checkpoint later from another direction after required earlier values are visited.
- **All cells numbered:** At every step only the exact next number is allowed, so the path is forced by checkpoint order if adjacent connections exist.
- **No valid Hamiltonian path:** Every start fully backtracks and the result is `[]`.
- **Successful path state:** Bits are not cleared on success because execution returns immediately and only the coordinate list is needed.
- **Parameter k:** The exact source does not reference it after entry. Correctness relies on the guarantee that the grid contains exactly the checkpoint values `1` through `k`.
- **Recursion depth:** At most 25 calls are active, so Python recursion limits are not a concern.
- **Any valid output:** Direction and start iteration order determine which solution is returned, but the statement permits any valid path.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V * 3^V)$. Let `V=mn` be the number of cells. There are up to `V` possible starts. After the first move, a self-avoiding grid path generally has at most three forward choices because it cannot immediately return to the preceding visited cell. A conventional loose bound for the explored search tree is therefore `O(V\cdot 3^V)` time, matching the manifest.
- **Auxiliary Space Complexity:** $O(V)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
