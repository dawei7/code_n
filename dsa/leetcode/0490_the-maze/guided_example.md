# Guided Example: The Maze

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"maze": [[0, 0, 0], [0, 0, 0], [0, 0, 0]], "start": [0, 0], "destination": [1, 1]}`
- **Required output:** `false`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a ball in a `maze` with empty spaces (represented as `0`) and walls (represented as `1`). The ball can go through the empty spaces by rolling **up, down, left or right**, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

The objective is to compute `false` from `{"maze": [[0, 0, 0], [0, 0, 0], [0, 0, 0]], "start": [0, 0], "destination": [1, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

This maze is not an ordinary “move one cell at a time” reachability problem. After choosing a direction, the ball passes through every open cell in that direction and stops only immediately before a wall or boundary. It cannot turn at an intermediate cell, even if that cell is the destination. Therefore the graph nodes that matter are stopping positions, and a graph edge represents one complete roll.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"maze": [[0, 0, 0], [0, 0, 0], [0, 0, 0]], "start": [0, 0], "destination": [1, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The solution discovers that graph implicitly with depth-first search. `dfs(i, j)` means that the ball can stop at cell `(i, j)` and that the algorithm is now exploring every complete roll available from that stop.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The solution discovers that graph implicitly with depth-firs... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Visited means reachable as a stopping point.** At the beginning of `dfs`, `vis[i][j]` is checked. If it is already true, this stopping position has already had all four outgoing rolls explored, so repeating the work cannot discover anything new. Otherwise the cell is marked visited.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `false` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"maze": [[0, 0, 0], [0, 0, 0], [0, 0, 0]], "start": [0, 0], "destination": [1, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `false` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Precompute stopping endpoints:** Sweep rows an:** - **Precompute stopping endpoints:** Sweep rows and columns to record where a roll from every open cell ends in each direction. This uses $O(RC)$ extra data and makes the graph traversal itself $O(RC)$, matching the manifest summary.
- **Breadth-first search:** A queue explores the same stopping-position graph and gives the same Boolean reachability result. Shortest roll count is not requested, so BFS offers no correctness advantage over DFS.
- **Ordinary cell-by-cell DFS:** Marking every crossed cell as a decision node is wrong because the ball cannot turn there. Only wall-stopped endpoints are graph nodes.
- **Destination crossed but not stopped on:** The code correctly leaves it unvisited unless a roll ends there.
- **Direction blocked immediately:** The roll endpoint equals the current stop; the visited guard turns the resulting recursive call into constant work.
- **Cycles among stops:** The ball can roll between the same endpoints repeatedly. `vis` ensures every stop's outgoing directions are expanded once.
- **Start and destination distinction:** The contract says they differ, but the code would still return true if they were equal because the initial DFS marks the start.
- **Recursion depth:** A maze with many sequential stopping positions can create a deep Python call stack. An explicit stack preserves the same search if runtime recursion limits matter.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(RC)$. Let $R$ be the row count and $C$ the column count. The visited matrix costs $O(RC)$ initialization and storage. At most $RC$ cells can become DFS states, and each state explores four directions.
- **Auxiliary Space Complexity:** $O(RC)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
