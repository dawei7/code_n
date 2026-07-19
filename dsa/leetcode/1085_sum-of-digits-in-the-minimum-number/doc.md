# Sum of Digits in the Minimum Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1085 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/) |

## Problem Description

### Goal

Given an array `nums` of positive integers, first identify the minimum number in the entire array. Then add the decimal digits of that minimum value; no other array element contributes to this digit sum.

Return `1` when the resulting digit sum is even. Return `0` when the digit sum is odd. Repeated occurrences of the same minimum do not change the result because they have the same decimal digits.

### Function Contract

**Inputs**

- `nums`: a non-empty list of $n$ positive integers.

Let $D$ be the number of decimal digits in `min(nums)`.

**Return value**

- `1` if the decimal digit sum of `min(nums)` is even; otherwise `0`.

### Examples

**Example 1**

- Input: `nums = [34, 23, 1, 24, 75, 33, 54, 8]`
- Output: `0`

The minimum is 1, whose digit sum is odd.

**Example 2**

- Input: `nums = [99, 77, 33, 66, 55]`
- Output: `1`

The minimum is 33, and $3+3=6$ is even.
