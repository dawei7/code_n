# Guided Example: Shortest Path to Get Food

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [["*", "#"]]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.

The objective is to compute `1` from `{"grid": [["*", "#"]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use breadth-first search because every move costs one

Each legal move goes to one orthogonally adjacent cell and contributes one step. This is an unweighted graph shortest-path problem: cells are vertices and legal adjacencies are edges of equal cost.

Breadth-first search explores all cells at distance one before distance two, all distance two before distance three, and so on. Therefore the first food cell it discovers is guaranteed to have minimum path length among every reachable food cell.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [["*", "#"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Find the unique starting position

The source uses

`next((i, j) for i in range(m) for j in range(n) if grid[i][j] == '*')`.

The generator scans rows and columns until it finds `'*'`. The contract guarantees exactly one, so `next` always succeeds and returns its coordinates.

This initial scan costs at most one full grid traversal.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Represent the BFS frontier with a queue

`q = deque([(i, j)])` begins with the start cell. The queue contains positions discovered but not yet expanded.

`dirs = (-1, 0, 1, 0, -1)` works with `pairwise` to produce the four direction pairs:

`(-1,0)`, `(0,1)`, `(1,0)`, and `(0,-1)`.

These are up, right, down, and left. No diagonal movement is generated.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [["*", "#"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Depth-first search:** It can test reachability but does not discover shortest paths in distance order without extra distance tracking and repeated relaxation.
- **A* search:** A Manhattan-distance heuristic can prioritize promising cells, but multiple foods and heuristic computation add complexity; BFS already gives linear worst-case time.
- **Separate visited set:** It preserves the input at the cost of another $O(mn)$ structure.
- **Food adjacent to start:** The first layer returns one.
- **Multiple foods:** The first one found by BFS has globally minimum distance.
- **No reachable food:** The queue empties and returns `-1`.
- **Narrow one-cell corridor:** BFS follows it without special handling.
- **Original obstacle:** It is never enqueued.
- **Visited open cell:** Rewriting it to `'X'` prevents duplicate queue entries.
- **Start revisitation:** The `'*'` marker is not accepted by the open-cell branch.
- **Grid mutation:** Callers must not expect original open-cell markers after execution.
- **Layer size capture:** Using the queue length before the loop is essential to keep newly added cells in the next distance layer.
- **Direction encoding:** `pairwise(dirs)` produces exactly four orthogonal moves.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. Let $m$ and $n$ be the grid dimensions. Finding the start costs $O(mn)$ in the worst case. Each open cell is enqueued at most once, and expansion checks four neighbors, so BFS also costs $O(mn)$. Total time is $O(mn)$.
- **Auxiliary Space Complexity:** $O(mn)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
