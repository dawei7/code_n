# Available Captures for Rook

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 999 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/available-captures-for-rook/) |

## Problem Description

### Goal

You are given an $8\times8$ matrix representing a chessboard. Exactly one white rook is marked `'R'`; white bishops are marked `'B'`, black pawns are marked `'p'`, and empty squares are marked `'.'`.

The rook can move horizontally or vertically through any number of empty squares until it reaches the board edge or another piece. It attacks a pawn when it can reach that pawn's square in one move, but it cannot pass through a bishop or another pawn. Return the number of black pawns currently attacked by the rook.

### Function Contract

**Inputs**

- `board`: exactly eight rows of eight characters each. Every cell is `'R'`, `'B'`, `'p'`, or `'.'`, and exactly one cell contains the rook.

**Return value**

- The number of directions in which the first piece visible from the rook is a black pawn.

### Examples

**Example 1**

- Input: a board with the rook at row $2$, column $3$ and unobstructed pawns above, right, and below it.
- Output: `3`
- Explanation: All three pawns are reachable in one rook move.

**Example 2**

- Input: a board with a bishop immediately adjacent to the rook in every direction.
- Output: `0`
- Explanation: Each bishop blocks the pawns beyond it.

**Example 3**

- Input: a board where the first visible pieces are pawns above, left, and right, while a bishop blocks the downward pawn.
- Output: `3`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Locate the unique rook:** Scan the fixed board until finding `'R'`. Its row and column are the common starting coordinates for all four possible attack rays.

**Inspect the first piece in each direction:** For each of up, down, left, and right, advance one square at a time. Empty squares do not change the ray. On reaching a bishop, stop because it blocks everything beyond it. On reaching a pawn, count one capture and stop because that pawn is itself the first blocking piece. Reaching the board boundary also ends the ray.

A rook attacks at most one pawn in each direction: any nearer piece prevents it from reaching a farther square in the same move. Thus examining the first nonempty square on all four rays counts every attacked pawn exactly once.

#### Complexity detail

The board always has 64 cells. Locating the rook examines at most 64 cells, and the four rays inspect at most seven squares each, so both time and auxiliary space are $O(1)$ over the fixed public domain.

#### Alternatives and edge cases

- **Scan the rook's full row and column:** This remains constant-time on an 8×8 board, but it must still preserve nearest-blocker order in both directions.
- **Chess move simulation:** Building a general chess engine adds unrelated rules and state without improving this fixed one-move visibility query.
- **Pawn behind a bishop:** The bishop ends the ray, so the pawn cannot be captured.
- **Second pawn on one ray:** The nearer pawn is capturable and blocks the farther pawn.
- **Rook at an edge or corner:** Directions that immediately leave the board contribute no capture.

</details>
