# Sum of Consecutive Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3284 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Sum of Consecutive Subarrays](https://leetcode.com/problems/sum-of-consecutive-subarrays/) |

## Problem Description

### Goal

A nonempty array is consecutive when every adjacent difference is `1`, or when every adjacent difference is `-1`. The direction must remain consistent throughout the array: a sequence that first rises and then falls is not consecutive. A one-element array is consecutive without needing an adjacent difference.

The value of a subarray is the sum of its elements. Consider every nonempty contiguous subarray of `nums` that satisfies the consecutive rule, add all of their values, and return the result modulo $10^9+7$.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, each at most $10^5$, where $1 \le n \le 10^5$.

**Return value**

Return the sum of the element sums of all consecutive subarrays, reduced modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 3]`
- **Output:** `20`
- **Explanation:** All six nonempty subarrays are increasing-consecutive.

#### Example 2

- **Input:** `nums = [1, 3, 5, 7]`
- **Output:** `16`
- **Explanation:** Only the four singleton subarrays qualify.

#### Example 3

- **Input:** `nums = [7, 6, 1, 2]`
- **Output:** `32`
- **Explanation:** Besides the singletons, `[7, 6]` and `[1, 2]` qualify.
