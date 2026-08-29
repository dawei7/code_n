# Guided Example: Count Unreachable Pairs of Nodes in an Undirected Graph

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "edges": [[0, 1], [0, 2], [1, 2]]}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n`. There is an **undirected** graph with `n` nodes, numbered from `0` to $n - 1$. You are given a 2D integer array `edges` where $\text{edges}[i] = [a_{i}, b_{i}]$ denotes that there exists an **undirected** edge connecting nodes $a_{i}$ and $b_{i}$.

The objective is to compute `0` from `{"n": 3, "edges": [[0, 1], [0, 2], [1, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Unreachability is determined entirely by connected components

In an undirected graph, two nodes can reach one another exactly when they belong to the same connected component. Therefore the individual paths do not need to be counted. The task reduces to finding each component's size and counting pairs whose endpoints come from different components.

If previously discovered components contain `s` nodes altogether and a newly discovered component contains `t` nodes, then every one of those `t` new nodes is unreachable from every one of the `s` previous nodes. This creates

`s \cdot t`

new unordered pairs. No pair inside the new component is counted because its endpoints are reachable, and pairs with components not discovered yet will be counted later when those components become new.

The solution combines this counting formula with depth-first search.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "edges": [[0, 1], [0, 2], [1, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build an undirected adjacency list

The list `g` has one inner list for every node. For an edge `[a, b]`, the code appends `b` to `g[a]` and `a` to `g[b]`. Both directions are required because reachability may traverse an undirected edge either way.

An isolated node simply has an empty neighbor list. It is still a connected component of size one and will be handled by the outer loop.

The Boolean list `vis` records whether a node has already been discovered by an earlier DFS call. It serves two purposes: it prevents endless movement back and forth across undirected edges, and it ensures each node contributes to exactly one component size.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Make DFS return the number of newly visited nodes

The helper `dfs(i)` first checks `vis[i]`. If the node was already visited, it returns zero because this call discovers no new member. Otherwise, it marks the node and returns

`1 + sum(dfs(j) for j in g[i])`.

The one counts node `i` itself. Each recursive neighbor call counts all still-unvisited nodes reachable through that neighbor. A neighbor already reached by another branch returns zero, so cycles and multiple routes do not double-count nodes.

When `dfs(i)` begins at an unvisited node, recursion follows every edge path within that component. It cannot leave the component because no edge crosses between components. It eventually visits every component node because each is connected to the start by some path. The returned sum is therefore exactly that component's size.

The outer loop still calls `dfs(i)` for every node `i`. If `i` belongs to a component found earlier, the immediate visited check returns `t = 0`. The later arithmetic then adds nothing and changes nothing. This avoids needing a separate `if not vis[i]` branch in the outer loop.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "edges": [[0, 1], [0, 2], [1, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Iterative DFS:** Replace recursive calls with an explicit stack and count nodes as they are popped or pushed. It has the same `O(n + e)` bounds and avoids Python recursion-depth failure.
- **Breadth-first search:** A queue finds the same component sizes level by level. It is equally correct and iterative, with a worst-case queue of `O(n)` nodes.
- **Union-find:** Union every edge, obtain each representative's component size, then apply the same cross-component formula. With path compression and union by size or rank, it is near-linear and uses `O(n)` space without an adjacency list.
- **Count all pairs then subtract reachable pairs:** Begin with `n(n-1)/2` and subtract `t(t-1)/2` for each component. This is mathematically equivalent; the running-prefix formula avoids one final combinatorial subtraction.
- **Multiply each component by `n - t` and sum:** This counts every cross-component pair twice, once from each endpoint's component, so it would require division by two. The prefix method counts once directly.
- **Complete connected graph:** The first DFS returns `n` while `s = 0`, and all later DFS calls return zero. The answer correctly remains zero.
- **No edges:** Every DFS discovers one isolated node. The accumulated products become `0 + 1 + 2 + \cdots + (n-1) = n(n-1)/2`.
- **One node:** Its component has size one and there is no different-node pair, so the answer is zero.
- **Several components of equal size:** Component identity and discovery order do not affect the total. Each cross-component endpoint combination is still counted once.
- **Cycles:** The visited check prevents recursion from looping and makes already reached neighbors contribute zero.
- **Multiple paths to one node:** The first path marks it; every later path receives zero from that node, preventing duplicate size contributions.
- **Input edge uniqueness:** Repeated edges are excluded by the contract. Even if present, visited checks would preserve correctness, but the adjacency list and traversal would do redundant work.
- **Self-loops:** The contract excludes them. A self-loop would immediately call an already visited node and contribute zero, so it would not change component size.
- **Recursion depth:** A star graph has shallow recursion, while a path graph may reach linear depth. The same asymptotic graph size can therefore behave differently under Python's recursion limit.
- **Input mutation:** The method builds separate adjacency and visited lists and never changes `edges`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n + e)$. Let `n` be the node count and `e` the edge count. Constructing the adjacency list takes `O(n + e)` time including creation of the `n` lists. DFS newly visits each node once. Each undirected edge appears in two adjacency lists, so neighbor traversal considers it twice. Calls made toward already visited neighbors return immediately and are included in this same `O(e)` accounting. The outer scan adds `O(n)` work. Total time is `O(n + e)`.
- **Auxiliary Space Complexity:** $O(n+e)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
