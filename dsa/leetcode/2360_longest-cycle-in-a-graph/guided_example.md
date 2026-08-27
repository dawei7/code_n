# Guided Example: Longest Cycle in a Graph

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"edges": [3, 3, 4, 2, 3]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **directed** graph of `n` nodes numbered from `0` to $n - 1$, where each node has **at most one** outgoing edge.

The objective is to compute `3` from `{"edges": [3, 3, 4, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use the functional-graph structure

Each node has at most one outgoing edge. Therefore, once a traversal starts at a node, its future is deterministic: it repeatedly follows one next node until it reaches `-1` or encounters a node seen before. There are no branches to explore.

A repeated node does not automatically mean that the current traversal found a new cycle. The repeated node might have been visited by an earlier outer-loop traversal. The algorithm must distinguish these situations:

- If the repeated node occurs in the path currently being recorded, the suffix beginning at its first occurrence is a cycle.
- If it was visited before but is absent from the current path, this path has merely joined an already processed component. Any cycle beyond that point was measured earlier.

The exact solution makes that distinction with a global Boolean array `vis` and a per-traversal list `cycle`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"edges": [3, 3, 4, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Start only from globally unvisited nodes

The outer loop considers every node `i`. If `vis[i]` is already true, it skips that start. This is safe because the graph has only one outgoing edge per node. During the first visit, the algorithm already followed that node's only possible future until termination or repetition. Starting from it again cannot reveal an alternate branch or a different cycle.

For a new start, `j = i` and `cycle = []`. Despite the variable's name, this list initially stores the entire current walk, including any non-cyclic prefix. During the loop, the algorithm:

1. marks `j` globally visited;
2. appends `j` to the current traversal list;
3. advances with `j = edges[j]`.

The loop continues only while `j != -1` and `vis[j]` is false. Every newly appended node is therefore unique within this walk and had never been processed by an earlier walk.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The outer loop considers every node `i`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Interpret how the walk stopped

If `j == -1`, the path reached a node with no outgoing edge. Such a path contains no cycle, so the solution continues to the next outer-loop start.

Otherwise, `j` is globally visited. Let `m = len(cycle)`. The expression



searches for `j` inside the current list and returns its first index `k`. If `j` belongs to the current walk, the nodes



form the cycle. The last node points back to `cycle[k]`, so its length is `m - k`.

For example, suppose the walk list is `[0, 1, 2, 4, 3]` and the next node is `2`. The repeated node first appears at index `2`. The suffix `[2, 4, 3]` is the cycle, and `m - k = 5 - 2 = 3`.

If `j` was visited by an earlier traversal, it is not in the current list. The generator finds no index, so `next(..., inf)` returns `inf`. Then `m - k` is negative infinity. Taking `max(ans, m - k)` leaves the finite current answer unchanged. This is an unusual but compact way for the exact solution to ignore a path that merges into old work without writing a separate membership test.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"edges": [3, 3, 4, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Three-state visitation:** Mark nodes as unseen:** - **Three-state visitation:** Mark nodes as unseen, active in the current traversal, or completely processed. This detects current-path revisits in $O(1)$ without searching the list, but requires storing an entry time or depth to calculate length.
- **Traversal identifier and timestamps:** Arrays can record which traversal first saw each node and at what step. A repeated matching identifier proves that the node belongs to the current walk. This is often clearer than the `inf` sentinel trick.
- **Kahn's algorithm:** Repeatedly remove indegree-zero nodes. The remaining nodes belong to cycles, which can then be counted. It is also $O(n)$ but needs indegrees and a queue.
- **Recursive DFS:** Recursion can model active and finished states naturally, but a chain of length $10^5$ risks exceeding Python's recursion limit.
- **Path reaches `-1`:** No cycle closes, so the current list contributes nothing.
- **Path merges into earlier work:** The repeated node is absent from the current list, `k` becomes `inf`, and the maximum answer is unchanged.
- **Tail entering a cycle:** The index `k` excludes every tail node and counts only the repeated suffix.
- **Several disconnected cycles:** Separate unvisited starts discover them, and `max` retains the longest length.
- **Equal-length cycles:** Only the length is returned, so no tie-breaking by node is necessary.
- **No cycles anywhere:** `ans` is never raised above its initial value and the method returns `-1`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let $n$ be the number of nodes. Every node changes from unvisited to visited exactly once. The walking loops collectively append at most $n$ nodes, and the outer loop itself performs $n$ constant-time checks.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
