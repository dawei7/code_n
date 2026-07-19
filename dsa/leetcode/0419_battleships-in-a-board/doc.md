# Battleships in a Board

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 419 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/battleships-in-a-board/) |

## Problem Description
### Goal
Given a nonempty rectangular board containing ship cells `"X"` and empty cells `"."`, each battleship is one straight horizontal or vertical run of one or more ship cells. Ships never bend, and distinct ships do not touch through a horizontal or vertical edge.

Return the number of battleships in one pass, without modifying the board and using only $O(1)$ extra memory. A single isolated `"X"` is a one-cell ship, and diagonally touching ships remain distinct. Count each run once rather than once per occupied cell. The task returns only the number of ships, not their coordinates, lengths, or orientations.

### Function Contract
**Inputs**

- `board`: a nonempty rectangular character matrix containing only `"X"` and `"."`

**Return value**

- Return the number of distinct battleships without modifying the board.

### Examples
**Example 1**

- Input: `board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]`
- Output: `2`

**Example 2**

- Input: `board = [["."]]`
- Output: `0`

**Example 3**

- Input: `board = [["X"]]`
- Output: `1`
