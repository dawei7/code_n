# Guided Example: Even Number of Knight Moves

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"start": [1, 1], "target": [2, 2]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two integer arrays `start` and `target`, where each array is of the form `[x, y]` representing a cell on a standard 8 x 8 chessboard.

The objective is to compute `true` from `{"start": [1, 1], "target": [2, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

**Color the board by coordinate parity.**  On a checkerboard, two cells have the same color exactly when the sums of their coordinates have the same parity. In zero-based coordinates:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"start": [1, 1], "target": [2, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

- a cell `[x, y]` belongs to one color when `(x + y) % 2 == 0`;
- it belongs to the other color when `(x + y) % 2 == 1`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The names “black” and “white” are unimportant. Only the two parity classes matter, and adding the coordinates gives a simple numerical way to identify them.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"start": [1, 1], "target": [2, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Breadth-first search with move parity:** A BFS over states `(x, y, parity)` can answer the question and is small on an `8 \times 8` board. It is unnecessary because the checkerboard invariant reduces the answer to constant-time arithmetic.
- **Ordinary shortest-path BFS:** Computing only the shortest distance would be more information than needed. The color classes already determine whether every route length is even or odd.
- **Searching for one explicit route:** A found route demonstrates one answer but requires predecessor or queue state. The endpoint parity proves the answer for all routes at once.
- **Manhattan or Euclidean distance:** These distances do not determine knight reachability parity. Knight movement is governed by the `(2,1)` displacement and its resulting color flip.
- **Start equals target:** Zero moves are allowed by “can move ... in an even number of moves.” Since zero is even, the method correctly returns `true`.
- **One legal knight move apart:** A single move always changes color, so the method returns `false` for even-move reachability. Any route between those opposite colors must have odd length.
- **Same color but not directly reachable:** Direct reachability is irrelevant. Connectivity supplies some route, and matching endpoint colors force that route's length to be even.
- **Different colors with a long detour:** Adding detours cannot change the required parity between the two color classes. Every additional closed detour in this bipartite graph has even length.
- **Board boundaries:** The sufficiency argument uses the connected standard `8 \times 8` knight graph. On a smaller or obstructed board, matching colors might not be sufficient because the graph could be disconnected.
- **Coordinate convention:** Whether `x` is viewed as a row or a column does not matter. A knight changes one coordinate by `2` and the other by `1` in either convention.
- **Maximum coordinate values:** Coordinates `0` and `7` behave exactly like interior coordinates for the parity test. Boundaries affect which particular moves are legal, but not the color-flip rule.
- **Boolean result:** The equality comparison already produces Python's `true` or `false` value, so no conditional statement or conversion is needed.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The source reads four coordinates, performs two additions, two remainder operations, and one equality comparison. The amount of work does not depend on the positions or on the number of possible routes.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
