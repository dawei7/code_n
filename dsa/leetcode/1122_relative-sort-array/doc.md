# Relative Sort Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1122 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting, Counting Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/relative-sort-array/) |

## Problem Description

### Goal

You are given two integer arrays, `arr1` and `arr2`. Every value in `arr2` also occurs in `arr1`, and the values of `arr2` are distinct. The order of `arr2` therefore supplies a priority ordering for selected values of `arr1`, including all repeated copies of those values.

Reorder `arr1` so that its values that appear in `arr2` come first, grouped in the same relative order as the corresponding values in `arr2`. Place every value that does not appear in `arr2` after those priority groups, in ascending order, and return the resulting array.

### Function Contract

**Inputs**

- `arr1`: an integer array of length $n$, where $1 \le n \le 1000$ and every value is in $[0, 1000]$.
- `arr2`: an integer array of length $m$, where $1 \le m \le 1000$; its values are distinct, lie in $[0, 1000]$, and each occurs in `arr1`.

Let $V = 1001$ be the size of the allowed value domain.

**Return value**

An array containing exactly the values of `arr1`, with values named by `arr2` grouped first in `arr2` order and all remaining values afterward in ascending order.

### Examples

**Example 1**

- Input: `arr1 = [2,3,1,3,2,4,6,7,9,2,19]`, `arr2 = [2,1,4,3,9,6]`
- Output: `[2,2,2,1,4,3,3,9,6,7,19]`

**Example 2**

- Input: `arr1 = [28,6,22,8,44,17]`, `arr2 = [22,28,8,6]`
- Output: `[22,28,8,6,17,44]`
