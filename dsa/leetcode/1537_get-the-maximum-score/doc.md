# Get the Maximum Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1537 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Two Pointers, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/get-the-maximum-score/) |

## Problem Description
### Goal
You are given two strictly increasing arrays of distinct positive integers. A valid path begins at index zero of either array and moves from left to right. Whenever the current value occurs in both arrays, the path may continue in its present array or switch to the other one. A shared value is counted only once when a switch occurs.

The score of a path is the sum of its visited values. Find the maximum score among all valid paths and return it modulo $10^9 + 7$.

### Function Contract
**Inputs**

- `nums1`: a strictly increasing array with length $n$.
- `nums2`: a strictly increasing array with length $m$.
- Both lengths are between $1$ and $10^5$, and every value is between $1$ and $10^7$.

**Return value**

The greatest valid-path score, reduced modulo $10^9 + 7$.

### Examples
**Example 1**

- Input: `nums1 = [2, 4, 5, 8, 10], nums2 = [4, 6, 8, 9]`
- Output: `30`
- Explanation: The path `[2, 4, 6, 8, 10]` has the largest score.

**Example 2**

- Input: `nums1 = [1, 3, 5, 7, 9], nums2 = [3, 5, 100]`
- Output: `109`
- Explanation: The best path is `[1, 3, 5, 100]`.

**Example 3**

- Input: `nums1 = [1, 2, 3, 4, 5], nums2 = [6, 7, 8, 9, 10]`
- Output: `40`
- Explanation: With no shared value, the entire second array is optimal.
