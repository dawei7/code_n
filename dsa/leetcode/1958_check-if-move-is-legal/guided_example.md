# Guided Example: Check if Move is Legal

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"board": [[".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."], ["W", "B", "B", ".", "W", "W", "W", "B"], [".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."]], "rMove": 4, "cMove": 3, "color": "B"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** `8 x 8` grid `board`, where $\text{board}[r][c]$ represents the cell `(r, c)` on a game board. On the board, free cells are represented by `'.'`, white cells are represented by `'W'`, and black cells are represented by `'B'`.

The objective is to compute `true` from `{"board": [[".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."], ["W", "B", "B", ".", "W", "W", "W", "B"], [".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."]], "rMove": 4, "cMove": 3, "color": "B"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A legal line must leave the move in one of eight directions

The newly placed piece is one endpoint of a horizontal, vertical, or diagonal line. From its cell, the other endpoint must lie in one of eight direction vectors $(a,b)$ where each component is $-1$, $0$, or $1$, excluding $(0,0)$.

The nested loops enumerate exactly those eight directions. The board is not mutated; the algorithm treats `(rMove, cMove)` conceptually as the first endpoint of `color` and scans outward.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"board": [[".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."], ["W", "B", "B", ".", "W", "W", "W", "B"], [".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."]], "rMove": 4, "cMove": 3, "color": "B"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Require opposite-colored middle cells

For one direction, `i, j` start at the move cell and `cnt` starts at zero. Each while iteration first increments the distance and steps to the next board cell.

At distance one, finding another `color` piece must not succeed. A good line needs at least three cells, so there must be at least one middle cell. The check requires `cnt > 1` before accepting a same-colored endpoint.

If the visited cell is the same color too early, the second condition breaks. If it is free `"."`, the scan also breaks because a good line cannot contain gaps. The only way the scan continues is when the cell contains the opposite color.

After one or more opposite pieces, encountering `color` at distance two or greater returns true. This describes exactly:

new piece, one or more opponent pieces, same-colored closing piece.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why condition order matters

The success test appears before `if board[i][j] in (color, "."): break`. At a valid far endpoint, the method must return true rather than treating the same color only as a stopping condition.

At the immediate neighbor, `cnt > 1` is false, so the same-color neighbor falls through to the break. That direction cannot skip over it to find a farther endpoint because middle cells must all be the opposite color.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"board": [[".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."], ["W", "B", "B", ".", "W", "W", "W", "B"], [".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."]], "rMove": 4, "cMove": 3, "color": "B"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Temporarily write the move:** One may set the board cell to `color` and scan lines, then restore it. The exact method avoids mutation because the start color is already known.
- **Generate whole lines:** Extract row, column, and diagonals as strings and search patterns. This allocates unnecessary sequences and complicates endpoint direction.
- **Immediate same-color neighbor:** It cannot close a three-cell line, so that direction fails.
- **Exactly one opponent between endpoints:** Distance two satisfies `cnt > 1` and is the shortest legal line.
- **Several opponents:** The scan continues through all of them until a same-colored endpoint.
- **Free cell in the middle:** It breaks the line and stops that direction.
- **Opponent sequence reaches the edge:** Without a closing same-colored endpoint, that direction is invalid.
- **Board edge:** Leaving bounds simply ends that directional scan.
- **Move at a corner:** Only three directions enter the board, while the other scans terminate immediately.
- **Good line with move in the middle:** It does not qualify; scanning from the move requires the move to be an endpoint.
- **Multiple good directions:** The first found returns true, which is sufficient for legality.
- **Board remains unchanged:** The scan is observational, so callers retain the original free move cell.
- **Guaranteed free move cell:** The code relies on the contract and does not validate it separately.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The board is fixed at $8$ by $8$. There are eight directions, and each scan takes at most seven steps before leaving the board. The operation count is bounded by a small constant, so time is $O(1)$ under the problem constraints.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
