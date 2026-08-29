# Guided Example: Walls and Gates

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"rooms": [[-1]]}`
- **Required output:** `[[-1]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` grid `rooms` initialized with these three possible values.

The objective is to compute `[[-1]]` from `{"rooms": [[-1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reverse the direction of the search

A direct interpretation would start from each empty room and search outward until finding a gate. That repeats much of the same grid exploration for many rooms. The optimal insight is to reverse the perspective: start from every gate simultaneously and let distance waves spread into empty rooms.

This is multi-source breadth-first search. Ordinary BFS from one source reaches positions in nondecreasing distance from that source. Placing all gates in the initial queue is equivalent to adding an imaginary super-source connected to every gate by a zero-cost setup: the first wave reaches rooms one step from any gate, the second reaches rooms two steps from their nearest gate, and so on.

Because the waves compete in one shared queue, a room is claimed by whichever gate can reach it at the smallest distance. No separate comparison among gates is needed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"rooms": [[-1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Interpret the three grid values as both data and state

The grid begins with:

- `0` for a gate;
- `-1` for a wall; and
- `2**31 - 1` for an unfilled empty room.

The source stores the infinity sentinel in `inf`. During BFS, an `inf` cell means both “this is traversable empty space” and “this room has not yet been visited.” As soon as the algorithm assigns a finite distance, the cell becomes its own visited marker.

This reuse avoids a separate `visited` matrix. Gates and walls are never confused with unvisited rooms because neither equals `inf`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Seed the queue with every gate

The queue comprehension scans all `m * n` cells and inserts the coordinates of every cell whose value is zero. All gates therefore occupy BFS layer zero before expansion begins.

Starting from all gates at once is essential. If gates were processed with separate BFS runs that overwrote rooms, later searches would need comparisons and could revisit the entire grid. In the shared queue, the standard BFS ordering resolves the minimum distance automatically.

If there are no gates, the queue is empty. The BFS loop never runs, and every empty room correctly remains `INF` because no gate is reachable anywhere.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[-1]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"rooms": [[-1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[-1]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **BFS from every empty room:** It can find a nearest gate but repeats exploration and costs up to $O(m^2n^2)$ time.
- **Separate BFS from every gate:** Distances must be minimized across runs, and cells may be revisited many times. Multi-source BFS combines all gates into one shortest-path computation.
- **DFS from gates:** DFS does not process paths by increasing length. It needs repeated relaxation or careful pruning to correct distances, while BFS provides shortest unweighted paths directly.
- **No gates:** The initial queue is empty and all empty rooms remain `INF`.
- **No empty rooms:** Gates and walls seed or skip normally, but no neighbor ever passes the `inf` test, so the grid is unchanged.
- **Room enclosed by walls:** It is never enqueued and correctly remains `INF`.
- **Multiple equally near gates:** The first discovery assigns the shared minimum distance. The identity of the winning gate is irrelevant.
- **Adjacent gate:** An empty room sharing an edge with any gate is assigned 1 in the first layer.
- **Walls:** Their `-1` value fails the infinity test, so search never crosses or modifies them.
- **Gates:** Their zero value also fails the infinity test after initialization, preventing one gate's wave from overwriting another gate.
- **One-cell wall grid:** No gate is enqueued and no mutation occurs, matching the second example.
- **One-cell gate grid:** The gate is processed, has no in-bounds neighbors, and stays zero.
- **Rectangular rather than square grids:** Separate `m` and `n` bounds handle all legal dimensions.
- **In-place contract:** Finite distances double as visited markers. Replacing them later with larger values would break the one-visit proof; the BFS first-arrival guarantee makes replacement unnecessary.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. Let the grid have $m$ rows and $n$ columns. The initial comprehension scans all $mn$ cells. Each gate is enqueued once initially, and each reachable empty room is enqueued once when its value changes from `INF` to a finite distance. Walls and already visited cells are never enqueued.
- **Auxiliary Space Complexity:** $O(mn)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
