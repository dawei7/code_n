# Stone Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_200` |
| Frontend ID | 877 |
| Difficulty | Medium |
| Topics | Array, Math, Dynamic Programming, Game Theory |
| Official Link | [stone-game](https://leetcode.com/problems/stone-game/) |

## Problem Description & Examples
### Goal
Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones `piles[i]`.

The objective of the game is to end with the most stones. The total number of stones is odd, so there are no ties.

Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.

Return `True` if Alice wins the game, or `False` if Bob wins.

### Function Contract
**Inputs**

- `piles`: List[int]

**Return value**

bool - True if Alice wins

### Examples
**Example 1**

- Input: `piles = [5, 3, 4, 5]`
- Output: `True`

**Example 2**

- Input: `piles = [15, 2]`
- Output: `True`

**Example 3**

- Input: `piles = [20, 3]`
- Output: `True`

---

## Underlying Base Algorithm(s)
- [Longest common subsequence](dp_04_longest-common-subsequence.md)
- [Edit distance](dp_08_edit-distance.md)
- [Unique paths](dp_10_unique-paths.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
