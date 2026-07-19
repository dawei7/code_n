# Maximum Equal Frequency

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1224 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-equal-frequency/) |

## Problem Description

### Goal

Given an array of positive integers `nums`, consider a prefix ending at any position. That prefix is valid when exactly one element can be removed so that every number still present in the prefix occurs the same number of times.

Return the length of the longest valid prefix. The removed element is one occurrence at one index, not every occurrence of its value; a prefix of length one is valid because removing its only element leaves no unequal frequencies.

### Function Contract

**Inputs**

- `nums`: An array of length $n$, where $1\le n\le10^5$ and $1\le\texttt{nums[i]}\le10^5$.

**Return value**

- The maximum prefix length for which removing exactly one element makes all remaining positive frequencies equal.

### Examples

**Example 1**

- Input: `nums = [2,2,1,1,5,3,3,5]`
- Output: `7`

In the first seven elements, removing `5` leaves `1`, `2`, and `3` with frequency two. The full length-eight prefix cannot be repaired by one removal.

**Example 2**

- Input: `nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]`
- Output: `13`

Removing the single `5` leaves four values that each occur three times.

**Example 3**

- Input: `nums = [1,1,1,2,2,2]`
- Output: `5`

For the first five elements, removing one `1` leaves both values with frequency two.
