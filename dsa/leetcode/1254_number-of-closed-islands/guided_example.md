# Guided Example: Number of Closed Islands

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a 2D `grid` consists of `0s` (land) and `1s` (water).  An *island* is a maximal 4-directionally connected group of `0s` and a *closed island* is an island **totally** (all left, top, right, bottom) surrounded by `1s.`

The objective is to compute `1` from `{"grid": [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat every land component as an island

Land cells have value zero and connect only up, down, left, or right. A depth-first search from one unvisited land cell reaches exactly its maximal island.

The method reuses `grid` as its visited structure. As soon as `dfs(i,j)` enters land, it sets `grid[i][j] = 1`. That turns visited land into water for later searches and prevents cycles inside the current recursion.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: A component is closed exactly when every cell is interior

An island touches the outside world exactly when at least one of its cells lies on the grid boundary. The local value

`int(0 < i < m - 1 and 0 < j < n - 1)`

is one for an interior cell and zero for a boundary cell.

`dfs` combines this value with the results of all connected land neighbors using bitwise AND. The final component result remains one only if the current cell and every recursively reached cell are interior. If any boundary land cell occurs, zero propagates through the AND operations to the island’s root.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | An island touches the outside world exactly when at least on... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the entire island is explored even after finding a boundary

The source uses:

`res &= dfs(x, y)`.

Unlike short-circuit Boolean `and`, augmented bitwise AND evaluates the recursive right-hand side even when `res` is already zero. This is essential. Once an island is known to be open, the traversal must still mark all of its cells visited; otherwise, a later outer-loop position could start inside the same island and count or traverse it again.

The result values are integers zero and one, so bitwise AND acts exactly like logical conjunction while preserving eager evaluation.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Flood boundary land first:** Remove every isla:** - **Flood boundary land first:** Remove every island connected to an edge, then count remaining components. This separates openness detection from counting and remains \(O(N)\).
- **Breadth-first search:** Use a queue and a boundary flag, avoiding recursion-limit risk.
- **Separate visited matrix:** Preserve the input grid at the cost of \(O(N)\) explicit memory.
- **All water:** No DFS starts and the sum is zero.
- **All land:** The component touches every boundary and contributes zero.
- **Single-cell interior island:** Surrounded by water, its DFS returns one.
- **One-row or one-column grid:** Every land cell is on a boundary, so no closed island exists.
- **Eager bitwise AND:** Replacing `&=` with short-circuit logic carelessly could leave part of an open island unvisited.
- **Input mutation:** The exact method converts land to water; copy the grid first if preservation is needed.
- **Required helper:** Standalone code needs `pairwise` from `itertools`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let \(N=mn\) be the number of cells. The outer scan visits all \(N\) positions. Every land cell enters DFS at most once and examines four neighbors, so total time is \(O(N)\).
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
