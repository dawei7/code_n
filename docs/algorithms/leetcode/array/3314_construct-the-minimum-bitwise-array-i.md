# Construct the Minimum Bitwise Array I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3314 |
| Difficulty | Easy |
| Topics | Array, Bit Manipulation |
| Official Link | [construct-the-minimum-bitwise-array-i](https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/) |

## Problem Description & Examples
### Goal
Given an array of integers `nums`, construct a new array `ans` of the same length such that for each index `i`, the bitwise OR of `ans[i]` and `ans[i] + 1` equals `nums[i]`. If multiple such `ans[i]` exist, choose the smallest non-negative integer. If no such integer exists for a given `nums[i]`, set `ans[i]` to -1.

### Function Contract
**Inputs**

- `nums`: A list of integers where $1 \le nums[i] \le 10^9$.

**Return value**

- A list of integers representing the constructed array `ans`.

### Examples
**Example 1**

- Input: `nums = [2, 3, 5, 7]`
- Output: `[-1, 1, 4, 3]`

**Example 2**

- Input: `nums = [11, 13, 31]`
- Output: `[9, 12, 15]`

**Example 3**

- Input: `nums = [1]`
- Output: `[-1]`

---

## Underlying Base Algorithm(s)
The problem relies on the property of bitwise OR and the behavior of the `+ 1` operation. Specifically, `x | (x + 1)` effectively clears the lowest zero bit of `x` and sets all bits to the right of it to 1. To find the smallest `ans[i]` such that `ans[i] | (ans[i] + 1) == nums[i]`, we iterate through possible values or use bit manipulation to identify the candidate. Since the constraints are relatively small for this version, a linear search for the smallest bit-flip pattern is efficient.

---

## Complexity Analysis
- **Time Complexity**: $O(N \cdot K)$, where $N$ is the length of the array and $K$ is the number of bits (at most 30).
- **Space Complexity**: $O(N)$ to store the resulting array.
