# Maximum Value at a Given Index in a Bounded Array

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/) |
| Frontend ID | 1802 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Binary Search, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Construct an integer array `nums` of length `n`. Every element must be positive, the absolute difference between adjacent elements may not exceed one, and the total sum of the array may not exceed `maxSum`.

Among all arrays satisfying those rules, maximize `nums[index]` and return that maximum value. Only the value at the designated zero-based index is required; the array itself does not need to be returned.

### Function Contract

**Inputs**

- `n`: the array length, where $1 \le n \le 10^9$.
- `index`: the zero-based target position, where $0 \le \texttt{index}<n$.
- `maxSum`: the inclusive sum limit, where $n \le \texttt{maxSum} \le 10^9$.

**Return value**

- Return the greatest possible positive integer at `nums[index]` in any valid bounded array.

### Examples

**Example 1**

- Input: `n = 4, index = 2, maxSum = 6`
- Output: `2`

One valid optimal array is `[1,2,2,1]`.

**Example 2**

- Input: `n = 6, index = 1, maxSum = 10`
- Output: `3`

The peak can reach three while respecting both the adjacent-difference and sum bounds.

**Example 3**

- Input: `n = 1, index = 0, maxSum = 24`
- Output: `24`

With no neighbors, the target may use the entire budget.
