# Sorting Three Groups

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2826 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/sorting-three-groups/) |

## Problem Description

### Goal

You are given an integer array `nums` in which every element is `1`, `2`, or `3`.

In one operation, remove any single element from the array. The remaining elements retain their original relative order, so a sequence of removals selects a subsequence of `nums`.

Find the minimum number of operations needed to make the remaining array non-decreasing. A non-decreasing result may contain any number of `1` values followed by any number of `2` values and then any number of `3` values; any of those groups may be absent. If `nums` already has that order, no removals are required.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers, where $1 \le n \le 100$ and each element belongs to $\{1,2,3\}$.

**Return value**

Return the minimum number of elements that must be removed so the remaining sequence is non-decreasing.

### Examples

#### Example 1

- **Input:** `nums = [2, 1, 3, 2, 1]`
- **Output:** `3`
- **Explanation:** Removing the original elements at indices `0`, `2`, and `3` leaves `[1, 1]`.

#### Example 2

- **Input:** `nums = [1, 3, 2, 1, 3, 3]`
- **Output:** `2`
- **Explanation:** Removing the original elements at indices `1` and `2` leaves `[1, 1, 3, 3]`.

#### Example 3

- **Input:** `nums = [2, 2, 2, 2, 3, 3]`
- **Output:** `0`
- **Explanation:** The array is already non-decreasing.
