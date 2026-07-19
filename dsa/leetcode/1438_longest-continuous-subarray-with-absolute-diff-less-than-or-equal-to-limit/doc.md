# Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1438 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Queue, Sliding Window, Heap (Priority Queue), Ordered Set, Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) |

## Problem Description

### Goal

Find the maximum length of a nonempty contiguous subarray of `nums` such that the absolute difference between any two elements in that subarray is at most `limit`.

For a fixed subarray, the largest absolute pairwise difference is the difference between its maximum and minimum values. The subarray is therefore valid exactly when `maximum - minimum <= limit`.

The selected elements must occupy consecutive indices in the original array; values cannot be skipped to create a longer subsequence.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.
- `limit`: the greatest permitted difference, where $0 \le \texttt{limit} \le 10^9$.

**Return value**

- The greatest length of a contiguous subarray whose maximum minus minimum is at most `limit`.

### Examples

**Example 1**

- Input: `nums = [8,2,4,7], limit = 4`
- Output: `2`

**Example 2**

- Input: `nums = [10,1,2,4,7,2], limit = 5`
- Output: `4`

**Example 3**

- Input: `nums = [4,2,2,2,4,4,2,2], limit = 0`
- Output: `3`
