# Guided Example: Modify Graph Edge Weights

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "edges": [[0, 1, -1], [0, 2, 5]], "source": 0, "destination": 2, "target": 6}`
- **Required output:** `[]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an **undirected weighted** **connected** graph containing `n` nodes labeled from `0` to $n - 1$, and an integer array `edges` where $\text{edges}[i] = [a_{i}, b_{i}, w_{i}]$ indicates that there is an edge between nodes $a_{i}$ and $b_{i}$ with weight $w_{i}$.

The objective is to compute `[]` from `{"n": 3, "edges": [[0, 1, -1], [0, 2, 5]], "source": 0, "destination": 2, "target": 6}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat unknown edges as progressively enabled

Known positive edge weights cannot change. An edge marked `-1` must eventually receive a positive value.

The exact solution begins by ignoring every unknown edge and measuring the shortest path using only fixed edges. It then considers unknown edges in input order, enabling each at the minimum legal weight one until the shortest distance crosses down to the target.

The first crossing edge is increased just enough to make the distance exactly equal to `target`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "edges": [[0, 1, -1], [0, 2, 5]], "source": 0, "destination": 2, "target": 6}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: How the helper computes distance

`dijkstra` builds an $n$ by $n$ adjacency matrix initialized to sentinel `inf = 2 * 10**9`. Unknown edges are skipped, while each active edge is written symmetrically because the graph is undirected.

It stores tentative distances from `source`, repeatedly selects the unvisited vertex with smallest distance by a full scan, and relaxes every possible neighbor by scanning its matrix row.

This is the array-and-matrix form of Dijkstra for nonnegative active weights.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `dijkstra` builds an $n$ by $n$ adjacency matrix initialized... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the finite infinity sentinel is sufficient

The target is at most $10^9$, while `inf` is $2\cdot10^9$.

The algorithm only needs to distinguish a path no greater than target from one safely above target or unavailable. It never needs an exact shortest value above the sentinel for its decisions.

The same sentinel is also a legal final unknown-edge weight because the allowed maximum is inclusive.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "edges": [[0, 1, -1], [0, 2, 5]], "source": 0, "destination": 2, "target": 6}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Heap-based adjacency-list reruns:** Reduces ea:** - **Heap-based adjacency-list reruns:** Reduces each Dijkstra run but can still repeat it for many unknown edges.
- **Two carefully designed Dijkstra passes:** Can assign weights during relaxation and achieve the manifest's near-linearithmic target, but it is not the exact source.
- **Fixed-only distance below target:** Impossible because that immutable path cannot be lengthened.
- **Fixed-only distance equal target:** Set every unknown edge to `2 * 10**9`.
- **All weight-one distance above target:** Impossible because no unknown edge may be smaller than one.
- **First crossing equals target:** Slack is zero, so the crossing edge remains one.
- **Disconnected active subgraph:** The sentinel represents an unavailable route until unknown edges connect it.
- **Multiple shortest paths using the crossing edge:** All rise by the same slack and remain at least target.
- **Later unknown edges:** Must receive legal values and are neutralized with the maximum weight.
- **Known edges:** Never modified.
- **Failure mutation:** A failed late attempt may leave the supplied edge list partially rewritten.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((u+1)$. Let $u$ be the number of unknown edges and $m$ the total edge count. One helper run builds an $O(n^2)$ matrix, loads $m$ edges, and performs $O(n^2)$ selection and relaxation work, for $O(n^2+m)$ time.
- **Auxiliary Space Complexity:** $O(n + m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
