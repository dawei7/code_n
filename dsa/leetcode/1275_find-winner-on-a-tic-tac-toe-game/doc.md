# Find Winner on a Tic Tac Toe Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1275 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/) |

## Problem Description

### Goal

Two players, `A` and `B`, play tic-tac-toe on an initially empty $3 \times 3$ grid. Player `A` moves first and marks `X`; player `B` marks `O`. They alternate turns, always selecting an empty cell. The game ends as soon as one player fills an entire row, column, or diagonal with their mark, or when all nine cells are occupied.

Array `moves` lists the played cells in chronological order. The sequence is guaranteed to describe a valid game, including the rule that no move occurs after the game has ended. Return the winning player's name if a win occurred. If the board filled without a winner, return `"Draw"`; if the valid sequence has not yet ended, return `"Pending"`.

### Function Contract

**Inputs**

- `moves`: a list of $m$ distinct coordinate pairs `[row, col]`, where $1 \le m \le 9$ and each coordinate is between $0$ and $2$ inclusive. Even-indexed moves belong to `A`; odd-indexed moves belong to `B`.

**Return value**

- Return exactly `"A"`, `"B"`, `"Draw"`, or `"Pending"` according to the final state represented by the valid move sequence.

### Examples

**Example 1**

- Input: `moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]`
- Output: `"A"`

**Example 2**

- Input: `moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]`
- Output: `"B"`

**Example 3**

- Input: `moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]`
- Output: `"Draw"`

### Required Complexity

- **Time:** $O(m)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Maintain signed totals for the three rows, three columns, and two diagonals. Give every move by `A` the value $1$ and every move by `B` the value $-1$. Add that value to the selected row and column, and also to a diagonal total when the cell belongs to it.

A line totals $3$ exactly when all three of its cells belong to `A`, and totals $-3$ exactly when they all belong to `B`; mixed or incomplete lines cannot have either magnitude. After applying the moves, any line with absolute total $3$ therefore identifies the winner. The input is a valid game, so there cannot be conflicting winners or later moves that obscure the first completed line.

If no line wins, nine moves mean that every cell is occupied and the result is `"Draw"`. With fewer moves, at least one cell remains available, so the result is `"Pending"`.

#### Complexity detail

Each of the $m$ moves updates a constant number of counters, giving $O(m)$ time. The eight counters occupy $O(1)$ auxiliary space. Since the legal board fixes $m \le 9$, the package verifies this bounded domain through exhaustive reachable-state regression rather than pretending that the input can scale asymptotically.

#### Alternatives and edge cases

- **Build the complete board:** Checking all eight winning lines after simulation is also correct, but the counters avoid storing the grid and express each line test directly.
- **Check only the last mover:** Because valid input stops at a win, only the final mover could have just won; that shortcut is valid but less direct than checking the eight accumulated totals.
- **Stop while processing moves:** Early winner detection is harmless, though the valid-sequence guarantee already ensures there are no later moves.
- **One move:** No line can be complete, so the result is `"Pending"`.
- **Full board without a winning line:** Exactly nine valid moves with no line of magnitude three produce `"Draw"`.
- **Both diagonals through the center:** A center move must update both diagonal counters.

</details>
