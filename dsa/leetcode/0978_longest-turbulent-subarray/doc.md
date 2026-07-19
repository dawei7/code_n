# Longest Turbulent Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 978 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/longest-turbulent-subarray/) |

## Problem Description

### Goal

Given an integer array `arr`, find the maximum length of a turbulent subarray. A subarray is contiguous, and it is turbulent when the comparison sign between adjacent elements flips at every step.

More formally, for a range `arr[i], ..., arr[j]`, one valid orientation requires `arr[k] > arr[k + 1]` at odd indices `k` and `arr[k] < arr[k + 1]` at even indices; the other orientation reverses those two signs. Either orientation is acceptable throughout the range. Equal adjacent values satisfy neither strict comparison and therefore stop a turbulent range. Return the length of the longest qualifying contiguous range; a single element is turbulent vacuously.

### Function Contract

**Inputs**

- `arr`: a list of $N$ integers, where $1 \le N \le 4\cdot10^4$ and $0 \le \texttt{arr[i]} \le 10^9$.

**Return value**

- The maximum number of elements in a contiguous subarray whose adjacent comparison signs strictly alternate.

### Examples

**Example 1**

- Input: `arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]`
- Output: `5`
- Explanation: `[4, 2, 10, 7, 8]` follows $4>2<10>7<8$.

**Example 2**

- Input: `arr = [4, 8, 12, 16]`
- Output: `2`
- Explanation: consecutive increases cannot both belong to a longer turbulent range.

**Example 3**

- Input: `arr = [100]`
- Output: `1`
