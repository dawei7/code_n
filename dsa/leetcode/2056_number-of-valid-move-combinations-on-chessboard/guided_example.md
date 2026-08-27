# Guided Example: Number of Valid Move Combinations On Chessboard

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"pieces": ["rook"], "positions": [[1, 1]]}`
- **Required output:** `15`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is an `8 x 8` chessboard containing `n` pieces (rooks, queens, or bishops). You are given a string array `pieces` of length `n`, where $\text{pieces}[i]$ describes the type (rook, queen, or bishop) of the $$i^{\text{th}}$$ piece. In addition, you are given a 2D integer array `positions` also of length `n`, where $\text{positions}[i] = [r_{i}, c_{i}]$ indicates that the $$i^{\text{th}}$$ piece is currently at the **1-based** coordinate $(r_{i}, c_{i})$ on the chessboard.

The objective is to compute `15` from `{"pieces": ["rook"], "positions": [[1, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Enumerate one destination for every piece

A move is completely determined by two choices: a legal direction for that piece and a distance along that direction. Choosing distance zero means the piece stays on its starting square.

The source assigns moves recursively. `dfs(i)` chooses the destination of piece `i` after pieces zero through `i-1` already have fixed moves. When `i == n`, every piece has a compatible move, so one valid combination is counted.

This exhaustive search is practical because the board is fixed at eight by eight and there are at most four pieces.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"pieces": ["rook"], "positions": [[1, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Generate only movement allowed by the piece type

The four rook directions are horizontal and vertical. The four bishop directions are diagonal. A queen receives their concatenation, named `queue_dirs` in the source even though it functions as the queen-direction list.

`get_dirs` examines the first letter of the piece name: `r` selects rook directions, `b` selects bishop directions, and the remaining possible type is queen.

For each direction, the source advances one square at a time until it leaves coordinates one through eight or encounters an unavoidable collision. Every square reached before then is considered as a possible destination.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The four rook directions are horizontal and vertical.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Record a complete time-indexed route

`dist[i][x][y]` records the integer second at which piece `i` visits square `(x,y)` while traveling to its currently selected destination. A value of negative one means that square is not on the route.

The starting square is marked with time zero. Each following square in the chosen direction receives time one, two, and so on. `end[i]` stores the destination coordinates and arrival time.

The route table and endpoint together distinguish two phases:

- before arrival, the piece visits one route square at each integer second;
- from its endpoint time onward, it remains on the endpoint forever.

Both phases matter when checking another piece.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `15` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"pieces": ["rook"], "positions": [[1, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `15` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate all destinations, then simulate:** S:** - **Enumerate all destinations, then simulate:** Simpler conceptually, but it delays collision pruning until complete combinations are built.
- **Pairwise trajectory formulas:** Compare two selected moves algebraically without route grids; less storage but easier to get stopping times wrong.
- **Stationary piece:** Occupies its starting square forever, so no other route may visit it at any time.
- **Two moving pieces meet:** Equal square and equal time is rejected.
- **Earlier piece already stopped:** `check_pass` rejects entering its endpoint at or after its arrival.
- **Earlier piece arrives later:** `check_stop` rejects choosing a destination that will be occupied in the future.
- **Earlier piece passed before stopping time:** Safe when its route time is strictly smaller and it did not end there.
- **Adjacent swap:** Allowed because pieces never share a square at an integer second.
- **Board boundary:** Direction extension stops before row or column zero or nine.
- **Queen direction variable:** `queue_dirs` is only a naming typo; it contains all eight queen directions.
- **At most one queen:** Further limits the already fixed search space.
- **Distinct starts:** Prevents a collision at time zero before moves begin.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Let $C_i$ be the number of legal destination choices generated for piece `i` before collision pruning. A queen has at most 28 destinations including staying, and rooks or bishops have fewer on an eight-by-eight board. The search examines at most the product of these choice counts, with pairwise collision work bounded by four pieces and eight travel steps.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
