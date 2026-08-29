# Guided Example: Available Captures for Rook

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"board": [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `8 x 8` **matrix** representing a chessboard. There is **exactly one** white rook represented by `'R'`, some number of white bishops `'B'`, and some number of black pawns `'p'`. Empty squares are represented by `'.'`.

The objective is to compute `3` from `{"board": [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A rook has four independent lines of sight

The rook attacks horizontally and vertically, so only four rays matter: up, right, down, and left from the rook's square. Along each ray, empty squares can be crossed, but the first encountered piece blocks every square beyond it.

Therefore, each direction contributes at most one capturable pawn:

- if the first piece is a black pawn, the rook attacks it;
- if the first piece is a white bishop, that direction contributes nothing;
- if the board edge is reached first, that direction also contributes nothing.

There is no need to simulate actual moves or examine diagonal squares.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"board": [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Locate the unique rook

The nested loops scan the square board until `board[i][j] == "R"`. The statement guarantees exactly one rook, so once it is found, all four directional scans can be performed and the answer can be returned immediately.

The code stores `n = len(board)` and uses it for both row and column bounds. This is valid because the board is guaranteed to be `8 x 8`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Generate the four directions compactly

The tuple

`dirs = (-1, 0, 1, 0, -1)`

combined with `pairwise(dirs)` produces:

- `(-1, 0)` for up;
- `(0, 1)` for right;
- `(1, 0)` for down;
- `(0, -1)` for left.

For direction `(a, b)`, the first examined square is `(i + a, j + b)`. Repeatedly adding the same offset walks along one straight rank or file exactly as a rook moves.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"board": [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Scan complete rook row and column:** One can inspect all aligned squares and track blockers, but stopping at the first piece in each direction is simpler and avoids irrelevant cells.
- **Simulate rook moves:** Generate every reachable empty square and capture. This reaches the same result but adds state the direct ray scan does not need.
- **Precompute piece coordinates:** Building sets or maps is unnecessary for a fixed 64-cell board and uses extra memory.
- **Bishop immediately adjacent:** The ray loop stops before entering it, contributing zero.
- **Pawn immediately adjacent:** It is counted immediately, and that ray stops.
- **Several pawns in one direction:** Only the nearest pawn is attacked because it blocks every farther pawn.
- **Pawn behind a bishop:** It is not counted because the bishop terminates the ray first.
- **No piece before the edge:** The boundary condition ends the scan with no capture.
- **Rook on an edge or corner:** Some first neighbor coordinates are out of bounds, so those directions perform no iterations.
- **No capturable pawns:** All rays end at bishops or edges, and the initialized answer zero is returned.
- **Maximum result:** At most one pawn can be attacked in each of four directions, so the answer cannot exceed four.
- **Input preservation:** The board is read-only; the method changes only local coordinates and the counter.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The board dimensions are fixed at eight by eight. Scanning for the rook examines at most 64 cells, and the four rays examine at most seven squares each. These are fixed constants, so time complexity is `O(1)` and auxiliary space is `O(1)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
