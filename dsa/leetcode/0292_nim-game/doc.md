# Nim Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 292 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Brainteaser, Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/nim-game/) |

## Problem Description
### Goal
A single pile starts with positive `n` stones. You move first, and the two players alternate removing exactly one, two, or three stones from the remaining pile. The player who takes the final stone wins the game.

Assuming both players choose moves optimally, return `True` when the first player has a strategy that guarantees victory regardless of the opponent's responses. Return `False` when every legal first move allows an optimal opponent to force the win. The task asks for the existence of a winning strategy, not for a particular sequence of removals or the number of turns.

### Function Contract
**Inputs**

- `n`: the positive number of stones in the initial pile

**Return value**

`True` when the first player can force a win; otherwise `False`.

### Examples
**Example 1**

- Input: `n = 4`
- Output: `false`

**Example 2**

- Input: `n = 1`
- Output: `true`

**Example 3**

- Input: `n = 2`
- Output: `true`
