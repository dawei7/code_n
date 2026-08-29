# Guided Example: Find Shortest Path with K Hops

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4, "edges": [[0, 1, 4], [0, 2, 2], [2, 3, 6]], "s": 1, "d": 3, "k": 2}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a positive integer `n` which is the number of nodes of a **0-indexed undirected weighted connected** graph and a **0-indexed** **2D array** `edges` where $\text{edges}[i] = [u_{i}, v_{i}, w_{i}]$ indicates that there is an edge between nodes $u_{i}$ and $v_{i}$ with weight $w_{i}$.

The objective is to compute `2` from `{"n": 4, "edges": [[0, 1, 4], [0, 2, 2], [2, 3, 6]], "s": 1, "d": 3, "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Expand one graph node into hop-count states

Reaching node $u$ after using $t$ free hops is different from reaching the same node after using another number, because the remaining free-hop budget differs.

The algorithm therefore treats `(u, t)` as a shortest-path state, where $0\le t\le k$ is the exact number of free edges already used.

Matrix `dist[u][t]` stores the minimum paid cost known for that state.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4, "edges": [[0, 1, 4], [0, 2, 2], [2, 3, 6]], "s": 1, "d": 3, "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build the ordinary undirected adjacency list

For every edge `[u, v, w]`, the source appends `(v, w)` to `g[u]` and `(u, w)` to `g[v]`.

The same physical edge can be traversed in either direction. All weights are positive, and using a hop changes one chosen traversal's paid cost to zero.

The input graph itself is not modified.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Start with no free edge used

At the source, the path cost is zero and no hop has been consumed:

`dist[s][0] = 0`.

The initial heap entry is `(0, s, 0)`. Every later heap entry orders states by current candidate distance first.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4, "edges": [[0, 1, 4], [0, 2, 2], [2, 3, 6]], "s": 1, "d": 3, "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Add the stale-entry check:** Preserves behavior and realizes the standard manifest heap bound.
- **Bellman-Ford-style DP by hops:** Can model layers but does not exploit nonnegative weights as efficiently.
- **Explicit expanded graph construction:** Correct but unnecessary because transitions can be generated from `g`.
- **`k = 0`:** Only paid transitions exist, reducing to ordinary shortest path.
- **Use fewer than `k` hops:** Final minimum over all layers permits it.
- **Hop a heavy edge:** Often beneficial, but global path structure decides the optimum.
- **Zero-cost expanded transitions:** Safe for Dijkstra because they are nonnegative.
- **Connected graph:** Guarantees at least one finite destination state.
- **Repeated visits to one original node:** Different hop counts remain distinct states.
- **Stale heap entry:** May add work but cannot worsen a stored distance.
- **Input preservation:** Hopping is represented in state transitions; edge weights are never edited.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(E*(K+1)*log(n*(K+1)))$. The expanded graph has $n(k+1)$ states and $O(E(k+1))$ transitions. With a stale-entry guard, standard Dijkstra costs $O(E(k+1)\log(n(k+1)))$ time.
- **Auxiliary Space Complexity:** $O((n+E)*(K+1))$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
