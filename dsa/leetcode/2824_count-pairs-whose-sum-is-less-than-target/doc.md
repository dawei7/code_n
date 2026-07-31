# Count Pairs Whose Sum is Less than Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2824 |
| Difficulty | Easy |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/) |

## Problem Description
### Goal

You are given a 0-indexed integer array `nums` of length $n$ and an integer `target`.

The array may contain positive values, negative values, and duplicates. A pair is determined by two different positions rather than by two distinct values, and requiring $i < j$ ensures that each choice of positions is considered only once.

Count the index pairs $(i, j)$ for which $0 \le i < j < n$ and `nums[i] + nums[j] < target`. The comparison is strict: a pair whose sum equals `target` must not be included.

### Function Contract
**Inputs**

- `nums`: A list of $n$ integers, where $1 \le n \le 50$ and every value is between $-50$ and $50$, inclusive.
- `target`: An integer between $-50$ and $50$, inclusive.

Each pair is identified by its two original indices, so equal values at different positions still form distinct pairs.

**Return value**

Return the number of index pairs whose sum is strictly less than `target`.

### Examples
**Example 1**

- Input: `nums = [-1, 1, 2, 3, 1], target = 2`
- Output: `3`
- Explanation: The valid index pairs are `(0, 1)`, `(0, 2)`, and `(0, 4)`. Pair `(0, 3)` is excluded because its sum equals `2` rather than being smaller.

**Example 2**

- Input: `nums = [-6, 2, 5, -2, -7, -1, 3], target = -2`
- Output: `10`

**Example 3**

- Input: `nums = [1, 1], target = 2`
- Output: `0`
- Explanation: The only pair has sum `2`, and equality does not satisfy the strict inequality.
