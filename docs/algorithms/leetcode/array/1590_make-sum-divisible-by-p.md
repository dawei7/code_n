# Make Sum Divisible by P

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1590 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Prefix Sum |
| Official Link | [make-sum-divisible-by-p](https://leetcode.com/problems/make-sum-divisible-by-p/) |

## Problem Description & Examples
### Goal
Remove the shortest non-empty contiguous subarray so the remaining sum is
divisible by `p`. Removing the whole array is not allowed.

### Function Contract
**Inputs**

- `nums`: an integer array.
- `p`: the divisor.

**Return value**

The minimum removed length, or `-1` if no valid removal exists.

### Examples
**Example 1**

- Input: `nums = [3, 1, 4, 2], p = 6`
- Output: `1`

**Example 2**

- Input: `nums = [6, 3, 5, 2], p = 9`
- Output: `2`

**Example 3**

- Input: `nums = [1, 2, 3], p = 3`
- Output: `0`

---

## Underlying Base Algorithm(s)
Let `need = sum(nums) % p`. If it is zero, no removal is needed. Otherwise scan
prefix sums modulo `p` and store the latest index for each remainder. At prefix
remainder `cur`, a removable subarray ending here must start after a prior
prefix with remainder `(cur - need) % p`; minimize that length.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(min(n, p))`.
