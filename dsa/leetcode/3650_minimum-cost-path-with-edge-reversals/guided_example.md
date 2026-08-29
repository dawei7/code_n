# Guided Example: Minimum Cost Path with Edge Reversals

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4, "edges": [[0, 1, 3], [3, 1, 1], [2, 3, 4], [0, 2, 2]]}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a directed, weighted graph with `n` nodes labeled from 0 to $n - 1$, and an array `edges` where $\text{edges}[i] = [u_{i}, v_{i}, w_{i}]$ represents a directed edge from node $u_{i}$ to node $v_{i}$ with cost $w_{i}$.

The objective is to compute `5` from `{"n": 4, "edges": [[0, 1, 3], [3, 1, 1], [2, 3, 4], [0, 2, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Represent a one-move reversal as another directed arc

For every original edge

`u -> v` with cost `w`,

there are two ways it may be traversed:

- Normally from `u` to `v` for cost `w`.
- By using the switch at `v` to reverse that incoming edge for one move, traveling from `v` to `u` for cost `2w`.

The source writes both possibilities into an adjacency list:

`g[u].append((v, w))`

and

`g[v].append((u, 2 * w))`.

The second arc does not permanently reverse the original edge. It is only a representation of the legal action “activate the switch here and immediately traverse this incoming edge backward.” Future moves still see the same original possibilities.

After this transformation, every legal move has become an ordinary directed weighted arc. The path problem can therefore be solved with a standard shortest-path algorithm rather than choosing reversals separately.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4, "edges": [[0, 1, 3], [3, 1, 1], [2, 3, 4], [0, 2, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the per-node one-use switch does not require an extra state bit

At first, adding every reverse arc seems to allow the switch at one node to be used repeatedly. A transformed walk could leave a node along a reverse arc, later return to that node, and leave along another reverse arc.

All original costs are positive, and every doubled reverse cost is positive as well. In a positive-weight graph, a minimum-cost path never needs to visit the same node twice. If a walk repeats node `u`, the portion from its first occurrence of `u` to the next occurrence is a positive-cost cycle. Removing that entire cycle joins the prefix and suffix at the same node, preserves a valid walk, and strictly lowers the cost.

Therefore some optimal transformed path is simple: it visits each node at most once. A simple path can depart from a node only once, so it can traverse at most one reverse arc associated with that node’s switch. The original “at most once per node” restriction is automatically respected by the shortest useful path.

This argument is why the source does not expand the state into combinations of used switches. Tracking one Boolean per node would create an impossible `2^n` state space and is unnecessary under positive weights.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why Dijkstra is the appropriate shortest-path algorithm

The transformed graph has no negative edges. Normal arcs cost at least one, and reverse arcs cost at least two. Dijkstra’s algorithm is designed for exactly this setting.

The array `dist` stores the smallest cost discovered so far from node zero to every node. Initially every entry is infinity except `dist[0] = 0`. The priority queue begins with `(0, 0)` and always removes the pending node occurrence with the smallest tentative distance.

When `(d, u)` is removed, the source examines every transformed outgoing arc `u -> v` of weight `w`. Traveling through it would produce

`nd = d + w`.

If `nd < dist[v]`, this route is strictly better than every previously discovered route to `v`. The method updates `dist[v]` and pushes `(nd, v)` into the heap.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4, "edges": [[0, 1, 3], [3, 1, 1], [2, 3, 4], [0, 2, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **State-expanded search over used switches:** Remembering which of `V` node switches were used would lead toward `2^V` combinations. Positive weights and simple optimal paths make that state unnecessary.
- **Bellman–Ford:** It handles negative edges but would cost `O(VE)`. All transformed weights are positive, so Dijkstra is substantially more efficient.
- **Breadth-first search:** BFS minimizes edge count, not weighted cost. Original weights vary and reverse arcs cost twice their originals, so a FIFO queue is not valid.
- **Permanently reverse edges:** The operation applies only to one immediate traversal. Mutating the graph would incorrectly affect later moves; adding a separate reverse option models the rule faithfully.
- **Add reverse cost `w` instead of `2w`:** This underprices switch use. Every reverse option must store exactly twice the original edge’s cost.
- **Use a switch at the edge’s source:** Reversing `u -> v` is initiated after arriving at `v`, so the added arc leaves `v` and conceptually uses node `v`’s switch.
- **No reversal needed:** Normal arcs remain present at their original costs, so Dijkstra can choose an entirely original directed path.
- **Destination unreachable:** If neither normal nor legal reverse arcs connect node zero to node `n - 1`, the heap empties and the source returns `-1`.
- **Parallel edges:** They may create several arcs between the same nodes with different weights. Relaxation naturally retains whichever yields the smaller total distance.
- **Self-loops:** A positive self-loop cannot improve a minimum path. It may be stored but never produces a smaller distance.
- **Cycles:** Every transformed cycle has positive cost. Removing it makes a route cheaper, which is also what justifies the per-node switch simplification.
- **Early destination return:** It is safe only after the stale-entry check. Returning from an obsolete larger destination entry before checking `dist` could be incorrect.
- **Integer costs:** The maximum route cost can exceed one edge’s bound, but Python integers do not overflow. Other languages should use a sufficiently wide integer type.
- **Missing imports:** The stored source refers to `List`, `inf`, `heappop`, and `heappush` without importing them. Standalone Python would need the corresponding `typing`, `math`, and `heapq` imports unless supplied by the harness.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(E)$. Let `V = n` and let `E` be the number of original edges. Graph construction creates exactly `2E` stored arcs and takes `O(V + E)` time including the adjacency-list allocation.
- **Auxiliary Space Complexity:** $O(V + E)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
