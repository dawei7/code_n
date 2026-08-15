# Intersection of Multiple Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2248 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Sorting, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/intersection-of-multiple-arrays/) |

## Problem Description

### Goal

You are given a nonempty 2D integer array `nums`. Every inner array is
nonempty and contains distinct positive integers, although the same value may
appear in different inner arrays.

Find exactly the integers that occur in every inner array. Return those common
values once each, sorted in ascending order. If no value belongs to all
arrays, return an empty list.

### Function Contract

**Inputs**

- `nums`: Between $1$ and $1000$ nonempty arrays whose combined length is at most $1000$. Each inner array contains distinct values from $1$ through $1000$.

**Return value**

Return the values present in every inner array, without duplicates and in
ascending order.

### Examples

#### Example 1

- **Input:** `nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]`
- **Output:** `[3,4]`

#### Example 2

- **Input:** `nums = [[1,2,3],[4,5,6]]`
- **Output:** `[]`

#### Example 3

- **Input:** `nums = [[5,1,3]]`
- **Output:** `[1,3,5]`
