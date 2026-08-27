# Guided Example: Design Tic-Tac-Toe

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 2, "moves": [[0, 0, 1], [1, 0, 2], [0, 1, 1]]}`
- **Required output:** `[0, 0, 1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Assume the following rules are for the tic-tac-toe game on an `n x n` board between two players:

The objective is to compute `[0, 0, 1]` from `{"n": 2, "moves": [[0, 0, 1], [1, 0, 2], [0, 1, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why line counts are sufficient.

An $n \times n$ board has $n$ horizontal winning lines, $n$ vertical winning lines, one main diagonal, and one anti-diagonal. A player wins exactly when that player owns all $n$ cells of at least one such line. Because moves are guaranteed to use different cells, one player cannot contribute twice to the same cell. Therefore, if that player's count for a line reaches $n$, those $n$ contributions must correspond to the $n$ different cells on that line. No board scan is needed to confirm the win.

This reasoning depends on the validity guarantees in the contract. If duplicate moves were allowed, blindly incrementing a line counter could make a count reach $n$ even though fewer than $n$ distinct cells had been occupied. The implementation deliberately does not store an occupancy board or reject repeated cells because the caller promises that such input never occurs.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 2, "moves": [[0, 0, 1], [1, 0, 2], [0, 1, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Separate counters for the two players.

The constructor stores `cnt` as a two-element list. Element `0` is a `defaultdict(int)` containing player 1's line counts, and element `1` contains player 2's line counts. A missing dictionary key behaves as if its value were zero. On a move, `cnt[player - 1]` selects the current player's dictionary: player 1 maps to index `0`, and player 2 maps to index `1`.

Keeping the players separate makes every stored count nonnegative and easy to interpret. A value of `5` simply means that this player has placed five marks on that particular line. The opponent's marks do not need to decrement or otherwise alter it. A line containing both players can never give either player a count of $n$, because the board has only $n$ distinct cells on that line.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The constructor stores `cnt` as a two-element list.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Encoding every kind of line in one dictionary.

Rows, columns, and diagonals need distinct keys so that unrelated counts cannot collide. The solution creates disjoint numeric key ranges:

- Row `row` uses key `row`, so row keys lie from `0` through `n - 1`.
- Column `col` uses key `n + col`, so column keys lie from `n` through `2n - 1`.
- The main diagonal uses key `n << 1`, which equals $2n$.
- The anti-diagonal uses key `n << 1 | 1`. Since $2n$ is even, bitwise OR with `1` produces $2n+1$.

The bit operations are only a compact way to form the final two unique keys. They do not implement a special bitmask algorithm. Conceptually, the diagonal keys are simply `2 * n` and `2 * n + 1`. This layout lets one dictionary replace separate row arrays, column arrays, and diagonal variables while preserving the same information.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, 0, 1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 2, "moves": [[0, 0, 1], [1, 0, 2], [0, 1, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, 0, 1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Store and scan the complete board:** Record ev:** - **Store and scan the complete board:** Record every mark in an $n \times n$ matrix, then inspect the affected row, affected column, and applicable diagonals after each move. This is straightforward, but one call can take $O(n)$ time and the board takes $O(n^2)$ space. Scanning the entire board would be even less efficient and is unnecessary because only lines through the latest cell can change.
- **- **One signed counter set:** Use one row array, o:** - **One signed counter set:** Use one row array, one column array, and two diagonal totals; add `1` for player 1 and `-1` for player 2. An absolute value of $n$ signals a win. This uses $O(n)$ space and $O(1)$ time per move, but the exact solution chooses separate dictionaries so each count directly belongs to one player.
- **- **Fixed arrays instead of dictionaries:** Alloca:** - **Fixed arrays instead of dictionaries:** Allocate `2 * n + 2` counters for each player and use the same key encoding. This removes hash-table overhead and preserves $O(1)$ time and $O(n)$ space, at the cost of eagerly allocating every possible counter.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m)$. Let $n$ be the board dimension and let $m$ be the number of calls made to `move`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
