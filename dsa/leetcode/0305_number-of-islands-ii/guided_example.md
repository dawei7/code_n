# Guided Example: Number of Islands II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"m": 3, "n": 3, "positions": [[0, 0], [0, 1], [1, 2], [2, 1]]}`
- **Required output:** `[1, 1, 2, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an empty 2D binary grid `grid` of size `m x n`. The grid represents a map where `0`'s represent water and `1`'s represent land. Initially, all the cells of `grid` are water cells (i.e., all the cells are `0`'s).

The objective is to compute `[1, 1, 2, 3]` from `{"m": 3, "n": 3, "positions": [[0, 0], [0, 1], [1, 2], [2, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Flattening grid positions

The usual row-major identifier for cell $(i,j)$ is

$$
id(i,j)=i\cdot n+j.
$$

For an $m\times n$ grid, this maps every cell to one unique integer from 0 through $mn-1$. Horizontal or vertical adjacency is still checked with row and column coordinates; flattening is used only as the union-find key.

The exact `UnionFind.union` method calls `find(a - 1)` and `find(b - 1)` rather than `find(a)` and `find(b)`. This looks like an off-by-one error, but under Python indexing it acts as a consistent cyclic relabeling of the valid identifiers:

$$
0\mapsto -1\equiv mn-1,
$$

$$
1\mapsto0,\quad2\mapsto1,\quad\ldots,\quad mn-1\mapsto mn-2.
$$

Python list index `-1` refers to the final entry. Thus, every valid cell identifier still maps to a distinct union-find slot, and the same mapping is applied to both endpoints of every union. Connectivity is unchanged by a one-to-one relabeling. The convention is unusual and would be unsafe in languages where negative indexing is invalid, but it is internally consistent in this exact Python source.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"m": 3, "n": 3, "positions": [[0, 0], [0, 1], [1, 2], [2, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Disjoint-set state

`p[x]` stores the parent of union-find slot `x`. Initially, every slot is its own root. `size[x]` is meaningful for a root and stores the number of represented slots in that tree.

`find(x)` follows parent links until reaching a root whose parent is itself. On the recursive return path, it assigns every visited node directly to that root. This is path compression: later searches from those nodes become much shorter.

`union(a, b)` first finds the two roots after applying the source's shifted indexing. If the roots are equal, both land cells are already in the same connected component, so it returns `false` and changes nothing.

If the roots differ, union by size attaches the smaller tree below the larger tree's root. On a tie, the first root is attached below the second. The new root's size is increased by the absorbed tree's size, and the method returns `true` to report that two components became one.

Path compression and union by size together make repeated connectivity operations extremely close to constant time amortized.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `p[x]` stores the parent of union-find slot `x`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why a separate grid is necessary

The union-find arrays are initialized for all $mn$ slots, including cells that are still water. Therefore, parent membership alone cannot say whether a cell is active land. The matrix `grid` supplies that missing state:

- `grid[i][j] == 0` means the cell has not been added;
- `grid[i][j] == 1` means it is active land.

The algorithm attempts a union only when the neighboring coordinate is in bounds and its grid entry is already land. Inactive union-find roots are never connected into the island graph.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 1, 2, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"m": 3, "n": 3, "positions": [[0, 0], [0, 1], [1, 2], [2, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 1, 2, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sparse dictionary union-find:** Create parent :** - **Sparse dictionary union-find:** Create parent and size entries only when a position first becomes land. This avoids $O(mn)$ initialization and uses $O(u)$ state for $u\le k$ unique added cells, matching the manifest's sparse summary.
- **Recount islands after every operation:** Run DFS or BFS over the entire grid each time. This can cost $O(kmn)$ and repeats almost all connectivity work.
- **Flood-fill only from the new cell:** It can discover connected land, but maintaining and relabeling components across many additions is less efficient than union-find.
- **Decrement for every land neighbor:** This is wrong when two neighboring cells already belong to the same island. Only a union of different roots reduces the component count.
- **Union diagonal neighbors:** Islands use horizontal and vertical adjacency only. Adding diagonals would incorrectly merge separate islands.
- **Duplicate position:** The current count must be repeated unchanged. The early `grid[i][j]` check prevents a false new component and repeated unions.
- **First operation:** A new cell has no previously active neighbor, so the answer is always one.
- **One-cell grid:** The first add returns one; any duplicate additions continue returning one.
- **Boundary cell:** Neighbor coordinates are checked before indexing the grid, preventing negative wrapping or out-of-range access.
- **A new isolated cell:** No union succeeds, so the initial count increment remains and the island count rises by one.
- **A new cell touching one island:** Exactly one root merge succeeds, canceling the singleton increment; the island count stays unchanged.
- **A bridge between several islands:** One successful union occurs for each distinct neighboring component, so the count can decrease by more than one during a single operation.
- **Several neighbors in one component:** Path compression makes their roots equal, and only the first merge succeeds.
- **Shifted union-find indices:** Subtracting one works here only because every valid flattened ID receives the same bijective Python-index transformation. Reusing this class with arbitrary IDs, zero-length arrays, or a language without negative indexing would be unsafe.
- **Recursive `find`:** Union by size limits tree height before compression, and compression flattens paths further. An iterative implementation could avoid recursion entirely but would preserve the same component logic.
- **Maximum grid product:** Dense storage is feasible under the stated $mn\le10^4$ constraint, even though it does not achieve the sparse follow-up bound.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $k$ be the number of operations and let $N=mn$ be the number of grid cells.
- **Auxiliary Space Complexity:** $O(mn)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
