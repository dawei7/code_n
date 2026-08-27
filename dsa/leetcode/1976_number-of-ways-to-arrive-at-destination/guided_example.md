# Guided Example: Number of Ways to Arrive at Destination

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 2, "roads": [[1, 0, 10]]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are in a city that consists of `n` intersections numbered from `0` to $n - 1$ with **bi-directional** roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

The objective is to compute `1` from `{"n": 2, "roads": [[1, 0, 10]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Solve two tasks together

The method must find the shortest travel time from intersection 0 to every intersection and count how many paths achieve each shortest time. The source extends Dijkstra's algorithm with a second array of path counts.

`dist[v]` is the best travel time currently known from 0 to `v`. `f[v]` is the number of paths achieving exactly that time. Initially, `dist[0] = 0` and `f[0] = 1` because the empty path reaches the source in one way with zero time. Every other distance starts at infinity and every other count starts at zero.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 2, "roads": [[1, 0, 10]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build the exact dense graph representation

The source allocates an $n$-by-$n$ matrix `g` filled with infinity. For every undirected road `[u, v, t]`, it assigns both `g[u][v]` and `g[v][u]` to `t`. Infinity means that no direct road exists.

It also sets `g[0][0] = 0`, although the relaxation loop explicitly skips `j == t` and therefore does not need a self-edge for correctness.

This matrix gives constant-time road-weight lookup, but it is dense storage even when few roads exist. That detail changes the exact complexity from the sparse adjacency-list version usually associated with heap-based Dijkstra.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The source allocates an $n$-by-$n$ matrix `g` filled with in... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Select the next finalized vertex

On each of $n$ rounds, the inner selection loop scans every vertex and chooses the unvisited vertex `t` with the smallest current `dist`. It then marks `vis[t] = true`.

All road times are positive. Therefore, once `t` has the smallest tentative distance among unvisited vertices, no route passing through another unvisited vertex can later make `dist[t]` smaller. The distance is finalized exactly as in ordinary Dijkstra.

The graph is guaranteed connected, so some finite-distance unvisited vertex exists on every round. The source would need a guard for `t == -1` on a disconnected graph, but that situation is outside the contract.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 2, "roads": [[1, 0, 10]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Heap Dijkstra with adjacency lists:** This ach:** - **Heap Dijkstra with adjacency lists:** This achieves $O((V+E)\log V)$ time and $O(V+E)$ space and matches the manifest, especially benefiting sparse graphs.
- **Floyd-Warshall:** It can compute all-pairs distances but costs $O(V^3)$ and is unnecessary for one source.
- **Ordinary BFS:** It is incorrect because road times are positive but not necessarily equal.
- **Strictly shorter relaxation:** Replace both the distance and count; keeping the old count would include nonshortest paths.
- **Equal relaxation:** Add the predecessor count because it represents additional shortest paths.
- **Longer relaxation:** Ignore it completely.
- **Non-edge represented by infinity:** The exact code may temporarily add meaningless counts to still-infinite vertices, but a real finite relaxation overwrites them before finalization in the connected graph.
- **Connected graph:** This guarantee prevents selection from leaving `t` at negative one.
- **Positive weights:** They ensure every shortest-path predecessor is finalized before its successor; zero-weight roads would complicate count finalization.
- **Direct source-to-destination road:** It competes normally with multi-road routes of the same total time.
- **Large path count:** Python avoids overflow, and the result is reduced modulo $10^9+7$.
- **No early exit:** The source processes all vertices even after the destination is finalized; this does not affect correctness.
- **Input preservation:** Road rows are read into a new matrix and are not modified.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(E)$. Let $V=n$ and let $E$ be the number of roads. Allocating and initializing `g` costs $O(V^2)$ time and space; inserting roads costs $O(E)$ time.
- **Auxiliary Space Complexity:** $O(E)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
