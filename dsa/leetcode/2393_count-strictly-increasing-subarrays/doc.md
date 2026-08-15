# Count Strictly Increasing Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2393 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-strictly-increasing-subarrays/) |

## Problem Description

### Goal

Given an array `nums` of positive integers, count its subarrays whose elements are in strictly increasing order. A subarray is a nonempty contiguous range of the original array, so ranges with the same values at different positions are counted separately.

Every one-element subarray is strictly increasing. For longer ranges, each adjacent value must be strictly smaller than the next; equality breaks an increasing run just as a decrease does. Return the total number of qualifying ranges.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, where $1 \le n \le 10^5$ and every value is at most $10^6$.

**Return value**

- Return the number of nonempty contiguous strictly increasing subarrays.

**Counting semantics**

- Length-one ranges always count.
- Equal adjacent values cannot share a qualifying range.
- The answer may exceed 32-bit signed integer range.

### Examples

#### Example 1

- **Input:** `nums = [1,3,5,4,4,6]`
- **Output:** `10`

#### Example 2

- **Input:** `nums = [1,2,3,4,5]`
- **Output:** `15`
- **Explanation:** Every subarray is strictly increasing.
