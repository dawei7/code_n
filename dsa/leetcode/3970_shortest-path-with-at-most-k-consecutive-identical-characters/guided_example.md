# Guided Example: Shortest Path With At Most K Consecutive Identical Characters

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "edges": [[0, 1, 1], [1, 2, 1], [0, 2, 3]], "labels": "aab", "k": 1}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n` representing the number of nodes in a **directed weighted** graph, numbered from 0 to $n - 1$. This is represented by a 2D integer array `edges`, where $\text{edges}[i] = [u_{i}, v_{i}, w_{i}]$ represents a directed edge from node $u_{i}$ to node $v_{i}$ with weight $w_{i}$.

The objective is to compute `3` from `{"n": 3, "edges": [[0, 1, 1], [1, 2, 1], [0, 2, 3]], "labels": "aab", "k": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Building the directed weighted graph

For every edge `[u,v,w]`, the source appends `(v,w)` to `graph[u]` only. It does not add a reverse edge because the original graph is directed.

The expanded state graph is not built explicitly. When a state is removed from the priority queue, the source scans the original outgoing edges and calculates the next run length on demand.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "edges": [[0, 1, 1], [1, 2, 1], [0, 2, 3]], "labels": "aab", "k": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Meaning of the distance table

`distance[u][r]` is the smallest cost discovered so far for a path that:

- starts at node zero;
- ends at node `u`;
- satisfies the run constraint everywhere;
- has a final same-label run of length exactly `r`.

Column zero is allocated for convenient indexing but is never a valid state. The table has `k+1` entries per node so that real run lengths can be used directly as indices.

The starting route already contains node zero's label, so its run length is one:



No edge has been taken, so the cost is zero. Initializing the run length to zero would be wrong: moving to a node with the same label must create a run of length two, not one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How one directed edge changes the state

From state `(u,r)`, consider an edge to `v`.

- If `labels[u] == labels[v]`, the current identical-character run continues, so the new length is `r+1`.
- Otherwise a different character starts a new run, so the new length is one.

The source computes:



If `next_run>k`, traversing this edge would create an invalid path and the transition is discarded. Otherwise, the state `(neighbor,next_run)` is legal.

Only the final run length must be remembered. Every earlier run is already complete and was checked while it was formed; later moves cannot change it.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "edges": [[0, 1, 1], [1, 2, 1], [0, 2, 3]], "labels": "aab", "k": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **One distance per node:** This merges arrivals with different run lengths even though they permit different future edges. It can discard the only valid continuation and is not sufficient.
- **Store the full label string of each route:** Future validity depends only on the label and length of the final run. The current node supplies the label, so only the run length needs extra state.
- **Breadth-first search:** BFS minimizes edge count, not total weight. The positive weights may differ, so a binary-heap Dijkstra traversal is required.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(k(n+m) log(nk))$. Let `n` be the number of original nodes, `m` the number of directed edges, and `k` the allowed maximum run length.
- **Auxiliary Space Complexity:** $O(n+m+nk+mk)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
