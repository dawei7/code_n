# Maximum Alternating Subarray Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2036 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-alternating-subarray-sum/) |

## Problem Description

### Goal

A subarray is a nonempty contiguous segment of the 0-indexed integer array
`nums`. For a subarray beginning at index $i$, form its alternating sum by
adding `nums[i]`, subtracting the next element, adding the following element,
and continuing with alternating signs through the chosen endpoint.

Consider every possible nonempty subarray. Return the greatest alternating sum
among them. The sign pattern always restarts with addition at the subarray's
left boundary; elements cannot be skipped, and the selected segment may have
either odd or even length.

### Function Contract

Let $N$ be the length of `nums`.

**Inputs**

- `nums`: an integer array with $1 \le N \le 10^5$ and
  $-10^5 \le \texttt{nums[i]} \le 10^5$.

**Return value**

- The maximum alternating sum of any nonempty contiguous subarray of `nums`.

### Examples

**Example 1**

- Input: `nums = [3, -1, 1, 2]`
- Output: `5`
- Explanation: Subarray `[3, -1, 1]` contributes `3 - (-1) + 1 = 5`.

**Example 2**

- Input: `nums = [2, 2, 2, 2, 2]`
- Output: `2`
- Explanation: A one-element subarray has sum `2`; odd-length alternating
  segments also have sum `2`.

**Example 3**

- Input: `nums = [1]`
- Output: `1`
