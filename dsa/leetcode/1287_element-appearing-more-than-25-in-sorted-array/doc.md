# Element Appearing More Than 25% In Sorted Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1287 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/) |

## Problem Description
### Goal
You are given an integer array `arr` sorted in non-decreasing order. Exactly one integer occurs more than $25\%$ of the array's length; every other value occurs at most that fraction.

Return the unique integer whose frequency is greater than one quarter of the array length. Equal values are contiguous because the input is sorted, and the qualifying frequency is strictly greater than—not merely equal to—$25\%$.

### Function Contract
**Inputs**

- `arr`: a nonempty integer array of length $n$, sorted in non-decreasing order, where $1 \le n \le 10^4$ and $0 \le \texttt{arr[i]} \le 10^5$.

**Return value**

The unique integer whose count $c$ satisfies $4c > n$.

### Examples
**Example 1**

- Input: `arr = [1,2,2,6,6,6,6,7,10]`
- Output: `6`

**Example 2**

- Input: `arr = [1,1]`
- Output: `1`

**Example 3**

- Input: `arr = [1,2,3,3,3,4]`
- Output: `3`
