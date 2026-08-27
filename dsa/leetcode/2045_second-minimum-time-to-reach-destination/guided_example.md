# Guided Example: Second Minimum Time to Reach Destination

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 5, "edges": [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], "time": 3, "change": 5}`
- **Required output:** `13`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A city is represented as a **bi-directional connected** graph with `n` vertices where each vertex is labeled from `1` to `n` (**inclusive**). The edges in the graph are represented as a 2D integer array `edges`, where each $\text{edges}[i] = [u_{i}, v_{i}]$ denotes a bi-directional edge between vertex $u_{i}$ and vertex $v_{i}$. Every vertex pair is connected by **at most one** edge, and no vertex has an edge to itself. The time taken to traverse any edge is `time` minutes.

The objective is to compute `13` from `{"n": 5, "edges": [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], "time": 3, "change": 5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate route length from traffic-signal timing

Every edge takes the same `time` minutes, and every traffic signal changes in synchronization. Starting from time zero, the elapsed time after a given number of traversed edges is therefore the same for every route of that length.

At each intermediate arrival, whether the signal is red depends only on the global elapsed time, not on the vertex or path. Consequently:

- first find the second-smallest distinct number of edges in a walk from vertex one to vertex `n`;
- then simulate that many edge traversals to obtain the second-minimum elapsed time.

This is why the graph search can ignore clock time entirely.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 5, "edges": [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], "time": 3, "change": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Store two distinct step counts per vertex

`dist[v][0]` and `dist[v][1]` are used to retain the two smallest distinct positive walk lengths discovered for vertex `v`. The queue stores pairs `(vertex, step_count)`.

For a popped state `(u,d)`, every neighbor `v` is reachable in `d+1` steps. If that value is smaller than `dist[v][0]`, it becomes the first stored length and is enqueued. Otherwise, it is accepted as the second length only when

`dist[v][0] < d + 1 < dist[v][1]`.

Both inequalities are strict. An equal-length route does not count as a second minimum because the definition asks for the smallest value strictly larger than the minimum.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `dist[v][0]` and `dist[v][1]` are used to retain the two sma... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The unusual source initialization

The source places `(1,0)` in the queue but assigns `dist[1][1] = 0` rather than the conventional `dist[1][0] = 0`.

This means a later two-edge return to vertex one can enter `dist[1][0]` even though zero sits in the other slot. The two entries for the source are not kept in sorted order. Nevertheless, the queued zero state starts the breadth-first expansion correctly, and allowing a positive revisit to the source is necessary because valid second-minimum walks may pass through vertex one again.

For all ordinarily discovered vertices, the two acceptance tests retain increasing distinct positive lengths. The target's second slot is populated with the required second walk length.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `13` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 5, "edges": [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], "time": 3, "change": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `13` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Time-aware Dijkstra:** Store the two smallest :** - **Time-aware Dijkstra:** Store the two smallest arrival times directly; correct but more machinery than step-count BFS under synchronized equal edges.
- **Enumerate simple paths:** Incorrectly excludes useful revisits and is computationally infeasible.
- **Duplicate shortest routes:** They share one minimum time and do not count as the second distinct value.
- **Return through vertex one:** Explicitly permitted; the source's revisit handling supports it.
- **Single edge graph:** The second walk goes to the destination, back, and to it again.
- **Arrival during green:** Departure is immediate; voluntary waiting is not allowed.
- **Arrival during red:** Wait exactly until the next multiple of `change` that begins a green phase.
- **Arrival at destination during red:** No wait matters because the journey is complete.
- **Exact phase boundary:** A boundary into red requires waiting; a boundary into green permits immediate departure.
- **Cycles:** Needed to create a second walk when only one simple route exists.
- **Strict second distance:** Equal edge counts are rejected by the strict inequalities.
- **Synchronized signals:** This is what makes elapsed time a function only of edge count.
- **Input preservation:** The source builds separate adjacency sets.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N+E)$. Let $N$ be vertices and $E$ edges. Building the undirected adjacency sets takes expected $O(E)$ time and $O(N+E)$ space.
- **Auxiliary Space Complexity:** $O(N+E)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
