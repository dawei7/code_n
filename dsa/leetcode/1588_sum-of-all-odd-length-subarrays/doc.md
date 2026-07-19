# Sum of All Odd Length Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1588 |
| Difficulty | Easy |
| Topics | Array, Math, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-all-odd-length-subarrays/) |

## Problem Description
### Goal

Given an array of positive integers, consider every contiguous subarray whose length is odd. This includes every one-element subarray, every valid three-element subarray, and so on through the largest odd length that fits.

Compute each such subarray's sum, then return the total across all of them. Overlapping subarrays are distinct and must each contribute. A subarray is contiguous; non-adjacent subsequences do not count.

### Function Contract
**Inputs**

- `arr`: An array of $N$ positive integers, where $1 \le N \le 100$ and $1 \le \texttt{arr[i]} \le 1000$.

**Return value**

Return the sum of the sums of all odd-length contiguous subarrays of `arr`.

### Examples
**Example 1**

- Input: `arr = [1,4,2,5,3]`
- Output: `58`

**Example 2**

- Input: `arr = [1,2]`
- Output: `3`

**Example 3**

- Input: `arr = [10,11,12]`
- Output: `66`
