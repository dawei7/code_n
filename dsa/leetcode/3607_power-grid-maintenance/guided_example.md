# Guided Example: Power Grid Maintenance

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"c": 3, "connections": [], "queries": [[1, 1], [2, 1], [1, 1]]}`
- **Required output:** `[1, -1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `c` representing `c` power stations, each with a unique identifier `id` from 1 to `c` (1‑based indexing).

The objective is to compute `[1, -1]` from `{"c": 3, "connections": [], "queries": [[1, 1], [2, 1], [1, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Building the permanent power grids

The Union-Find is created with `c + 1` positions because station identifiers run from 1 through `c`. Position 0 is unused.

For every bidirectional cable `[u, v]`, `uf.union(u, v)` merges the two components. `find` uses path compression, and `union` uses component sizes to attach the smaller tree beneath the larger one. After all connections are processed:

`uf.find(x)`

is a representative for the complete static grid containing station `x`.

No later query changes the Union-Find. Taking a station offline changes who can answer maintenance checks, not which stations are directly or indirectly connected.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"c": 3, "connections": [], "queries": [[1, 1], [2, 1], [1, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: One sorted online set per component

The source creates:

`st = [SortedList() for _ in range(c + 1)]`.

Only entries whose indices are actual final Union-Find roots receive station IDs; the other sorted lists remain empty. For each station `i`, the initialization performs:

`st[uf.find(i)].add(i)`.

Initially all stations are online, so every identifier appears exactly once in the sorted list for its grid. A `SortedList` preserves ascending order while supporting membership checks and deletion.

After initialization, the intended invariant is:

> For every final root `r`, `st[r]` contains exactly the IDs of currently online stations in that connected component, in increasing order.

This invariant directly answers both cases of a maintenance query.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Processing a type-1 maintenance query

For query `[1, x]`, the source first obtains `root = uf.find(x)`.

It then checks `if x in st[root]`. If true, station `x` is online. The contract says an online requested station resolves its own check even if a smaller online station exists in the same grid, so the answer must be `x`.

If `x` is absent, it is offline. When `st[root]` is nonempty, its first element `st[root][0]` is the smallest online ID in the grid because the collection is sorted. That station resolves the check.

If the sorted list is empty, the component has no operational station and the answer is `-1`.

The source appends an answer only for type-1 queries, so the returned array naturally has the requested query order and length.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, -1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"c": 3, "connections": [], "queries": [[1, 1], [2, 1], [1, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, -1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Reverse processing:** Count all offline operations, start from the final online state, and restore stations while scanning queries backward. Per-component minima can then be updated without deletions, but repeated offline operations require careful counting.
- **Lazy min-heaps:** Store all component IDs in heaps and mark stations offline separately. Pop offline minima only when needed; each station is removed from a heap at most once.
- **Balanced binary search tree:** Any ordered set supporting membership, deletion, and minimum can replace `SortedList` with the same high-level algorithm.
- **Unordered set only:** It supports status and deletion but cannot find the smallest online ID efficiently without scanning the whole component.
- **Recompute connectivity after an outage:** This is incorrect as well as expensive because an offline station remains part of the static power grid.
- **Requested station is online:** Return `x` itself, not the component minimum.
- **Requested station is offline:** Return the smallest remaining online ID in its original static component.
- **Entire component offline:** Its sorted list is empty, so the answer is `-1`.
- **Isolated online station:** Its component list contains only itself, and a type-1 query returns its ID.
- **Isolated station goes offline:** Its list becomes empty, and later maintenance checks return `-1`.
- **Repeated type-2 query:** `discard` leaves an already-absent value unchanged, making the operation idempotent.
- **Several disconnected grids:** Each final root indexes an independent sorted list, so outages in one grid cannot affect another.
- **Station ID 1 versus array index 0:** Arrays have length `c+1` to preserve one-based station identifiers; slot 0 is unused.
- **Duplicate connections:** Union-Find simply detects that endpoints are already connected; component membership remains correct.
- **Component root is not its smallest station:** This is harmless. The root is only a container key; `st[root][0]` supplies the smallest online ID.
- **All queries are outages:** The answer list remains empty because type 2 produces no output.
- **All queries are checks:** Every station remains online and resolves its own request.
- **Missing imports:** The exact file requires its environment to provide `SortedList` and `List`; standalone use must import them.
- **Input preservation:** The source mutates only Union-Find and sorted-list state. `connections` and `queries` retain their original order and contents.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((c + m) \alpha(c) + q + c log c)$. Let `c` be the number of stations, `m` the number of connections, and `q` the number of queries.
- **Auxiliary Space Complexity:** $O(c)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
