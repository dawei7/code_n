# Jump Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_211` |
| Frontend ID | 55 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Greedy |
| Official Link | [jump-game](https://leetcode.com/problems/jump-game/) |

## Problem Description & Examples
### Goal
You are given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return `True` if you can reach the last index, or `False` otherwise.

### Function Contract
**Inputs**

- `nums`: List[int]

**Return value**

bool - True if last index is reachable

### Examples
**Example 1**

- Input: `nums = [2, 3, 1, 1, 4]`
- Output: `True`

**Example 2**

- Input: `nums = [3, 0]`
- Output: `True`

**Example 3**

- Input: `nums = [4]`
- Output: `True`

---

## Underlying Base Algorithm(s)
- [Gas station](greedy_06_gas-station.md)
- [Jump game](greedy_07_jump-game.md)
- [Candy distribution](greedy_08_candy-distribution.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
