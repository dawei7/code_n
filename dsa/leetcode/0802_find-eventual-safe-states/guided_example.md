# Guided Example: Find Eventual Safe States

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"graph": [[1, 2], [2, 3], [5], [0], [5], [], []]}`
- **Required output:** `[2, 4, 5, 6]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a directed graph of `n` nodes with each node labeled from `0` to $n - 1$. The graph is represented by a **0-indexed** 2D integer array `graph` where $\text{graph}[i]$ is an integer array of nodes adjacent to node `i`, meaning there is an edge from node `i` to each node in $\text{graph}[i]$.

The objective is to compute `[2, 4, 5, 6]` from `{"graph": [[1, 2], [2, 3], [5], [0], [5], [], []]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Characterize safety through outgoing neighbors

A terminal node is safe because every path starting there ends immediately.

A nonterminal node is safe exactly when every one of its outgoing neighbors is safe. If even one edge leads toward a cycle, choosing that edge creates a path that never has to reach a terminal node, so the source is unsafe.

This suggests starting with known terminal nodes and repeatedly marking any node whose outgoing choices have all become known safe.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"graph": [[1, 2], [2, 3], [5], [0], [5], [], []]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reverse edges to move from a safe node to its predecessors

The input graph lists outgoing neighbors. Once node `j` is proven safe, the algorithm needs to find every node `i` that points to `j` so it can remove that now-resolved outgoing dependency.

Dictionary `rg` stores the reversed graph:

`rg[j].append(i)`

for every original edge `i -> j`.

Thus `rg[j]` is the list of original predecessors that may become safe after `j` is resolved.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The input graph lists outgoing neighbors.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Interpret `indeg` carefully

Despite its name, `indeg[i]` is not the original graph's incoming-edge count. The code assigns:

`indeg[i] = len(graph[i])`.

It is the number of outgoing edges from `i` that have not yet been proven to lead to safe nodes.

Calling it a remaining-outdegree counter makes the algorithm easier to understand. Initially every outgoing edge is unresolved. Each time a successor becomes safe, one counter is removed from each predecessor.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 4, 5, 6]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"graph": [[1, 2], [2, 3], [5], [0], [5], [], []]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 4, 5, 6]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Three-color depth-first search:** Mark nodes u:** - **Three-color depth-first search:** Mark nodes unvisited, active, or confirmed safe. It also takes $O(V+E)$ but uses recursion or an explicit stack.
- **- **Run cycle detection independently from every n:** - **Run cycle detection independently from every node:** It repeats work and can become quadratic without memoized states.
- **- **Return queue order:** Incorrect for the requir:** - **Return queue order:** Incorrect for the required ascending output; scan node indices afterward.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V+E)$. Let $V$ be the number of nodes and $E$ the number of directed edges. Building the reverse graph and remaining-outdegree counts examines each node and edge once. Queue processing removes each reverse edge once, and the final scan visits each node once. Total time is $O(V+E)$.
- **Auxiliary Space Complexity:** $O(V)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
