# Guided Example: Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4, "edges": [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]}`
- **Required output:** `[[], [0, 1, 2, 3]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a weighted undirected connected graph with `n` vertices numbered from `0` to $n - 1$, and an array `edges` where $\text{edges}[i] = [a_{i}, b_{i}, \text{weight}_{i}]$ represents a bidirectional and weighted edge between nodes $a_{i}$ and $b_{i}$. A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles and with the minimum possible total edge weight.

The objective is to compute `[[], [0, 1, 2, 3]]` from `{"n": 4, "edges": [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turning edge classification into controlled MST experiments

All minimum spanning trees have the same total weight, even when their edge sets differ. This lets the stored solution classify an edge by comparing constrained Kruskal runs with the ordinary minimum weight.

An edge is critical if removing it makes the graph disconnected or makes the cheapest remaining spanning tree heavier. It is pseudo-critical if it is not critical and there exists a minimum spanning tree that includes it. The source tests these definitions directly: exclude an edge to test necessity, then force it to test eligibility.

Before sorting, the loop appends each original position `i` to its edge record. An edge changes from three fields to four fields: endpoints, weight, and original index. The list is then sorted by weight for Kruskal's algorithm. Preserving the index is necessary because the returned identifiers refer to the original input order rather than sorted positions.

This preprocessing mutates `edges` in place by extending every inner list and reordering the outer list. That behavior does not affect the returned classification, but callers should not expect the input structure to remain unchanged.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4, "edges": [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: How the union-find supports Kruskal

`UnionFind` starts with every vertex in its own component. The array `p` stores parent links, and `n` stores the current number of components.

`find(x)` follows parent links to a representative. On the return path, it rewrites visited links to point directly toward that representative. This path compression accelerates later searches.

`union(a, b)` first checks whether both endpoints already share a representative. If so, adding the edge would create a cycle, so it returns false. Otherwise, it attaches one representative beneath the other, decreases the component count, and returns true. The implementation does not use union by rank or size.

Kruskal scans edges from smallest to largest weight. It accepts an edge exactly when `union` joins two previously separate components. Consequently, accepted edges never form a cycle. For a connected graph, they eventually join all vertices with the minimum possible total weight.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `UnionFind` starts with every vertex in its own component.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Computing the baseline

The first union-find run evaluates

`sum(w for f, t, w, _ in edges if uf.union(f, t))`.

The generator calls `union` as its filter. A weight enters the sum only when that edge connects two components. The resulting value `v` is the weight of an ordinary MST. The input graph is guaranteed connected, so this run reaches one component.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[], [0, 1, 2, 3]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4, "edges": [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[], [0, 1, 2, 3]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Weight-group bridge classification:** Process :** - **Weight-group bridge classification:** Process edges of equal weight together after contracting components formed by lighter edges, then find bridges in the temporary multigraph. This can achieve the manifest's $O(E \log E)$ target but is substantially more intricate.
- **Repeated Kruskal with rank and path compression:** This matches the editorial's near-constant union operations but remains $O(E^2 \alpha(V))$, not $O(E \log E)$.
- **Enumerating all spanning trees:** It can classify edges by direct observation but is exponential and unnecessary.
- **Unique MST:** Every edge in that one MST is critical, while edges outside it are neither critical nor pseudo-critical.
- **All equal-weight cycle:** No one cycle edge is required, but each can appear in some MST, so those edges are pseudo-critical.
- **Edge in no MST:** Its forced run has weight greater than `v`, so it belongs to neither output list.
- **Exclusion disconnects the graph:** Component count remains above one, and the edge is critical even if the partial forest's numeric weight is small.
- **Original indices:** Sorting changes positions, so appending indices before sorting is essential for returning the requested identifiers.
- **Input mutation:** The source appends a fourth field and sorts the provided list. Reusing the original three-field order afterward would be unsafe.
- **Equal weights:** Python's stable ordering is not needed for correctness; Kruskal may choose any safe edge among equal weights.
- **No union by rank:** Path compression is present, but the data structure can temporarily build less balanced parent trees than a fully optimized implementation.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V)$. Let $V$ be the number of vertices and $E$ the number of edges. Appending indices costs $O(E)$, and sorting costs $O(E \log E)$. The baseline Kruskal run scans $E$ edges.
- **Auxiliary Space Complexity:** $O(V)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
