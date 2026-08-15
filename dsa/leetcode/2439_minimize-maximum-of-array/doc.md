# Minimize Maximum of Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2439 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming, Greedy, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Minimize Maximum of Array](https://leetcode.com/problems/minimize-maximum-of-array/) |

## Problem Description

### Goal

You are given a 0-indexed array `nums` containing $n$ non-negative integers. In one operation, choose an index `i` with $1 \le i < n$ and `nums[i] > 0`. Decrease `nums[i]` by one and increase `nums[i - 1]` by one.

You may perform this operation any number of times, including zero. Because every unit can move only toward a smaller index, determine the minimum possible value of the largest array element after choosing the operations optimally.

### Function Contract

**Inputs**

- `nums`: A list of $n$ non-negative integers, where $2 \le n \le 10^5$ and $0 \le \texttt{nums[i]} \le 10^9$.

**Return value**

- The smallest maximum element attainable by applying any number of the permitted operations.

### Examples

#### Example 1

- **Input:** `nums = [3, 7, 1, 6]`
- **Output:** `5`
- **Explanation:** Operations can transform the array through `[4, 6, 1, 6]` and `[4, 6, 2, 5]` to `[5, 5, 2, 5]`. No arrangement with maximum below 5 is possible.

#### Example 2

- **Input:** `nums = [10, 1]`
- **Output:** `10`
- **Explanation:** The first value cannot move right, so leaving the array unchanged is optimal.
