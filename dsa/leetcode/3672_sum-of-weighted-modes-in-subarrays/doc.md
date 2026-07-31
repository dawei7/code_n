# Sum of Weighted Modes in Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3672 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window, Counting, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-weighted-modes-in-subarrays/) |

## Problem Description
### Goal

Given an integer array `nums` and a window length `k`, consider every contiguous subarray containing exactly `k` elements.

Within one window, its mode is a value having the largest frequency. If several values share that maximum frequency, choose the numerically smallest tied value. Define the window's weight as the selected mode multiplied by its frequency in that window.

Return the sum of the weights of all length-`k` windows as the window moves from the beginning of `nums` to the end.

### Function Contract

**Inputs**

- `nums`: a positive integer array of length $n$, where $1\le n\le10^5$ and $1\le\texttt{nums[i]}\le10^5$.
- `k`: the exact subarray length, where $1\le k\le n$.

**Return value**

Return the sum, over all $n-k+1$ windows, of `mode * frequency(mode)`, using the smallest value to resolve frequency ties.

### Examples

**Example 1**

- Input: `nums = [1, 2, 2, 3]`, `k = 3`
- Output: `8`
- Both windows choose mode `2` with frequency `2`, contributing `4` each.

**Example 2**

- Input: `nums = [1, 2, 1, 2]`, `k = 2`
- Output: `3`
- Every window is tied at frequency one, so each chooses the smaller value `1`.

**Example 3**

- Input: `nums = [4, 3, 4, 3]`, `k = 3`
- Output: `14`
- The two weights are `4 * 2 = 8` and `3 * 2 = 6`.
