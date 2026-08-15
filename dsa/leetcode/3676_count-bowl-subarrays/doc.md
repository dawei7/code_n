# Count Bowl Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3676 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-bowl-subarrays/) |

## Problem Description

### Goal

Given an integer array `nums` whose elements are distinct, call a contiguous subarray `nums[l...r]` a bowl when it contains at least three elements and both endpoints rise strictly above every interior element. Equivalently, the smaller of `nums[l]` and `nums[r]` must be strictly greater than the maximum value in `nums[l + 1...r - 1]`.

Count all index pairs `(l, r)` whose subarray satisfies these conditions. Subarrays are distinguished by their endpoints, and adjacent endpoints do not form a bowl because they leave no interior element.

### Function Contract

**Inputs**

- `nums`: a list of $n$ distinct positive integers, where $3\le n\le10^5$ and each value is at most $10^9$.

**Return value**

Return the number of bowl subarrays in `nums`.

### Examples

#### Example 1

- **Input:** `nums = [2, 5, 3, 1, 4]`
- **Output:** `2`

The qualifying ranges are `[3, 1, 4]` and `[5, 3, 1, 4]`.

#### Example 2

- **Input:** `nums = [5, 1, 2, 3, 4]`
- **Output:** `3`

The left endpoint `5` forms a bowl with each of `2`, `3`, and `4`.

#### Example 3

- **Input:** `nums = [1000000000, 999999999, 999999998]`
- **Output:** `0`

The middle value is greater than the smaller right endpoint, so the only length-three range is not a bowl.
