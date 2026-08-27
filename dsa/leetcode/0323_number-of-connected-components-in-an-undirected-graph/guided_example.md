# Guided Example: Number of Connected Components in an Undirected Graph

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 5, "edges": [[0, 1], [1, 2], [3, 4]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have a graph of `n` nodes. You are given an integer `n` and an array `edges` where $\text{edges}[i] = [a_{i}, b_{i}]$ indicates that there is an edge between $a_{i}$ and $b_{i}$ in the graph.

The objective is to compute `2` from `{"n": 5, "edges": [[0, 1], [1, 2], [3, 4]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A component is discovered by one complete graph traversal.

Two vertices belong to the same connected component when some path of undirected edges connects them. Starting a depth-first search from one vertex follows every reachable edge, then every edge reachable from those neighbors, and so on. Therefore, after that search finishes, every vertex in the start vertex's component has been visited.

This leads to a counting rule: scan all vertices, and start a new search only when the current vertex has never been reached before. Each such new search discovers one previously unseen component. Vertices encountered later from that same component are already marked and do not increase the count.

The exact optimal source expresses this rule compactly by making `dfs(i)` return `1` when `i` begins a new traversal and `0` when `i` was already visited. Summing `dfs(i)` over every vertex then gives the number of components.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 5, "edges": [[0, 1], [1, 2], [3, 4]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build the graph in both directions.

The input supplies endpoint pairs rather than an adjacency structure. The source creates `g`, a list containing one neighbor list for every vertex from `0` through `n - 1`. For each edge `[a,b]`, it performs both updates:

- append `b` to `g[a]`;
- append `a` to `g[b]`.

Both are necessary because the graph is undirected. If only the first direction were stored, reachability would depend on the arbitrary endpoint order used in `edges`. For example, an input edge written as `[1,0]` must still allow a traversal starting at `0` to reach `1`.

An isolated vertex naturally has an empty neighbor list. It is still present in `g`, because `g` is created from `n`, not merely from vertices mentioned in `edges`. This ensures isolated vertices are counted as one-vertex components.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The input supplies endpoint pairs rather than an adjacency s... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Meaning and behavior of `dfs(i)`.

The set `vis` contains every vertex that has already been claimed by a traversal. On entry, the helper first asks whether `i` is in that set.

If it is, `dfs(i)` immediately returns `0`. No new component began, and there is no reason to explore the same neighbors again. This early return is also what prevents infinite recursion in an undirected graph. Every stored edge can lead back to the vertex from which the search just came, and cycles can lead to many previously seen vertices.

If `i` is not visited, the helper adds it to `vis` before following any edge. Marking before recursion is crucial. If marking were delayed until after the neighbor loop, an edge from `i` to `j` could recurse from `j` straight back to the still-unmarked `i`, causing repeated recursion.

The helper then calls `dfs(j)` for every neighbor `j` in `g[i]`. It does not check `j in vis` in the loop itself; the called helper performs that check at its entrance. Return values from these neighbor calls are deliberately ignored. A neighbor reached during the current traversal belongs to the same component as `i`, so it must not be counted as a separate component even if that neighbor was previously unseen. Only the outer scan's fresh roots contribute to the answer.

After all reachable neighbors have been explored, the original fresh call returns `1`. That value means “this call started discovery of one component,” not “this component contains one vertex.” Regardless of whether the traversal reaches one vertex or hundreds, its root contributes exactly one.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 5, "edges": [[0, 1], [1, 2], [3, 4]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Iterative depth-first search:** Use an explici:** - **Iterative depth-first search:** Use an explicit stack instead of recursive calls. It has the same $O(V+E)$ time and space bounds and follows the same component-counting proof, while avoiding language recursion-depth limits.
- **- **Breadth-first search:** A queue can explore ev:** - **Breadth-first search:** A queue can explore every vertex reachable from each fresh root. BFS also counts components in $O(V+E)$ time and uses $O(V+E)$ total storage including the graph. Traversal order changes, but the discovered component does not.
- **- **Disjoint set union:** Begin with $V$ component:** - **Disjoint set union:** Begin with $V$ components and union the endpoints of each edge, decrementing the count only when two different sets merge. With path compression and union by size, this uses $O(V)$ extra space without an adjacency list and takes $O(V + E\alpha(V))$ time. It matches the current manifest summary but is not the exact optimal solution file.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V)$. Let $V=n$ be the number of vertices and let $E$ be the number of undirected edges. Creating the $V$ empty adjacency lists costs $O(V)$. Adding both endpoints for every input edge costs $O(E)$.
- **Auxiliary Space Complexity:** $O(V)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
