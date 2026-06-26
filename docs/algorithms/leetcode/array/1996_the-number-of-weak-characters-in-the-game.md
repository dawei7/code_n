# The Number of Weak Characters in the Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1996 |
| Difficulty | Medium |
| Topics | Array, Stack, Greedy, Sorting, Monotonic Stack |
| Official Link | [the-number-of-weak-characters-in-the-game](https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/) |

## Problem Description & Examples
### Goal
A character is weak if another character has both strictly higher attack and strictly higher defense. Count weak characters.

### Function Contract
**Inputs**

- `properties`: pairs `[attack, defense]`.

**Return value**

Return the number of weak characters.

### Examples
**Example 1**

- Input: `properties = [[5,5],[6,3],[3,6]]`
- Output: `0`

**Example 2**

- Input: `properties = [[2,2],[3,3]]`
- Output: `1`

**Example 3**

- Input: `properties = [[1,5],[10,4],[4,3]]`
- Output: `1`

---

## Underlying Base Algorithm(s)
Sort by attack descending and defense ascending for ties. Sweep in that order while tracking the maximum defense seen among strictly larger attacks; a character is weak when its defense is below that maximum.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` beyond sorting.
