# Maximum of Minimum Values in All Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1950 |
| Difficulty | Medium |
| Topics | Array, Stack, Monotonic Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-of-minimum-values-in-all-subarrays/) |

## Problem Description
### Goal
You are given an integer array `nums` of length $N$. For each possible window
length $L$ from 1 through $N$, consider every contiguous subarray containing
exactly $L$ elements. Find the minimum value within each such subarray, then
take the maximum among those minima.

Return all $N$ query answers in one array. Position `i` corresponds to window
length $i+1$, so `answer[i]` is the greatest minimum obtainable from any
subarray of that length.

### Function Contract
**Inputs**

- `nums`: an array of length $N$, where $1 \le N \le 10^5$ and
  $0 \le \texttt{nums[i]} \le 10^9$.

**Return value**

- An array `answer` of length $N$ such that `answer[L - 1]` is the maximum
  minimum over all subarrays of length $L$.

### Examples
**Example 1**

- Input: `nums = [0, 1, 2, 4]`
- Output: `[4, 2, 1, 0]`

**Example 2**

- Input: `nums = [10, 20, 50, 10]`
- Output: `[50, 20, 10, 10]`

**Example 3**

- Input: `nums = [5, 5, 5]`
- Output: `[5, 5, 5]`
