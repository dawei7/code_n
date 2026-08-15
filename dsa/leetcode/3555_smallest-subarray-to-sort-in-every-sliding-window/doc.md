# Smallest Subarray to Sort in Every Sliding Window

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3555 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Stack, Greedy, Sorting, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-subarray-to-sort-in-every-sliding-window/) |

## Problem Description

### Goal

You are given an integer array `nums` and a window length `k`. Consider every contiguous subarray of exactly `k` elements, from left to right.

For each window, find the minimum length of one contiguous segment whose elements can be sorted so that the entire window becomes non-decreasing. Sorting may change only the chosen segment. If a window is already non-decreasing, its answer is zero.

Return the answers for all windows in their original order. The result therefore contains exactly $n-k+1$ values, where $n=\lvert\texttt{nums}\rvert$.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$.
- `k`: The exact length of every sliding window.

The constraints are $1 \le n \le 1000$, $1 \le k \le n$, and $1 \le \texttt{nums[i]} \le 10^6$.

**Return value**

Return an integer array of length $n-k+1$. Its value at index $s$ is the shortest segment length that must be sorted to make `nums[s:s+k]` non-decreasing, or zero when that window is already non-decreasing.

### Examples

#### Example 1

- **Input:** `nums = [1,3,2,4,5], k = 3`
- **Output:** `[2,2,0]`
- **Explanation:** In each of the first two windows, sorting the adjacent pair `[3,2]` is sufficient. The last window is already non-decreasing.

#### Example 2

- **Input:** `nums = [5,4,3,2,1], k = 4`
- **Output:** `[4,4]`
- **Explanation:** Each length-four window is strictly decreasing, so every element in that window must be included.

---
