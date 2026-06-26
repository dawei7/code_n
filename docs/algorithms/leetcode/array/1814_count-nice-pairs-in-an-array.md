# Count Nice Pairs in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1814 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math, Counting |
| Official Link | [count-nice-pairs-in-an-array](https://leetcode.com/problems/count-nice-pairs-in-an-array/) |

## Problem Description & Examples
### Goal
Count pairs `(i, j)` where `nums[i] + reverse(nums[j]) == nums[j] + reverse(nums[i])`.

### Function Contract
**Inputs**

- `nums`: a list of non-negative integers.

**Return value**

Return the number of nice pairs modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `nums = [42,11,1,97]`
- Output: `2`

**Example 2**

- Input: `nums = [13,10,35,24,76]`
- Output: `4`

**Example 3**

- Input: `nums = [1,1,1]`
- Output: `3`

---

## Underlying Base Algorithm(s)
Rearrange the equality to `nums[i] - reverse(nums[i]) == nums[j] - reverse(nums[j])`. Scan the array, compute this key for each value, add how many times the key has appeared before, and then increment its frequency.

---

## Complexity Analysis
- **Time Complexity**: `O(total digits)`
- **Space Complexity**: `O(n)`
