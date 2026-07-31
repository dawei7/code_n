# Smallest Missing Non-negative Integer After Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2598 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/) |

## Problem Description

### Goal

You are given a zero-indexed integer array `nums` and a positive integer `value`. In one operation, you may add or subtract `value` from any chosen array element. Each element may be changed any number of times.

The MEX of an array is its smallest non-negative integer that does not occur. Negative values do not directly affect this definition, although the allowed operations may transform them into non-negative values.

Return the greatest MEX that can be achieved after applying any number of operations.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers, where $1 \leq n \leq 10^5$ and $-10^9 \leq \texttt{nums[i]} \leq 10^9$.
- `value`: The positive operation amount, satisfying $1 \leq \texttt{value} \leq 10^5$.

**Return value**

- The maximum possible MEX after independently adding or subtracting `value` any number of times from each element.

### Examples

**Example 1**

- Input: `nums = [1,-10,7,13,6,8], value = 5`
- Output: `4`

Elements from the required remainder classes can be transformed into `0`, `1`, `2`, and `3`, but no unused element can represent `4` afterward.

**Example 2**

- Input: `nums = [1,-10,7,13,6,8], value = 7`
- Output: `2`

The remainder supplies can cover `0` and `1`; the class needed for `2` is unavailable next.
