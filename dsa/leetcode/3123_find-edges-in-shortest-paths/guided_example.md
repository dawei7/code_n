# Guided Example: Find Edges in Shortest Paths

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4, "edges": [[2, 0, 1], [0, 1, 1], [0, 3, 4], [3, 2, 2]]}`
- **Required output:** `[true, false, false, true]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an undirected weighted graph of `n` nodes numbered from 0 to $n - 1$. The graph consists of `m` edges represented by a 2D array `edges`, where $\text{edges}[i] = [a_{i}, b_{i}, w_{i}]$ indicates that there is an edge between nodes $a_{i}$ and $b_{i}$ with weight $w_{i}$.

The objective is to compute `[true, false, false, true]` from `{"n": 4, "edges": [[2, 0, 1], [0, 1, 1], [0, 3, 4], [3, 2, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**First compute shortest distances from node zero.** The source builds an undirected adjacency list. Every neighbor tuple contains the other endpoint, edge weight, and original edge index so a later traversal can mark the correct Boolean result.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4, "edges": [[2, 0, 1], [0, 1, 1], [0, 3, 4], [3, 2, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

It runs Dijkstra from node zero because all weights are positive. `dist[v]` becomes the shortest distance from zero to `v`. Stale heap entries with `da > dist[a]` are skipped, and a relaxation updates only on a strictly shorter route.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

If `dist[n - 1]` remains infinity, no path from zero to the destination exists. Then no edge can belong to a shortest path, and the all-false result is returned immediately.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[true, false, false, true]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4, "edges": [[2, 0, 1], [0, 1, 1], [0, 3, 4], [3, 2, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[true, false, false, true]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Add a visited set to reverse traversal:** Process each tight-reachable node once, yielding $O(n+m)$ reverse work while marking all its tight incoming edges.
- **Two Dijkstra runs:** Compute distances from zero and destination, then test both edge orientations against the global shortest distance. This matches the manifest.
- **Destination unreachable:** Return all false before reverse traversal.
- **Several shortest paths:** Every edge in their union should be true.
- **Edge tight from zero but not destination-reachable:** Reverse traversal never reaches its later endpoint, so it remains false.
- **Positive weights:** Ensure distances strictly decrease backward and prevent tight cycles.
- **No repeated input edges:** Given, though different shortest routes can still merge and split.
- **Stale Dijkstra entries:** Skipped by comparing popped and stored distances.
- **Direction of an undirected edge:** The reverse equality automatically chooses the orientation from smaller to larger shortest distance.
- **An edge not satisfying equality:** Cannot lie on a shortest prefix in that orientation.
- **Duplicate queue entries:** They do not change truth values but can destroy performance.
- **Boolean idempotence:** Re-marking true is harmless for correctness, not for runtime.
- **One direct shortest edge:** Destination processing marks it and reaches node zero.
- **Disconnected side components:** Their distances remain infinity and they are never reverse-reached.
- **Source/manifest mismatch:** Exact source uses one Dijkstra and has an exponential revisit risk absent from the claimed bound.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((n + m) log n)$. Building the adjacency list costs $O(n+m)$ space and $O(m)$ time. Dijkstra costs $O((n+m)\log n)$ time with the heap.
- **Auxiliary Space Complexity:** $O(m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
