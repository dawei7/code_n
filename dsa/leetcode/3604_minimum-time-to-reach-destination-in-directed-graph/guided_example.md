# Guided Example: Minimum Time to Reach Destination in Directed Graph

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "edges": [[0, 1, 0, 1], [1, 2, 2, 5]]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n` and a **directed** graph with `n` nodes labeled from 0 to $n - 1$. This is represented by a 2D array `edges`, where $\text{edges}[i] = [u_{i}, v_{i}, \text{start}_{i}, \text{end}_{i}]$ indicates an edge from node $u_{i}$ to $v_{i}$ that can **only** be used at any integer time `t` such that $\text{start}_{i} \le t \le \text{end}_{i}$.

The objective is to compute `3` from `{"n": 3, "edges": [[0, 1, 0, 1], [1, 2, 2, 5]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Building the directed adjacency list

For every input edge `[source, destination, start, end]`, the source appends:

`(destination, start, end)`

to `graph[source]`. It does not add the reverse direction because the cables are directed. The adjacency list lets the main loop inspect only edges that can leave the node currently being processed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "edges": [[0, 1, 0, 1], [1, 2, 2, 5]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The meaning of `earliest`

`earliest[v]` is the smallest arrival time at node `v` discovered so far. Initially:

- `earliest[0] = 0` because the traveler starts at node 0 at time 0;
- every other value is infinity because no route to those nodes is known.

The heap begins with `(0, 0)`. Each tuple stores arrival time first, so Python's min-heap orders entries primarily by time.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Using one edge at the earliest possible moment

Suppose node `u` is reached at time `time` and an outgoing edge is usable for integer departure times from `start` through `end`, inclusive.

If `time > end`, the entire availability window has already closed. Waiting only increases time, so that edge is permanently unusable from this arrival and is skipped.

Otherwise, the traveler can use the edge:

- if `time >= start`, depart immediately at `time`;
- if `time < start`, wait until `start` and then depart.

These cases combine into:

`departure = max(time, start)`.

Because the earlier guard guarantees `time <= end` and the input guarantees `start <= end`, this chosen departure also satisfies `departure <= end`. Traversal consumes one unit of time, so:

`arrival = max(time, start) + 1`.

The inclusive upper endpoint is important. Departing exactly at `end` is legal and arrives at `end + 1`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "edges": [[0, 1, 0, 1], [1, 2, 2, 5]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicit time-expanded graph:** Creating a state for every node and time is infeasible because availability endpoints can be as large as `10^9`. The arrival formula handles waiting symbolically.
- **Breadth-first search:** Edge traversal takes one unit, but forced waiting varies by edge and current arrival time, so the effective transition costs are not uniform.
- **Bellman-Ford:** It could repeatedly relax temporal edges but would be much slower; the nondecreasing arrival property permits Dijkstra.
- **Indexed priority queue:** A true decrease-key heap can maintain one active entry per node and support the manifest's conventional `\log n` heap factor.
- **Node 0 is the destination:** When `n = 1`, the initial tuple is already the target and the result is 0.
- **No outgoing edge from the start:** Unless `n = 1`, the queue empties and the result is `-1`.
- **Arrive before an edge opens:** `max(time, start)` waits exactly as long as necessary.
- **Arrive exactly at `end`:** The edge remains usable because the window is inclusive.
- **Arrive after `end`:** The source skips the edge because no amount of further waiting can reopen it.
- **Self-loops:** The constraints exclude them, but they would not improve an earliest time because traversal adds one.
- **Several edges to the same neighbor:** Each is tested independently; a later discovery may improve `earliest` and make an earlier heap entry stale.
- **Directedness:** A listed edge from `u` to `v` gives no route from `v` to `u` unless another edge explicitly provides it.
- **Cycles:** Every traversal increases time by one, and only strictly better arrival labels are pushed, so cycles cannot cause endless improvements.
- **Large time endpoints:** Python integers represent them exactly, and the algorithm never iterates through each waiting second.
- **Stale destination entry:** Stale tuples are rejected before the destination check, preventing a premature nonoptimal return.
- **Input preservation:** The solution builds a separate adjacency list and does not sort or mutate `edges`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+m)$. Let `n` be the number of nodes and `m` the number of directed edges. Building the adjacency list takes `O(n+m)` time and `O(n+m)` space.
- **Auxiliary Space Complexity:** $O(n+m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
