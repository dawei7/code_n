# Guided Example: Path with Maximum Probability

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "edges": [[0, 1]], "succProb": [0.5], "start_node": 0, "end_node": 2}`
- **Required output:** `0.0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an undirected weighted graph of `n` nodes (0-indexed), represented by an edge list where $\text{edges}[i] = [a, b]$ is an undirected edge connecting the nodes `a` and `b` with a probability of success of traversing that edge $\text{succProb}[i]$.

The objective is to compute `0.0` from `{"n": 3, "edges": [[0, 1]], "succProb": [0.5], "start_node": 0, "end_node": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A maximum-product version of Dijkstra

The success probability of a path is the product of its edge probabilities. The stored solution adapts Dijkstra's algorithm: instead of minimizing an additive distance, it maximizes a multiplicative probability.

`dist[v]` stores the best probability discovered so far for reaching node `v` from `start_node`. The starting probability is one because an empty path succeeds with certainty. Every other node begins at zero, meaning no route has been discovered.

For an edge from `a` to `b` with probability `p`, a path reaching `a` with probability `w` reaches `b` with probability `w * p`. If that product exceeds `dist[b]`, the code records the improvement and schedules `b` for processing.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "edges": [[0, 1]], "succProb": [0.5], "start_node": 0, "end_node": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Building an undirected adjacency list

The source creates one empty neighbor list per node. For each paired edge and probability, it appends `(b, p)` to `g[a]` and `(a, p)` to `g[b]`. Both directions are required because the graph is undirected.

`zip(edges, succProb)` relies on the guaranteed equal lengths and associates each edge with its matching probability.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Using a min-heap as a max-heap

Python's heap returns the smallest key. The queue stores negative probabilities, beginning with `(-1, start_node)`. The most negative value corresponds to the largest positive probability, so it is popped first.

After `w, a = heappop(pq)`, the source executes `w = -w` to recover the positive probability.

An improved node can have older, worse heap entries still waiting. The test `if dist[a] > w: continue` recognizes such a stale entry. A strictly better probability is already known, so expanding the worse route cannot improve any neighbor beyond what expanding the better route can provide.

Equality is not stale. Processing an equal entry is harmless, although under normal strict-improvement pushes duplicate equal entries are limited.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0.0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "edges": [[0, 1]], "succProb": [0.5], "start_node": 0, "end_node": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0.0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Negative logarithms:** Transform probability p to cost `-log(p)` and run ordinary shortest-path Dijkstra. Zero-probability edges need special handling.
- **Bellman-Ford relaxation:** Repeatedly scan all edges for $O(NE)$ time. It is simpler conceptually but slower.
- **Queue-based relaxation:** It may work well on some graphs but has $O(NE)$ worst-case time.
- **Unreachable destination:** Its stored probability stays zero.
- **Direct edge versus longer path:** The heap compares products, not hop counts, so a longer route can win.
- **Probability one cycle:** It cannot create a strictly larger label, so strict comparisons prevent infinite pushes.
- **Probability zero edge:** It produces zero and cannot improve an undiscovered zero label.
- **Stale heap entry:** The source skips it when a better array value exists.
- **Undirected edge:** Both adjacency directions must be inserted.
- **Required imports:** `heappop` and `heappush` must be available from `heapq`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((n+e)\log n)$. Let $N$ be the number of nodes and $E$ the number of undirected edges. Building adjacency lists costs $O(N+E)$ time and space.
- **Auxiliary Space Complexity:** $O(N+E)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
