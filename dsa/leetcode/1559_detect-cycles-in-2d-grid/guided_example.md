# Guided Example: Detect Cycles in 2D Grid

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]]}`
- **Required output:** `false`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a 2D array of characters `grid` of size `m x n`, you need to find if there exists any cycle consisting of the **same value** in `grid`.

The objective is to compute `false` from `{"grid": [["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Interpret equal-character neighbors as an undirected graph

Treat each grid cell as a graph vertex. Two vertices share an undirected edge when their cells are vertically or horizontally adjacent and contain the same character.

The question then becomes ordinary cycle detection in an undirected graph. A valid grid cycle uses at least four cells because an orthogonal grid graph is bipartite and has no triangle; immediately returning along the same edge is explicitly forbidden.

The source explores every equal-character connected component with a depth-first traversal implemented by a Python list.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Track both the cell and its parent

Each stack entry is `(x, y, px, py)`:

- `x, y` are the current row and column.
- `px, py` are the cell from which the traversal entered it.

When inspecting neighbors, the algorithm skips `(px, py)`. In an undirected graph, every edge appears in both directions. Without this parent exception, the current cell would see the vertex it just came from as already visited and incorrectly report a two-step return as a cycle.

Any different already-visited same-character neighbor represents an alternate connection within the explored component and therefore closes a genuine cycle.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Start one traversal per unvisited component

The outer loops visit every grid coordinate. If `vis[i][j]` is already true, that cell belongs to a component explored earlier and is skipped.

For a new root, the source marks it visited and pushes `(i, j, -1, -1)`. Negative parent coordinates cannot match any valid cell, so the root has no excluded neighbor.

The list is named `q`, but `q.pop()` removes from its end. It therefore behaves as a LIFO stack and produces depth-first traversal rather than queue-based breadth-first traversal. Either traversal order supports the same undirected-cycle rule.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `false` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `false` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Recursive DFS:** It uses the same parent rule but risks Python recursion overflow on a large component.
- **Breadth-first search:** A deque with parent coordinates is equally correct; traversal order does not affect detection.
- **Union-find:** Process each equal-character edge once and report a cycle when endpoints are already connected. It uses $O(RC)$ storage.
- **Skip no parent edge:** That would falsely call every ordinary undirected edge a cycle.
- **Single cell:** It has no edge and returns false.
- **One row or one column:** The graph is a path or disjoint paths, so no valid cycle exists.
- **Different neighboring characters:** No graph edge connects them.
- **Large uniform rectangle:** The traversal quickly encounters a non-parent visited neighbor and returns true.
- **Diagonal equality:** Diagonal cells are not adjacent and create no edge.
- **Multiple components:** The outer loops start a fresh traversal for each unvisited one.
- **Mark on push:** It prevents duplicate scheduling and makes frontier cross-edges visible as cycles.
- **Minimum cycle length:** Orthogonal grid structure rules out a same-character triangle, while parent skipping rules out immediate two-edge backtracking.
- **Iterator dependency:** `pairwise(dirs)` must be supplied by the execution environment exactly as the stored source expects.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(RC)$. Let $R$ and $C$ be grid dimensions. Every cell is marked at most once and, when popped, examines exactly four directions. Total time is $O(RC)$, matching the manifest.
- **Auxiliary Space Complexity:** $O(RC)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
