# Guided Example: Shortest Bridge

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[0, 1], [1, 0]]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `n x n` binary matrix `grid` where `1` represents land and `0` represents water.

The objective is to compute `1` from `{"grid": [[0, 1], [1, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separating identification from expansion

The grid contains exactly two islands. A bridge is formed by changing water cells from `0` to `1` until the islands become connected, and the goal is to change as few cells as possible.

The optimal solution has two distinct phases:

1. Find and mark every cell of one island.
2. Expand outward from that entire island through water, one distance layer at a time, until the other island is reached.

The first phase uses depth-first search because it needs to collect one connected component. The second phase uses breadth-first search because breadth-first layers correspond exactly to the number of water cells that would be changed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[0, 1], [1, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Finding the first island

The generator expression searches the grid in row-major order and returns the first coordinate whose value is nonzero. Since the original grid contains only `0` and `1` at this point, this is a land cell.

Calling `dfs(i, j)` from that coordinate visits every four-directionally connected land cell in the same island. The direction tuple is `(-1, 0, 1, 0, -1)`. Applying `pairwise` produces the four direction vectors `(-1, 0)`, `(0, 1)`, `(1, 0)`, and `(0, -1)` without listing four separate pairs.

For each visited island cell, DFS performs two actions:

- it appends the coordinate to `q`;
- it changes the grid value from `1` to `2`.

Changing the value marks the cell as visited. The recursive search continues only into neighbors that are still `1`, so no island cell is processed twice.

DFS cannot accidentally absorb the second island. The two islands are separate four-directional components, so moving from the first island to the second requires crossing at least one water cell. DFS follows only cells whose value is `1` and never crosses `0`.

When DFS finishes, every cell of the chosen first island is marked `2` and stored in the queue. Every untouched `1` belongs to the second island.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why every first-island cell enters the BFS

The shortest bridge might leave the first island from any boundary cell. Starting breadth-first search from just the originally discovered cell would also count travel inside the first island, even though moving across existing land requires no water conversion. One could explicitly find boundary cells, but that extra filtering is unnecessary.

Instead, the queue initially contains all cells of the first island as simultaneous sources at distance zero. This is multi-source breadth-first search. It behaves as though a wave starts from the entire island at once, ensuring that the first contact with the second island uses the best departure point automatically.

Interior island cells are harmless seeds. They cannot expand through other marked island cells because the BFS adds only water cells, and they do not make the answer too small. They merely perform constant neighbor checks.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[0, 1], [1, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Run BFS from only one first-island cell:** This can overcount movement through existing land and miss the best shoreline. Multi-source BFS correctly assigns zero distance to the entire first island.
- **Start BFS from boundary cells only:** This is also correct and may reduce the initial queue, but it requires an additional boundary test. Enqueuing every island cell is simpler and retains the same `O(n^2)` bound.
- **Compute all pairs of island cells:** Measuring distances between every cell of one island and every cell of the other can become quadratic in the number of land cells, which is up to `O(n^4)` overall. BFS explores the grid once.
- **Depth-first search for both phases:** DFS is suitable for identifying a component, but ordinary DFS does not visit positions by shortest distance. Using it for expansion would require extra distance bookkeeping or exhaustive search.
- **Bidirectional breadth-first search:** Expanding from both islands can reduce practical search depth, but one side must still be identified and the meeting-distance accounting becomes more involved. The one-sided multi-source BFS already satisfies the optimal asymptotic bound.
- **Iterative island marking:** Replacing recursive DFS with an explicit stack preserves the algorithm and `O(n^2)` bounds while avoiding Python recursion-limit failures on large or snake-shaped islands.
- **One water cell between islands:** The first water layer sees the second island and returns `1`. The algorithm counts converted water cells, not graph edges between land cells.
- **Grid edges and corners:** Every neighbor is checked against `0 <= x < n` and `0 <= y < n` before access, so cells on the border need no special branch.
- **Repeated discovery of the same water:** Setting a water cell to `2` before enqueueing it ensures that later neighbors do not add it again.
- **Input mutation:** The marking strategy destroys the original binary grid. If preservation were required, the algorithm would need a separate visited set or a copied grid, increasing memory use.
- **Exactly two islands:** The recognition that every untouched `1` belongs to the target relies on this contract. With more islands, the first contact would find the nearest other island, which would be a different problem.
- **Direction semantics:** Only vertical and horizontal neighbors count. Diagonal contact does not join islands and is correctly ignored by the four generated direction pairs.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let `n` be the side length of the square grid.
- **Auxiliary Space Complexity:** $O(n^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
