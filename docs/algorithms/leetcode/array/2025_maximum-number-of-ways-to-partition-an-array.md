# Maximum Number of Ways to Partition an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2025 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Counting, Enumeration, Prefix Sum |
| Official Link | [maximum-number-of-ways-to-partition-an-array](https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/) |

## Problem Description & Examples
### Goal
Choose at most one element to replace with `k`. Maximize how many split positions have equal left and right sums after that optional change.

### Function Contract
**Inputs**

- `nums`: an integer array.
- `k`: replacement value.

**Return value**

Return the maximum number of valid partitions.

### Examples
**Example 1**

- Input: `nums = [2,-1,2], k = 3`
- Output: `1`

**Example 2**

- Input: `nums = [0,0,0], k = 1`
- Output: `2`

**Example 3**

- Input: `nums = [22,7,28,-13,14], k = -3`
- Output: `1`

---

## Underlying Base Algorithm(s)
For each split, define its balance as `left_sum - right_sum`. Without changes, balance `0` is valid. Replacing `nums[i]` by `k` shifts balances before and after index `i` in opposite ways. Sweep `i`, maintaining balance counts on the left and right of the replacement point, and test the needed shifted balances.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
