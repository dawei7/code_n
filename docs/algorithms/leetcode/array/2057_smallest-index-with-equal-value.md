# Smallest Index With Equal Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2057 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [smallest-index-with-equal-value](https://leetcode.com/problems/smallest-index-with-equal-value/) |

## Problem Description & Examples
### Goal
Find the first index whose index modulo `10` equals the value stored there.

### Function Contract
**Inputs**

- `nums`: an integer array.

**Return value**

Return the smallest valid index, or `-1` if none exists.

### Examples
**Example 1**

- Input: `nums = [0,1,2]`
- Output: `0`

**Example 2**

- Input: `nums = [4,3,2,1]`
- Output: `2`

**Example 3**

- Input: `nums = [1,2,3,4,5,6,7,8,9,0]`
- Output: `-1`

---

## Underlying Base Algorithm(s)
Scan from left to right and return the first index `i` satisfying `i % 10 == nums[i]`.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
