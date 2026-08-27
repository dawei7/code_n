# Guided Example: All Paths from Source Lead to Destination

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "edges": [[0, 1], [0, 2]], "source": 0, "destination": 2}`
- **Required output:** `false`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given the `edges` of a directed graph where $\text{edges}[i] = [a_{i}, b_{i}]$ indicates there is an edge between nodes $a_{i}$ and $b_{i}$, and two nodes `source` and `destination` of this graph, determine whether or not all paths starting from `source` eventually, end at `destination`, that is:

The objective is to compute `false` from `{"n": 3, "edges": [[0, 1], [0, 2]], "source": 0, "destination": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate "all paths lead there" into graph conditions

For the answer to be true, the part of the directed graph reachable from `source` must satisfy two structural rules:

1. Every reachable node with no outgoing edge must be `destination`.
2. No directed cycle may be reachable from `source`.

The first rule prevents a path from getting stuck at the wrong terminal. The second prevents a path from looping forever and creates only finitely many possible paths in the reachable subgraph.

These rules also ensure that a path to `destination` actually exists. In a finite acyclic directed graph, repeatedly following outgoing edges must eventually reach a terminal node. If every reachable terminal is `destination`, at least one such walk from `source` ends there.

Depth-first search is a natural fit because its active recursion stack identifies directed cycles, while its return value can say whether every continuation from one node is valid.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "edges": [[0, 1], [0, 2]], "source": 0, "destination": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build the adjacency list

The graph representation is:



`g[i]` contains every node reachable by one outgoing edge from node `i`. A node is terminal exactly when `g[i]` is empty.

Parallel edges are retained. That is harmless: following the same destination twice does not change whether it is valid, and memoized states make repeated completed work constant time.

Self-loops are also retained. They must be detected as cycles, and the DFS coloring does so.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The graph representation is:



`g[i]` contains every node r... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The destination itself must be terminal

Before starting DFS, the exact solution checks:



If `destination` has an outgoing edge, a path can arrive there and then continue. It is not a terminal endpoint as required. A self-loop at the destination is also invalid because it permits infinitely many traversals.

This check is valid even if destination is unreachable. In that case the overall answer would be false anyway because no source path reaches the destination.

Making the requirement explicit also simplifies the interpretation of the recursive base case: the only acceptable terminal node is an actually terminal destination.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `false` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "edges": [[0, 1], [0, 2]], "source": 0, "destination": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `false` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Iterative three-color DFS:** Store explicit st:** - **Iterative three-color DFS:** Store explicit stack frames containing a node and its next neighbor index. This preserves `O(V + E)` bounds while avoiding Python recursion-depth limits on a chain of up to 10000 nodes.
- **Topological processing of the reachable subgraph:** One can first identify reachable nodes, reject reachable cycles with a topological count, and verify all reachable terminals. This is valid but needs more bookkeeping than the direct DFS.
- **A simple visited Boolean is insufficient:** Seeing an already visited node does not say whether it is an active back edge or a safely completed shared subgraph. Three states are necessary for directed-cycle reasoning.
- **Destination has an outgoing edge:** The explicit precheck returns false, including when that edge is a self-loop.
- **Source equals destination:** The result is true only when destination is terminal. If it has outgoing edges, paths can continue and the precheck returns false.
- **Source is a wrong terminal:** `g[source]` is empty but `source != destination`, so DFS immediately returns false.
- **Wrong terminal on one branch:** Even if many other branches reach destination, the first wrong terminal makes its recursive call false and invalidates the universal condition.
- **Reachable cycle with an exit to destination:** The exit does not help. A path may traverse the cycle arbitrarily many times, so the visiting-state encounter returns false.
- **Unreachable cycle:** DFS never touches it, and it correctly has no effect on paths beginning at source.
- **Self-loop:** The node is marked visiting before its neighbor call reaches the same node. State one returns false and detects the cycle.
- **Parallel edges:** If the first copy leads to a verified child, later copies return true immediately. They do not create a cycle by themselves.
- **Diamond-shaped DAG:** Multiple branches may converge on one node. The first traversal verifies it, and later branches reuse state two rather than treating convergence as a cycle.
- **No edges:** The answer is true only when `source == destination`; otherwise source is a wrong terminal.
- **Long chain:** Correctness is straightforward, but recursive depth may exceed the interpreter's configured limit. An iterative stack is safer in environments with a low recursion limit.
- **At least one path condition:** In a finite reachable acyclic graph, following edges must end at a terminal. If DFS returns true, that terminal can only be destination, so existence follows from the other verified conditions.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V + E)$. Let `V = n` and let `E` be the number of directed edges.
- **Auxiliary Space Complexity:** $O(V + E)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
