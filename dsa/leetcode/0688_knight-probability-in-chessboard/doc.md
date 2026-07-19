# Knight Probability in Chessboard

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 688 |
| Difficulty | Medium |
| Topics | Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/knight-probability-in-chessboard/) |

## Problem Description
### Goal
A chess knight starts at `(row, column)` on a zero-indexed $n \times n$ board and attempts to make exactly `k` moves. At every move, it chooses uniformly at random among all eight standard knight moves, including choices whose destination lies outside the board.

The knight stops once it moves off the board and cannot return. Return the probability that it remains on the chessboard after completing all `k` moves. For $k = 0$, the starting square is still occupied and the probability is `1`.

### Function Contract
**Inputs**

- `n`: the positive board side length
- `k`: the nonnegative number of moves
- `row`: the starting zero-based row
- `column`: the starting zero-based column

**Return value**

- The probability, between zero and one, that the knight is still on-board after exactly `k` moves

### Examples
**Example 1**

- Input: `n = 3, k = 2, row = 0, column = 0`
- Output: `0.0625`

**Example 2**

- Input: `n = 1, k = 0, row = 0, column = 0`
- Output: `1.0`

**Example 3**

- Input: `n = 1, k = 1, row = 0, column = 0`
- Output: `0.0`
