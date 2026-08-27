# Guided Example: Shortest Path in a Hidden Grid

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"master": {"mode": "unweighted", "grid": [[-1, 2]]}}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

This is an **interactive problem**.

The objective is to compute `1` from `{"master": {"mode": "unweighted", "grid": [[-1, 2]]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate discovery from shortest-path search

The robot cannot inspect the hidden grid directly. It can only ask whether a move is possible, physically move, and test its current cell for the target.

The exact solution uses two phases:

- A depth-first traversal controls the robot, assigns relative coordinates to reachable cells, and backtracks after every exploration.
- A breadth-first search runs on the discovered coordinate set to compute the true shortest number of moves from start to target.

DFS is convenient for physically exploring and restoring position. BFS is necessary afterward because the order in which DFS first reaches the target does not guarantee a shortest path.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"master": {"mode": "unweighted", "grid": [[-1, 2]]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Invent coordinates relative to the unknown start

The start is labeled coordinate `(0, 0)`. These coordinates do not need to match the hidden grid's real row and column numbers. They only need to preserve relative moves.

Direction string `s = "URDL"` pairs with:

`dirs = (-1, 0, 1, 0, -1)`.

For direction index `k`, delta is `(dirs[k], dirs[k + 1])`:

- U gives minus one, zero.
- R gives zero, one.
- D gives one, zero.
- L gives zero, minus one.

Moving the robot and applying the same delta keeps the invented coordinate consistent with physical location.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The start is labeled coordinate `(0, 0)`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Explore a legal unvisited neighbor

At coordinate `(i, j)`, DFS considers every direction character `c`. It first asks `master.canMove(c)`. It also requires that the corresponding coordinate `(x, y)` is not already in `vis`.

When both conditions hold, it:

- adds the coordinate to `vis`,
- physically calls `master.move(c)`,
- recursively explores from `(x, y)`,
- physically moves in the opposite direction to return.

The opposite direction is `s[(k + 2) % 4]`: up pairs with down, and right pairs with left. This final move restores the robot to `(i, j)`, so the next loop direction is tested from the correct physical cell.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"master": {"mode": "unweighted", "grid": [[-1, 2]]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **BFS directly through GridMaster:** A queue can:** - **BFS directly through GridMaster:** A queue cannot freely jump the physical robot between frontier cells, so interactive movement and restoration become difficult.
- **DFS distance only:** The first target discovery is not necessarily the shortest path.
- **Build an explicit adjacency map:** It is unnecessary because discovered coordinates and four-direction geometry determine adjacency.
- **Target adjacent to start:** DFS records it, and BFS returns one.
- **Target unreachable:** DFS never sets `target` and the method returns minus one.
- **Start differs from target:** The guarantee makes the initial target check false.
- **Blocked direction:** `canMove` prevents both coordinate insertion and physical movement.
- **Target early return:** Its neighbors are not explored, but no path needs to continue beyond the destination.
- **Opposite direction:** Adding two modulo four maps U to D and R to L.
- **Start not initially visited:** It may be rediscovered once; `discard` normalizes the BFS set.
- **Multiple routes to one cell:** `vis` ensures one DFS discovery, while BFS later finds the shortest route.
- **BFS mark on enqueue:** Removing from `vis` prevents duplicate frontier entries.
- **Relative coordinates:** Absolute hidden-grid dimensions and start location are never needed.
- **Recursion depth:** A long corridor is a practical Python stack risk.
- **Master position after DFS:** Balanced descent and opposite moves restore it to the start.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V)$. Let $V$ be the number of reachable open cells discovered and $E$ their grid adjacencies. A grid has at most four edges per cell, so $E=O(V)$.
- **Auxiliary Space Complexity:** $O(V)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
