# Guided Example: Distance to a Cycle in Undirected Graph

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 7, "edges": [[1, 2], [2, 4], [4, 3], [3, 1], [0, 1], [5, 2], [6, 5]]}`
- **Required output:** `[1, 0, 0, 0, 0, 1, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a positive integer `n` representing the number of nodes in a **connected undirected graph** containing **exactly one** cycle. The nodes are numbered from `0` to $n - 1$ (**inclusive**).

The objective is to compute `[1, 0, 0, 0, 0, 1, 2]` from `{"n": 7, "edges": [[1, 2], [2, 4], [4, 3], [3, 1], [0, 1], [5, 2], [6, 5]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Build mutable neighbor sets

For every undirected edge `a, b`, the code adds `b` to `g[a]` and `a` to `g[b]`.

Sets make it possible to remove a peeled neighbor from another node's current adjacency in expected constant time. Their current lengths represent degrees in the graph that remains after prior peeling.

The initial queue contains every node whose degree is one.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 7, "edges": [[1, 2], [2, 4], [4, 3], [3, 1], [0, 1], [5, 2], [6, 5]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Peel leaves toward the unique cycle

When leaf `i` is popped, it is appended to `seq`. At that moment, its current set contains its one surviving neighbor `j`.

The code removes `i` from `g[j]` and records `f[i] = j`. This neighbor lies one edge closer to the unpeeled core.

If `j`'s degree becomes one after removal, it is now a leaf and is enqueued. Finally `g[i].clear()` marks the removed node as absent from the remaining graph.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why cycle nodes are never peeled

Every cycle node has two cycle neighbors. Tree branches attached to it may be removed, but those two cycle edges remain.

Its residual degree therefore never drops below two during leaf peeling, so it never enters the degree-one queue.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 0, 0, 0, 0, 1, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 7, "edges": [[1, 2], [2, 4], [4, 3], [3, 1], [0, 1], [5, 2], [6, 5]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 0, 0, 0, 0, 1, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Multi-source BFS from cycle nodes:** After peeling, enqueue every residual cycle node at distance zero and expand outward. This matches the manifest and also runs in linear time.
- **DFS cycle detection:** Find one back edge, mark the cycle path through parents, then traverse attached trees. It works but recursion depth may be large.
- **All nodes on the cycle:** No degree-one node enters the queue, `seq` stays empty, and every answer correctly remains zero.
- **Single long branch:** Peeling records nodes from farthest to nearest; reversal restores distances from nearest to farthest.
- **Several trees on cycle nodes:** Each branch peels independently and uses its own inward parent chain.
- **Degree changes:** A node is enqueued precisely when its residual degree becomes one.
- **Unique-cycle guarantee:** It ensures the residual two-core is exactly one cycle rather than a more complex core.
- **Connected guarantee:** Every peeled parent chain eventually reaches that cycle.
- **Set mutation:** The code removes only currently present leaf edges, so `remove` is valid.
- **Cycle nodes initialized implicitly:** Their zero values need no explicit assignment.
- **No second graph traversal:** Reverse peel order replaces multi-source BFS in the exact source.
- **Input preservation:** Edge descriptions are read into separate mutable sets.
- **Manifest discrepancy:** The solution peels plus reverse-propagates; it does not run the summarized BFS.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The graph has exactly $n$ edges. Building two adjacency entries per edge takes $O(n)$ expected time and space.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
