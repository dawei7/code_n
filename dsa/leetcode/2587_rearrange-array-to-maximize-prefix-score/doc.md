# Rearrange Array to Maximize Prefix Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2587 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums`, and you may rearrange all of its elements into any order, including leaving the original order unchanged.

After choosing an order, define `prefix[i]` as the sum of the elements from index `0` through index `i`, inclusive. The score of that arrangement is the number of entries in `prefix` that are strictly positive. A zero prefix sum does not contribute.

Return the largest score obtainable over every possible rearrangement. The requested result is a count of positive prefix sums, not the greatest numerical prefix sum.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers, where $1 \leq n \leq 10^5$ and each value lies between $-10^6$ and $10^6$, inclusive.

**Return value**

- The maximum possible number of strictly positive prefix sums after rearranging `nums`.

### Examples

**Example 1**

- Input: `nums = [2,-1,0,1,-3,3,-3]`
- Output: `6`

For example, ordering the values as `[2,3,1,-1,-3,0,-3]` produces prefix sums `[2,5,6,5,2,2,-1]`, of which six are positive.

**Example 2**

- Input: `nums = [-2,-3,0]`
- Output: `0`

No rearrangement can create a positive prefix sum.
