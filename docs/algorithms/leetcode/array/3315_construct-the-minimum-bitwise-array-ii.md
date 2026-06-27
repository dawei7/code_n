# Construct the Minimum Bitwise Array II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3315 |
| Difficulty | Medium |
| Topics | Array, Bit Manipulation |
| Official Link | [construct-the-minimum-bitwise-array-ii](https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/) |

## Problem Description & Examples
### Goal
Given an array of integers `nums`, construct a new array `ans` of the same length such that for each index `i`, `ans[i] | (ans[i] + 1) == nums[i]`. If multiple such `ans[i]` exist, choose the smallest possible value. If no such value exists for a given `nums[i]`, set `ans[i]` to -1.

### Function Contract
**Inputs**

- `nums`: A list of integers where each element is the result of a bitwise OR operation between some integer `x` and `x + 1`.

**Return value**

- A list of integers representing the smallest possible `x` for each `nums[i]`, or -1 if no solution exists.

### Examples
**Example 1**

- Input: `nums = [2, 9, 16]`
- Output: `[1, 8, -1]`

**Example 2**

- Input: `nums = [15, 11, 1]`
- Output: `[7, 3, 0]`

**Example 3**

- Input: `nums = [7]`
- Output: `[3]`

---

## Underlying Base Algorithm(s)
The core observation is that `x | (x + 1)` effectively turns the least significant zero bit of `x` into a one. Specifically, if `x` has a binary representation ending in `...011...1`, then `x + 1` will end in `...100...0`. The OR operation fills all trailing zeros of `x` with ones. To find the smallest `x` such that `x | (x + 1) == target`, we look for the rightmost zero bit in `target` and flip it to zero while setting the bit to its right to one, effectively creating the smallest candidate. If `target` is even, no solution exists (except for 0, but the problem constraints imply target > 0).

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we perform constant-time bitwise operations for each element.
- **Space Complexity**: `O(n)` to store the resulting array.
