# Guided Example: Is Graph Bipartite?

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"graph": [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]}`
- **Required output:** `false`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is an **undirected** graph with `n` nodes, where each node is numbered between `0` and $n - 1$. You are given a 2D array `graph`, where $\text{graph}[u]$ is an array of nodes that node `u` is adjacent to. More formally, for each `v` in $\text{graph}[u]$, there is an undirected edge between node `u` and node `v`. The graph has the following properties:

The objective is to compute `false` from `{"graph": [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate the partition into a two-coloring

A bipartite graph can split its vertices into sets `A` and `B` so every edge crosses between the sets. Assign color `1` to vertices in one set and color `-1` to vertices in the other.

Then the requirement becomes simple: every edge must connect vertices with opposite colors. The actual names or signs of the colors do not matter; only equality versus opposition matters.

The solution stores one integer per vertex in `color`:

- `0` means the vertex has not been colored;
- `1` means the first side;
- `-1` means the second side.

Using `-c` produces the opposite side without a conditional expression.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"graph": [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Propagate forced colors with depth-first search

Function `dfs(a, c)` assigns color `c` to vertex `a`. Once `a` has a side, every neighbor `b` is forced to use `-c`.

For each neighbor, the condition handles two failure routes:

`color[b] == c or (color[b] == 0 and not dfs(b, -c))`.

The first route detects an immediate conflict: `a` and `b` are joined by an edge but already have the same color.

The second route applies only to an uncolored neighbor. It recursively colors that neighbor oppositely and explores everything forced by that choice. If the recursive component exploration finds any conflict, it returns `false`, which propagates through every active call.

If a neighbor is already colored `-c`, neither route applies. That edge is consistent, so scanning continues.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why greedy coloring does not require backtracking

Choosing the starting vertex's color may seem arbitrary, but swapping all colors within a connected component produces an equivalent partition. Once that first choice is made, every path forces the color of its endpoint according to whether the path length is even or odd.

There is therefore no meaningful alternative color choice to try at an individual neighbor. Giving a neighbor the same color would violate their connecting edge immediately. Giving it the opposite color is forced.

If two different paths later force contradictory colors for one vertex, the graph contains an odd cycle, and no global recoloring can resolve it. Returning false is conclusive; backtracking to flip only part of the component would break an edge elsewhere.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `false` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"graph": [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `false` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Breadth-first coloring:** A queue can propagate the same opposite-color rule iteratively in $O(V + E)$ time and $O(V)$ space, avoiding recursion-depth concerns.
- **Union-find with doubled sets:** Represent each vertex and its opposite side, then union edge constraints. It works but is more elaborate than direct traversal.
- **Check only one component:** Incorrect because an unvisited component may contain an odd cycle.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V + E)$. Let $V$ be the number of vertices and $E$ the number of undirected edges. Each vertex is colored once. Its adjacency list is scanned during that one DFS visit. Because every undirected edge appears in two adjacency lists, total time is $O(V + E)$.
- **Auxiliary Space Complexity:** $O(V)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
