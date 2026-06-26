# Minimum Elements to Add to Form a Given Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1785 |
| Difficulty | Medium |
| Topics | Array, Greedy |
| Official Link | [minimum-elements-to-add-to-form-a-given-sum](https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/) |

## Problem Description & Examples
### Goal
You may append integers whose absolute value is at most `limit`. Find how many numbers must be appended so the final array sum equals `goal`.

### Function Contract
**Inputs**

- `nums`: the current integer array.
- `limit`: the maximum absolute value for each added number.
- `goal`: the desired final sum.

**Return value**

Return the minimum count of appended elements.

### Examples
**Example 1**

- Input: `nums = [1,-1,1], limit = 3, goal = -4`
- Output: `2`

**Example 2**

- Input: `nums = [1,-10,9,1], limit = 100, goal = 0`
- Output: `1`

**Example 3**

- Input: `nums = [0], limit = 5, goal = 0`
- Output: `0`

---

## Underlying Base Algorithm(s)
Let `diff = abs(goal - sum(nums))`. Each appended number can reduce the remaining difference by at most `limit`, so the answer is the ceiling of `diff / limit`.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
