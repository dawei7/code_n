# Guided Example: Find Closest Node to Given Two Nodes

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"edges": [2, 2, 3, -1], "node1": 0, "node2": 1}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **directed** graph of `n` nodes numbered from `0` to $n - 1$, where each node has **at most one** outgoing edge.

The objective is to compute `2` from `{"edges": [2, 2, 3, -1], "node1": 0, "node2": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn the optimization into distance data

For a candidate node `i`, the score is

$$
\max(d_1(i),d_2(i)),
$$

where $d_1(i)$ is the shortest directed distance from `node1` and $d_2(i)$ is the shortest directed distance from `node2`. A node is eligible only if both distances are finite. Once both complete distance arrays are known, the remaining work is a simple scan: compute every node's score and keep the smallest one.

The graph has an unusually strong restriction: every node has at most one outgoing edge. Starting from a node, there is never a choice of which edge to follow. The reachable portion is a single directed path that may end at `-1` or eventually enter a cycle. This makes traversal simpler than in a general graph, although the exact solution still uses ordinary breadth-first search machinery.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"edges": [2, 2, 3, -1], "node1": 0, "node2": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Building the adjacency representation

The input `edges` stores one possible destination for each source index. The solution converts it to `g`, a `defaultdict(list)`. For every pair `(i, j)` produced by `enumerate(edges)`, it appends `j` to `g[i]` only when `j != -1`. Thus, each adjacency list has either zero or one neighbor.

This conversion is not strictly necessary—one could follow `edges[i]` directly—but it makes the traversal look like standard graph BFS. It also ensures that a node with no outgoing edge has an empty neighbor list when `g[i]` is accessed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Computing distances from one start

The nested function `f(i)` creates a distance array filled with `inf`. Infinity is a sentinel meaning “not reached from this start.” It then assigns distance zero to the starting node and pushes that node into a deque.

While the queue is nonempty, it removes a node from the left and inspects its adjacency list. For a neighbor `j`, it assigns



and enqueues `j` only if `dist[j] == inf`. The test serves as the visited check. Once a node has a finite distance, it cannot enter the queue again.

This visited condition is vital when the reachable path enters a cycle. Without it, traversal would follow the cycle forever. With it, the edge back to an already reached node is ignored and the queue eventually empties.

Because every edge has unit length, discovering a node from a node at distance $d$ assigns distance $d+1$. Breadth-first search processes discoveries in non-decreasing distance order, so the first assigned distance is shortest. In this special outdegree-at-most-one graph, there is only one directed route that can be followed from the start before a repetition, making that conclusion even more direct.

The solution calls `f(node1)` to obtain `d1` and `f(node2)` to obtain `d2`. These traversals are independent; a node can be reachable from one start but not the other.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"edges": [2, 2, 3, -1], "node1": 0, "node2": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Follow `edges` directly:** Since every node has at most one outgoing edge, a simple while-loop can record distances without building adjacency lists or using a deque. It preserves $O(n)$ time and can reduce constants.
- **Recursive depth-first search:** DFS also follows the unique path correctly, but a path of length $n$ can exceed Python's recursion limit. The iterative traversal avoids that risk.
- **Search from both starts simultaneously:** A combined traversal is possible, but separate distance arrays keep reachability and objective calculation clearer and make tie handling straightforward.
- **Cycle reachable from a start:** The finite-distance test prevents revisiting a node, so traversal stops after visiting each cycle node once.
- **A path ending at `-1`:** No adjacency entry is appended for that edge, so the sink has no neighbor and the queue becomes empty normally.
- **Reachable from only one start:** One distance stays `inf`, making the maximum infinite and preventing selection.
- **No common reachable node:** No strict improvement over the initial infinite best score occurs, so the method returns `-1`.
- **Equal objective scores:** Nodes are scanned in increasing index order, and the strict `<` update retains the smallest index.
- **Identical start nodes:** The shared start has score zero and is immediately the unique best possible answer.
- **Merging paths:** Two different starting paths may enter the same node and then share all later nodes. The distance arrays preserve their possibly different arrival lengths, allowing the final maximum to choose the best meeting point.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of nodes. Constructing `g` inspects all $n$ entries of `edges` and stores at most one directed edge per node, so it takes $O(n)$ time and $O(n)$ space.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
