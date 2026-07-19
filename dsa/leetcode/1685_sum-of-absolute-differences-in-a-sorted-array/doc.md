# Sum of Absolute Differences in a Sorted Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1685 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/) |

## Problem Description
### Goal

Given an integer array `nums` sorted in non-decreasing order, construct another array of the same length. At every index `i`, the new value must be the sum of the absolute differences between `nums[i]` and each other array element.

Formally, the result at `i` is the sum of $\lvert \texttt{nums[i]} - \texttt{nums[j]} \rvert$ over all indices `j` other than `i`. The omitted self-term would be zero, so including it would not change the numeric result. Return every per-index sum in the original array order; equal input values occupy separate positions and receive their own, possibly identical, results.

### Function Contract
**Inputs**

- `nums`: a non-decreasing list of $n$ positive integers

**Return value**

A length-$n$ integer list whose value at index `i` is the total absolute distance from `nums[i]` to all other elements.

### Examples
**Example 1**

- Input: `nums = [2, 3, 5]`
- Output: `[4, 3, 5]`

For value 2, the total is $\lvert 2-3 \rvert + \lvert 2-5 \rvert = 4$.

**Example 2**

- Input: `nums = [1, 4, 6, 8, 10]`
- Output: `[24, 15, 13, 15, 21]`

**Example 3**

- Input: `nums = [1, 1, 1]`
- Output: `[0, 0, 0]`

Equal values contribute zero distance to one another.
