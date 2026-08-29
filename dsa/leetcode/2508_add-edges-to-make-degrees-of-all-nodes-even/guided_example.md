# Guided Example: Add Edges to Make Degrees of All Nodes Even

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 5, "edges": [[1, 2], [2, 3], [3, 4], [4, 2], [1, 4], [2, 5]]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is an **undirected** graph consisting of `n` nodes numbered from `1` to `n`. You are given the integer `n` and a **2D** array `edges` where $\text{edges}[i] = [a_{i}, b_{i}]$ indicates that there is an edge between nodes $a_{i}$ and $b_{i}$. The graph can be disconnected.

The objective is to compute `true` from `{"n": 5, "edges": [[1, 2], [2, 3], [3, 4], [4, 2], [1, 4], [2, 5]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Adding one edge toggles exactly two degree parities

An undirected edge increases the degree of each endpoint by one. Therefore:

- an even endpoint becomes odd;
- an odd endpoint becomes even.

No other node changes parity.

The task is governed by the set of odd-degree nodes. Their exact degree values do not matter, except that existing adjacency determines which new edges are legal.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 5, "edges": [[1, 2], [2, 3], [3, 4], [4, 2], [1, 4], [2, 5]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build adjacency sets and collect odd nodes

For each edge `[a,b]`, the code inserts `b` into `g[a]` and `a` into `g[b]`. Sets serve two purposes:

- `len(g[v])` gives the degree;
- membership such as `a in g[b]` tells whether an edge already exists.

`vs` contains nodes whose adjacency-set length is odd.

Nodes absent from `g` have degree zero, which is already even, so omitting them from `vs` is correct. They remain available as possible intermediate nodes because `defaultdict(set)` supplies an empty adjacency set when accessed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Only zero, two, or four odd nodes can be repaired

The handshaking lemma guarantees an even number of odd-degree vertices in every undirected graph. One added edge can toggle at most two odd nodes, and two edges can toggle at most four.

Consequently:

- zero odd nodes need no edges;
- two odd nodes may be fixable with one or two edges;
- four odd nodes require two edges;
- more than four cannot be fixed within the limit.

The code handles precisely these cases and returns false for every other count.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 5, "edges": [[1, 2], [2, 3], [3, 4], [4, 2], [1, 4], [2, 5]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Degree array plus edge hash set:** Store degrees separately and encode edges in one global set; it gives the same asymptotic bounds.
- **Already all even:** Return true without adding anything.
- **Two nonadjacent odd nodes:** One direct edge is sufficient.
- **Two adjacent odd nodes:** A third node must be nonadjacent to both endpoints for the two-edge path.
- **Isolated intermediate:** It has even degree zero, receives two edges, and remains even.
- **Four odd nodes:** Test all three perfect matchings; there are no others.
- **More than four odd nodes:** Two edges cannot toggle enough endpoints.
- **Repeated edge restriction:** Every proposed pair must be absent from the adjacency sets.
- **Self-loops:** They are never proposed by a successful tested arrangement.
- **Disconnected input:** Component boundaries do not limit which legal new edges may be added.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+m)$. Let $m$ be the number of existing edges. Building two adjacency entries per edge takes expected $O(m)$ time. Collecting odd nodes is $O(n)$ worst case.
- **Auxiliary Space Complexity:** $O(n+m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
