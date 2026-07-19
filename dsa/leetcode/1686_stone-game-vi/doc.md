# Stone Game VI

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1686 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Greedy, Sorting, Heap (Priority Queue), Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/stone-game-vi/) |

## Problem Description
### Goal

There are $n$ stones. Stone `i` is worth `aliceValues[i]` points if Alice takes it and `bobValues[i]` points if Bob takes it; the same physical stone may therefore have different values to the two players. Alice and Bob alternate taking one remaining stone, Alice moves first, and the chosen stone is removed. The game ends after all stones have been taken.

Both players choose optimally to determine the winner from their personal score totals. Return `1` when Alice finishes with more points, `-1` when Bob finishes with more points, and `0` when the totals are equal. Taking a stone both earns its current player's value and permanently denies the other player that stone's value.

### Function Contract
**Inputs**

- `aliceValues`: a length-$n$ list giving Alice's value for each stone
- `bobValues`: a length-$n$ list giving Bob's value for the corresponding stones

**Return value**

`1` if optimal play makes Alice win, `-1` if it makes Bob win, or `0` for a tie.

### Examples
**Example 1**

- Input: `aliceValues = [1, 3], bobValues = [2, 1]`
- Output: `1`

Alice takes stone 1 for three points; Bob then receives two points from stone 0.

**Example 2**

- Input: `aliceValues = [1, 2], bobValues = [3, 1]`
- Output: `0`

Optimal play gives both players one point.

**Example 3**

- Input: `aliceValues = [2, 4, 3], bobValues = [1, 6, 7]`
- Output: `-1`

Bob can force a strictly larger total.
