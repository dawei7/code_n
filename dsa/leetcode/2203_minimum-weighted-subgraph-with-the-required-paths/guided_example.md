# Guided Example: Minimum Weighted Subgraph With the Required Paths

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "edges": [[0, 1, 1], [2, 1, 1]], "src1": 0, "src2": 1, "dest": 2}`
- **Required output:** `-1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n` denoting the number of nodes of a **weighted directed** graph. The nodes are numbered from `0` to $n - 1$.

The objective is to compute `-1` from `{"n": 3, "edges": [[0, 1, 1], [2, 1, 1]], "src1": 0, "src2": 1, "dest": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Build forward and reversed graphs

For each directed edge `f -> t` of weight `w`:

- `g[f]` stores `(t, w)` for travel in the original direction;
- `rg[t]` stores `(f, w)` for travel in the reversed graph.

The reversed edge does not change the original problem. It is a computational tool for finding distances toward `dest` with one single-source shortest-path run.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "edges": [[0, 1, 1], [2, 1, 1]], "src1": 0, "src2": 1, "dest": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Run Dijkstra from both sources

`dijkstra(g, src1)` returns array `d1`, where `d1[v]` is the minimum weight of a directed path from `src1` to `v`.

The analogous run from `src2` creates `d2`.

All edge weights are positive, satisfying Dijkstra's requirement that once the smallest current distance is finalized, no later route through nonnegative edges can improve it unexpectedly.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Compute every node-to-destination distance

Running `dijkstra(rg, dest)` follows reversed edges outward from `dest`.

A reversed path from `dest` to `v` corresponds edge-for-edge to an original directed path from `v` to `dest` with the same total weight. Thus `d3[v]` is the needed forward distance from `v` into the destination.

Without reversal, one would need a separate Dijkstra run from every possible meeting node or a different all-pairs method.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `-1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "edges": [[0, 1, 1], [2, 1, 1]], "src1": 0, "src2": 1, "dest": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `-1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Run Dijkstra only forward from `dest`:** This gives distances from destination to nodes, the wrong direction in a directed graph; reversing edges is essential.
- **Floyd–Warshall:** All-pairs shortest paths cost $O(n^3)$ and cannot handle $n=10^5$.
- **Bellman–Ford:** It supports negative weights but is unnecessary and much slower because all weights are positive.
- **Meeting at `src1` or `src2`:** The formula allows any node; a zero source-to-self distance handles these cases.
- **Meeting at `dest`:** Then `d3[dest] = 0`, representing two independent paths that share no earlier suffix.
- **Parallel directed edges:** Relaxation naturally chooses the cheaper useful route.
- **Unreachable component:** Infinity excludes that meeting node.
- **No feasible subgraph:** Every triple contains infinity and the return becomes `-1`.
- **Shared edges:** The conceptual union pays once; the optimal meeting-node proof accounts for shared suffix structure.
- **Positive weights:** They justify Dijkstra and removal of unnecessary cycles or split branches.
- **Stale heap entries:** The distance comparison prevents obsolete candidates from being expanded.
- **Input preservation:** Edges are copied into adjacency structures and not modified.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((n+m)$. Let $m$ be the number of edges. One binary-heap Dijkstra run takes $O((n+m)\log n)$ time in the standard bound. Three runs change only the constant factor, so total time remains $O((n+m)\log n)$.
- **Auxiliary Space Complexity:** $O(n+m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
