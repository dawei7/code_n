# Minimum Operations to Make Numbers Non-positive

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2702 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/minimum-operations-to-make-numbers-non-positive/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums` and positive integers `x` and `y`, where $y < x$. During one operation, choose any valid index `i`. Decrease `nums[i]` by `x`, while every other array element is decreased by `y`.

Determine the minimum number of operations required to make every value in `nums` less than or equal to zero. The same index may be chosen more than once, and values are allowed to become negative.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.
- `x`: The decrement applied to the selected index, with $1 \le y < x \le 10^9$.
- `y`: The decrement applied to every unselected index in an operation.

**Return value**

Return the minimum number of operations after which all elements are non-positive.

### Examples

**Example 1**

- Input: `nums = [3,4,1,7,6]`, `x = 4`, `y = 2`
- Output: `3`
- Explanation: Selecting index `3` twice and index `4` once is sufficient; no plan using fewer operations can remove every positive value.

**Example 2**

- Input: `nums = [1,2,1]`, `x = 2`, `y = 1`
- Output: `1`
- Explanation: Selecting the middle element once changes the array to `[0,0,0]`.

**Example 3**

- Input: `nums = [5]`, `x = 3`, `y = 1`
- Output: `2`
- Explanation: With only one index, each operation applies the selected decrement `x`; two selections reduce the value to a non-positive number.
