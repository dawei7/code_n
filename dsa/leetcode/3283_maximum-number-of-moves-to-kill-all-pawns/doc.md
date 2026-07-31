# Maximum Number of Moves to Kill All Pawns

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3283 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Bit Manipulation, Breadth-First Search, Game Theory, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Maximum Number of Moves to Kill All Pawns](https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/) |

## Problem Description

### Goal

A knight and up to fifteen pawns occupy distinct cells of a $50\times50$ chessboard. Alice and Bob alternate turns, beginning with Alice. On a turn, the player chooses any remaining pawn, and the knight captures that selected pawn using the fewest legal knight moves from its current cell.

The knight may pass through cells occupied by other pawns without capturing them; only the selected destination pawn disappears. Its captured cell becomes the knight's starting position for the next turn. Thus a turn's cost depends only on the previous captured position and the newly selected pawn.

The game ends after every pawn has been captured. Alice wants to maximize the total number of knight moves made by both players, while Bob wants to minimize that same total. Return the resulting total under optimal play.

### Function Contract

**Inputs**

- `kx`: The knight's initial row, from `0` through `49`.
- `ky`: The knight's initial column, from `0` through `49`.
- `positions`: Between one and fifteen unique pawn coordinates, each distinct from the knight's initial cell.

Let $p$ be the number of pawns and $B=2500$ the number of board cells.

**Return value**

Return the optimal total number of moves when Alice maximizes and Bob minimizes, with Alice taking the first pawn-selection turn.

### Examples

**Example 1**

- Input: `kx = 1, ky = 1, positions = [[0, 0]]`
- Output: `4`
- Explanation: Board boundaries make the shortest knight path to the corner four moves long.

**Example 2**

- Input: `kx = 0, ky = 2, positions = [[1, 1], [2, 2], [3, 3]]`
- Output: `8`
- Explanation: Optimal choices contribute `2`, `2`, and `4` moves.

**Example 3**

- Input: `kx = 0, ky = 0, positions = [[1, 2], [2, 4]]`
- Output: `3`
- Explanation: Passing through the first pawn while targeting the second does not capture it.
