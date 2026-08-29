# Guided Example: Minimum Path Cost in a Hidden Grid

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"master": {"mode": "weighted", "grid": [[99, 7]], "start": [0, 0], "target": [0, 1]}}`
- **Required output:** `7`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

This is an **interactive problem**.

The objective is to compute `7` from `{"master": {"mode": "weighted", "grid": [[99, 7]], "start": [0, 0], "target": [0, 1]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate discovery from shortest-path optimization

The robot knows the grid only through `GridMaster` and physically changes position when `move` is called. A shortest-path algorithm cannot run until reachable cells and their entry costs are known.

The protected solution therefore has two phases:

1. depth-first exploration controls the robot, maps every reachable cell into local coordinates, and records the target;
2. Dijkstra's algorithm runs on that discovered weighted map without further interactive movement.

This separation prevents shortest-path bookkeeping from becoming entangled with the robot's physical location.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"master": {"mode": "weighted", "grid": [[99, 7]], "start": [0, 0], "target": [0, 1]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Create a safe local coordinate system

The real grid has at most 100 rows and 100 columns, but its dimensions and start coordinates are hidden. The solution allocates a 200 by 200 array `g` and places the unknown start at synthetic coordinate `(100,100)`.

Any real reachable cell differs from the start by at most 99 rows and 99 columns, so its translated coordinate fits in the allocated range.

Value -1 means not yet discovered. A discovered cell stores the cost returned when the robot moves into it.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Explore with reversible DFS movement

Directions `"URDL"` correspond to coordinate steps from `dirs = (-1,0,1,0,-1)`. For direction index $k$, `dirs[k]` and `dirs[k+1]` form its row and column change.

At DFS coordinate `(x,y)`, `master.isTarget()` records that coordinate when true. Then each direction is considered.

A neighbor is explored only when it stays inside the synthetic array, still has `g[nx][ny] == -1`, and `master.canMove(direction)` reports that movement is legal. The forward `move` returns the destination's entry cost, which is stored before recursion.

After the recursive call finishes, the robot must return to the caller's physical cell. Direction index `(k + 2) % 4` is the opposite direction, so a second `move` backtracks. The return cost is irrelevant to mapping because the earlier cell is already known.

This restoration is the DFS invariant: whenever `dfs(x,y)` begins and ends, the robot is physically at the cell represented by `(x,y)`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `7` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"master": {"mode": "weighted", "grid": [[99, 7]], "start": [0, 0], "target": [0, 1]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `7` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Dijkstra while physically exploring:** It is difficult to preserve heap order while the robot occupies only one cell; mapping first cleanly separates concerns.
- **Breadth-first search after mapping:** It minimizes moves, not total cost, and is wrong when cell costs differ.
- **Iterative DFS:** An explicit stack can preserve backtracking actions while avoiding recursion-depth failure.
- **Mark the start immediately:** Using a separate visited structure or a special start marker avoids the exact source's one redundant start rediscovery.
- **Stale-entry guard:** Skipping when `w != dist[x][y]` avoids unnecessary Dijkstra neighbor scans.
- **Target unreachable:** DFS never records it and the method returns -1.
- **Start cost:** It is not charged because the initial heap distance is zero.
- **Re-entering the start later:** Its recorded cell cost is correctly charged when a path moves back into it.
- **Blocked or off-grid neighbor:** `canMove` prevents movement and the cell remains undiscovered.
- **Target different from start:** The contract removes the zero-move target case.
- **Backtracking direction:** Adding two modulo four maps U to D and R to L.
- **Fixed coordinate padding:** Centering at 100 safely represents every relative location in a grid of dimension at most 100.
- **Positive costs:** They justify Dijkstra and early return on the first target pop.
- **Physical-state invariant:** Every recursive call must backtrack before returning, or later coordinates would no longer match the robot.
- **API ownership:** `GridMaster` is provided by the platform and is not implemented by the solution.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V\log V)$. Let $V$ be the number of reachable cells and $E$ their adjacencies. Grid degree is at most four, so $E=O(V)$.
- **Auxiliary Space Complexity:** $O(V)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
