# Sliding Subarray Beauty

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2653 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sliding-subarray-beauty/) |

## Problem Description

### Goal

Given an integer array `nums` of length $n$, inspect every contiguous, non-empty subarray of exactly `k` elements. For each window, order its values and identify its $x$-th smallest integer. The window's beauty is that integer when it is negative; otherwise its beauty is `0`. Equivalently, a window containing fewer than `x` negative values has beauty `0`.

Return the $n-k+1$ beauty values in window order, beginning with the subarray at index `0` and advancing its start by one position each time. Repeated negative values occupy separate positions in the ordering, so their frequencies affect which value is the $x$-th smallest.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $1 \le n \le 10^5$ and $-50 \le \texttt{nums[i]} \le 50$.
- `k`: The fixed window length, where $1 \le k \le n$.
- `x`: The one-based order statistic requested within each window, where $1 \le x \le k$.

**Return value**

- Return an integer array of length $n-k+1$ containing each window's beauty from left to right.

### Examples

**Example 1**

- Input: `nums = [1,-1,-3,-2,3], k = 3, x = 2`
- Output: `[-1,-2,-2]`
- Explanation: The second-smallest values of the three windows are `-1`, `-2`, and `-2`, and all are negative.

**Example 2**

- Input: `nums = [-1,-2,-3,-4,-5], k = 2, x = 2`
- Output: `[-1,-2,-3,-4]`
- Explanation: Each window contains two negatives, so its larger value is its second-smallest value and its beauty.

**Example 3**

- Input: `nums = [-3,1,2,-3,0,-3], k = 2, x = 1`
- Output: `[-3,0,-3,-3,-3]`
- Explanation: The window `[1,2]` has no negative value and therefore contributes `0`; every other window has `-3` as its smallest value.
