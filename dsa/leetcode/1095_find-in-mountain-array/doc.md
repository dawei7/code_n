# Find in Mountain Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1095 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Interactive |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open](https://leetcode.com/problems/find-in-mountain-array/) |

## Problem Description

### Goal

This is an interactive problem. A mountain array has length at least three and contains an interior peak: its values are strictly increasing from index 0 through the peak, then strictly decreasing from the peak through the final index.

Given `target` and a `MountainArray`, return the minimum index whose value equals `target`, or `-1` when the value is absent. The underlying array cannot be accessed directly. Only `MountainArray.get(index)` and `MountainArray.length()` are available, and a submission that makes more than 100 calls to `MountainArray.get` is rejected.

### Function Contract

**Inputs**

- `target`: an integer to locate, with $0 \leq \texttt{target} \leq 10^9$.
- `mountain_arr`: a mountain array of length $n$, where $3 \leq n \leq 10^4$ and every value lies in $[0,10^9]$. LeetCode exposes it through `get(index)` and `length()`; the app-local adapter receives the same values as a list.

**Return value**

The smallest index containing `target`, or `-1` if no such index exists.

### Examples

**Example 1**

- Input: `target = 3, mountain_arr = [1, 2, 3, 4, 5, 3, 1]`
- Output: `2`

The target occurs on both slopes at indices 2 and 5, so the smaller index is required.

**Example 2**

- Input: `target = 3, mountain_arr = [0, 1, 2, 4, 2, 1]`
- Output: `-1`
