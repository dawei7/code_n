# Guided Example: Divide Nodes Into the Maximum Number of Groups

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 6, "edges": [[1, 2], [1, 4], [1, 5], [2, 6], [2, 3], [4, 6]]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a positive integer `n` representing the number of nodes in an **undirected** graph. The nodes are labeled from `1` to `n`.

The objective is to compute `4` from `{"n": 6, "edges": [[1, 2], [1, 4], [1, 5], [2, 6], [2, 3], [4, 6]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Group numbers behave like BFS levels

For every edge, endpoint group indices must differ by exactly one. If one node is placed in a group and graph distance is measured from it, assigning each node to one plus its shortest-path distance is a natural candidate: adjacent vertices have distances differing by at most one.

However, an edge whose endpoints have the same distance would violate the exact-difference rule. A graph permits this level assignment precisely when it is bipartite. An odd cycle forces some edge to connect equal-parity levels and makes every valid grouping impossible.

The exact solution combines bipartiteness checking and layer counting inside a breadth-first search started from every node.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 6, "edges": [[1, 2], [1, 4], [1, 5], [2, 6], [2, 3], [4, 6]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: One BFS from source `i`

Array `dist` begins with zeros, meaning unvisited. The source receives distance label one rather than zero, and `mx` also begins at one. These labels are directly the number of occupied BFS layers.

When BFS crosses from `a` to an unvisited neighbor `b`, it assigns

`dist[b] = dist[a]+1`,

updates `mx`, and enqueues `b`. Standard BFS guarantees this is one plus the shortest unweighted distance from source `i`.

For an already visited neighbor, the code requires

`abs(dist[b]-dist[a]) == 1`.

In an undirected graph, shortest-path distances of adjacent vertices can differ by at most one. Therefore, failure means they are equal. Such a same-level edge joins vertices of the same parity and exposes an odd cycle, so no valid grouping exists and the method returns `-1`.

Conversely, in a bipartite component every edge crosses between the two parity classes. BFS distances then have opposite parity at its endpoints; combined with the at-most-one property, their difference must be exactly one. The check accepts every edge.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the maximum BFS layer count is the component answer

For a fixed source, assigning nodes according to `dist` creates `mx` consecutive groups and satisfies every edge when the component is bipartite. Thus `mx` groups are achievable.

The farthest node from that source has shortest-path distance `mx-1`. Across every possible source, the greatest such distance is the component's diameter, the longest shortest-path distance between any two vertices. The code runs BFS from every node and takes the largest `mx`, so it obtains

$$
\text{diameter}+1
$$

groups for the component.

No valid grouping can use more. Along any edge, the group number changes by one. Choose nodes in the smallest and largest occupied groups of a connected component. Any graph path between them must make enough unit changes to cover that group-index difference, so their shortest-path distance is at least the difference. That difference cannot exceed the diameter. Therefore, the number of occupied consecutive groups is at most diameter plus one.

The BFS construction reaches this bound, proving maximality.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 6, "edges": [[1, 2], [1, 4], [1, 5], [2, 6], [2, 3], [4, 6]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Separate coloring pass:** First test bipartiteness per component, then BFS from every component node for diameter. It is conceptually separated but has the same asymptotic cost.
- **Union-find for component keys:** It can replace the minimum-vertex `root` technique but does not test bipartiteness or compute diameters by itself.
- **Odd cycle:** Some BFS encounters an already visited same-level neighbor and returns `-1`.
- **Even cycle:** Alternating BFS layers satisfy every edge, so it is valid.
- **Disconnected graph:** Store one maximum layer count per component and add them.
- **Isolated node:** It forms a valid one-group component.
- **One BFS per component is insufficient:** An arbitrary source may not be a diameter endpoint and may yield too few layers.
- **Labels start at one:** Zero remains available as the unvisited sentinel in `dist`.
- **Common component key:** Taking the minimum visited index makes all sources in a component update the same dictionary entry.
- **Parallel or self edges:** The contract excludes them, simplifying adjacency behavior.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n(n+m))$. Let $m$ be the number of edges. Building `g` takes $O(n+m)$ space and time. A BFS from one source allocates an $O(n)$ distance array and, in the worst case, scans its component's vertices and edges in $O(n+m)$ time. Repeating for all $n$ sources gives $O(n(n+m))$ worst-case time.
- **Auxiliary Space Complexity:** $O(n+m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
