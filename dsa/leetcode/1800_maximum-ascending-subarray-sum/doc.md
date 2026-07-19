# Maximum Ascending Subarray Sum

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-ascending-subarray-sum/) |
| Frontend ID | 1800 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

An ascending subarray is a contiguous, nonempty part of an integer array in which every value after the first is strictly greater than the value immediately before it. Equal adjacent values therefore end an ascending subarray; elements cannot be skipped to preserve the relation.

Given the positive integer array `nums`, consider every ascending subarray and calculate the sum of its elements. Return the largest such sum. A single element is itself a valid ascending subarray.

### Function Contract

**Inputs**

- `nums`: a list of $n$ positive integers, where $1 \le n \le 100$ and $1 \le \texttt{nums[i]} \le 100$.

**Return value**

- Return the maximum element sum among all contiguous strictly ascending subarrays of `nums`.

### Examples

**Example 1**

- Input: `nums = [10,20,30,5,10,50]`
- Output: `65`

The final ascending run `[5,10,50]` has the greatest sum.

**Example 2**

- Input: `nums = [10,20,30,40,50]`
- Output: `150`

The entire array is strictly ascending.

**Example 3**

- Input: `nums = [12,17,15,13,10,11,12]`
- Output: `33`

The best run is `[10,11,12]`.
