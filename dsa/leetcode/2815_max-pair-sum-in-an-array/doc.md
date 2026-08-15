# Max Pair Sum in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2815 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/max-pair-sum-in-an-array/) |

## Problem Description

### Goal

You are given an array of positive integers. Choose two elements at different indices whose largest decimal digits are equal. For example, the largest digit of `2373` is `7`, regardless of how often any digit occurs.

Return the greatest sum obtainable from a qualifying pair. If no two array elements share the same largest digit, return `-1`. The pair is determined by indices, so equal numeric values at two different positions may be selected together.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, where $2 \leq n \leq 100$ and $1 \leq \texttt{nums[i]} \leq 10^4$.

Let $V$ be the largest input value.

**Return value**

Return the maximum sum of two distinct-index values having the same largest decimal digit, or `-1` if no such pair exists.

### Examples

#### Example 1

- **Input:** `nums = [112, 131, 411]`
- **Output:** `-1`
- **Explanation:** Their largest digits are `2`, `3`, and `4`, so none can pair.

#### Example 2

- **Input:** `nums = [2536, 1613, 3366, 162]`
- **Output:** `5902`
- **Explanation:** All have largest digit `6`; the two greatest values sum to `2536 + 3366`.

#### Example 3

- **Input:** `nums = [51, 71, 17, 24, 42]`
- **Output:** `88`
- **Explanation:** The best eligible pair is `71` and `17`, both with largest digit `7`.
