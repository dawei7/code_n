# Stone Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 877 |
| Difficulty | Medium |
| Topics | Array, Math, Dynamic Programming, Game Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/stone-game/) |

## Problem Description
### Goal
Alice and Bob play with an even number of piles arranged in a row. Every `piles[i]` is a positive number of stones, and the total number of stones across all piles is odd, so the final scores cannot tie. The objective is to collect more stones than the other player.

Alice moves first, and the players then alternate turns. On each turn, the player removes the entire pile at either the beginning or the end of the remaining row. Play continues until no piles remain. Assuming both players play optimally, return `true` if Alice wins and `false` if Bob wins.

### Function Contract
**Inputs**

- `piles`: an array of an even number $n$ of piles, where $2 \leq n \leq 500$, $1 \leq \texttt{piles[i]} \leq 500$, and the sum of all pile sizes is odd.

**Return value**

Return `true` when Alice wins under optimal play; otherwise, return `false`.

### Examples
**Example 1**

- Input: `piles = [5,3,4,5]`
- Output: `true`

Alice can take an endpoint pile of `5` and preserve a winning response to either of Bob's choices.

**Example 2**

- Input: `piles = [3,7,2,3]`
- Output: `true`

**Example 3**

- Input: `piles = [1,2]`
- Output: `true`

Alice takes the pile containing `2`.
