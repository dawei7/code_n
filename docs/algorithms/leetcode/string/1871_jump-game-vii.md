# Jump Game VII

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_213` |
| Frontend ID | 1871 |
| Difficulty | Medium |
| Topics | String, Dynamic Programming, Sliding Window, Prefix Sum |
| Official Link | [jump-game-vii](https://leetcode.com/problems/jump-game-vii/) |

## Problem Description & Examples
### Goal
You are given a 0-indexed binary string `s` and two integers `min_jump` and `max_jump`. In the beginning, you are standing at index `0`, which is equal to `'0'`. You can move from index `i` to index `j` if the following conditions are fulfilled:
- `i + min_jump <= j <= min(i + max_jump, s.length - 1)`
- `s[j] == '0'`

Return `True` if you can reach index `s.length - 1` in `s`, or `False` otherwise.

### Function Contract
**Inputs**

- `s`: str
- `min_jump`: int
- `max_jump`: int

**Return value**

bool - True if target reachable

### Examples
**Example 1**

- Input: `s = "011010", min_jump = 2, max_jump = 3`
- Output: `True`

**Example 2**

- Input: `s = '0100', min_jump = 2, max_jump = 5`
- Output: `True`

**Example 3**

- Input: `s = '010', min_jump = 1, max_jump = 3`
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
