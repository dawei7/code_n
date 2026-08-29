# Guided Example: Shortest Path with Alternating Colors

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "redEdges": [[0, 1], [1, 2]], "blueEdges": []}`
- **Required output:** `[0, 1, -1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n`, the number of nodes in a directed graph where the nodes are labeled from `0` to $n - 1$. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

The objective is to compute `[0, 1, -1]` from `{"n": 3, "redEdges": [[0, 1], [1, 2]], "blueEdges": []}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A node alone is not enough state

Whether an outgoing edge is legal depends on the previous edge color. Reaching node five after red is different from reaching node five after blue.

The BFS state is therefore `(node, color)`, where `color` represents the color of the edge used to reach that state, or equivalently determines which color must be used next after toggling.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "redEdges": [[0, 1], [1, 2]], "blueEdges": []}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build separate adjacency lists

`g[0]` stores red outgoing neighbors and `g[1]` stores blue outgoing neighbors. Parallel and self edges are preserved in the lists because the graph permits them.

The queue starts with `(0,0)` and `(0,1)`. These two conceptual states allow the first real edge to be either color. Both have distance zero because no edge has yet been taken.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Process BFS by distance layers

`d` is the current edge count. The snapshot `len(q)` fixes one layer, so states appended during processing wait for the next distance.

When state `i,c` is dequeued, the code writes `ans[i] = d` only if that node has no answer yet. BFS layer order guarantees this first node-level answer is the shortest alternating path regardless of ending color.

It records the colored state in `vis`, flips `c` with XOR one, and follows only adjacency edges of the opposite color. Each enqueued state therefore extends a valid alternating path by one edge.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, 1, -1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "redEdges": [[0, 1], [1, 2]], "blueEdges": []}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, 1, -1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enqueue-time visited marking:** The standard repair that ensures each colored state enters the queue once.
- **Distance matrix:** Store separate red-ending and blue-ending distances, then take the minimum per node.
- **Dijkstra:** Correct but unnecessary because every edge has unit length.
- **Node-only BFS:** Incorrect because previous color changes future legality.
- **No edges:** Node zero is zero and every other answer stays `-1`.
- **Only same-color chain:** At most its first edge can be used because colors fail to alternate.
- **Parallel edges:** They may enqueue duplicate states in the exact code but do not change shortest distance.
- **Self-edge:** It is legal only when its color alternates with the prior edge and may change the usable ending color at the same node.
- **Both colors to one node:** Both states should be explored because they enable different next colors.
- **Cycle:** Colored visited state prevents endlessly discovering new semantic states, though duplicate expansion remains possible.
- **Unreachable node:** Its initialized `-1` is returned.
- **Start node:** Its shortest path length is zero without traversing an edge.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n + r + b)$. The intended colored-state graph has $2n$ vertices and $O(r+b)$ transitions. A standard enqueue-once BFS takes $O(n+r+b)$ time and space.
- **Auxiliary Space Complexity:** $O(n + r + b)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
