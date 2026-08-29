# Guided Example: Find Winner on a Tic Tac Toe Game

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"moves": [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]}`
- **Required output:** `"A"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

**Tic-tac-toe** is played by two players `A` and `B` on a `3 x 3` grid. The rules of Tic-Tac-Toe are:

The objective is to compute `"A"` from `{"moves": [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Only the last player can be the winner

The move list is guaranteed valid, and play stops as soon as someone wins. Therefore, if a winner exists, that winner made the final recorded move. Player A uses even move indices and player B uses odd indices. The exact source exploits this fact by examining only indices with the same parity as `n - 1`:

`range(n - 1, -1, -2)`.

Starting from the last move and subtracting two visits every move made by the last player and none made by the opponent. It is unnecessary to represent opponent marks because a valid finished game cannot contain an opponent win followed by another move.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"moves": [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Eight counters represent all winning lines

The $3$ by $3$ board has three rows, three columns, one main diagonal, and one anti-diagonal. Array `cnt` has eight entries. For move `(i, j)`, `cnt[i]` counts the chosen player's marks in row `i`, while `cnt[j + 3]` counts marks in column `j`.

If `i == j`, the cell lies on the main diagonal and `cnt[6]` increases. If `i + j == 2`, it lies on the anti-diagonal and `cnt[7]` increases. The center cell satisfies both conditions and correctly contributes to both diagonals.

After each processed mark, `any(v == 3 for v in cnt)` checks all eight possible lines. A count of three means the last player owns all three cells of that line because the input contains no repeated moves and only that player's moves were counted.

Although traversal goes backward in time, line membership is independent of ordering. Once all three marks of a winning line have been encountered, the counter reaches three. All visited indices have the same parity, so returning `"B" if k & 1 else "A"` identifies the last player. `k & 1` is one for an odd index and zero for an even index.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why ignoring the other player is safe

Suppose player A had won before B's final move. The rules would have ended the game immediately, making B's later move invalid. The valid-input guarantee rules this out. Thus, when the list ends on B's move, only B can possibly be the winner; symmetrically, a list ending on A's move can only have A as winner.

If the last player has a winning line, the loop eventually counts its three cells and returns that player. If the loop finishes without a counter reaching three, the last player did not win, and validity implies the opponent did not win either.

For the first example, the last move index is four, so the loop counts A's moves at indices four, two, and zero. Those coordinates fill the main diagonal, making counter six reach three and returning A.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"A"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"moves": [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"A"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Process both players with signed counters:** Add one for A and minus one for B to rows, columns, and diagonals. An absolute value of three identifies a winner and supports checking moves forward.
- **Build the full board:** Mark each move and scan its row, column, and diagonals. It is intuitive but stores more state and may rescan cells.
- **Count only the last player without valid-input guarantee:** This would be unsafe if moves could continue after an earlier win. The optimization depends on the stated validity.
- **Center move:** It increments its row, column, main diagonal, and anti-diagonal counters.
- **Corner move:** It belongs to one row, one column, and one or possibly both relevant diagonals according to the tests.
- **Winning final move:** Backward counting finds the completed line regardless of the order in which that player's earlier marks are encountered.
- **Nine moves without a winner:** Every square is occupied, so the result is `"Draw"`.
- **Fewer than nine moves without a winner:** At least one legal move remains, so the result is `"Pending"`.
- **Odd final index:** The last mover is B; every loop index is odd and the parity expression returns `"B"`.
- **Even final index:** The last mover is A and the parity expression returns `"A"`.
- **No repeated coordinates:** This guarantee prevents one cell from inflating a line counter more than once.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m)$. Let $m$ be the number of moves. The loop visits only one player's moves, at most $\lceil m/2\rceil$. Updating counters is constant work, and checking eight entries is also constant because the board size is fixed. Total time is $O(m)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
