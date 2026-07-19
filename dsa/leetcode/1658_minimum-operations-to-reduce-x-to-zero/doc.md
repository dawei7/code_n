# Minimum Operations to Reduce X to Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1658 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/) |

## Problem Description
### Goal
You are given an integer array `nums` and an integer `x`. In one operation, remove either the current leftmost element or the current rightmost element, then subtract that removed value from `x`. Each removal modifies the array, so later operations may choose only from the ends that remain.

Find the minimum number of operations that reduces `x` to exactly zero. If no sequence of end removals has exactly the required sum, return `-1`. Every array value is positive, so removed sums only increase as more elements are taken.

### Function Contract
**Inputs**

- `nums`: an array of $n$ positive integers, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^4$.
- `x`: the positive target to remove, where $1 \le x \le 10^9$.

**Return value**

Return the minimum number of left-end and right-end removals whose values sum to `x`. Return `-1` if no valid sequence exists.

### Examples
**Example 1**

- Input: `nums = [1, 1, 4, 2, 3], x = 5`
- Output: `2`

Removing `2` and then `3` from the right uses two operations and subtracts exactly 5.

**Example 2**

- Input: `nums = [5, 6, 7, 8, 9], x = 4`
- Output: `-1`

Every available end value already exceeds `x`, so no exact removal sequence exists.

**Example 3**

- Input: `nums = [3, 2, 20, 1, 1, 3], x = 10`
- Output: `5`

Removing the first two values and the last three values subtracts exactly 10 in five operations.
