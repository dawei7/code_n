# Guided Example: The Maze II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"maze": [[0, 0, 0], [0, 0, 0], [0, 0, 0]], "start": [0, 0], "destination": [2, 2]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a ball in a `maze` with empty spaces (represented as `0`) and walls (represented as `1`). The ball can go through the empty spaces by rolling **up, down, left or right**, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

The objective is to compute `4` from `{"maze": [[0, 0, 0], [0, 0, 0], [0, 0, 0]], "start": [0, 0], "destination": [2, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

This maze forms a weighted graph of stopping positions. From one stop, choosing a direction rolls through zero or more open cells until the next wall; the endpoint is another node, and the number of cells crossed is that edge's weight. The task asks for minimum traveled distance, not the fewest direction choices, so edge weights must be accumulated.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"maze": [[0, 0, 0], [0, 0, 0], [0, 0, 0]], "start": [0, 0], "destination": [2, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

`dist[i][j]` stores the shortest distance currently known from `start` to a stop at `(i, j)`. Every entry begins at infinity except the start, whose distance is zero. The queue begins with the start coordinates.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `dist[i][j]` stores the shortest distance currently known fr... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Generate the four direction vectors compactly.** `dirs = (-1, 0, 1, 0, -1)` and `pairwise(dirs)` produce

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"maze": [[0, 0, 0], [0, 0, 0], [0, 0, 0]], "start": [0, 0], "destination": [2, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Heap-based Dijkstra:** Pop the smallest curren:** - **Heap-based Dijkstra:** Pop the smallest current distance first and ignore stale heap entries. With cached or efficiently generated endpoints, this matches the manifest and gives a cleaner shortest-path bound.
- **Precompute roll endpoints and lengths:** Directional sweeps replace repeated corridor scans with constant-time edge lookup at an $O(RC)$ storage cost.
- **Plain visited BFS:** Marking a node final on first discovery is incorrect because roll edges have unequal weights.
- **Destination crossed but not stopped on:** It receives no relaxation unless it is the wall-stopped endpoint.
- **Blocked direction:** The candidate is a zero-length self-edge and cannot strictly improve its current distance.
- **Unreachable destination:** Infinity remains in its table cell and is converted to `-1`.
- **Several routes to one stop:** Only strictly shorter distances trigger re-enqueueing; equal distances need no path tie-breaking in this problem.
- **Queue duplicates:** They affect efficiency rather than correctness because popped coordinates read current table distances.
- **Start and destination distinction:** The contract says they differ; if equal, the initialized zero would naturally be returned.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(rows \cdot cols \log(rows \cdot cols))$. Let $R$ and $C$ be the grid dimensions, $V = RC$, and $L = \max(R,C)$. One expansion examines four rolls, each scanning at most $L$ cells. If every stop were expanded only once, this gives the editorial's $O(RCL)$ rolling bound.
- **Auxiliary Space Complexity:** $O(rows \cdot cols)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
