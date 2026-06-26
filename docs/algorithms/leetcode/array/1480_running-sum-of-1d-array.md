# Running Sum of 1d Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1480 |
| Difficulty | Easy |
| Topics | Array, Prefix Sum |
| Official Link | [running-sum-of-1d-array](https://leetcode.com/problems/running-sum-of-1d-array/) |

## Problem Description & Examples
### Goal
Return the running prefix sums of the input array.

### Function Contract
**Inputs**

- `nums`: a list of integers.

**Return value**

A list where position `i` is the sum of `nums[0]` through `nums[i]`.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4]`
- Output: `[1,3,6,10]`

**Example 2**

- Input: `nums = [1,1,1,1,1]`
- Output: `[1,2,3,4,5]`

**Example 3**

- Input: `nums = [3,1,2,10,1]`
- Output: `[3,4,6,16,17]`

---

## Underlying Base Algorithm(s)
Prefix accumulation.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` for the returned list, or `O(1)` extra if updating in place.
