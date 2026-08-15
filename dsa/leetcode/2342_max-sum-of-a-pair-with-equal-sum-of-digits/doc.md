# Max Sum of a Pair With Equal Sum of Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2342 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/) |

## Problem Description

### Goal

Given a 0-indexed array `nums` of positive integers, choose two different
indices $i$ and $j$. The pair is eligible only when the decimal digits of
`nums[i]` have the same sum as the decimal digits of `nums[j]`.

Among every eligible pair, return the largest possible value of
`nums[i] + nums[j]`. The two indices must be distinct even when the chosen
values are equal. If the array contains no eligible pair, return `-1`.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $1 \le n \le 10^5$ and
  $1 \le \texttt{nums[i]} \le 10^9$.

**Return value**

The maximum sum of two values at distinct indices whose decimal digit sums are
equal, or `-1` if no such pair exists.

### Examples

#### Example 1

- **Input:** `nums = [18,43,36,13,7]`
- **Output:** `54`
- **Explanation:** `18` and `36` both have digit sum 9 and total 54; the eligible
  pair `43` and `7` totals only 50.

#### Example 2

- **Input:** `nums = [10,12,19,14]`
- **Output:** `-1`
- **Explanation:** All four digit sums differ, so no eligible pair exists.
