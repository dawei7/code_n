# Stone Game III

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_190` |
| Frontend ID | 1406 |
| Difficulty | Hard |
| Topics | Array, Math, Dynamic Programming, Game Theory |
| Official Link | [stone-game-iii](https://leetcode.com/problems/stone-game-iii/) |

## Problem Description & Examples
### Goal
Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array `stone_value`.

Alice and Bob take turns, with Alice starting first. On each turn, a player can take `1`, `2`, or `3` stones from the first remaining stones in the row.

The game ends when no more stones are left. The player with the highest score wins. The score of a player is the sum of the values of the stones taken by that player.

Return `"Alice"` if Alice wins, `"Bob"` if Bob wins, or `"Tie"` if they get the same score.

### Function Contract
**Inputs**

- `stone_value`: List[int]

**Return value**

str - 'Alice', 'Bob', or 'Tie'

### Examples
**Example 1**

- Input: `stone_value = [1, 2, 3, 7]`
- Output: `"Bob"`

**Example 2**

- Input: `stone_value = [2]`
- Output: `'Alice'`

**Example 3**

- Input: `stone_value = [-6, 8]`
- Output: `'Alice'`

---

## Underlying Base Algorithm(s)
- [Climbing stairs recurrence](dp_02_climbing-stairs.md)
- [Coin change](dp_05_coin-change.md)
- [Longest increasing subsequence](dp_07_longest-increasing-subsequence.md)
- [House robber](dp_11_house-robber.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
