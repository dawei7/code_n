# Sum of Subarray Ranges

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2104 |
| Difficulty | Medium |
| Topics | Array, Stack, Monotonic Stack |
| Official Link | [sum-of-subarray-ranges](https://leetcode.com/problems/sum-of-subarray-ranges/) |

## Problem Description & Examples
### Goal
For every subarray, compute maximum minus minimum and sum those ranges.

### Function Contract
**Inputs**

- `nums`: an integer array.

**Return value**

Return the sum of all subarray ranges.

### Examples
**Example 1**

- Input: `nums = [1,2,3]`
- Output: `4`

**Example 2**

- Input: `nums = [1,3,3]`
- Output: `4`

**Example 3**

- Input: `nums = [4,-2,-3,4,1]`
- Output: `59`

---

## Underlying Base Algorithm(s)
Compute each element's total contribution as a subarray maximum and as a subarray minimum using monotonic stacks for previous/next greater and smaller boundaries. The answer is total maximum contributions minus total minimum contributions.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
