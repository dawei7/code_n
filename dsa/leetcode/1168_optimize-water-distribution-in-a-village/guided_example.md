# Guided Example: Optimize Water Distribution in a Village

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 2, "wells": [1, 1], "pipes": [[1, 2, 1], [1, 2, 2]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` houses in a village. We want to supply water for all the houses by building wells and laying pipes.

The objective is to compute `2` from `{"n": 2, "wells": [1, 1], "pipes": [[1, 2, 1], [1, 2, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn wells and pipes into one graph problem

Pipes are ordinary undirected weighted edges between houses. A well is different on the surface because it supplies one house directly rather than connecting two houses.

Introduce a virtual vertex zero representing the water source. Building a well at house `i` is now modeled as selecting an edge

`(0, i, wells[i - 1])`.

If house `i` connects to zero, it has a well. If it reaches zero through other houses and pipes, water flows from some selected well through those connections. Supplying every house is therefore equivalent to connecting vertices zero through `n` in one graph.

The minimum-cost connected subgraph with positive or zero edge costs can be reduced to a tree: any cycle edge can be removed without disconnecting the graph and without increasing cost. The task is exactly a minimum spanning tree over the virtual-source graph.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 2, "wells": [1, 1], "pipes": [[1, 2, 1], [1, 2, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Add all well choices as virtual edges

`enumerate(wells, 1)` pairs the first well cost with house one and so on. Each virtual edge `[0, i, w]` is appended directly to `pipes`.

After this loop, the list contains every choice: the original pipe offers plus one well edge for each house. Parallel pipe offers remain separate edges, which is correct because Kruskal's algorithm can consider their different costs independently.

The exact source mutates the caller-provided `pipes` list by appending virtual edges and then sorting it. This is acceptable for a one-shot judge call, but a caller needing the original order or contents would have to pass a copy.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `enumerate(wells, 1)` pairs the first well cost with house o... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Process edges from cheapest to most expensive

`pipes.sort(key=lambda x: x[2])` orders all well and pipe edges by cost. Kruskal's algorithm scans them in this order.

For edge `(a, b, c)`, `find(a)` and `find(b)` return the current disjoint-set representatives of its endpoints. If the representatives are equal, the endpoints are already connected; adding the edge would form a cycle and provide no new water reachability.

If the representatives differ, the edge joins two components. The code sets `p[pa] = pb`, adds `c` to `ans`, and reduces the number of remaining required unions.

The `find` helper uses path compression. When a vertex's parent is not itself, it recursively finds the root and writes that root back into `p[x]`. Later representative queries along the same path become faster.

The implementation does not keep rank or component size, so it attaches `pa` directly below `pb`. Path compression still avoids repeatedly following unchanged long paths, while edge sorting dominates the documented overall bound.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 2, "wells": [1, 1], "pipes": [[1, 2, 1], [1, 2, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Prim's algorithm:** Starting from the virtual :** - **Prim's algorithm:** Starting from the virtual source and growing a tree through a heap also solves the augmented MST in `O(e log n)` time. Kruskal is natural when all choices are already an edge list.
- **Choose the cheapest well only:** Cheap pipes may not connect every house to that well, and building several wells can be better than expensive pipes. The MST evaluates all combinations.
- **Build a well at every house:** This is always feasible but can be unnecessarily expensive when cheap pipes share one well.
- **Ignore the virtual node:** Treating wells separately complicates the choice. Virtual edges unify both purchase types under one cut-property proof.
- **Parallel pipe offers:** Sorting considers them independently; a more expensive parallel edge will normally be skipped after the cheaper one connects the same components.
- **Disconnected original pipe graph:** Virtual well edges connect every component to zero, so a feasible augmented spanning tree always exists.
- **Zero-cost wells or pipes:** Kruskal processes them first, and the same correctness proof applies.
- **Cycle-forming edge:** It is skipped because it adds cost without connecting a new component.
- **Input mutation:** The exact method appends to and sorts `pipes`. Reusing that list after the call will expose the virtual edges and new order.
- **No union-by-rank array:** The source uses path compression only. Its behavior remains correct; rank would affect efficiency constants and tighter disjoint-set analysis, not MST validity.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(e log e)$. Let `p` be the original number of pipe offers and `e = n + p` be the augmented edge count. Appending well edges takes `O(n)` time. Sorting all edges takes `O(e log e)` time.
- **Auxiliary Space Complexity:** $O(e)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
