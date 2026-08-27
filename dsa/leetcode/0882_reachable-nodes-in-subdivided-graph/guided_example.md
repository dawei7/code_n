# Guided Example: Reachable Nodes In Subdivided Graph

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"edges": [[0, 1, 10], [0, 2, 1], [1, 2, 2]], "maxMoves": 6, "n": 3}`
- **Required output:** `13`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an undirected graph (the **"original graph"**) with `n` nodes labeled from `0` to $n - 1$. You decide to **subdivide** each edge in the graph into a chain of nodes, with the number of new nodes varying between each edge.

The objective is to compute `13` from `{"edges": [[0, 1, 10], [0, 2, 1], [1, 2, 2]], "maxMoves": 6, "n": 3}` while avoiding redundant calculations and unnecessary overhead.

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

Expanding every subdivided edge into thousands of explicit nodes could make the graph unnecessarily large. The central idea is to compute shortest distances only among original nodes, then count how far the remaining move budget reaches into each subdivided edge from its two endpoints.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"edges": [[0, 1, 10], [0, 2, 1], [1, 2, 2]], "maxMoves": 6, "n": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

An original edge `[u, v, cnt]` becomes a chain with `cnt` inserted nodes and `cnt + 1` unit edges. Therefore traveling all the way from original node `u` to original node `v` costs `cnt + 1` moves. The adjacency list stores exactly that compressed weight in both directions.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | An original edge `[u, v, cnt]` becomes a chain with `cnt` in... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Shortest distances to original nodes.** The intended algorithm is Dijkstra's algorithm from node 0 because all compressed edge weights are positive. `dist[u]` is the smallest known number of moves needed to reach original node `u`. It begins at zero for node 0 and infinity elsewhere.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `13` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"edges": [[0, 1, 10], [0, 2, 1], [1, 2, 2]], "maxMoves": 6, "n": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `13` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicitly build the subdivided graph:** This :** - **Explicitly build the subdivided graph:** This is conceptually simple but may add up to $10^4$ nodes per edge and consume excessive time and memory.
- **Correct priority-queue Dijkstra:** Use `heappush(q, (t, v))` and optionally skip stale pops with `if d != dist[u]: continue`. This realizes the intended complexity.
- **Plain breadth-first search on compressed edges:** Edge weights are `cnt + 1` rather than all one, so BFS among original nodes does not compute shortest move counts.
- **Bellman-Ford-style relaxation:** It can compute distances with positive weights but is much slower than properly implemented Dijkstra.
- **No edges:** Node 0 is the only reachable node, regardless of move budget.
- **`maxMoves = 0`:** Only original node 0 is reachable; no unit can be spent entering an internal node.
- **`cnt = 0`:** The edge has no internal nodes. Its compressed weight is one, and its counting contribution is zero.
- **Disconnected graph:** Unreachable endpoints retain infinity, contribute no remaining budget, and are not counted as original nodes.
- **Reach from only one endpoint:** The formula counts that one reachable prefix even if the opposite endpoint is unreachable.
- **Prefixes overlap:** `min(cnt, a + b)` caps the union at the number of distinct internal nodes.
- **Reach endpoint with exactly the budget:** The original endpoint counts, but it leaves zero moves for entering adjacent subdivided edges.
- **Extra distance-array entry:** The $n+1$-st infinity is harmless but unnecessary; a length-$n$ array would be cleaner.
- **Stale scheduled distances:** A correct Dijkstra implementation should skip them for efficiency. The relaxation condition prevents a stale record from overwriting a better distance.
- **No multiple original edges:** Each internal chain belongs to one edge, which makes independent per-edge counting valid.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((n+m)$. Let $n$ be the number of original nodes and $m$ the number of original edges.
- **Auxiliary Space Complexity:** $O(n+m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
