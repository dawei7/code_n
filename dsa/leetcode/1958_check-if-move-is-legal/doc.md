# Check if Move is Legal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1958 |
| Difficulty | Medium |
| Topics | Array, Matrix, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-move-is-legal/) |

## Problem Description
### Goal
An 8-by-8 game board uses `"."` for a free cell, `"W"` for a white piece,
and `"B"` for a black piece. A move places the given color on the specified
free cell.

The move is legal only when the newly occupied cell becomes one endpoint of a
horizontal, vertical, or diagonal good line. Such a line contains at least
three cells: both endpoints have the played color, every cell strictly between
them has the opposite color, and no cell in the line is free. Return whether
the proposed move is legal.

### Function Contract
**Inputs**

- `board`: an 8-by-8 matrix containing only `"."`, `"W"`, and `"B"`.
- `rMove`, `cMove`: zero-based coordinates in $[0,7]$ identifying a free cell.
- `color`: either `"W"` or `"B"`, the color placed by the proposed move.

**Return value**

- `True` if the new piece is an endpoint of at least one good line; otherwise
  `False`.

### Examples
**Example 1**

- Input: `board = [[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]], rMove = 4, cMove = 3, color = "B"`
- Output: `True`

**Example 2**

- Input: `board = [[".",".",".",".",".",".",".","."],[".","B",".",".","W",".",".","."],[".",".","W",".",".",".",".","."],[".",".",".","W","B",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".","B","W",".","."],[".",".",".",".",".",".","W","."],[".",".",".",".",".",".",".","B"]], rMove = 4, cMove = 4, color = "W"`
- Output: `False`

**Example 3**

- Input: `board = [[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".","W","B",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]], rMove = 3, cMove = 3, color = "B"`
- Output: `True`

### Required Complexity
- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Search the eight possible directions**

The placed piece can be an endpoint only along one of the eight horizontal,
vertical, or diagonal rays leaving `(rMove, cMove)`. For each direction, move
one cell at a time. The first cell must have the opposite color, which ensures
that a potential line has at least one middle cell.

**Recognize the closing endpoint**

Continue while cells have the opposite color. The direction forms a good line
exactly when this nonempty run is followed, before leaving the board, by a cell
of the played color. A free cell, the board edge, or an immediate same-colored
cell cannot close a valid line. Returning true for the first successful ray is
sound because one good line is sufficient; if all eight rays fail, no allowed
line orientation remains.

#### Complexity detail

The board dimensions are fixed by the contract. There are eight rays and each
contains at most seven cells, so at most 56 cell inspections are required.
This fixed upper bound gives $O(1)$ time. Only direction and coordinate
variables are retained, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Temporarily place the piece and scan complete rows:** This can be made
  correct, but it mutates the input unnecessarily and examines cells unrelated
  to lines having the move as an endpoint.
- **Check only four undirected lines:** Each line has two possible rays from
  the move, so both directions must still be inspected independently.
- An adjacent piece of the played color does not form a good line because at
  least one opposite-colored middle cell is required.
- A run of opposite pieces that reaches the board boundary without a matching
  endpoint is not sufficient.
- A good line elsewhere on the board, or one having the move as a middle cell,
  does not make the proposed move legal.

</details>
