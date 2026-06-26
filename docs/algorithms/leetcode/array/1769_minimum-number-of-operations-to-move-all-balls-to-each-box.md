# Minimum Number of Operations to Move All Balls to Each Box

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1769 |
| Difficulty | Medium |
| Topics | Array, String, Prefix Sum |
| Official Link | [minimum-number-of-operations-to-move-all-balls-to-each-box](https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/) |

## Problem Description & Examples
### Goal
Each box may contain a ball. For every target box, compute how many adjacent moves are needed to move all balls into that box.

### Function Contract
**Inputs**

- `boxes`: a binary string where `1` means a box contains a ball.

**Return value**

Return an array of move counts, one for each target box.

### Examples
**Example 1**

- Input: `boxes = "110"`
- Output: `[1,1,3]`

**Example 2**

- Input: `boxes = "001011"`
- Output: `[11,8,5,4,3,4]`

**Example 3**

- Input: `boxes = "0"`
- Output: `[0]`

---

## Underlying Base Algorithm(s)
Use two linear passes. From left to right, keep how many balls have been seen and the moves they contribute to the current index. Repeat from right to left and add the symmetric contribution. This avoids recomputing distances for every target.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` besides the output array
