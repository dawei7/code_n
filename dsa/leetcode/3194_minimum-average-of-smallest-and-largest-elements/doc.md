# Minimum Average of Smallest and Largest Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3194 |
| Difficulty | Easy |
| Topics | Array, Two Pointers, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/) |

## Problem Description
### Goal
You are given an integer array `nums` of even length. Begin with an empty
array of floating-point values called `averages`.

Repeat the following process exactly `n / 2` times: remove the current
smallest element and the current largest element from `nums`, compute their
average, and append that value to `averages`. Return the minimum value that
was appended. Because $n$ is even, every input value participates in exactly
one removal pair.

### Function Contract
**Inputs**

- `nums`: An array of an even number $n$ of integers, where
  $2 \le n \le 50$ and $1 \le \texttt{nums[i]} \le 50$.

**Return value**

The minimum average produced while repeatedly removing the current smallest
and largest remaining elements.

### Examples
**Example 1**

- Input: `nums = [7, 8, 3, 4, 15, 13, 4, 1]`
- Output: `5.5`

The successive averages are `8`, `8`, `6`, and `5.5`, so the minimum is
`5.5`.

**Example 2**

- Input: `nums = [1, 9, 8, 3, 10, 5]`
- Output: `5.5`

Removing the extremes in pairs produces `5.5`, `6`, and `6.5`.

**Example 3**

- Input: `nums = [1, 2, 3, 7, 8, 9]`
- Output: `5.0`

Every smallest-largest pair has sum `10`, so every recorded average is `5`.
