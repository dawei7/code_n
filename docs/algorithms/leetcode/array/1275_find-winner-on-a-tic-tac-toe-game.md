# Find Winner on a Tic Tac Toe Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1275 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Matrix, Simulation |
| Official Link | [find-winner-on-a-tic-tac-toe-game](https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/) |

## Problem Description & Examples
### Goal
Given the sequence of moves in a `3 x 3` tic-tac-toe game, report whether player A wins, player B wins, the game is a draw, or the game is still pending.

### Function Contract
**Inputs**

- `moves`: positions played in order; A moves first and players alternate.

**Return value**

`"A"`, `"B"`, `"Draw"`, or `"Pending"`.

### Examples
**Example 1**

- Input: `moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]`
- Output: `"A"`

**Example 2**

- Input: `moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]`
- Output: `"B"`

**Example 3**

- Input: `moves = [[0,0],[1,1]]`
- Output: `"Pending"`

---

## Underlying Base Algorithm(s)
Small-board simulation and line checking.

---

## Complexity Analysis
- **Time Complexity**: `O(1)` because the board size is fixed.
- **Space Complexity**: `O(1)`
