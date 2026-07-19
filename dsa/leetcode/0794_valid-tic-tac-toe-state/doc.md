# Valid Tic-Tac-Toe State

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 794 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-tic-tac-toe-state/) |

## Problem Description

### Goal

Given a $3 x 3$ Tic-Tac-Toe board containing `X`, `O`, and empty spaces, determine whether the displayed state can occur during a legal game. Player `X` moves first, and the players then alternate placing one mark in an empty cell.

The game ends immediately when either player completes a full row, column, or diagonal, so no later marks may be played after that win. Return `True` if some legal move sequence reaches exactly the supplied board and `False` otherwise.

### Function Contract

**Inputs**

- `board`: three strings of length three representing the current board.

**Return value**

- `True` if some legal move sequence reaches exactly this state; otherwise `False`.

### Examples

**Example 1**

- Input: `board = ["O  ","   ","   "]`
- Output: `False`
- Explanation: `O` cannot move before `X`.

**Example 2**

- Input: `board = ["XOX"," X ","   "]`
- Output: `False`
- Explanation: Three `X` marks and one `O` mark cannot result from alternating turns.

**Example 3**

- Input: `board = ["XOX","O O","XOX"]`
- Output: `True`
- Explanation: The marks alternate correctly and neither player has already won.
