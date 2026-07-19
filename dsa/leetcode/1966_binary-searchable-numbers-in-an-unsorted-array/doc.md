# Binary Searchable Numbers in an Unsorted Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1966 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-searchable-numbers-in-an-unsorted-array/) |

## Problem Description
### Goal
Consider a search process on a sequence. While elements remain, it chooses any
current element as a pivot. If the pivot equals the target, the search
succeeds. If it is smaller than the target, the pivot and everything to its
left are removed; if it is larger, the pivot and everything to its right are
removed. The process fails when the sequence becomes empty.

Given an array `nums` of unique integers, count the values guaranteed to be
found for every possible sequence of pivot choices. The input need not be
sorted.

### Function Contract
**Inputs**

- `nums`: a list of $N$ unique integers, where $1\le N\le10^5$ and every value
  lies between $-10^5$ and $10^5$, inclusive.

**Return value**

- The number of array values that the described search always finds,
  regardless of how pivots are chosen.

### Examples
**Example 1**

- Input: `nums = [7]`
- Output: `1`

**Example 2**

- Input: `nums = [-1, 5, 2]`
- Output: `1`

**Example 3**

- Input: `nums = [1, 3, 2, 4]`
- Output: `2`
