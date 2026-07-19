# Unique Number of Occurrences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1207 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/unique-number-of-occurrences/) |

## Problem Description

### Goal

You are given an integer array `arr`. For each distinct integer appearing in the array, its number of occurrences is the count of positions that contain that value. The values themselves may be equal only when they represent the same distinct integer; positive, negative, and zero values are all counted in the same way.

Determine whether these occurrence counts are unique across the distinct values. Return `true` exactly when no two different integers occur the same number of times. If any pair of distinct integers has an equal occurrence count, return `false`.

### Function Contract

**Inputs**

- `arr`: An integer array of length $n$, where $1\le n\le1000$ and every value lies between $-1000$ and $1000$, inclusive.
- Let $k$ be the number of distinct values in `arr`.

**Return value**

- `true` if all $k$ occurrence counts are pairwise distinct; otherwise `false`.

### Examples

**Example 1**

- Input: `arr = [1,2,2,1,1,3]`
- Output: `true`

The values `1`, `2`, and `3` occur three, two, and one time respectively.

**Example 2**

- Input: `arr = [1,2]`
- Output: `false`

Both distinct values occur once.

**Example 3**

- Input: `arr = [-3,0,1,-3,1,1,1,-3,10,0]`
- Output: `true`
