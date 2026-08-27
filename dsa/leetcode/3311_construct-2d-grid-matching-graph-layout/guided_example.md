# Guided Example: Construct 2D Grid Matching Graph Layout

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4, "edges": [[0, 1], [0, 2], [1, 3], [2, 3]]}`
- **Required output:** `[[3, 1], [2, 0]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a 2D integer array `edges` representing an **undirected** graph having `n` nodes, where $\text{edges}[i] = [u_{i}, v_{i}]$ denotes an edge between nodes $u_{i}$ and $v_{i}$.

The objective is to compute `[[3, 1], [2, 0]]` from `{"n": 4, "edges": [[0, 1], [0, 2], [1, 3], [2, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Grid geometry is encoded by node degrees.** In a rectangular grid graph, a corner has degree two when both dimensions exceed one, a non-corner boundary cell has degree three, and an interior cell has degree four. In a one-cell-wide grid, the graph is a path whose endpoints have degree one. These recognizable degrees let the source discover one boundary row without knowing coordinates.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4, "edges": [[0, 1], [0, 2], [1, 3], [2, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The adjacency list `g` stores the undirected graph. Array `deg` has five slots and records one example node for each observed degree. It does not count nodes; assignment `deg[len(ys)] = x` overwrites earlier examples. One representative is enough for the case analysis.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The adjacency list `g` stores the undirected graph.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Case one: the grid is a path.** If a degree-one node exists, one grid dimension is one. The source makes that endpoint the initial `row` of length one. Later row extension follows the path one node at a time, producing an $n\times1$ layout. Rotating it to $1\times n$ would also be valid.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[3, 1], [2, 0]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4, "edges": [[0, 1], [0, 2], [1, 3], [2, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[3, 1], [2, 0]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Coordinate propagation:** Assign a corner coor:** - **Coordinate propagation:** Assign a corner coordinate and infer neighbor directions through common-neighbor relationships. It is more general-looking but needs conflict handling and more bookkeeping.
- **Try all corner-side orientations:** One could build candidate layouts from both neighbors of a corner and validate edges. The guaranteed grid structure makes the source's arbitrary valid side sufficient.
- **One-row path:** Degree-one detection chooses an endpoint and the extension produces a single-column rotation of the same path.
- **Two-by-two grid:** No degree-four node exists; a corner and any degree-two neighbor form an initial side of length two.
- **Two-by-many grid:** Adjacent degree-two corners identify the short side. Degree-three nodes then fill successive rows.
- **Both dimensions at least three:** Degree-four presence selects boundary walking from one degree-two corner to another.
- **Square grid:** Either corner direction has the same length, and rotations or reflections are all accepted.
- **Rectangular non-square grid:** The source may choose either side, not necessarily the shortest. The number of generated rows adjusts through `n // len(row)`.
- **Adjacency-list order:** It affects rotation/reflection and which side is chosen, but any resulting valid layout is allowed.
- **Why mark the whole row first:** If nodes were marked one at a time while choosing neighbors, a horizontal neighbor later in the current row might still look unvisited and be mistaken for the next layer.
- **Degree representative overwrite:** `deg[d]` keeps only the last node of degree $d$; existence and one starting example are all the case split needs.
- **Malformed non-grid input:** Missing outward neighbors or unexpected degrees could leave variables unset or rows incomplete. The guarantee excludes such cases.
- **Manifest discrepancy:** No shortest-path or shortest-side computation occurs; the code follows an arbitrary boundary side determined by adjacency order.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+m)$. Let $n$ be the number of nodes and $m$ the number of edges. Building adjacency takes $O(n+m)$ time and space. Boundary discovery follows at most one side, $O(n)$. During row extension, every node becomes part of one row, and each scan inspects at most its grid degree of four; equivalently total adjacency work is $O(n+m)$. Overall time is $O(n+m)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
