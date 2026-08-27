# Guided Example: Critical Connections in a Network

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4, "connections": [[0, 1], [1, 2], [2, 0], [1, 3]]}`
- **Required output:** `[[1, 3]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` servers numbered from `0` to $n - 1$ connected by undirected server-to-server `connections` forming a network where $\text{connections}[i] = [a_{i}, b_{i}]$ represents a connection between servers $a_{i}$ and $b_{i}$. Any server can reach other servers directly or indirectly through the network.

The objective is to compute `[[1, 3]]` from `{"n": 4, "connections": [[0, 1], [1, 2], [2, 0], [1, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Build an undirected adjacency list

For each connection `[a, b]`, the code appends `b` to `g[a]` and `a` to `g[b]`. Both directions are necessary because the network is undirected. The input has no repeated connections, so each neighbor entry corresponds to one distinct edge.

The arrays `dfn` and `low` both start with zeros. A zero `dfn` means the vertex has not been visited. The variable `now` is a monotonically increasing timestamp shared by the nested DFS through `nonlocal now`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4, "connections": [[0, 1], [1, 2], [2, 0], [1, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Discovery time records DFS order

When `tarjan(a, fa)` first enters vertex `a`, it increments `now` and assigns that value to both `dfn[a]` and `low[a]`.

`dfn[a]` never changes again. It is the time at which `a` was discovered, so ancestors in the current DFS tree have smaller discovery values.

`low[a]` can decrease. Its eventual meaning is the smallest discovery time reachable from `a`’s DFS subtree by following zero or more tree edges downward and then, if useful, one non-parent edge to an already discovered vertex. Informally, it tells how high that subtree can reconnect without using the tree edge from `a` to its parent.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | When `tarjan(a, fa)` first enters vertex `a`, it increments ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Ignore the exact edge back to the parent

While exploring neighbors `b` of `a`, the check `if b == fa` skips the tree edge that brought the recursion into `a`. In an undirected adjacency list, that same physical edge appears in both endpoint lists. Treating it as an alternate route would falsely make every child appear connected back to its parent.

This simple parent-vertex check is safe because the input forbids repeated parallel connections. With parallel edges between the same endpoints, an edge identifier rather than just the parent vertex would be needed to distinguish the tree edge from another valid back edge.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 3]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4, "connections": [[0, 1], [1, 2], [2, 0], [1, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 3]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Remove every edge and test connectivity:** Run:** - **Remove every edge and test connectivity:** Running a graph traversal after each removal can cost $O(m(n+m))$, far too much for $10^5$ edges.
- **Iterative low-link DFS:** Store explicit frames containing vertex, parent, and neighbor position. This avoids Python recursion depth but requires more bookkeeping to perform child-return updates.
- **Union-find in reverse or offline bridge algorithms:** More advanced techniques exist for dynamic settings, but low-link DFS is the direct linear solution for one static graph.
- **Graph is a tree:** Every edge is the sole connection between two components, so every child has `low[child] > dfn[parent]` and all edges are returned.
- **Graph is one cycle:** Every tree child can reconnect to an ancestor, so no edge satisfies the bridge inequality.
- **Two vertices with one edge:** The child has no back edge, and the only connection is correctly reported.
- **Disconnected input:** A general implementation would start DFS from every unvisited vertex. This solution starts only at zero because the local contract states that all servers are mutually reachable.
- **No repeated connections:** Skipping by parent vertex is safe only under this guarantee. Parallel undirected edges would require tracking edge IDs.
- **Strict comparison:** `low[b] == dfn[a]` means a route returns to `a`, so the edge lies on a cycle and is not a bridge.
- **Output orientation and order:** The contract accepts any order and either endpoint orientation, so appending tree direction `[a, b]` is sufficient.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+m)$. Let $n$ be the number of servers and $m$ be the number of connections.
- **Auxiliary Space Complexity:** $O(n+m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
