# Minimum Array End

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3133 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-array-end/) |

## Problem Description

### Goal

You are given two positive integers, `n` and `x`. Construct an array `nums` containing exactly `n` positive integers. The array must be strictly increasing, so `nums[i + 1]` is greater than `nums[i]` for every index $0 \le i < n - 1$.

The bitwise AND of all values in `nums` must equal `x`. Among every array satisfying both conditions, determine the minimum possible value of the final element `nums[n - 1]`. Only that minimum final value is returned; the array itself does not need to be produced.

### Function Contract

**Inputs**

- `n`: The required array length, with $1 \le n \le 10^8$.
- `x`: The required all-element bitwise AND, with $1 \le x \le 10^8$.

**Return value**

- Return the minimum possible value of `nums[n - 1]` as an integer.

### Examples

**Example 1**

- Input: `n = 3, x = 4`
- Output: `6`
- Explanation: The array `[4, 5, 6]` is strictly increasing, its bitwise AND is `4`, and its final value is minimal.

**Example 2**

- Input: `n = 2, x = 7`
- Output: `15`
- Explanation: The array `[7, 15]` meets the requirements and has the minimum possible final value.
