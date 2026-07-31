# Find the Maximum Sequence Value of Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3287 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/) |

## Problem Description

### Goal

For an even-length sequence `seq` of size $2x$, define its value by taking the bitwise OR of its first $x$ elements, taking the bitwise OR of its last $x$ elements, and XORing those two results.

Given `nums` and a positive integer `k`, choose any subsequence of exactly $2k$ elements while preserving their original order. Return the largest possible value of that subsequence. Values are smaller than $2^7$, so every OR result is one of the 128 masks from 0 through 127.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, each smaller than $2^7$.
- `k`: The number of selected elements in each half of the subsequence.

The length $n$ is between $2$ and $400$, and $1\le k\le n/2$.

**Return value**

Return the maximum of `(OR of first k selected values) XOR (OR of last k selected values)` over all length-$2k$ subsequences.

### Examples

**Example 1**

- Input: `nums = [2,6,7], k = 1`
- Output: `5`

Selecting `[2,7]` gives `2 XOR 7 = 5`.

**Example 2**

- Input: `nums = [4,2,5,6,7], k = 2`
- Output: `2`

Selecting `[4,5,6,7]` gives `(4 OR 5) XOR (6 OR 7) = 2`.
